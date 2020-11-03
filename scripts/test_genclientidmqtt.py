# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
import hashlib
import sys
import time
import urllib

if len(sys.argv) < 2:
    print('参数个数错误')
    sys.exit()

token = str(sys.argv[1])

print('token=', token)

serKey = 'bb635dd47e5861f717472df95652077356a8f38dea6347851c191f66b7cf9dc8'

ttInt = int(round(time.time() * 1000))
ttStr = str(ttInt)
if len(sys.argv) > 2:
    print('get ts in argv')
    ttStr = str(sys.argv[2])
print('timeStamp=', ttStr)

rawStr = 'AUTH-TIMESTAMP=' + ttStr + '&AUTH-TOKEN=' + token + '#' + serKey
print('rawToMd5=', rawStr)

mdMake = hashlib.md5()
mdMake.update(rawStr.encode("utf-8"))
sign = mdMake.hexdigest()
print('sign=', sign)

clienid = token + '#' + ttStr + '#' + sign

print('clienid=', clienid)