FROM python:3.12-alpine as base-image
FROM base-image as builder
ARG KERIPY_BRANCH=main

RUN apk add --no-cache bash patch libsodium-dev linux-headers git gcc musl-dev rustup libffi-dev
RUN rustup-init -y && source $HOME/.cargo/env
ENV PATH="/root/.cargo/bin:${PATH}"

RUN python -m pip install --upgrade pip

RUN git clone --depth 1 --branch ${KERIPY_BRANCH} https://github.com/provenant-dev/keripy.git /keripy


WORKDIR /keripy
RUN pip install -r requirements.txt
RUN echo "GitHash(with commit message): " > .version && git --no-pager log --oneline -n1 >> .version && echo "Branch Name: provenant-dev/keripy/tree/${KERIPY_BRANCH}" >> .version
RUN rm -rf /keripy/.git


COPY . /public-schema
WORKDIR /public-schema/tools
RUN pip install -r requirements.txt --no-cache-dir
RUN echo "GitHash(with commit message): " > .version && git --no-pager log --oneline -n1 >> .version
RUN rm -rf /public-schema/.git

FROM base-image

RUN apk update && apk upgrade && apk add --no-cache bash patch libsodium-dev jq linux-headers tini

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

COPY --from=builder /usr /usr

RUN addgroup --system --gid 1001 schema \
  && adduser --system --uid 1001 --disabled-password --shell /bin/false -G schema schema
USER schema

COPY --from=builder --chown=schema:schema /public-schema /public-schema
COPY --from=builder --chown=schema:schema /keripy /keripy
WORKDIR /public-schema/tools

ENV SCHEMA_REGISTRY_PORT=7723

ENTRYPOINT ["/sbin/tini", "--"]
CMD schema_registry_server --http ${SCHEMA_REGISTRY_PORT} -r registry.json
