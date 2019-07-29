import sys
mlist = []
sum = 0
for n in sys.argv:
    mlist.append(n)

for i in mlist[1:]:
    sum += int(i)

print(sum)
