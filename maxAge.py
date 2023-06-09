max_age = -1
max_name = ""
file_handler = open("names.txt", "r")
for line in file_handler:
    (name, age) = line.rstrip().split("\t")
    if int(age) > max_age:
        max_age = int(age)
        max_name = str(name)
print("Max Age: ", max_age)
print("Max Name: ", max_name)    

file_handler.close()
