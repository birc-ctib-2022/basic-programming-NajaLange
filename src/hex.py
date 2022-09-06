import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]


match command:
    case "encode":
        list = []
        for i in x:
            list.append(hex(ord(i)))
            encoding = ''.join(list)
        print(encoding)

    case "decode":
        y = (x.split("0x"))
        y.pop(0)
        list =[]
        for x in y:
            list.append((chr(int(x, base = 16))))
        decoding = "".join(list)
        print(decoding)
