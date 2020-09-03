a,b=input(),input()
di={"zhangir":"qwertyu","hsdsf":"sdhfs"}
try:
    di[a]==b
except KeyError:
    print("Login or pass not right")
else:
    print("Right")