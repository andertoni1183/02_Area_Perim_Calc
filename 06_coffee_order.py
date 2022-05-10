print()
print("*** Coffee Order Demo ***")

keep_going = ""
while keep_going == "":

    want_coffee = input("Do you want coffee?")
    if want_coffee != "yes":
        print("wrong answer, you always want coffee")
        continue

    else:
        print("good choice")
        break

print()
print("End of program")
print()
