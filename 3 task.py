x1,y1=int(input()),int(input())
x2,y2=int(input()),int(input())
x,y=int(input()),int(input())
k=(y2-y1)/(x2-x1)
b=y1-k*x1
if y>k*x+b:
    print("Выше")
else:
    print("Ниже")