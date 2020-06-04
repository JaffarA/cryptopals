from codecs import encode
from codecs import decode


def hex_to_base64(hex_str):
  return encode(decode(hex_str, 'hex'), 'base64').decode()


def xor(a, b):
  a = bytes.fromhex(a)
  b = bytes.fromhex(b)
  return bytes([b1 ^ b2 for b1, b2 in zip(a, b)])