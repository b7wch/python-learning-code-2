# i!/usr/bin/env python
# -*- coding:utf-8 -*-

# 这里使用pycrypto‎库
# 安装方法: easy_install pycrypto‎

import sys, json
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16但是不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            text = text + ('\0' * add)
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的
        # 输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


if __name__ == '__main__':
    data = {
        "key": 'bf406e4ecdcb24074feeed0c129fbbee83669d229709b841f19f96e60b43a40d',
        "product": "TAC",
        "hash": "D3C4-7695-35C3-3E7A",
        "prodVersion": "V2.0R01F00",
        "engineVersion": "V2.0R01F00SP07",
        "licType": "正式证书",
        "licSN": "14-38-L-0256",
        "licStartTime": "2017-04-27",
        "licEndTime": "2020-05-31",
        "deviceIP": "10.8.15.110",
        "expireTime": 1511426404,
        "reserved": {
            "avVersion": "V7.0R19F12",
            "svnBulid": "56441",
        }
    }
    pc = prpcrypt('J0hRz&ED!&YdrFG!')  # 初始化密钥
    print json.dumps(data)
    e = pc.encrypt(json.dumps(data))  # 加密
    d = pc.decrypt(e)  # 解密
    j = '24322b2d5ede98e5bf63be1b9c20b48aad857b3fa84a26d65011f9c1458942a603c8ba13456baeeb548d95d905c6571b90bf86fc15a73cc7227c9b40c32eb639035e339e2441017eb0439982bca5b6dbb1f49b4f88eed104d1b4deeaa6cfbb4297f67cd56b85fd2087c5e40280e6d1df11d1816925d4967afd845b869a59b0224a72b145fefb5219b1e2e0783df5825faf672153aab927f27a7a7387a27d49d44c7aa8e1e6436bcf4897fc97a1458f3c2bef20f5b62d1cc9b95d1261adaed7ee6323c9cfe6fd7186e2b45a82b12d16178df21c75fd77432dddea37dc5618273deff97e6c01259ca5704da7ca3f2e4b361b3b68b1a8cbee7e70e9a0a99c62f60840747ab08ea29fdca267b786d566cdf3d42507496fa956afd5b614c372d83d473f82f5ad9a36abc0c4381cc14db27b8ace7f7e85ef923e5038d045ca6ec44ffcbbff9d9d861e173803c0bca8234c0b180f0d4ef9a78440ec0b9527e444b8ca15f7908637ccd5ccab0b87e3e7772aa667'
    print "加密:",len(e), e
    print "解密:", d
    f = pc.decrypt(j)
