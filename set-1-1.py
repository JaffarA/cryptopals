from tools import hex_to_base64


expected_out = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
if __name__ == "__main__":
    string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    assert hex_to_base64(string) == expected_out, f'output is \n\nOUT:\n{string}\n\nEXPECTED:\n{expected_out}'
