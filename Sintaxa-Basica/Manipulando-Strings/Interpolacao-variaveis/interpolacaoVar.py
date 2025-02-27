# Old Style --> % Usando Porcentagem

nome = input("Insira seu nome: ") 
idade = int(input("Insira sua idade: "))
profissao = input("Profissao: ")
linguagem = input("Qual linguagem principal de trabalho: ")

# Print usando %
print("Olá %s, obrigado por acessar nosso site! Por voce ja possuir %d anos, é permitido seu acesso. Verifiquei que seu cargo é o de %s e sua principal linguagem de programacao para trabalhar é %s. Temos diversas vagas abaixo relacionadas ao seu perfil!\n" % (nome, idade, profissao, linguagem))