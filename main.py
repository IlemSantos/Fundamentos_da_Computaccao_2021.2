from automato import Automato


def le_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        text_file = arquivo.read().split('\n')

    text_file_data = list()
    for line in text_file:
        word = line.split(';')
        if '//' not in word[0]:
            text_file_data.append(word[0].rstrip())
    # text_file_data.pop()
    return text_file_data


if __name__ == '__main__':

    text_file_data = le_arquivo('AFD_teste01.txt')
    # print(text_file_data)

    AFD = Automato()

    [AFD.add_estado(n) for n in text_file_data[0].split()]  # Estados do AFD
    [AFD.add_simbolo_alfabeto(n)
     for n in text_file_data[1].split()]  # Alfabeto

    marcador = text_file_data.index('#')  # Indicado que não há mais transições
    for n in text_file_data[2:marcador]:
        estado_de_partida, estado_de_chegada, simbolo_consumido = [
            i for i in n.split()]
        AFD.add_transiccao(estado_de_partida,
                           estado_de_chegada, simbolo_consumido)

    AFD.set_as_estado_inicial(text_file_data[marcador + 1])  # Estado inicial
    [AFD.set_as_estados_finais(n)
     for n in text_file_data[marcador + 2].split()]  # Estados finais

    AFD.checar_automato()

    # Palavras a serem verificadas
    for word in text_file_data[marcador + 3].split():
        print(AFD.checar_palavra(word))
