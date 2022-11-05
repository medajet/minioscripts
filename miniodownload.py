from minio import *

client = Minio(
    "192.168.56.104:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

client.fget_object("static", "favicon_trans.png", "favicon_trans.png")
