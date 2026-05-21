clientes = [
    ["Ana", 22, 1],
    ["carlos", 35, 10],
    ["Mariana", 28, 7],
    ["João", 19, 0],
    ["Fernanda", 40, 15],
    ["Rojerio", 45, 18],
    ["Marcos", 20, 5],
    ["Francisco", 13, 0],
    ["Adonias", 38, 30],
    ["Lucas", 24, 10]
]

print("== ANÁLISE DE CLIENTES ==")

for cliente in clientes:

    nome = cliente[0]
    idade = cliente[1]
    compras = cliente[2]

    if compras > 5:

        print(nome, "- Cliente com ALTA chance de interesse")

    else :

        print(nome, "- Cliente com BAIXA chance de interesse")    
        
        
        
produtos = [
    ["Café", 500],
    ["Arroz", 300],
    ["Leite", 600],
    ["Feijão", 400],
    ["Danoni", 100],
    ["Fermento", 200],
    ["Macarão", 500],
    ["Batata", 700],
    ["Tomate", 300],
    ["Laranja", 800]
]

print("== ANÁLISE DE PRODUTOS ==")

for produto in produtos:

    nome = produto[0]
    compras = produto[1]

    if compras > 5:

        print(nome, "- Produto com ALTA demanda")

    else :

        print(nome, "- Produto com BAIXA demanda")    