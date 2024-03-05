stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
mantissa, exponent = stdform.split("x10^")
print("This number in E notation is {}E{}.".format(mantissa, exponent))