#!/usr/bin/env python3

from Crypto.Util.number import *
from pwn import xor
import base64

# ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# print("Here is your flag:")
# print("".join(chr(o) for o in ords))

# num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# print(long_to_bytes(num))

# name = "label"
# result = ""
# for c in name:
#     result += chr(ord(c) ^ 13)
# print(result)

# def xor_string(string1, string2):
#     result = ""
#     for i in range(len(string1)):
#         result += chr(ord(string1[i]) ^ ord(string2[i]))
#     return result

# KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
# KEY1 = bytes.fromhex(KEY1)
# KEY1 = bytes_to_long(KEY1)

# KEY2_1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
# KEY2_1 = bytes.fromhex(KEY2_1)
# KEY2_1 = bytes_to_long(KEY2_1)

# KEY2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
# KEY2_3 = bytes.fromhex(KEY2_3)
# KEY2_3 = bytes_to_long(KEY2_3)

# FLAG = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
# FLAG = bytes.fromhex(FLAG)
# FLAG = bytes_to_long(FLAG)

# KEY2 = KEY2_1 ^ KEY1
# KEY3 = KEY2_3 ^ KEY2
# FLAG = FLAG ^ KEY1 ^ KEY2 ^ KEY3
# FLAG = long_to_bytes(FLAG)
# print(FLAG)

# flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# flag = bytes.fromhex(flag)
# for key in range(256):
#     cipher = bytes([b^key for b in flag])
#     if bytes('_', 'utf-8') in cipher:
#         print(cipher)
#         print(key)

flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
flag = bytes.fromhex(flag)
print(xor(flag, 'myXORkey'.encode()))