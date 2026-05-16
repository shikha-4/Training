o_list = [1, 2, 4, 6,1,3,5,5]
a = []
duplicates = []

for i in o_list:
    if i in a:
        if i not in duplicates:
            duplicates.append(i)
    else:
        a.append(i)

print(f"Original list: {o_list}")
print(f"Duplicates: {duplicates}")
print(a)