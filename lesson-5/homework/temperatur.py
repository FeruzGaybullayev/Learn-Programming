# Task 1
# Write a script called temperature.py that defines two functions:

# # F = C * 9/5 + 32 convert_cel_to_far()
def convert_cel_to_far(cel):
    far = cel * 9/5 + 32
    return far

# C = (F - 32) * 5/9 convert_far_to_cel()
def convert_far_to_cel(far):
    cel = (far - 32) *5/9
    return cel

user_input_far = float(input('Convert Celsius to Celsius. Enter Fahrenheit: '))
in_cel = convert_far_to_cel = convert_far_to_cel(user_input_far)

result1 = f'{in_cel:.2f}'
print(result1, 'Celsius')


user_input_cel = float(input('Convert Celsius to Fahrenheit. Enter Celsius: '))
in_far = convert_cel_to_far(user_input_cel)

result2 = f'{in_far:.2f}'
print(result2, 'Fahranheit')
