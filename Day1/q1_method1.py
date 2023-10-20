hex_string = input('Enter hexadecimals: ')

dec_string = int(hex_string, 16)

bin_string = bin(dec_string)
bin_string = bin_string[2:]

print(bin_string)
