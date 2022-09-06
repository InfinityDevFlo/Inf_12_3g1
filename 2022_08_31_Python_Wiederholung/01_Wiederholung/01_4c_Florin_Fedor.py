names = ["Luke Skywalker", "Darth Vader", "Anakin Skywalker"]
usernames = list()

for name in names:
    split = name.split(" ")
    forname = split[0].lower()
    lastname = split[1].lower()
    usernames.append(forname + "_" + lastname)


print(usernames)
