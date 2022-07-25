# Return a new list with each element multiplied by 5

nums = [56, 34, 34, 1, 1, 1, 23, 12, 89, 89, 89, 70, 56] 


newNums = []
for i in nums:
    five =i*5
    newNums.append(five)
print(newNums)














# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).
l = [("name", "Elie"), ("job", "Instructor")]
res = {}
res2 = {}


for i in range(len(l)):
    res[l[i][0]]=l[i][1]

print(res)
res2.update(l)
print(res2)






