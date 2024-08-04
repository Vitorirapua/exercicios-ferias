agenda = {}

agenda["Duda"] = {
    "telefone": "1234-5678",
    "email": "duda@email.com"
}
agenda["bruno"] = {
    "telefone": "2345-6789", 
    "email": "bn@email.com"
}
agenda["Vitor"] = {
    "telefone": "3456-7890", 
    "email": "vt@email.com"
}

primeiro_amigo = list(agenda.keys())[0]
print(f"Telefone do primeiro amigo ({primeiro_amigo}):", agenda[primeiro_amigo]["telefone"])

agenda["bruno"]["email"] = "bruno@email.com"

agenda["Vitor"]["cidade"] = "Rio de Janeiro"

print("Informações do terceiro amigo:")
for chave, valor in agenda["Vitor"].items():
    print(f"{chave}: {valor}")

import pprint
pprint.pprint(agenda)

import json
print(json.dumps(agenda, indent=4, ensure_ascii=False))