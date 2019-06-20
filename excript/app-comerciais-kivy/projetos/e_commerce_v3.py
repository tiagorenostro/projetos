from enum import Enum


class Produto:
    def __init__(self, valor, codigo, quant_estoque):
        self.valor = valor
        self.codigo = codigo
        self.quant_estoque = quant_estoque


class Eletro(Produto):
    def __init__(self, valor, codigo, quant_estoque, marca, voltagem):
        super().__init__(valor, codigo, quant_estoque)
        self.marca = marca
        self.voltagem = voltagem


class Geladeira(Eletro):
    def __init__(self, valor, codigo, quant_estoque, marca, voltagem, cor):
        super().__init__(valor, codigo, quant_estoque, marca, voltagem)
        self.cor = cor
        self.descricao = 'Geladeira ' + self.marca + ' ' + self.cor


class Televisao(Eletro):
    def __init__(self, valor, codigo, quant_estoque, marca, voltagem, polegadas):
        super().__init__(valor, codigo, quant_estoque, marca, voltagem)
        self.polegadas = polegadas
        self.descricao = 'Televisão ' + self.marca + ' ' + self.polegadas


class Livro(Produto):
    def __init__(self, valor, codigo, quant_estoque, titulo, autor):
        super().__init__(valor, codigo, quant_estoque)
        self.titulo = titulo
        self.autor = autor
        self.descricao = 'Livro ' + self.titulo


class ItemDoPedido:
    def __init__(self, produto, quant):
        self.produto = produto
        self.quant = quant

    def obter_valor_itens(self):
        return self.produto.valor * self.quant

    def descricao_item_pedido(self):
        descricao = self.produto.descricao + ' - R$ {:.2f} x {} = R$ {:.2f}'.format(self.produto.valor, self.quant, self.obter_valor_itens())
        return descricao


class StatusDoPedido(Enum):
    Pendente = 0
    Finalizado = 1
    Cancelado = 2

    def descricao_status(self):
        return self.name


class Pedido:
    def __init__(self, valor_frete):
        self.valor_frete = valor_frete
        self.status_pedido = StatusDoPedido(0)
        self.lista_itens = []

    def obter_valor_total(self):
        soma_produtos = 0
        for i in self.lista_itens:
            soma_produtos += i.obter_valor_itens()
        valor_total_frete = soma_produtos + self.valor_frete
        return valor_total_frete

    def obter_quant_total(self):
        quantidade = 0
        for i in self.lista_itens:
            quantidade += i.quant
        return quantidade

    def obter_resumo(self):
        resumo_pedido = '\n'
        for i in self.lista_itens:
            resumo_pedido += i.descricao_item_pedido()
            resumo_pedido += '\n'
        resumo_pedido += 'Frete = R$ {:.2f}'.format(self.valor_frete)
        resumo_pedido += '\nTotal = R$ {:.2f} ({} itens)'.format(Pedido.obter_valor_total(self), self.obter_quant_total())
        resumo_pedido += '\nStatus {}'.format(self.status_pedido.descricao_status())
        return resumo_pedido

    def adicionar_item(self, produto_quant):
        msg_sem_estoque = 'Produto {} não possui saldo em estoque suficiente'.format(produto_quant.produto.descricao)
        status = 'Pedido {}. Não é possível alterar o pedido'.format(self.status_pedido.descricao_status())
        if self.status_pedido.descricao_status() == 'Finalizado' or self.status_pedido.descricao_status() == 'Cancelado':
            return status
        else:
            if produto_quant.quant > produto_quant.produto.quant_estoque:
                 return msg_sem_estoque
            else:
                for i in self.lista_itens:
                    if produto_quant.produto.codigo == i.produto.codigo:
                        if produto_quant.quant > produto_quant.produto.quant_estoque:
                            return msg_sem_estoque
                        else:
                            i.quant += produto_quant.quant
                            produto_quant.produto.quant_estoque -= produto_quant.quant
                            msg = 'Item {} adicionado anteriormente, atualizado apenas a quantidade'.format(produto_quant.produto.descricao)
                            return msg
                self.lista_itens.append(produto_quant)
                produto_quant.produto.quant_estoque -= produto_quant.quant
                msg = 'Item {} adicionado ao Carrinho'.format(produto_quant.produto.descricao)
                return msg

    def remover_item(self, produto_quant):
        status = 'Pedido {}. Não é possível alterar o pedido'.format(self.status_pedido.descricao_status())
        if self.status_pedido.descricao_status() == 'Finalizado' or self.status_pedido.descricao_status() == 'Cancelado':
            return status
        else:
            for a, b in enumerate(self.lista_itens):
                if produto_quant.produto.codigo == b.produto.codigo:
                    del(self.lista_itens[a])
                    msg = '\nItem {} Removido do Carrinho\n'.format(produto_quant.produto.descricao)
                    return msg

    def alterar_quantidade_item(self, produto, quant):
        msg_sem_estoque = 'Quantidade é maior que saldo em Estoque'
        status = 'Pedido {}! Não é possível alterar o pedido'.format(self.status_pedido.descricao_status())
        if self.status_pedido.descricao_status() == 'Finalizado' or self.status_pedido.descricao_status() == 'Cancelado':
            return status
        else:
            for i in self.lista_itens:
                if produto.produto.codigo == i.produto.codigo:
                    estoque = i.produto.quant_estoque + i.quant
                    if quant > estoque:
                        return msg_sem_estoque
                    else:
                        i.produto.quant_estoque = estoque
                        i.quant = quant
                        i.produto.quant_estoque -= i.quant
                        msg = 'Quantidade do item {} alterada!'.format(i.produto.descricao)
                        return msg

    def finalizar_pedido(self):
        self.status_pedido = StatusDoPedido(1)
        return self.obter_resumo()

    def cancelar_pedido(self):
        self.status_pedido = StatusDoPedido(2)
        for i in self.lista_itens:
            i.produto.quant_estoque += i.quant
        return self.obter_resumo()


televisao = Televisao(1000, 123456, 10, 'LG', 220, '40 polegadas')
geladeira = Geladeira(1500, 789789, 10, 'Eletrolux', 240, 'Branca')
livro = Livro(50, 789456, 10, 'O Senhor dos Aneis', 'Desconhecido')

item1 = ItemDoPedido(televisao, 3)
item2 = ItemDoPedido(geladeira, 1)
item3 = ItemDoPedido(televisao, 7)
item4 = ItemDoPedido(livro, 3)

pedido = Pedido(50)
print(pedido.adicionar_item(item1))
print(pedido.adicionar_item(item2))
print(pedido.adicionar_item(item3))
print(pedido.adicionar_item(item4))

print(pedido.obter_resumo())

print(pedido.remover_item(item2))

#print(pedido.alterar_quantidade_item(item1, 9))
print(pedido.finalizar_pedido())

#print(pedido.remover_item(item2))

print(pedido.cancelar_pedido())
#print(pedido.obter_resumo())
