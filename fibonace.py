1
1
1+1=2
2+1=3
3+2=5
5+3=8
8+5=13
13+8=21
21+13=34
34+21=55
55 +34 =89
89+55=144
144

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + fibo(num-1)
