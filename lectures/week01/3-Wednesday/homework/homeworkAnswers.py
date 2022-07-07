# Number 1

total_bill = float(input("What is the total bill amount?  "))
service = input("How would you rate your service? Good, Fair, or Bad:  ")
good = "${:,.2f}".format(total_bill*.20)
fair = "${:,.2f}".format(total_bill*.15)
bad = "${:,.2f}".format(total_bill*.10)
total_good = "${:,.2f}".format(total_bill*1.2)
total_fair = "${:,.2f}".format(total_bill*1.15)
total_bad = "${:,.2f}".format(total_bill*1.1)
if service == 'Good':
    print(f"""Total Tip: {good}
Total Amount: {total_good}""")
elif service == 'Fair':
    print(f"""Total Tip: {fair}
Total Amount: {total_fair}""")
else:
    print(f"""Total Tip: {bad}
Total Amount: {total_bad}""")

# Number 2


total_bill = float(input("What is the total bill amount?  "))
service = input("How would you rate your service? Good, Fair, or Bad:  ")
people = float(input("How many ways is this being split?    "))
good = "${:,.2f}".format(total_bill*.20)
fair = "${:,.2f}".format(total_bill*.15)
bad = "${:,.2f}".format(total_bill*.10)
total_good = "${:,.2f}".format(total_bill*1.2)
total_fair = "${:,.2f}".format(total_bill*1.15)
total_bad = "${:,.2f}".format(total_bill*1.1)
split_good = "${:,.2f}".format((total_bill*1.2)/people)
split_fair = "${:,.2f}".format((total_bill*1.15)/people)
split_bad = "${:,.2f}".format((total_bill*1.1)/people)
if service == 'Good':
    print(f"""Total Tip: {good}
Total Amount: {total_good}
Amount Per Person: {split_good}""")
elif service == 'Fair':
    print(f"""Total Tip: {fair}
Total Amount: {total_fair}
Amount Per Person: {split_fair}""")
else:
    print(f"""Total Tip: {bad}
Total Amount: {total_bad}
Amount Per Person: {split_bad}""")




# Number 3


count = 0
answer = ''
while answer != 'No':
    count = count + 1    
    print(f"""You have {count} coins.""")
    answer = input("Do you want another?  ")

    






#Number 4

n=int(input("Enter the height:"))
m=int(input("Enter the width:"))

print('*' + '-'*(m) + '*')
for i in range(n):
    print('|' + '.'*(m) + '|')
    
print('*' + '-'*(m) + '*')







#Number 5

def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
triangle(n)