# # ------ Truthy/Falsey ------ #
# print("What is your name?")
# name = input()
# if name:
#     print(f"Hello {name}, how are you?")
# else:
#     # if value is falsey ie. black, else is met
#     print("You did not give me your name!")


# # ------ Not Operator ------ #

# bool = False  # our input
# if bool != True:  # not true
#     print(False)
# else:
#     print(True)

# # ------ Try Except ------ #


def add_up():
    n1 = input("1st num\n")
    n2 = input("2nd num\n")

    try:
        print(f"{n1} + {n2} is {(int(n1) + int(n2))}!")

    except:
        print("*******************")
        print("ERROR: only numbers")
        print("*******************")
        add_up()


add_up()


# def add_up1():
#     n1 = input("1st num\n")
#     n2 = input("2nd num\n")

#     try:
#         if (n1 + n2) == 4:
#             print(n1 + n2)

#     except:
#         print("There is error")
#     else:
#         print("whats happening here")
#     finally:
#         print("i give up")

#         add_up()


# add_up1()

# ------ Scope ------ #
# light = False


# def light_switch():
#     global light  # makes variable global throught code
#     if light:
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("HEY! Who turned out the lights?")
#         light = True


# light_switch()
# light_switch()

# # ------ Lists and Tuple ------ #

# even_nums = [2, 4, 6, 8, 10]  # list #?Mutablle
# odd_nums = (1, 3, 5, 7, 9)  # tuple #?Immutable

# # lists can be changed, tuples cannot

# even_nums[-1] = "ten"
# #! odd_nums[-1] = "nine" --> Error

# # ------ Slicing ------ #

# aplphabet = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z"]
# # the alphabet in a list


# def user():
#     usernum = input("1-26?\n")
#     usernum = int(usernum) - 1
#     print(usernum)

#     return aplphabet[:12]


# print(user())

# ------ WHILE ------ #

# while True: #loop_runs = True
#     print("Run orever")

#     loop_runs = False #stops loop

# loop = True
# name = input("\nUsername:")

# while loop:
#     if name == "Admin":
#         print(f"Hello {name}")
#         break
#     else:
#         print(f"Fuck Off {name}")
#         continue
