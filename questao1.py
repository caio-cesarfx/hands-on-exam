def fibonacci(n):
    if n<0:
        print(f"Somente valores positivos.")
    elif n==0:
        print(0)
    nx, n1, n2 = 0, 0, 1
    while nx <= n:
        print(n1)
        nx = n1 + n2
        n1 = n2
        n2 = nx
    print(n1)

fibonacci(int(input(f"Insira um número positivo")))