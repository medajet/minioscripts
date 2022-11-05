from minio import *

client = Minio(
    "192.168.56.104:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

client.fget_object("static", "uploaded.png", "aa.png")
