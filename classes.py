class Locadora:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.clientes = []
        self.itens = []

    def cadastrarCliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.get_nome()}' cadastrado com sucesso!")

    def cadastrarItem(self, item):
        self.itens.append(item)
        print(f"Item '{item.get_titulo()}' cadastrado com sucesso!")

    def listarItens(self):
        print(f"\nItens da locadora '{self.nome}':")
        if not self.itens:
            print("Nenhum item cadastrado.")
        for item in self.itens:
            status = "Disponível" if item.get_disponivel() else "Alugado"
            print(f"- {item.get_titulo()} ({status})")

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None  

    def buscar_item(self, codigo):
        for item in self.itens:
            if item.get_codigo() == codigo:
                return item
        return None  


class Item:
    def __init__(self, codigo, titulo, disponivel=True):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = disponivel

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Item '{self.titulo}' foi alugado com sucesso!")
        else:
            print(f"Item '{self.titulo}' não está disponível.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Item '{self.titulo}' foi devolvido e está disponível novamente.")
        else:
            print(f"Item '{self.titulo}' já está disponível.")
            
    def get_codigo(self):
        return self.codigo

    def get_titulo(self):
        return self.titulo

    def get_disponivel(self):
        return self.disponivel


class Filme(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        super().__init__(codigo, titulo)
        self.genero = genero
        self.duracao = duracao

    def get_genero(self):
        return self.genero

    def get_duracao(self):
        return self.duracao


class Jogo(Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria):
        super().__init__(codigo, titulo)
        self.plataforma = plataforma
        self.faixaEtaria = faixaEtaria

    def get_plataforma(self):
        return self.plataforma

    def get_faixa_etaria(self):
        return self.faixaEtaria


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.itensLocados = []

    def locar(self, item):
        if item.get_disponivel():
            item.alugar()
            self.itensLocados.append(item)
        else:
            print(f"O item '{item.get_titulo()}' já está alugado.")

    def devolver(self, item):
        if item in self.itensLocados:
            item.devolver()
            self.itensLocados.remove(item)
        else:
            print(f"O cliente {self.nome} não possui o item '{item.get_titulo()}' alugado.")

    def listarItens(self):
        print(f"\nItens alugados por {self.nome}:")
        if not self.itensLocados:
            print("Nenhum item alugado.")
        for item in self.itensLocados:
            print(f"- {item.get_titulo()}")

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf
