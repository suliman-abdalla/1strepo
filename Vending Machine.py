print("Welcome to Candies Vending Machine\n")

x=int(input("How many candies do you want? "))
c=1
total=5
while x>total :
    print("current stock =",total)
    print("do you want to continue with ",total, "candies?")
    z=input()
    if z=='y' or z=='Y':
        while total >= 1:
            print(c, ",CANDIES ", end="")
            total -= 1
            c += 1
        else:
            print("\nTotal = ",c-1,"Candies.")
            break
    if z == 'n' or z == 'N':
        print("No Candies for you")
        break
    else:
        print("Invalid Input")

else:
    while x >= 1:
        print(c, ",CANDIES ", end="")
        x -= 1
        c += 1
    else:
        print("\nTotal = ",c-1,"Candies.")
