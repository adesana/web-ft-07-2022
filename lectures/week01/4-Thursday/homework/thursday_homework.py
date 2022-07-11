# Number 1

count1 = 0

list1 = [2, 4, 5]
list2 = [2, 3, 6]
list3 = []

while count1 < len(list1):
    answer = (list1[count1]*list2[count1])
    count1 +=1
    list3.append(answer)
print(list3)



# Number 2

index1 = 0

matrix = [ [2, -2], [5, 3]]
list4 = []
list5 = []
matrix2 = [[1,2],[3,4]]
matrix3 = []
while index1 < len(matrix):
    result = matrix[0][index1] + matrix2[0][index1]
    result2 = matrix[1][index1] + matrix2[1][index1]
    list4.append(result)
    list5.append(result2)
    index1 +=1
matrix3.append(list4)
matrix3.append(list5)
print(matrix3)

# Number 3

mtrx = [ [2, -2], [5, 3], [1, 1]]
mtrx2 = [[1,2],[3,4], [1, 1]]
lst3 = []
result = [mtrx[i][j] + mtrx2[i][j] for i in range(len(mtrx)) for j in range(len(mtrx[0]))]
     
print(result)

# Number 4


l = [1, 1, 2, 2, 3, 3, 4, 4]
nl = []
for x in l:
    if x not in nl:
        nl.append(x)
print(nl)

# Number 5

letters = ['a','e','i', 'o', 's', 't']
nmbrs = str([4, 3, 6, 1, 0, 5, 7])
sentence = input('Please say your sentence >>>>')
for q in letters:
    for a in nmbrs:
        if q in sentence:
           newsentence = sentence.replace(q,a)
print(newsentence)








# Number 6


vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Please enter a word>>>>>')

for x in vowels:
    if x in word:
        x1 = x*5
        newword = word.replace(x,x1)
        
        
print(newword)
