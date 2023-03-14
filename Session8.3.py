fp = open("dracula.txt")
count = 0
for line in fp:
    line = line.lower()
    count = count + line.count("dracula")
#    if "Dracula" in line:
#        count = count + 1
print(f"The word dracula shows up {count} times")