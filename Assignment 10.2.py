name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    line = line.strip()
    wds = line.split()
    if len(wds) < 3 or not line.startswith('From'): continue
    w = wds[5].split(':')
    di[w[0]] = di.get(w[0], 0) + 1
x = (sorted([(k, v) for k, v in di.items()]))
for k,v in x[0:]:
    print(k,v)