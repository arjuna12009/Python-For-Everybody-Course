# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print('Enter a valid file')
    quit()
for line in fh:
    l= line.upper()
    w = l.strip()
    print(w)
