[1, "hola", 1.34, True, [1, 2, 3]]
colors = ["red", "blue", "green"]

numbers_list = list((1, 2, 3, 4))
# print(type(numbers_list))

# r = list(range(1, 101))
# print(r)

# print(len(colors))

# print(colors[1])

# print("blue" in colors)

# print(colors)
# colors[2] = "yellow"

# print(colors)

# print(dir(colors))

# colors.append("violet")
# colors.extend(["violet", "yellow"])
# colors.extend(["pink", "black"])


# colors.insert(1, "violet")
colors.insert(len(colors), "violet")
print(colors)

colors.pop()
print(colors)

colors.remove("red")
print(colors)

colors.sort()

print(colors)
