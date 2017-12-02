from Projeto.model import *
from datetime import date
import json

def main(args=[]):

         # Variáveis
         agenda =  None
         def menu(self):
            print("MENU")
            print("1-listar participantes")
            print("2-adiciona participante")
            print("3-sair")


         menu()


         continuar = True

         while continuar:
            try:
                # Continuar a execução do programa.
                opcao = int(input("Digite a opção: "))

                if (opcao == 1):
                    pass

                elif (opcao == 2):
                    agenda=criarPessoa()

                elif (opcao == 3):
                    continuar = False
                else:
                    print("Ops! Opção inválida!")


            except ValueError:
                print("Ops! Digite um valor válido")



        while True:
            try:
                    pessoas = []

                    # Leitura do Arquivo.
                    f = open("pessoas.txt", 'r', encoding="utf8")

                    # Parser do JSON em Objeto.
                    jsonObjs = json.loads(f.read())

                    # Iteração dos elementos do JSON.
                    for jsonObj in jsonObjs:
                        nome = jsonObj["nome"]
                        email = jsonObj["email"]
                        data = jsonObj["nascimento"].split("-")
                        nascimento = date(int(data[0]), int(data[1]), int(data[2]))
                        pessoa = Participante(nome, email, nascimento)
                        print(pessoa)
                        pessoas.append(pessoa)

                    hugo = Participante("Pedro", "01/03/2017","sanos@gmail.com")
                    pessoas.append(hugo)

                    pedroJson = {}
                    pedroJson['nome'] = hugo.nome
                    pedroJson['nascimento'] = hugo.nascimento
                    pedroJson['nascimento'] = hugo.email
                    print(pedroJson)

                    jsonObjs.append(pedroJson)





                    with open('data.txt', 'w', encoding='utf-8') as f:
                    json.dump(jsonObjs, f, ensure_ascii=False, indent=4)



                break
            except FileNotFoundError as err:
                print(err)
                print("Arquivo não encontrado!")

        if (__name__ == "__main__"):
            main()

