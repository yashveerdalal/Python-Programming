squares = {x:x**2 for x in range(11) }
for key, pair in squares.items():
    print(key," ",pair)

keys = ['1','2','3','4','5']
default_value = "test"


new_dict = dict.fromkeys(keys,default_value)
print(new_dict)