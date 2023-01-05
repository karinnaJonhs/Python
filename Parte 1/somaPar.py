num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

nums = list((num1, num2, num3, num4))
print(nums)
soma = 0

for i in range(0,4):
    if(nums[i] % 2 == 0):
        soma += nums[i]

print(f'A soma dos números pares é: {soma}')


