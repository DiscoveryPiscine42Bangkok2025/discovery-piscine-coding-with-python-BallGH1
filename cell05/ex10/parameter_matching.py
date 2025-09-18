import sys

if len(sys.argv) != 2:
    print("none")
else:
    target = sys.argv[1]
    answer = input("What was the parameter? ")
    if answer == target:
        print("Good job!")
    else:
        print("Nope, sorry...")