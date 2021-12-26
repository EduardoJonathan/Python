def new_func():
    fib = [0, 1]
    n = int(input('Digite um número: '))
    i = 2
    while i < n:
        ant = fib[i - 1]
        ant_ant = fib[i - 2]
        atual = ant + ant_ant
        fib.append(atual)
        i += 1
    print(fib)


new_func()
