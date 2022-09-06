from curses.ascii import isupper
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

count = []
for x in password:
    if 1 not in count:
        if x.islower():
            count.append(1)
    if 2 not in count:
        if x.isupper():
            count.append(2)
    if 3 not in count:
        if x.isnumeric():
            count.append(3)
    if 4 not in count:
        if x in "$#@":
            count.append(4)
    if 5 not in count:
        if 6 < len(password) < 16 : 
            count.append(5)
if len(count) == 5: 
    is_valid = "TRUE"



print(is_valid)
