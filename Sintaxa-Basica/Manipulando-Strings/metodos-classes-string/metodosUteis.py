# Maiuscula, Minuscula e Titulo

# Variavel com letras de tamanho diferente
curso = "pYtHon"

# Transformando em Maiuscula
print(curso.upper())
# >>> Resultado -> PYTHON

# Transformando em Minuscula
print(curso.lower())
# >>> Resultado -> python

# Transformando em Titulo
print(curso.title())
# >>> Resultado -> Python

# Eliminando espacoes em branco da String
curso = "   Curso de Python   "

# Print para remover todos os espaços
print(curso.strip())
# >>> Resultado -> Curso de Python

# Print para removar os espacos do inicio
print(curso.lstrip())
# >>> Resultado -> Curso de Python

# Print para remover os espacos do final
print(curso.rstrip())
# >>> Resultado -> Curso de Python


# Junções e Centralização

cursoB = "Javascript"

print(cursoB.center(16, "#"))
# Resultado -> "##Python##"

print(".".join(cursoB))
# Resultado -> "P.y.t.h.o.n"  # O separador é o ponto determinado
