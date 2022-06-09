# ====== Dictionaries ====== #

# List


# my_dog = ["Clara", "Black", "Noisy Bastard"]


#! Dictionary
# my_dog2 = {"name": "Ernie", "colour": "Yellow", "mood": "Good Boii"}
# # #           "key":"value"

# # name = my_dog2["name"]

# # print(f"My dog is called {name}")
# # print("My dog is " + my_dog2["colour"] + " and is a " + my_dog2["mood"] + "!")
# # # print(my_dog2["name"])

# # for x in my_dog2.items():
# #     print(x)
# #        # prints both key and value e.g: name, ernie

# # for x in my_dog2.keys():
# #     print(x)
# #        # prints dictionary keys e.g name, colour, mood

# # for x in my_dog2.values():
# #     print(x)
# #         # prints the dictionary values e'g: ernie, yellow, good boii

# print(list(my_dog2.keys())) # .method() tells syntax which bit of code to list
#     # output == ['name', 'colour', 'mood']


doggo = {
    "one": {
        "name": "Oscar",
        "colour": "Black",
        "mood": "Old Boii"},
    "two": {
        "name": "Clara",
        "colour": "Black",
        "mood": "Noisy Bastard"},
    "three": {
        "name": "Ernie",
        "colour": "Yellow",
        "mood": "Good Boii"}
}

# print(list(doggo.get("one").items()))
# prints as a list/truple/
# .get() chooses key "one"
# itsms chooses every value and key in one

# for j in doggo.keys():
#     print(j)

# for j in doggo.values():
#     print(j)

# for j in doggo.items():
#     print(j)

doggo.setdefault("Old Boii", True)

doggo.setdefault("mood", "sleepy")
doggo["one"].pop("mood")


print(list(doggo.items()))
