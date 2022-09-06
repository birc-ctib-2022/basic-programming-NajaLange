
# Print the numbers described in the exercise

from readline import append_history_file


count = ""

for x in range(1,11):
    if x == 1:
        count = count + str(x)
    else:
        count = count + " " + str(x)
    print(count)
