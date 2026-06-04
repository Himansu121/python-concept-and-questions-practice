# find the first non- repeated charcter in a string
string="teeterabababa"
for char in string:
    print(char)
    if string.count(char)==1:
        print( " the charcter is: ",char)
        break
        