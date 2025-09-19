import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    found = False
    for ch in s:
        if ch == "z":
            print("z" , end = "")
            found = True
    if not found:
        print("none")
    print()