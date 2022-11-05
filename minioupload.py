from minio import *

client = Minio(
    "192.168.56.104:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

found = client.bucket_exists("static")
if not found:
    client.make_bucket("static")
else:
    print("Bucket 'static' already exists")

client.fput_object(
        "static", "favicon_trans.png", "favicon_trans.png",
    )
