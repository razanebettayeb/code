#6008514743
i = 2

while i < 6008514743:
    if (6008514743 % i == 0):
        print(i)
    i += 1
    
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum = 0
for number in numbers:
    if number % 3 == 0 or number % 5 == 0:
        sum +=number
print(sum)    

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b



# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print (x)