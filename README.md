# AFD-em-Python
Implementação de um AFD em Python com as seguintes regras:
--IDs com nome de variáveis, devem começar com ao menos uma letra, que pode ser seguida de letras ou números
--Constantes - valores numéricos
--Palavras reservadas: IF, FOR e WHILE
Como funciona o AFD:
O estado atual do autômato é mantido no atributo "estado_atual". 
Os estados finais são armazenados em um conjunto no atributo "estados_finais".
Cada estado é representado por uma chave de valores, cujo valor é outro dicionário com as entradas possíveis e os estados para os quais elas levam.
O método "processar" recebe uma cadeia de caracteres e processa cada caractere um por vez, atualizando o estado atual do autômato de acordo com a "tabela de transições".
Se o autômato chegar a um estado final, a cadeia é aceita e o método retorna "verdadeiro", caso contrário retorna "falso".
O método "imprimir_tipo" recebe uma cadeia e imprime o valor da cadeia e o seu tipo (ID, Constante, palavra reservada , palavra rejeitada). 
