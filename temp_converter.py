# value = float(input("Enter a Value"))
# temp = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ").strip().upper()

# if temp == 'C':
#     converted_value = (value * 9/5) + 32
#     print(f"{value}°C is equal to {converted_value}°F")
# elif temp == 'F':
#     converted_value = (value - 32) * 5/9
#     print(f"{value}°F is equal to {converted_value}°C")
# else:
#     print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


c_to_f = input("Enter Temp from C to F: ")
print(float(c_to_f) * 9/5 + 32)

f_to_c = input("Enter Temp from F to C: ")
print(float(f_to_c) - 32 * 5/9)