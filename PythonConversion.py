# Converts decimal to binary
def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")


# Converts decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "")

# Asks for a decimal number
decimal_input = int(input("Enter a decimal number: "))


# Convert the decimal number to binary and hexadecimal
binary_value = decimal_to_binary(decimal_input)
hexadecimal_value = decimal_to_hexadecimal(decimal_input)

# Spaces it out
print()

# Prints the results
print("The binary of " + str(decimal_input) + " is " + binary_value)
print("The hexadecimal of " + str(decimal_input) + " is " + hexadecimal_value)