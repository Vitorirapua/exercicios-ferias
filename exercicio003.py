letras = {"a", "e", "i", "o", "u"}

print(f"Tamanho do conjunto de letras:", len(letras))

letras.add("b")

print("a vogal 'i' está presnte no conjunto letras:", "i" in letras)

letras.remove("b")

consoantes = {"b", "d", "f"}

print("O conjunto consoantes está presente no conjunto letras:", consoantes.issubset(letras))

