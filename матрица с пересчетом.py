'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:

9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:

3 21 22
10 6 19
20 16 -1
Sample Input 2:

1
end
Sample Output 2:

4
'''
st=input()
a=[]
c=[]
while st!='end':
    a+=[st.split()]
    st=input()
#print(a)
l=len(a[0])
#print(a[-1])
c=[[0 for i in range(l)] for j in range(len(a))]
#print(c)
    
for i in range(len(a)):
    for j in range(l):
        if i<len(a)-1 and j<l-1:
            c[i][j]=(int(a[i-1][j])+int(a[i+1][j])+int(a[i][j-1])+int(a[i][j+1]))
        elif i==len(a)-1 and j<l-1:
            c[i][j]=(int(a[i-1][j])+int(a[0][j])+int(a[i][j-1])+int(a[i][j+1]))
        elif j==l-1 and i<len(a)-1:
            c[i][j]=(int(a[i-1][j])+int(a[i+1][j])+int(a[i][j-1])+int(a[i][0]))
        elif i==len(a)-1 and j==l-1:
            c[i][j]=(int(a[i-1][j])+int(a[0][j])+int(a[i][j-1])+int(a[i][0]))
for i in range(len(a)):
    for j in range(l):
        print(c[i][j],end=' ')
    print()
        
    
