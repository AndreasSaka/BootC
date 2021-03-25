def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + fibo(num-1)
