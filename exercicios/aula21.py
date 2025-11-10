entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '123456'


if entrada == 'E' and senha_digitada == senha_permitida :
    print('Você entrou no sistema.')
else : 
    print('Você saiu do sistema.')
    
print(True and False and True)
print(True and 0 and True)

if 0 and 1:
    print('true and 1')