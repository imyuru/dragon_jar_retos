c = [120, 114, 127, 121, 101, 127, 65, 124, 119, 106, 65, 122, 119, 120, 120, 119, 125, 107, 114, 106, 65, 108, 119, 106, 123, 99]
key = 30

decrypted_message = [byte ^ key for byte in c]

print(decrypted_message)
decrypted_message_as_string = ''.join([chr(byte) for byte in decrypted_message])

print(decrypted_message_as_string)
