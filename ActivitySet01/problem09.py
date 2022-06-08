# Lists

filename = "dataset/romeo.txt"
fname=input('enter the file name ')
fh=open(fname)
lst=list()

for line in fh:
  world=line.rstrip().split()
  for element in world:
    if lement in line:
      continue
    else:
      lst.append(element)

l=lst.sort()
print(l)