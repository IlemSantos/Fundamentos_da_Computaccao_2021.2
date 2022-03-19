import sys

BRANCO = 0
AMARELO = 1


class Automato:
    def __init__(self):
        self.alfabeto = list()
        self.estados = list()
        self.transiccoes = list()
        self.estado_inicial = None
        self.estados_finais = list()

    # Adiciona um novo estado a lista de estados do autômato
    def add_estado(self, new_estado):
        self.estados.append(new_estado)
        self.estados.sort()  # Ordenando os estados

    # Adiciona um símbolo para a lista de alfabetos
    def add_simbolo_alfabeto(self, new_simbolo):
        self.alfabeto.append(new_simbolo)
        self.alfabeto.sort()  # Ordenando o alfabeto

    # Adiciona uma transição ao autômato
    def add_transiccao(self, estado_de_partida, estado_de_chegada, simbolo_consumido):
        if simbolo_consumido in self.alfabeto:  # Verificação de que se o símbolo está presente no alfabeto

            # Verificando se os estados estão na lista de estados do autômato
            if estado_de_partida in self.estados and estado_de_chegada in self.estados:
                for trans in self.transiccoes:  # Percorrendo-se as transições
                    if trans[:2] == (estado_de_partida, simbolo_consumido):
                        print('Erro 04 ;')
                        sys.exit()
                    continue
                ''' Adicionando transição = Do estado 'estado_de_partida' com a 'simbolo_consumido' do alfabeto
                    eu chego no estado 'estado_de_chegada' '''
                self.transiccoes.append(
                    (estado_de_partida, simbolo_consumido, estado_de_chegada))
                self.transiccoes.sort()  # Ordenando as transições
                return True

            else:
                # Indicando que os estados não estão na lista de estados
                print('Erro 03 ;')
                sys.exit()

        else:
            # Indicando que símbolo que não fazem parte do alfabeto
            print('Erro 01 ;')
            sys.exit()

    # Adiciona uma estado como estado inicial(podendo ser apenas um)
    def set_as_estado_inicial(self, estado):
        if estado in self.estados and self.estado_inicial is None:
            self.estado_inicial = estado
            return True

        return False

    # Seta os estados finais do autômato(podendo ser mais de um)
    def set_as_estados_finais(self, estado):
        if estado in self.estados:
            self.estados_finais.append(estado)
            self.estados_finais.sort()
            return True

        return False

    # Método para percorrer o autômato utilizando-se de uma string de letras de seu alfabeto
    def checar_palavra(self, string):
        if self.estado_inicial is None:
            return 'Autômato não possui estado inicial'

        current_estado = self.estado_inicial  # Começando a percorrer do estado inicial
        for char in string:  # Percorrendo-se a String
            if char in self.alfabeto:
                for trans in self.transiccoes:  # Percorrendo-se as transições
                    # Verificando o estado de partida e a letra para ele percorrer para um próx. estado
                    if trans[0] == current_estado and trans[1] == char:
                        # Percorreu-se para o próximo estado
                        current_estado = trans[2]
                        break  # Saindo do laço pois já gastou-se o caracter da string
            else:
                # Caso em que encontrou um caracter que não está na lista do alfabeto do autômato
                # String não aceita pelo autômato
                return 'Erro 02 ;'

        if current_estado in self.estados_finais:
            # String aceita pelo autômato
            return f'{string} sim ;'
        else:
            # String não aceita pelo autômato
            return f'{string} não ;'

    def visitaL(self, u, cor):
        fila = list()
        cor[self.estados.index(u)] = AMARELO
        fila.append(self.estados.index(u))
        while fila:
            u = self.estados[fila[0]]
            fila.pop(0)
            for i in self.transiccoes:
                if u in i[0]:
                    v = self.estados.index(i[2])
                    if cor[v] == BRANCO:
                        cor[v] = AMARELO
                        fila.append(v)

    # Método para verificar o autômato, utilizando-se o algoritmo de busca em largura tendo como partida o estado inicial verifica se possui como visitado algum estado final.
    def checar_automato(self):
        cor = list()
        for u in range(len(self.estados)):
            cor.append(BRANCO)
        self.visitaL(self.estado_inicial, cor)
        # print(cor) #visitados
        for i in self.estados_finais:
            if cor[self.estados.index(i)] == 1:
                return True
        print('Erro 04 ;')
        sys.exit()


if __name__ == '__main__':

    automato = Automato()

    automato.add_simbolo_alfabeto('0')
    automato.add_simbolo_alfabeto('1')

    automato.add_estado('A')
    automato.add_estado('B')
    automato.add_estado('C')
    automato.add_estado('D')

    automato.add_transiccao('A', 'B', '0')
    automato.add_transiccao('A', 'C', '1')

    automato.add_transiccao('B', 'A', '0')
    automato.add_transiccao('B', 'D', '1')

    automato.add_transiccao('C', 'A', '1')
    automato.add_transiccao('C', 'D', '0')

    automato.add_transiccao('D', 'B', '1')
    automato.add_transiccao('D', 'C', '0')

    automato.set_as_estado_inicial('A')
    automato.set_as_estados_finais('B')
    automato.set_as_estados_finais('C')

    automato.checar_automato()

    # Exemplo de string
    print(automato.checar_palavra('000'))
    print(automato.checar_palavra('10011'))
    print(automato.checar_palavra('0101'))
    print(automato.checar_palavra('11100'))
