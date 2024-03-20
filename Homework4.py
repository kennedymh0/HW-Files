# 2.1 Part 1
number_list = list(range(51))

print(number_list)

# 2.2 Part 2
def square(lis):
    squared_list = [num**2 for num in lis]
    return squared_list

lis = [2, 3, 4]
print(square(lis))

# Error 1: Type Error Accididentally typed 'list' instead of 'lis' in line 12

# 2.3 Part 3
def odd_integers_sorted(listA, listB):
    combined_list = listA + listB
    odd_numbers = [num for num in combined_list if num % 2 != 0]
    return sorted(odd_numbers)

listA = list(range(1,11))
listB = list(range(20,31))

result = odd_integers_sorted(listA, listB)
print(result)


#3.1 Part 1
lists = [[0 for x in range(5)] for y in range(5)]

num = 1
for i in range(5):
    for j in range(5):
        lists[i][j] = num
        num += 1

for row in lists:
    print(row)

# 3.2 Part 2

for i in range(5):
    for j in range(5):
        if lists[i][j] % 3 == 0:
            lists[i][j] = '?'

for row in lists:
    print(row)

# Error 2: not realy an error I recieved but it kept returning either full lists of questions marks or 0's. I did not need to rewrite defining the 'lists', so i deleted the second time i defined it.

# 4. More list Practice
def remove_duplicate(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

ex_list = [1,2,3,4,2,3,5]
result = remove_duplicate(ex_list)
print(result)