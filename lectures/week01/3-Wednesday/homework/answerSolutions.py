# July 7th, 2022
# Number 3

coin_tally = 0
print("You have 0 coins.")
give_coin = input("Would you like a coin?")
while give_coin == "yes":
    coin_tally +=1
    print(f"You have {coin_tally} coins")
    give_coin = input("Do you want another?")
else:
    print("Bye")


# Number 4

width = input("width? ")
width = int(width)

height = input("height? ")
height = int(height)

print("*"*width)

while (height-2 > 0):
    print("*" + " " * (width-2) + "*")
    height -=1
    
print("*"*width)

# Number 5 

triangle_rows = int(input("amount of rows in triangle?"))
for star in range(1, triangle_rows + 1):
    amount_space = triangle_rows - star
    amount_star = 2 * star - 1
    print((" " * amount_space)+ ("*" * amount_star))


height = int(input("What is the height? "))

i = 0
while i < height:
    # print((height - 1) * " " + "*" * (2(i + 1)- 1) + (height - 1) * " ")
    # print((height - i) * ' ' + (1 + 2*i) * '*' + (height - i) * ' ')
    print((height - i) * " " + (2 * (i + 1) - 1) * "*" + (height - i) * " ")
    i +=1



# height = int(input('Enter a height >> '))

# count = 0 
# stars = 1

# base_width = height * 2 - 1

# while count <  height : 
#     star = '*' * stars
#     count +=1 # count = count + 1
#     stars +=2 # stars = stars + 2 
#     print(star.center(base_width))