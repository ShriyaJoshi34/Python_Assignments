a=int(input("Enter number of rows in Matrix1"))
b=int(input("Enter number of column in Matrix1"))
Mat1 = []
for i in range(0,a):
    Mat1.append([])
for i in range(0,a):
    for j in range(0,b):
        Mat1[i].append(j)
        Mat1[i][j]=0
        print("entry in row: ",i+1,"column: ",j+1)
        Mat1[i][j] = int(input())
print(Mat1)

c=int(input("Enter number of rows in Matrix2"))
d=int(input("Enter number of column in Matrix2"))
Mat2 = []
for i in range(0,c):
    Mat2.append([])
for i in range(0,c):
    for j in range(0,d):
        Mat2[i].append(j)
        Mat2[i][j]=0
        print("entry in row: ",i+1,"column: ",j+1)
        Mat2[i][j] = int(input())
print(Mat2)
result = []
for i in range(0,a):
    result.append([])
for i in range(0,a):
    for j in range(0,d):
        result[i].append(j)
        result[i][j]=0
for c in range(len(Mat1)):
    for d in range(len(Mat2[0])):
        for r in range(len(Mat2)):
            result[c][d] += Mat1[c][r] * Mat2[r][d]
print(result)
