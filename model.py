class Participante:

    def __init__(self,nome,nascimento,email):
        self.nome=nome
        self.nascimento=nascimento
        self.email=email

    def __str__(self):
        return "nome: " + str(self.nome) + "nascimento: " + str(self.nascimento) + "email: " + (self.email)







    def criarPessoa():
        # Dados do proprietário
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        nascimento = input("Digite sua data de nascimento: ")

        pessoa = Participante(nome, nascimento, email)

        return pessoa















