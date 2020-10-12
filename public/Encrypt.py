#import pycryptodome
from Crypto.Cipher import AES
from Crypto.Cipher.AES import MODE_CBC
from Crypto import Random
from pyDes import *
import base64
from binascii import b2a_hex,a2b_hex
import hashlib
import rsa
from rsa import common,core,transform

def encryptRsa(message,pube,pubn):
	payload = rsa.transform.bytes2int(message.encode())
	encrypted = rsa.core.encrypt_int(payload, pube, pubn)
	nkey_length = rsa.common.byte_size(pubn)
	block = rsa.transform.int2bytes(encrypted, nkey_length)
	return block.hex()

def test_rsa(empoent,module,passwd):
    key_length = common.byte_size(int(module,16))
    print(key_length)
    pubkey, privkey = rsa.newkeys(512)
    key_length1 = common.byte_size(pubkey.n)
    # print(pubkey.n)
    # print(type(pubkey.n))
    # print(key_length1)
    reverseSize = 11
    maxlength = key_length - reverseSize
    # originempoent = "10001"
    # originmodule = "c5539e0f93bfc2f0f070353b473c8417c8593089d7b3c475f85760401c3f4aaf0e90206715d1d9fa7a51ab423eedd782b2bda94d9bf372587d01a23d88aab6ef114ba58256858c80f50e6a1f10f91b7cafc4a3e910b5dfec1fdf2f743e6575d97dc712300a83c19851c3f70339048793ba8af077f732bf14191766e6247f495f"
    myempoent = int(empoent,16)
    mymodule = int(module,16)
    mypubkey = rsa.PublicKey(mymodule,myempoent)
    testRSA = encryptRsa(passwd,myempoent,mymodule)
    # print("^^^^^^^^^^")
    # print(testRSA)
    # mypubkey = rsa.PublicKey(module, empoent)
    # print("--------------")
    # print(mypubkey)
    # myprikey = rsa.PrivateKey(myempoent,mymodule)
    # mypubkey1 = rsa.PublicKey(originmodule,originempoent)
    message = passwd.encode('utf8')
    # message = "Hello,Bob!".encode('utf8')
    cryinfo = rsa.encrypt(message, pubkey)
    cryinfo1 = rsa.encrypt(message, mypubkey)
    print("**********")
    # print(cryinfo)
    print(cryinfo1.hex())
    myinfo = rsa.decrypt(cryinfo,privkey)
    print(myinfo)
    return testRSA

def test_des():
    #              des模式  填充方式  ECB加密方式
    from pyDes import des, PAD_PKCS5, ECB

    #  秘钥  （如果和Java对接，两边要有相同的秘钥）
    DES_SECRET_KEY = 'bb635dd4'
    s = '这是一段明文'.encode()  # 这里中文要转成字节， 英文好像不用
    des_obj = des(DES_SECRET_KEY, ECB, DES_SECRET_KEY, padmode=PAD_PKCS5)  # 初始化一个des对象，参数是秘钥，加密方式，偏移， 填充方式
    secret_bytes = des_obj.encrypt(s)  # 用对象的encrypt方法加密
    s = des_obj.decrypt(secret_bytes)  # 用对象的decrypt方法解密
    print(secret_bytes)
    print(s.decode())

def md5(input):
    input = input.encode('utf-8');
    md5sign = hashlib.md5()
    md5sign.update(input)
    md5value = md5sign.hexdigest()
    return md5value

class encrypt_passwd_bydes():
    def __int__(self,enKey,secret,enType="ECB"):
        # self.enKey = enKey
        # self.secret = secret
        pass
    def encyptKey(self,str):
        #k = des(b"DESCRYPT", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        tmpK = des(b"bb635dd4", ECB, b"", pad=None, padmode=PAD_PKCS5)
        EncryptStr = tmpK.encrypt(str)
        print(base64.b64encode(EncryptStr))
        return base64.b64encode(EncryptStr)

    def decyptKey(self,str):
        tmpK = des(b"bb635dd4", ECB, b"", pad=None, padmode=PAD_PKCS5)
        data = base64.b64decode(str)
        dncryptStr = tmpK.decrypt(data)
        print(dncryptStr)
        return base64.b64decode(str)
        pass

