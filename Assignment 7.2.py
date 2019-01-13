fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
count = 0
w = list()
for line in fh:
    w = line.split()
    if not w.startswith('From'): continue
    words = line.split()
    print(words[1])



