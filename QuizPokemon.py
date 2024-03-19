def run_quiz():
    questions = [
        {
            "pergunta": "Qual é o tipo de Pokémon que é resistente a ataques do tipo Elétrico?",
            "opcoes": ["a) Terra", "b) Água", "c) Aço", "d) Normal"],
            "resposta": "a"
        },
        {
            "pergunta": "Qual destes Pokémon evolui para Milotic?",
            "opcoes": ["a) Magikarp", "b) Goldeen", "c) Carvanha", "d) Feebas"],
            "resposta": "d"
        },
        {
            "pergunta": "Quem é o líder do ginásio da cidade de Pewter na região de Kanto?",
            "opcoes": ["a) Misty", "b) Brock", "c) Lt. Surge", "d) Erika"],
            "resposta": "b"
        },
        {
            "pergunta": "Qual é o Pokémon lendário que representa a destruição na mitologia de Galar?",
            "opcoes": ["a) Zacian", "b) Zamazenta", "c) Eternatus", "d) Calyrex"],
            "resposta": "c"
        },
        {
            "pergunta": "Quem é o líder do ginásio de Cerulean City em Pokémon Red/Blue?",
            "opcoes": ["a) Misty", "b) Brock", "c) Lt. Surge", "d) Erika"],
            "resposta": "a"
        },
        {
            "pergunta": "Qual é o Pokémon lendário da região de Hoenn associado à terra?",
            "opcoes": ["a) Rayquaza", "b) Kyogre", "c) Groudon", "d) Jirachi"],
            "resposta": "c"
        },
        {
            "pergunta": "Qual o foi o lendário que Ash Ketchum viu logo nos primeiros episódios?",
            "opcoes": ["a) Zapdos", "b) Articuno", "c) Moltres", "d) Ho-oh"],
            "resposta": "d"
        },
        {
            "pergunta": "Em qual geração foi introduzida as Megas Pedras de Pokémon?",
            "opcoes": ["a) Oitava Geração", "b) Sexta Geração", "c) Sétima Geração", "d) Quinta Geração"],
            "resposta": "b"
        },
        {
            "pergunta": "Qual é o item utilizado para a evolução de Scyther para Scizor",
            "opcoes": ["a) Up-Grade", "b) Razor Fang", "c) Razor Claw", "d) Metal Coat"],
            "resposta": "d"
        },
        {
            "pergunta": "Qual é a tipagem do pokémon Gengar?",
            "opcoes": ["a) Água", "b) Fantasma", "c) Fogo", "d) Voador"],
            "resposta": "b"
        },
    ]

    pontuacao = 0

    print("Bem-vindo ao Quiz de Pokémon para iniciantes!\n")

    for i, pergunta in enumerate(questions, 1):
        print(f"Pergunta {i}: {pergunta['pergunta']}")
        for opcao in pergunta['opcoes']:
            print(opcao)
        resposta_usuario = input("Escolha a opção correta (a, b, c, d): ").lower()

        if resposta_usuario == pergunta['resposta']:
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print("Resposta incorreta!\n")

    print(f"Você acertou {pontuacao} de {len(questions)} perguntas.")

run_quiz()
