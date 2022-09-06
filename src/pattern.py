
# Print the pattern


count = "*"
count2 = 2

for x in range(1,10):
    if x == 0:
        print(count*(x))
    elif x <= 5:
        print((count + " ")*(x))
    elif x <= 9:
        print((count + " ")*(x-count2))
        count2 = count2 + 2
    else:
        print((count)*(x-count2))