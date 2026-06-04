# counting  the positive number in a list
numbers=[1,-2,3,-4,5,6,7,-8,9,10]
positive_count_numbers=0
for num in numbers:
    if num>0:
        positive_count_numbers += 1
        
print("the number of positive numbers in the list is:",positive_count_numbers)        