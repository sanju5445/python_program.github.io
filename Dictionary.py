dict={
    "brand":"Lambarghini",
    "Modle":"Aventadour",
    "Year":1999,
    # "year":2000
}
# print(len(dict))
# print(type(dict))
# print(dict)
# print(dict["brand"])
# print(dict["Year"])


dct={
    "brand":"Lambarghini",
    "model":"Aventadour",
    "year":2000,
    "colors":["red","green","yellow","purple"]
}
# print(dct)
# print(dct["colours"])
# for i,j in dct:
#     print(i)
# print(dct.get(""))
# print(dict)
# for i in dct:
#     print(dct[i])
# print(len(dct))
# print(dct["colors"])
# for i in dct["colors"]:
#     print(i)

# print(dct.keys())
print(dct.values())
# print(dct.items())
# print(dct.get("modellcavhsdvhsdau bisudvisug "))
# print("The model is: ",dct["model"])


dct["price"]=50000000
# print(dct.items())
# print(dct)
# dct["colors"]="blue"
# print(dct)
# print(dct.items())

# if "model" in dct:
#     print("yes")

dct.update({"m":200})
dct.update({"colors":["blue","red","green","yellow","purple"]})
print(dct)
dct.popitem()
print(dct)
del dct["price"]
print(dct)
# dct.popitem()
dct["colors"].pop(4)
print(dct)
print(dict)
# dict.clear()
print(dict)
# print(dict)
# print(dict)
del dict
# print(dict)
print(dict)
for i in dct.values():
    print(i)
# for i in dct:
#     print(dct[i])
dict=dct.copy()
print(dict)
dct.update({"price":50000000})
print(dct)