from tools import xor
from tools import hex_to_base64


expected_out = '746865206b696420646f6e277420706c6179'
if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"

    result = xor(hex1, hex2)
    print(result)
