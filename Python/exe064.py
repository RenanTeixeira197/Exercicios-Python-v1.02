#Construa um programa efetue a leitura das quatro notas de 20 alunos
#calcule e mostre a média de cada aluno e a média geral da turma.

notas = []

for i in range(20):
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1} do aluno {i+1}: "))
        notas_aluno.append(nota)
    notas.append(notas_aluno)


media_alunos = [sum(notas_aluno) / len(notas_aluno) for notas_aluno in notas]
media_geral = sum(media_alunos) / len(media_alunos)

print("\nMédias dos alunos:")
for i, media in enumerate(media_alunos, start=1):
    print(f"Aluno {i}: {media:.2f}")

print(f"\nMédia geral da turma: {media_geral:.2f}")
