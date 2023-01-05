import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

anos = int(input("Quantos anos você fuma? "))
dia = int(input("Quantos maços por dia? "))
preco = float(input("Preço do maço: "))

#um maço tem em média, 20 cigarros

valor = 365 * anos * dia * preco
quant = 365 * anos * dia * 20

print(f'Parabéns, chaminé! Tu conseguiu baforar aproximadamente {quant} cigarros!!! E isso tudo lhe custou {locale.currency(valor)}!!! PARABÉNS!!!')