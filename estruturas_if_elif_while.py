def decimal_para_binario(decimal):
    binario = ''
    while decimal > 0:
        binario+= str(decimal%2)
        decimal//= 2
    return binario[::-1]
try:
  if __name__ == '__main__':
      num = int(input("Digite um número:"))
      print("O número em binário é: "+decimal_para_binario(num))
except:
  print("Entre com o valor numérico e não letras")