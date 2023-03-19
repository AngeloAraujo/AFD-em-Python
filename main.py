class Automato:
    def __init__(self):
        self.estado_atual = 0
        self.estados_finais = {1, 3, 5, 7, 8, 10, 12}
        self.tabela_transicoes = {
            0: {'id': 1, 'constante': 2, 'if': 4, 'for': 9, 'while': 11},
            1: {'id': 1, 'constante': 1},
            2: {'constante': 3},
            3: {},
            4: {},
            5: {'id': 6},
            6: {'id': 6, 'constante': 6},
            7: {'id': 8},
            8: {'id': 8, 'constante': 8},
            9: {},
            10: {},
            11: {'id': 12},
            12: {'id': 12, 'constante': 12}
        }

    def processar(self, cadeia):
        for caractere in cadeia:
            if caractere.isalpha():
                entrada = 'id'
            elif caractere.isdigit():
                entrada = 'constante'
            else:
                continue

            if entrada not in self.tabela_transicoes[self.estado_atual]:
                return False

            self.estado_atual = self.tabela_transicoes[self.estado_atual][entrada]

        return self.estado_atual in self.estados_finais


def imprimir_tipo(cadeia):
    automato = Automato()
    if automato.processar(cadeia):
        if cadeia in ['if', 'for', 'while']:
            print(f'{cadeia} é uma palavra reservada')
        elif cadeia.isnumeric():
            print(f'{cadeia} é uma constante')
        else:
            print(f'{cadeia} é um ID')
    else:
        print(f'{cadeia} é inválido')


palavra = str(input("Insira uma palavra para verificar!"))
imprimir_tipo(palavra)
