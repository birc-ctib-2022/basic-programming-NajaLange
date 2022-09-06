
# Print the pattern


count = "*"
count2 = 3

for x in range(1,10):
    if x == 0:
        print(count*(x))
    elif x <= 5:
        print((count + " ")*(x-1)+ count)
    elif x <= 9:
        print((count + " ")*(x-count2)+ count)
        count2 = count2 + 2
    else:
        print(count)