num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

nums = list((num1, num2, num3))
nums.sort()
print(f'Ordem crescente: {"".join(str(nums))}')