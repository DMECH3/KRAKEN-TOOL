import base64 as b6

print("Encode or decode")
decide = input("")
if decide == "encode":
    encode = input("Enter the text to encode: ")
    encoded_bytes = b6.b64encode(encode.encode())
    encoded_str = encoded_bytes.decode()   
    print("Encoded:", encoded_str)
    input('press enter to stop...')
if decide == "decode":
    decode = input("Enter the base64 to decode: ")
    decoded_bytes = b6.b64decode(decode)
    decoded_str = decoded_bytes.decode()
    print("Decoded:", decoded_str)
    input('press enter to stop...')