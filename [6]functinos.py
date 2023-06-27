#1. functions
def greet():
    print("Hello Sir!!!")


greet()

#2. passing parameter and argument in functions

def welcome(first_name, last_name):                     #PARAMETERS:inputs that we define our function
        print("Hello", first_name,"Welcome!")
        print(f"We hope Mr. {last_name} had an amazing experience")


welcome("Ravi", "Shastri")                               #ARGUMENTS:actual value for a given parameter
welcome("john","smith")

#3. Types of Functions:
def result(num1,num2):
    return num1+num2

print(result(5,3))
print(result(num1=5,num2=8))

#4. default parameter;optional parameter should always come after required parameter rightmost
def result1(num4,num5=1):
    return num4*num5
print(result1(6))
print(result1(7,8))

#5. working with tuples
def multiply(*numbers):
    total=1
    for number in numbers:
        total=number*total
    return total

print(multiply(5,6,10,2))
#concept of dictionary **

#6.Scopes

a="global variable"
def fun_b():
    b="local variable"
    print(b)
fun_b()





#FizzBuzz
def fizz_buzz(n):
    if (n % 3) and (n % 5) == 0 :
        return"FIZZBUZ"

    if n % 3 == 0:
        return"fizz"
    if n % 5 == 0:
        return"buzz"
    return n
print(fizz_buzz(15))
