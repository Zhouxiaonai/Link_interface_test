import requests
import json
import hashlib
import time

def get_sign(timestamp,token):
    SECRET = 'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8'
    md5 = "AUTH-TIMESTAMP=" + timestamp + "&AUTH-TOKEN=" + token + "#" + SECRET
    m1 = hashlib.md5()
    m1.update(md5.encode("utf-8"))
    sign = m1.hexdigest()
    return sign