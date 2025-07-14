gabarito = [ ]
contador = 0

print('Correção de provas')
print(' ')
print('Primeiro digite qual é o gabarito da prova.')
print('Em seguida, digite as respostas dos alunos.')
print(' ')

while contador < 5:
    questao = input(f'Gabarito - Questão {contador + 1}: ').lower()
    if questao in ['a','b','c','d','e']:
        gabarito.append(questao)
        contador += 1
    
aprovados = 0
aluno = 1
while aluno <= 5:
    print(f'Aluno {aluno}')
    acertos = 0
    respostas = 0
    while respostas < 5:
            questao = input(f'Resposta - Questão {respostas + 1}: ').lower()
            if questao in ['a','b','c','d','e']:
                 if questao == gabarito[respostas]:
                      acertos += 1
            respostas += 1
        
    nota = acertos * 2
    print(f'Nota: {nota}')
    if nota >= 7:
         aprovados += 1
    aluno += 1

percentual = (aprovados / 5) * 100
print(' ')
print (f'O percentual de aprovação é: {percentual:.0f}%')

