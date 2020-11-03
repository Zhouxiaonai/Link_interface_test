# coding: utf-8
"""
author:zhouwenchao
"""
import os
import time
import uiautomator2 as u2

def start_app():
    d = u2.connect("10.9.40.66")
    print(d.info)
    d.press("home")
    d(resourceId="com.android.launcher3:id/all_apps_handle").click()
    time.sleep(1)
    d(resourceId="com.android.launcher3:id/icon", text="SensePassPro").click()
    print("start app")
    # d(resourceId="com.sensetime.sensepasspro:id/tv_name", text="GANESAN+MURUGESAN（1630785492）").click()
    time.sleep(5)
    x=0.481
    y=0.398
    print("double click")
    d.long_click(x,y,5)
    print("end long click")
    d.send_keys("admin1234")
    # d(focused=True).set_text("admin1234")
    time.sleep(1)
    d(resourceId="com.sensetime.sensepasspro:id/tv_confirm").click()
    time.sleep(1)
    d(resourceId="com.sensetime.sensepasspro:id/tv_left", text="通行设置").click()
    time.sleep(1)
    d(resourceId="com.sensetime.sensepasspro:id/tv_left", text="通行组").click()
    time.sleep(1)
    d(resourceId="com.sensetime.sensepasspro:id/tv_group_name").click()
    # d(scrollable=True).scroll.to(description="")
    time.sleep(3)
    sx = 0.09
    sy = 0.898
    ex = 0.298
    ey = 0.28
    f =open(r"D:\tasks\SenseLink\App_test\log.txt","w")
    for i in range(0,200):
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]').all()
        for elem in d.xpath("//android.widget.EditText").all():
            print("Text:"+elem.text)
            f.write(elem.text+"\n")
        d.swipe(sx, sy, ex, ey)
    f.close()

def get_all_staffname(d = u2.connect("10.9.40.66")):
    pass

# start_app()
# get_all_staffname(d = u2.connect("10.9.40.66"))

f = open(r"D:\tasks\SenseLink\App_test\log.txt","r")
# f_rts = open(r"D:\tasks\SenseLink\App_test\log_rts.txt","w",encoding="utf-8")
alllines = f.readlines()
print(alllines)
allname = []
with open(r"D:\tasks\SenseLink\App_test\log_rts1.txt","w",encoding="utf-8") as f_rts:
    for item in alllines:
        # if "Text:" in item:
        name = item.strip()
        # print(name)
        if name not in allname:
            f_rts.write(name+"\n")
            allname.append(name)
        # else:
        #     print(item)
f_rts.close()
f.close()

