# Hexadecimal to Binary Conversion

def hex_to_bin(hex_string):
    hex_to_bin_dict = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    bin_output = ""

    for i in hex_string:
        if i.upper() in hex_to_bin_dict:
            bin_output += hex_to_bin_dict[i.upper()]
    
    return bin_output

hexa_string = input('Enter hexadecimals: ')
bin_string = hex_to_bin(hexa_string)

print(bin_string)