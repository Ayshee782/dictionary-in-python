#dict.keys()

a={
    "b":"hg",
    "c":"gfj",
    "d":"kh",
}
print(a.keys())

#dict.values()

print(a.values())
print(list(a.values()))

#dict.items()

print(a.items())
pairs=list(a.items())
print(pairs[0])

#dict.get("key")
print(a.get("c"))

#dict.update(new_dict)

print(a.update({"b":"kkj"}))