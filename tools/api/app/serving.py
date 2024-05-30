# -*- encoding: utf-8 -*-
"""
 schema api serving module

"""
import json
from pathlib import Path
import falcon
from hio.core import http
from api.app import caching
from keri.help import nowIso8601


class SchemaEnd:

    def __init__(self, schemaCache):
        self.schemaCache = schemaCache
        print()        

        
    def on_get(self, _, rep, said):
        if said in self.schemaCache:
            data = self.schemaCache[said]

            rep.status = falcon.HTTP_200
            rep.content_type = "application/schema+json"
            rep.data = data
            return


class SchemaCollectionEnd:

    def __init__(self, schemaCache):
        self.schemaCache = schemaCache
        
    def on_get(self, req, rep):
        """ GET cached schema SAIDs

        Parameters:
            req: falcon.Request HTTP request
            rep: falcon.Response HTTP response

       ---
        summary:  Get SAIDs of all schemas
        description:  Get SAIDs of all schemas
        tags:
           - Schema
        responses:
           200:
              description: Array of all schema saids JSON
        """
        
        said_list = list(self.schemaCache.keys())
        rep.status = falcon.HTTP_200
        rep.content_type = "application/json"
        rep.data = json.dumps(said_list).encode("utf-8")
        

class HealthEnd:
    """Health resource for determining that schema-registry is live"""

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_OK
        resp.media = {"message": f"Schema Registry server is running! Time is {nowIso8601()}"}

def loadEnds(app, registryFile):
    sink = http.serving.StaticSink(staticDirPath="./static")
    app.add_sink(sink, prefix=sink.DefaultStaticSinkBasePath)

    schemaCache = caching.cacheSchema(registryFile, dict())

    schemaEnd = SchemaEnd(schemaCache=schemaCache)
    app.add_route("/oobi/{said}", schemaEnd)
   
    schemaColEnd = SchemaCollectionEnd(schemaCache=schemaCache)
    app.add_route("/schema", schemaColEnd)

    healthEnd = HealthEnd()
    app.add_route("/health", healthEnd)
