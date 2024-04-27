import sys

print('--------------------Simulador de Memória RAM---------------------------')
print() #mostra mensagem na tela 

tamanho = int(input('Qual a profundidade da memória:')) #mostra mensagem na tela
memoria = [""] * tamanho #calculo para dado de memória

while True: #enquato afirmação for verdade
  
    print('Digite "INSERIR" para inserir um dado na memória') #mostra mensagem na tela 
    print('Digite "CARREGAR" para ler um valor da memória.') #mostra mensagem na tela
    print('Digite "SAIR" para sair.') #mostra mensagem na tela

    cmdo = str(input('Digite o comando:')).upper() #escrevera uma string especifica para seguir no programa
    while True: #se o comando for verdadeiro
        if cmdo == 'INSERIR': #se o comando for 'inserir'
            local = int(input('Qual o endereço para gravar: ')) #mostra mensagem na tela
            if local > tamanho or local <= 0: #se o dado do local for maior que tamanho ou menor e igual a 0
                print("Endereço invalido") 
                print("----------Retornando para o inicio----------")
                print("")  #mostra mensagem na tela
                break #retorna para o inicio.
            dado = str(input('Qual o dado a ser gravado: ')) #mostra mensagem na tela 
            if local < tamanho and local >= 0: #se o locar for menor que o tamnaha e maior ou igual a 0
                memoria[local] = dado #armazena o dada na memoria[local]
            else: #se não
                print('Endereço inexistente.') #mostra mensagem na tela

        elif cmdo == 'CARREGAR': #se o comando digitado for "carregar"
            local = int(input('Qual o endereço para ler: ')) #mostra mensagem na tela
            if local > tamanho or local <= 0: #se o local for maior que o tamanho ou menor e igual a que 0
                break #retorna ao inicio
            if local < tamanho and local >= 0: #se local menor que tamanho ou maior e igual a 0
                print(f'endereço {local}: {memoria[local]}') #mostra mensagem na tela
                print("-------Simulador Finalizado-----------")
                print("") # mostra mensagem na tela
            else: #outra coisa 
                print('Endereço inexistente.') #mostra mensagem na tela
        elif cmdo == 'SAIR': #se digitar o comando sair 
            sys.exit() #sai do programa
        else:
            print('Comando inexistente!') #se  digitar outra coisa
        
        break #finalizar




