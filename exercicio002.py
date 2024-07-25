frutas = ("banana", "maçã", "laranja")
legumes = ("tomate", "conoura", "batata")

mercado = frutas + legumes

if "laranja" in mercado:
    print("Sim, 'laranja' existe no mercado.")
else:
    print("'Laranja' não existe no mercado.")



if "alface" in mercado:
    print("Sim, 'alface' existe no mercado.")
else:
    print("'alface' não existe no mercado.")


print(f"O ultimo item da lista de compras é: {mercado[-1]}")

