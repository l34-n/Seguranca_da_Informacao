
import random

alfa = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
especiais = "!@#$%&*^|()_+"
cedilha = "ç"

def caracteres_disponiveis(inclui_digitos, inclui_especiais, inclui_cedilha):
    caracteres_disp = alfa
    if inclui_digitos:
        caracteres_disp += num
    if inclui_especiais:
        caracteres_disp += especiais
    if inclui_cedilha:
        caracteres_disp += cedilha
    return caracteres_disp

def gera_senha(cumprimento = 20, 
               minusculo_maiusculo = False, 
               inclui_digitos = False, 
               inclui_especiais = False,
               inclui_cedilha = False):
    senha = []
    caracteres_disp = caracteres_disponiveis(inclui_digitos, inclui_especiais,inclui_cedilha)
    
    for i in range(cumprimento):
        character = random.choice(caracteres_disp)
        
        if minusculo_maiusculo and character.isalpha():
            change_to_upper = random.randint(0, 1)
            if change_to_upper:
                character = character.upper()
                
        senha.append(character)
    return ''.join(senha)


print(
'''
-----------------------------------------------------------------------------------------------
                 ██████╗ ███████╗██████╗  █████╗ ██████╗  ██████╗ ██████╗     
                 ██╔════╝ ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
                 ██║  ███╗█████╗  ██████╔╝███████║██║  ██║██║   ██║██████╔╝    
                 ██║   ██║██╔══╝  ██╔══██╗██╔══██║██║  ██║██║   ██║██╔══██╗    
                 ╚██████╔╝███████╗██║  ██║██║  ██║██████╔╝╚██████╔╝██║  ██║    
                  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                               
               ██████╗ ███████╗    ███████╗███████╗███╗   ██╗██╗  ██╗ █████╗ 
               ██╔══██╗██╔════╝    ██╔════╝██╔════╝████╗  ██║██║  ██║██╔══██╗
               ██║  ██║█████╗      ███████╗█████╗  ██╔██╗ ██║███████║███████║
               ██║  ██║██╔══╝      ╚════██║██╔══╝  ██║╚██╗██║██╔══██║██╔══██║
               ██████╔╝███████╗    ███████║███████╗██║ ╚████║██║  ██║██║  ██║
               ╚═════╝ ╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝                                                                                                                             
-----------------------------------------------------------------------------------------------

A proteção de senha começa com a consciência e instrução ao usuário. 
 Algumas regras para uma senha ideal:

  • Evitar senhas / palavras comuns e pessoais (datas especiais, nomes específicos...);
  • Evitar padrões de teclados. (Ex: 123456);
  • Uma senha diferente para cada cadastro realizado;
  • Utilizar, SEMPRE, autenticação de 2 fatores;
  • Quanto maior a senha, mais difícil de quebrar;
  • Não deixar a senha visível.
''')
def menu():
 while True:        
  e = input('''Escolha uma opção:
    (1) Gerar Senha
    (2) Fechar Programa
    \nSeleção: ''')

  if e == '1':
    tipo_senha()

  elif e == '2':
        print('\nPrograma Finalizado\n')
        break

  else:
    print('\nSeleção Inválida - Por gentileza, escolha ou 1 ou 2')

def tipo_senha():
    cumprimento = int(input('\n1. Quantos caracteres terá a senha: '))
    incluir_maiusculo = input('2. Letras Maiúsculas? (s/n): ').lower().strip() == 's'
    incluir_digitos = input('3. Dígitos? (s/n): ').lower().strip() == 's'
    incluir_especiais = input('4. Caracteres Especiais? (s/n): ').lower().strip() == 's'
    incluir_cedilha = input('5. Adicionar Cedilha(ç)? (s/n): ').lower().strip() == 's'
    print('\nSenha Gerada:', gera_senha(cumprimento, incluir_maiusculo, incluir_digitos, incluir_especiais,incluir_cedilha),'\n')

if __name__ == '__main__':
    menu()
