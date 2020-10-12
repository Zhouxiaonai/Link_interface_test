import base64

def get_pic_base64(picPath):
    with open(picPath, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    # print(s)
    print(type(base64_data))
    # return base64_data
    print(type(s))
    return s

if __name__ == "__main__":
    get_pic_base64(r"D:\tasks\SenseLink\测试数据\打卡记录数据\record01\27902_0_0.978_20200925205709_SPS-535e5626391860d3ba2de1cbda221d26_1_rgb.jpg")