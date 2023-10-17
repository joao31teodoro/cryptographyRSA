class GeradoraDeVariaveis:
    def __init__(self, p: int, q: int):
        # Inicializa a classe com os valores de p e q.
        self.p = p
        self.q = q
        self.n = 0  # Variável para armazenar n (produto de p e q)
        self.e = 0  # Variável para armazenar e (expoente de encriptação)
        self.d = 0  # Variável para armazenar d (expoente de decriptação)
        self.gerarN()  # Chama o método para gerar n
        self.gerarZ()  # Chama o método para gerar z
        self.gerarE()  # Chama o método para gerar e
        self.gerarD()  # Chama o método para gerar d

    def gerarN(self):
        # Gera o produto n a partir de p e q.
        self.n = self.p * self.q

    def gerarZ(self):
        # Gera o valor de z a partir de p e q.
        self.z = (self.p - 1) * (self.q - 1)

    def gerarD(self):
        try:
            # Tenta gerar o valor de d usando um loop.
            for i in range(10):
                x = 1 + (i * self.z)
                if x % self.e == 0:
                    self.d = int(x / self.e)
                    break
        except Exception:
            print("Erro ao gerar o D")  # Mensagem de erro em caso de exceção.

    def gerarE(self):
        z = self.z
        e = 0
        for e in range(2, z):
            if self.recursivaE(e, z) == 1:
                break
        self.e = e

    @staticmethod
    def recursivaE(e: int, z: int) -> int:
        # Função recursiva para encontrar o expoente de encriptação e.
        if e == 0:
            return z
        else:
            return GeradoraDeVariaveis.recursivaE(z % e, e)

    def calcular_valores(self):
        # Calcula os valores de n, z, e, e d chamando os métodos correspondentes.
        self.gerarN()
        self.gerarZ()
        self.gerarE()
        self.gerarD()

    def retornar_valores_calculados(self) -> dict:
        # Retorna os valores calculados (e, d, n) em um dicionário.
        dict_chaves = {'e': self.e, 'd': self.d, 'n': self.n}
        return dict_chaves


class RSAMensagem:
    # Classe para encriptar e decriptar mensagens usando o algoritmo RSA.
    def __init__(self, mensagem: list, dict_valores: dict):
        self.mensagem = mensagem  # A mensagem a ser processada (em forma de lista de números)
        self.dict_valores = dict_valores  # Os valores de e, d e n usados no algoritmo RSA

    def transforma_em_texto_criptografado(self):
        try:
            # Encripta a mensagem transformando os números usando a fórmula do RSA.
            mensagem_criptografada = []
            for i in self.mensagem:
                mensagem_criptografada.append(str((i ** self.dict_valores['e']) % self.dict_valores['n']))
            return mensagem_criptografada
        except Exception:
            print("Erro ao tentar criptografar a mensagem")  # Mensagem de erro em caso de exceção.

    def decripta_mensagem(self, mensagem_encript):
        try:
            # Decripta a mensagem transformando os números encriptados usando a fórmula do RSA.
            mensagem_decriptada = []
            for i in mensagem_encript:
                mensagem_decriptada.append((int(i) ** self.dict_valores['d']) % self.dict_valores['n'])
            return mensagem_decriptada
        except Exception:
            print("Erro ao tentar decriptar a mensagem")  # Mensagem de erro em caso de exceção.

    def retorna_mensagem_encriptada(self):
        # Retorna a mensagem encriptada.
        return self.transforma_em_texto_criptografado()

    def retorna_mensagem_decriptada(self, mensagem_decript):
        # Retorna a mensagem decriptada.
        return self.decripta_mensagem(mensagem_decript)


def transforma_mensagem_ascii(mensagem: str):
    # Converte a mensagem em uma lista de números ASCII.
    lista_ascii = [ord(i) for i in mensagem]
    return lista_ascii


def transforma_ascii_msg(lista_ascii: list):
    # Converte uma lista de números ASCII de volta para texto.
    texto = ''.join(chr(i) for i in lista_ascii)
    return texto


if __name__ == "__main__":
    # Parte principal do código que é executada ao rodar o script.
    # Cria uma instância da classe GeradoraDeVariaveis com p e q dados.
    geradoraVariaveis = GeradoraDeVariaveis(487, 599)
    dict_valores = geradoraVariaveis.retornar_valores_calculados()  # Obtém os valores de e, d e n
    mensagem = input('Digite o mensagem para encriptar: ')  # Solicita a entrada da mensagem

    lista = transforma_mensagem_ascii(mensagem)  # Converte a mensagem para ASCII

    # Cria uma instância da classe RSAMensagem com a mensagem e os valores de e, d e n
    rsa_msg = RSAMensagem(lista, dict_valores)
    msg_encript = rsa_msg.retorna_mensagem_encriptada()  # Encripta a mensagem
    msg_decript = rsa_msg.retorna_mensagem_decriptada(msg_encript)  # Decripta a mensagem

    # Printa a mensagem encriptada e decriptada
    print("Mensagem encriptada: ", ''.join(msg_encript))
    print("Mensagem decriptada: ", transforma_ascii_msg(msg_decript))