class EncryptByAES():
    def __init__(self,empoent,module,passwd):
        self.empoent = empoent
        self.module = module
        self.passwd = passwd

    def get_max_length(self):
        pubkey = rsa.PublicKey(int(self.module,16),int(self.empoent,16))
        key_length =int(common.bit_size(pubkey.n)/8)
        reverSize = 0  #RSA_PKCS1_PADDING填充模式
        max_length = key_length - reverSize
        # print(max_length)
        return max_length

    def encrypt_with_pubkey(self,message):
        """
        通过公钥加密信息
        :param message: 被加密的信息
        :return: 已加密的base64编码字符串
        """
        encrypt_result = b''
        max_length = self.get_max_length()
        pubkey = rsa.PublicKey(int(self.module,16),int(self.empoent,16))
        # print(pubkey)
        message = self.passwd[::-1]
        randomNo = max_length-len(message)-3
        randompadding = (b"\x00")*randomNo
        # print(randompadding)
        # print(randomNo)
        if len(message) < max_length:
            message = (b'\x00\x00')+randompadding+(b"\x00")+message.encode('utf-8')
            # print(message)
            pass
        else:
            pass
        # print(max_length)
        # print(message)
        # print(pubkey)
        testmessage = rsa.transform.bytes2int(message)
        encrypt_result_test = core.encrypt_int(testmessage,pubkey.e,pubkey.n)
        test_rts = rsa.transform.int2bytes(encrypt_result_test,max_length)
        # print(test_rts.hex())
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # while message:
        #     input = message[:max_length]
        #     message = message[max_length:]
        #     print(input)
        #     out = rsa.encrypt(input, pubkey)
        #     encrypt_result += out
        #encrypt_result = base64.b64encode(encrypt_result)
        return test_rts.hex()

    def decrypt_by_private_key(self, message,prikey):
        """使用私钥解密.
            :param message: 需要解密的内容.
            解密之后的内容直接是字符串，不需要在进行转义
        """
        decrypt_result = ""
        max_length = self.get_max_length()
        decrypt_message = base64.b64decode(message)
        while decrypt_message:
            input = decrypt_message[:max_length]
            decrypt_message = decrypt_message[max_length:]
            out = rsa.decrypt(input, prikey)
            decrypt_result += out
        return decrypt_result

if __name__ == "__main__":
    # test_rsa("10001","993510eef84fea940aca8ff462b3c8d7b6a4f125a1b21ebdb1238ac8b09bf64fc5d2c9996d458dd75fc9b7bbb71249a9a3f324fa054ee60b2cd77412c8434bd970ae26e787ade68708d7b86aee6ae3dd7390410b2f2335bdbe615a8ce3197b6c07462bbfa63312d2c89614e8d6bc68e2c028d4237857a5b64edb34de31805f63","admin1234")
    # print("***************************************************")
    # print((b"X00").hex())
    AEStest = EncryptByAES("10001","ac1152d6bbf4c27cff54877059af22402eadbfa852201d66412af1fce9de704e92df84315b28eaa9e1be8dc69c450bc9f5f1bdce6a954dc4233a79c4a4be53c91d0d938bd9611bfe7f4c15edcffe6896ddc12e71e63663bacdc7d379051f2c18a5ca4c3db94cad53b399e8679de9049fb45b27ba205a1f40da269a56af454f6b","admin1234")
    # AEStest = encrypt_passwd_byaes()
    # print("*********")
    # print(str(AEStest.encrypt_with_pubkey("admin1234")))
    # testRSA1=encryptRsa("10001","d0b0daa0b63c44cd1228b8ec736917cb7cb1a3806ef6f5f078ca7b9171828c7614d492565f9166c1b6f5877845faa9682e94163510a9413d3ca8fb6509aa9e1df5b2513b126ffdd071b5ae11dcc18d3223b3f5aa6363edeb0d40cb6dfdc551a0d630564f7bbfef5d12f5fd64b6f23b77a5614fe3a55c16f94a433f5da33a7df7","admin1234")
    # print(testRSA1)
    pass
    # test = encrypt_passwd()
    # test.encyptKey("123$4567788")
    # test.decyptKey("bDY/L/51V0bFqKV00+ZCqA==")