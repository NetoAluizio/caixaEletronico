#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
- Exemplo 1: 
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
- Exemplo 2: 
Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
uma nota de 5 e quatro notas de 1.
"""
while True:
    valor = input('Informe o valor do saque: ')
    if (valor.isnumeric()):
        valor = int(valor)
        saque = int(valor)
        if (valor >= 10) and (valor <= 600):
            break
        else:
            print('Valor mínimo de saque: R$ 10,00. Valor máximo de saque: R$ 600,00')
    else:
        print('Valor inválido.')
        continue
        
cem = int(valor / 100)
valor = valor - (cem*100)
    
cinquenta = int(valor/50)
valor = valor - (cinquenta*50)

dez = int(valor/10)
valor = valor - (dez*10)

cinco = int(valor/5)
valor = valor - (cinco*5)

um = valor

notas = []

if cem == 0:
    notaCem = ''
else:
    if cem == 1:
        notaCem = (f'{cem} nota de R$ 100,00')
        notas.append(notaCem)
    else:
        notaCem = (f'{cem} notas de R$ 100,00')
        notas.append(notaCem)
    
if cinquenta == 0:
    notaCinq = ''
else:
    notaCinq = (f' 1 nota de R$ 50,00')
    notas.append(notaCinq)
    
if dez == 0:
    notaDez = ''
else:
    if dez == 1:
        notaDez = (f'{dez} nota de R$ 10,00')
        notas.append(notaDez)
    else:
        notaDez = (f'{dez} notas de R$ 10,00')
        notas.append(notaDez)
    
if cinco == 0:
    notaCinco = ''
else:
    notaCinco = (f' 1 nota de R$ 5,00')
    notas.append(notaCinco)
    
if um == 0:
    notaUm = ''
else:
    if um == 1:
        notaUm = (f'{um} nota de R$ 1,00')
        notas.append(notaUm)
    else:
        notaUm = (f'{um} notas de R$ 1,00')
        notas.append(notaUm)

print(f'Para sacar a quantia de {saque} reais, você receberá: ', end = '')
if len(notas) == 1:
    print(f'{notas[0]}.')
elif len(notas) == 2:
    print(f'{notas[0]} e {notas[1]}.')
elif len(notas) == 3:
    print(f'{notas[0]}, {notas[1]} e {notas[2]}.')
elif len(notas) == 4:
    print(f'{notas[0]}, {notas[1]}, {notas[2]} e {notas[3]}.')
else:
    print(f'{notas[0]}, {notas[1]}, {notas[2]}, {notas[3]} e {notas[4]}.')


# In[ ]:




