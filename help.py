with open(".\Don'tTouchMyPresents\Don'tTouchMyPresents", 'rb') as file:
    # Read the binary data from the file
    binary_data = file.read()

# Now, you can work with the binary data as needed
# For example, you can print the binary data as a hexadecimal string
hex_string = binary_data.hex()
print(hex_string)