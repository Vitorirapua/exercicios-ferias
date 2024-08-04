def calcula_media(notas):
    total = sum(notas.values())
    quantidade = len(notas)
    media = total / quantidade
    return media

alunos = {
    "vior": {
        "matematica": 90,
        "portugues": 75, 
        "historia": 95
    },
    "duda": {
        "matematica": 90, 
        "portugues": 90, 
        "historia": 100
    },
    "bruno": {
        "matematica": 60, 
        "portugues": 75, 
        "historia": 85
    }
}

for aluno, notas in alunos.items():
    media = calcula_media(notas)
    
    # Exiba na tela o nome de cada aluno e sua média final.
    print(f" • {aluno} → {media:.2f}")
    