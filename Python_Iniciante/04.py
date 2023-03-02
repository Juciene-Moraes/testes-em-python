notas_media = []
while len(notas_media) < 4:
    notas_media.append(float(input("Digite o " + str((len(notas_media) + 1 )) + "º número:")))
print((sum(notas_media) / len(notas_media)))