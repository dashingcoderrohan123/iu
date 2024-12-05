def calculate_power(base, exponent):
    # Calculate the power
    result = base ** exponent
    return result

# Taking user input
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate power
result = calculate_power(base, exponent)

# Display the result
print(f"{base} raised to the power of {exponent} is {result}")
