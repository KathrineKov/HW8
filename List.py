Mylist = [1, "MIBA", 3.14, "st", True, "Python", 13]
string_count = 0

for i in Mylist:
    if type(i) == str:
        string_count += 1

print("Number of strings in the list:", string_count)