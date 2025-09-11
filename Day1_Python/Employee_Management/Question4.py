name_inupt = input("Enter name seperated by spaces: ")

names_list = name_inupt.split()

names_list.sort()

names_tuple = tuple(names_list)

with open('namesInfo.txt', 'w') as f:
    f.write("Sorted names List "+str(names_list) +"\n")
    f.write("Names Tuple: \n")
    f.write(str(names_tuple) + '\n') 

print("Reading data from 'namesInfo.txt': ")
with open('namesInfo.txt','r') as f:
    content = f.read()
    print(content)