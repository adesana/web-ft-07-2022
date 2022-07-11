# Friday July 8//



# result = []
# index = 0
# index2 = 0
# while index < 3:
#     list1 = []
#     while index2 < 3:
#         list1.append(index2)
#         index2 += 1
#     result.append(list1)
#     index2 = 0
#     index +=1
# print(result)





# greeting = 'hello'

# greeting_list = list(greeting)

# print(greeting_list)

# greeting_list[0] = 9

# greeting =''.join(greeting_list)

# print(greeting)



num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: ", reversed_num)