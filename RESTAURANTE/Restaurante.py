from RESTAURANTE.avaliacao import Avaliar
from RESTAURANTE.cardapio.itens_cardapio import Itemcardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print (f"{"nome do restaurante".ljust(31)} | {"categoria".ljust(36)} | {"Avaliacao".ljust(31)} | {"status"}")
        for restaurante in cls.restaurantes:
            print (f"{restaurante.nome.ljust(31)} | {restaurante.categoria.ljust(36)} | {str(restaurante._ativo).ljust(31)} | {str(restaurante.media_avaliacao).ljust(25)}")

    @property
    def ativo(self):
        return "ativo" if self._ativo else "inativo"
    
    def alternar_ativo(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliar(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_nota = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_nota, 1)
        return media 

    def adicionar_cardapio(self,item):
        if isinstance(item,Itemcardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
            print(f'Cardapio do restaurante {self.nome}\n')
            for i,item in enumerate(self._cardapio,start=1):
                if hasattr(item,"descricao"):
                    mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descricao: {item.descricao}"
                    print(mensagem_prato)
                else:
                    mensagem_bebida = mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}"
                    print(mensagem_bebida)



"""1-o CLASS Ela serve para organizar dados (atributos) e ações (métodos) que um objeto pode ter.
 Isso faz parte do paradigma de Programação Orientada a Objetos (POO).
 
 2-Ao escrevermos o ponto (.) depois de ifood, acessamos esse objeto e, dessa forma,
ele abre um menu suspenso com várias opções, como ativo, categoria e nome. Selecionaremos a opção nome
e atribuiremos o nome 'bistro', como string: ifood.nome = 'bistro'.

3-função que podemos utilizar, que é a função dir(). Então, ao invés de passarmos o nome da classe no print(),
passamos o dir(ifood), com o nome do objeto, ifood, como atributos,serve para ver o que você 
pode usar em uma variável, classe ou módulo.

4-Portanto, o dir() mostrará tudo: os atributos, métodos e propriedades de um objeto.
Quando o substituímos por vars(), queremos um dicionário desses atributos e métodos.
Ao executarmos dessa vez, recebemos no formato que tínhamos na função, com o 'nome': 'bistro', 'categoria': 'italiana'

5-vamos usar agora é o __init__. Ele vai construir para nós um método construtor, que é sempre chamado quando criamos
uma instância de um objeto e espera alguma informação.
função __init__, o que esperamos dela? Quando estivermos definindo esse objeto, por exemplo, ifood,
queremos que todas as suas informações sejam realmente de ifood. Quando criarmos um próximo objeto,
todas as informações do food99 devem ser de food99.
Para conseguirmos afirmar que cada restaurante terá suas próprias informações, vamos passar um nome reservado chamado self.
E esperamos dois argumentos desse restaurante: o nome e a categoria.

sempre passamos o self como primeiro parâmetro, para entendermos que se trata daquele objeto que estamos referenciando
naquele momento.
Depois, queremos que nome seja o nome do objeto que está vindo. Então, vamos colocá-lo como self.nome a atribuir o nome que
recebermos como parâmetro. Já self.categoria, será a categoria que estivermos passando como parâmetro. O self.ativo,
por sua vez, vai continuar com a propriedade de falso.

6- colocar as duas variavel dentro do parenteses ifood = Restaurante("bistro", "italiana") para que ele chama os valores
para fazer o int

7-O método __str__ é um método especial que pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto,
mostraremos determinada informação. Podemos escolher se queremos mostrar o nome, a categoria ou o ativo. Ou seja,
podemos escolher e definir. Então, em vez de mostrar a representação do endereço de memória, ele mostrará o que decidirmos.

depois colocamos entre parenteses para sinalizar o SELF para ele pegar o importante. dps damos o return para ele retornar com 
o resultado de uma funcao que e dada para o nome e categoria que esta sendo sendo usado no self, e no print aparece o nome do 
restaurante e categoria

8- agora foi criado uma lista com o nome restaurante para armazenar os nomes, categorias e ativos, com isso
Restaurante.restaurantes.append(self) esse codicos pedimos pra ele puxar os nomes que estao na lista para fazer 
alguam utilidade com ele.
depois criamos uma funcao para simplificar o print para que nao precisamos adicionar varios no fim do codigo

na linha 21 foi substituido a lista pre definida e tb o print pois ja foi colocado a funcao que ja imprime os dois

e Restaurante.listar_restaurantes() colocamos o ponto que e pra chamar a funcao para que seja executada, dentro do listar 
ja foi implementado a funcao print

9-escrevemos @property, temos a capacidade de pegar um atributo — neste caso, o ativo. Então, abaixo da linha atual,
vamos criar uma função com o mesmo nome do nosso atributo, abrir e fechar parênteses e escrever entre estes o self,
porque vamos modificar a forma como ele vai ser lido, não para um, mas para todos os restaurantes.
Sempre que utilizarmos @property, queremos modificar como aquele atributo vai ser lido.
mostrar o valor false ou true não explica muito bem o que está acontecendo. Então, podemos colocar no interior dessa função
um return, por exemplo. Queremos retornar determinada informação.

10- ._ativo colocamos o anderline para que a variavel ativo nao seja publico ou seja, o computador nao estaja esperando nada daquela
varialvel, assim resolvendo o problema de "setter"

11-.title() serve pra colocar a primeira letra em maiusculo de todo nome colocado e .upper() e para todas as letras maiuscula 

12-É uma boa prática indicar que se trata de um método da classe sempre que temos um método que não está referenciado com uma instância,
mas sim à classe. Para isso utilizamos o @classmethod — vamos adicioná-lo acima de listar_restaurantes().
Sempre que temos um @classmethod e estamos utilizando informações referentes a esse método, podemos colocar como argumento entre os parênteses
do método um cls. Se trata de uma convenção também.

13- exclui as informacoes dos restaurante ate as chamadas por causa que criei outro arquivo para organizar melhor as informacoes
para ficar mais proximo a vida real

14- agora vou criar a opcao avaliacao e criei outro arquivo chamado avaliacao para fazer essa funcao, add o self.avaliacao e 
coloquei uma lista para armazenar elas

15- coloquei as variaveis de avaliacao no outro arquivo app restaurante e exclui os doi restaurantes para focar no primeiro

16- na linha 16 eu fiz uma funcao onde ele pega as notas do outro arquivo e faz a soma com SUM e joga para a variavel avaliacao
e caso nao tiver nota como na linha 35 e 36 retorna 0 

depois colocando o len para pegar todas as nota pela quantidade

criamos a media e colocando o round que faz com que a nota seja arredonda para uma casa

17- coloquei o propety para que a nota seja lida 

18- tinha que executar o arquivo do app restaurant e dps colocar o str na linha 20 na part do self.ativo para ele 
identificar que o false ou true e texto

19- depois troquei o return 0 para "-" para que quando nao tivesse avaliacao numerica ele coloca o traco

20- depois coloquei uma condicao de que apenas as notas de 0-5 pode ser colocada no parametro se nao, nao contabilizaram na formula 

21-Existe uma função no Python chamada isinstance(), que verifica se o item que estamos adicionando é uma instância de itemCardapio.
Digitamos if isinstance(item, itemCardapio).

precisamos importar itemCardapio. Lá no início do arquivo, lembram quando estávamos importando a avaliação? Aplicamos a mesma coisa:
from modelos.cardapio import itemCardapio. Este itemCardapio é a classe base que criamos.

Contudo, nesta ocasião, ao invés de criarmos entidades distintas para bebida e prato, optamos por utilizar self._cardapio.append().
Se aprovado, adicionamos o item através de append().

22-exibir_cardapio(), inserimos uma anotação @property para informar que isso será uma propriedade de leitura apenas. 

para fins de organização, inserimos um print(f'') (fstring) com uma informação simples de qual é o cardápio que estamos acessando.

Ao lidar com uma lista, podemos empregar um loop for, conforme já demonstrado previamente. Existe uma abordagem mais simples para
enumerar o cardápio? :função enumerate()

enumerate() vai devolver sempre duas informações: o índice que desejamos e o próprio item. Podemos escrever, por exemplo, for i,
item in enumerate(self._ cardapio, start=1). Aqui, i simboliza o índice.

enumerate() normalmente inicia a enumeração a partir do 0, no entanto, começar do 1 faz mais sentido. Pense em solicitar o
item 0 da lista e receber um pãozinho - não faria sentido. Portanto, estamos definindo start=1 para iniciar a enumeração a partir
do número 1.

23- tiver if hasattr(item, 'descricao'):, ele vai imprimir como prato. Caso tenha hasattr(item, 'tamanho'),
imprimirá como bebida. E imprimimos a mensagem correspondente para cada caso. Se for um prato, imprimimos a descrição;
se for uma bebida, imprimimos o tamanho.

 """
 