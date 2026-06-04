# multiplication table but skip the 5th iteration
number=25
for i in range(1,11):
    if i==5:
        continue
    
    print(number, 'x', i, '=', number*i)