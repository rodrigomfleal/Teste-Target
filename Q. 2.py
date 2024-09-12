num_informado = int(input("Informe um número: "))

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n


if fibonacci(num_informado):
    print("O número pertence a sequência!")
else:
    print("O número NÃO pertence a sequência!")
