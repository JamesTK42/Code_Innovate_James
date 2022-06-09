# --- Activity 1 --- #
# def activity_1():
#     code = "Welcome to Code Nation!"


#     lencode = len(code)

#     if lencode % 2 == 0:
#         print(f"The length of '{code}' is {lencode} and is even in length")
#     else:
#         print(f"The length of '{code}' is {lencode} and is odd in length")


# activity_1()


# --- Activity 2 --- #
def activity_2():
    aplphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z"]
# the alphabet in a list

    userchoice = int(input("Choose a number between 1 and 26: "))
    userchoice = int(userchoice) - 1
    final = aplphabet[userchoice]

    print(f"You Chose The Letter: {final.upper()}")


activity_2()
