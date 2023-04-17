# section B from 2018 paper

while True:
    num = int(input("Enter a number: "))
    primeBool = True
    if num <= 1:
        print("Not greater than 1")
    else:
        for i in range(2,num-1):
            if num % i == 0:
                primeBool = False
                break
        if primeBool:
            print("Is prime")
        else:
            print("Is not prime")
    quitQ = input("Do you want to quit? (y/n): ")
    if quitQ == "y":
        break