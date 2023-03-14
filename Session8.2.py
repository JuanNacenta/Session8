import requests
# simplest way to work with a file
fp = open("text.txt")
print(fp.read())
fp.close()

fp = open("text.txt")

# files are iterable !!
for line in fp:
    print(line.rstrip())
    # print(line[:-1])
    # print(line, end="")

r = requests.get("https://www.gutenberg.org/cache/epub/345/pg345.txt")
# print(r.text)
# print(r.content)
fp = open("dracula.txt", "wb")
fp.write(r.content)
