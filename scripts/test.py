params={'device_id':"device_id",
        'package_name':"package_name",
        'version_code':"version_code",
        'version_name':'version_name',
         'timestamp':"159892834921",
        }
tmpsignOri = sorted(params.items(), key=lambda d: d[0], reverse=True)
tmpsignOri1 = sorted(params.items(), key=lambda d: d[0], reverse=False)
print(tmpsignOri)
print(dict(tmpsignOri1))
mystr = ''
for item in tmpsignOri1:
    mystr = mystr+"&"+item[1]
print(mystr)