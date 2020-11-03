# -*- coding: UTF-8 -*-

import rsa
from rsa import common, transform, core
import base64

test_dic = {"name":"zzz","gender":'female',"age":"67"}
print(test_dic.get("name"))


def get_pic_base64(picPath):
    with open(picPath, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    # print(s)
    print(base64_data)
    return base64_data


class RsaUtil(object):

    def __init__(self, _exponent, _modulus):
        self.exponent = _exponent
        self.modulus = _modulus

    def populate_public_key(self):
        """
            通过rsa包依据模数和指数生成公钥，实现加密
            :return:
        """
        rsa_exponent = int(self.exponent, 16)
        rsa_modulus = int(self.modulus, 16)
        rsa_pubkey = rsa.PublicKey(rsa_modulus, rsa_exponent)
        return rsa_pubkey

    @staticmethod
    def _pad_for_encryption(message, key_length):
        """
        RSA加密常用的填充方式
        1.RSA_PKCS1_PADDING 填充模式，最常用的模式
        要求: 输入：必须 比 RSA 钥模长(modulus) 短至少11个字节, 也就是　RSA_size(rsa) – 11
        如果输入的明文过长，必须切割，　然后填充
        输出：和modulus一样长
        根据这个要求，对于512bit的密钥，　block length = 512/8 – 11 = 53 字节

        :param message:
        :param key_length:
        :return:
        """
        message = message[::-1]
        # max_message_length = key_length - 11
        message_length = len(message)

        padding = b''
        padding_length = key_length - message_length - 3
        print(key_length)

        for i in range(padding_length):
            padding += b'\x00'
        print(b''.join([b'\x00\x00', padding, b'\x00', message]))
        # print(b''.join([b'\x00\x00', padding, b'\x00', message])
        return b''.join([b'\x00\x00', padding, b'\x00', message])

    def _encrypt(self, message, pub_key):
        key_length = rsa.common.byte_size(pub_key.n)
        padded = self._pad_for_encryption(message, key_length)

        payload = rsa.transform.bytes2int(padded)
        encrypted = rsa.core.encrypt_int(payload, pub_key.e, pub_key.n)
        block = rsa.transform.int2bytes(encrypted, key_length)
        print(key_length)
        print(message)
        print(pub_key)

        return block

    def encrypt_by_public_key(self, message):
        """
        加密 公钥
        :param message:
        :return:
        """
        rsa_pubkey = self.populate_public_key()
        crypto = self._encrypt(message.encode(), rsa_pubkey)
        return crypto.hex()


if __name__ == '__main__':
    modulus = "ac1152d6bbf4c27cff54877059af22402eadbfa852201d66412af1fce9de704e92df84315b28eaa9e1be8dc69c450bc9f5f1bdce6a954dc4233a79c4a4be53c91d0d938bd9611bfe7f4c15edcffe6896ddc12e71e63663bacdc7d379051f2c18a5ca4c3db94cad53b399e8679de9049fb45b27ba205a1f40da269a56af454f6b"
    exponent = "10001"
    ru = RsaUtil(exponent, modulus)
    encrypt_result = ru.encrypt_by_public_key("admin1234")
    print(encrypt_result)
