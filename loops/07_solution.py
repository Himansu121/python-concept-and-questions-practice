# validate input
while True:
    number= int(input("enter anumber b/w 1and10: "))
    if 1 <= number <= 10:
        print("thanks")
        break
    else:
     print("invalid input. please enter a number between 1 and 10.")