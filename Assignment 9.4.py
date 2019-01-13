name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    line = line.strip()
    wds = line.split()
    if len(wds) < 3 or not line.startswith('From'): continue
    di[wds[1]] = di.get(wds[1], 0) + 1
bigcount = None
bigword = None
for k,v in di.items():
    if bigcount == None or v > bigcount:
        bigword = k
        bigcount = v
print (bigword, bigcount)

