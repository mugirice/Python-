#read()
f = open('python.txt')
a = f.read()
f.close()
print(a)

print()

#readlines()
f = open('python.txt')
b = f.readlines()
f.close()

aa = 0
for i in b:
    print(b[aa] , end = "")
    aa += 1

print()
print()

#readline()
f = open('python.txt')
c = f.readline()
 
while c:
    print(c, end = "")
    c = f.readline()
f.close()