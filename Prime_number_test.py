

# User enter a positive Number
print("Function o find a prime number")
user_input = int(input("Enter a Number: "))

# function to test if the number is positive
test_number = 0
if user_input > 0:
    test_number = user_input
# if the number is not positive the function returns a message to the user
else:
    print("The Number entered is not Positive")
# test flag for the function to determine if the number entered is prime or not
flag = False

# function to test if the number the user entered is prime
for i in range(2, test_number):
    # the numbers tested are 2 to the test_number
    if test_number % i == 0:
        flag = True
        break
# display results to the user by printing a message
if flag:
    # if the flag is True the user input is not prime
    print(user_input, " is not a Prime Number")
else:
    # the flag is False the user input is Prime
    print(user_input, " is a Prime Number")

