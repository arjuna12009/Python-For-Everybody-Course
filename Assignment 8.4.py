fname = input("Enter file name: ")
if len(fname) < 1: fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:				#iterate through each line of text
    for i in line.split():	#iterate through each word of line
        if i in lst: continue
        lst.append(i)
lst.sort()
print(lst)
