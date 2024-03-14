# 1. Write a function to compute the value of x raised to the power y without using the built-in pow or ** operator.
def power_of_a_number(x,y):
    answer = x
    for i in range(y):
        answer = x*answer
    return answer
print(power_of_a_number(2,5))


# 2. Write a function that takes a list of numbers as input and returns the minimum and maximum values in the list as a tuple.
def min_and_max(x):
    minimum = min(x)
    maximum = max(x)
    return(minimum,maximum)

print(min_and_max([1,2,5,57,7,386,32,9]))


# 3. Write a function that takes a year is input and returns True if it's a leap year, and False otherwise. A leap year is divisible by 4 bot not divisible by 100 unless it is also divisible by 400.
def check_leap_year(x):
    if x% 400 == 0: 
        return True
    elif x% 4 == 0:
        if x% 100 != 0:
            return True
    return False
print(check_leap_year(2013))
print(check_leap_year(2024))
print(check_leap_year(3200))


# 4. Write a function that takes a person's weight (in kilograms) amd height (in meters) as input and returns their BMI.
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi
print(calculate_bmi(85, 1.66))


# 5. Implement a function called rotate digits that takes an integer n as input and rotates its digits to the right by one position.
def rotate_digits(x):
    last_digit = x % 10
    remaining_digits = x // 10
    digits = 1
    temp = remaining_digits
    while temp > 0:
        temp //= 10
        digits += 1
    rotated_number = last_digit * (10 ** (digits - 1)) + remaining_digits
    return rotated_number
print(rotate_digits(37129))


# 6. For both minimum and maximum, write one function to manually find that value using a for loop and another to manually find it using a while loop
def find_minimum_for_loop(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum

def find_minimum_while_loop(arr):
    minimum = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] < minimum:
            minimum = arr[i]
        i += 1
    return minimum

def find_maximum_for_loop(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

def find_maximum_while_loop(arr):
    maximum = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] > maximum:
            maximum = arr[i]
        i += 1
    return maximum

arr = [3, 7, 1, 9, 2, 8]

print("Minimum (for loop):", find_minimum_for_loop(arr))
print("Minimum (while loop):", find_minimum_while_loop(arr))
print("Maximum (for loop):", find_maximum_for_loop(arr))
print("Maximum (while loop):", find_maximum_while_loop(arr))


# 7. Write a function which takes in a string and outputs the number of vowels.
def vowel_count(x):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in x:
        if char in vowels:
            count += 1
    return count

print(vowel_count('supercalifragilisticexpialidocious'))


# 8. Write a function that takes in an integer and returns the sum of the digits(the digital root).
def digital_root(x):
    sum = 0
    while x > 0:
        digit = x % 10
        sum += digit
        x = x//10
    return sum
print(digital_root(928))