file=open('file1.txt','r')
points = []
f = open('file1.txt')
points1 = f.read().splitlines()
f.close()
print(points1)

file=open('file2.txt','r')
points = []
f = open('file2.txt')
points2 = f.read().splitlines()
f.close()
print(points2)