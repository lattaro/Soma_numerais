n = int(input("Digite um número inteiro"))

i = 10
x = 0

while (n // i) > 0:
    x = x + n % i
    n = n // i
print (x + n)