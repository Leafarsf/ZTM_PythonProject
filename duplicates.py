some_list = ['a','b','c','b','d','m','n','n']
duplicate_list = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicate_list:
            duplicate_list.append(i)
print(f"The repeating letters are: {duplicate_list}")