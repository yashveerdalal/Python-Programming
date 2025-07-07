# tuple is basically just immutable list 
fruits = ("apple","mango","banana","cherry")
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[:3])
print(len(fruits))
new_fruits = ("pomegranate","guava","blackberry")
all_fruits = fruits+new_fruits
print(all_fruits)
if "banana" in all_fruits:
    print("banana is there")

# count will give away the count as for the unique values inside of the tuple 


(tasty, healthy, zesty, sour) = fruits

# this is known by the name un-wrapping 
print(tasty)