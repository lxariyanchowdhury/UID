import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
