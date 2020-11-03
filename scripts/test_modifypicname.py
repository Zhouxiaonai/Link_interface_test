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

import os
picpath = r"E:\picture\toolkit_test"
for item in os.listdir(picpath):
    print(item)
    itemnew = "K"+item
    print(itemnew)
    # os.rename(item,item)
    try:
        os.rename(os.path.join(picpath,item),os.path.join(picpath,itemnew))
    except BaseException as e:
        print(item)