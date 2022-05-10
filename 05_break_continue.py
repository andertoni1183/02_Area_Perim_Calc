print()
print("*** Looping Demo #2 ***")
print()

for item in range(0, 5):
    print(item)

    # ask the user if they want to keep going...
    keep_going = input("<enter> to keep looping, or amy key to quit")

    #ending loop if user if they want to keep going...
    if keep_going != "":
        break

print()
print("We are done")
print()