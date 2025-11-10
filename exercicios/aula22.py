# entrada = input('[E]ntrar ou [S]air: ')
# senha_digitada = input('Digite sua senha: ')

# senha_permitida = '123456'


# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida :
#     print('Você entrou no sistema.')
# else : 
#     print('Você saiu do sistema.')

senha = input('Digite sua senha: ') or 'Sem Senha'
print(senha)