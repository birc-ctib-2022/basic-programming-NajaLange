
# Print the pattern


count = "*"
count2 = 1

for x in range(9):
    if x == 0:
        print(count*(x+1))
    elif x <= 4:
        print((count + " ")*(x+1))
    elif x <= 8:
        print((count + " ")*(x-count2))
        count2 = count2 + 2
    else:
        print((count)*(x-count2))