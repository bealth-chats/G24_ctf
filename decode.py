import base64
import binascii

hex_str = "5a7a4a375757396656574666636d56665a325666546d6c7664584e664d4739516331397a6347567364463970564639796232356e66513d3d"
ascii_str = binascii.unhexlify(hex_str).decode('utf-8')
print("Ascii:", ascii_str)

b64_decoded = base64.b64decode(ascii_str)
print("Base64 decoded:", b64_decoded)
