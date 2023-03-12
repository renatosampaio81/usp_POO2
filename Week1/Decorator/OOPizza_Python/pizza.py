class Pizza:
    
    def preco():
        pass


class PizzaDaNonna(Pizza):

    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def preco(self):
        valor = 0
        for i,p in self.ingredientes.items():
            valor += self.ingredientes[i]
        return(valor)

class PizzaDecorator(Pizza):

    def __init__(self, pizzadecorada):
        self.pizzadecorada = pizzadecorada

class BordaRecheada(PizzaDecorator):

    """Adiciona Borda Recheada"""

    def preco(self):
        return self.pizzadecorada.preco() + 10

class MassaIntegral(PizzaDecorator):

    """Adiciona Massa Integral"""

    def preco(self):
        return self.pizzadecorada.preco() + 5

class ExtraGrande(PizzaDecorator):

    """Define Valor da Pizza Extra Grande"""

    def preco(self):
        return self.pizzadecorada.preco() * 1.3

class PizzariaDaNonna:
    ingredientes = {'Massa':10,
                    'Muzzarela':20,
                    'Tomate':5,
                    'Manjericao':5}
    margerita = PizzaDaNonna(ingredientes)
    minhaSuperMargerita = ExtraGrande(BordaRecheada(MassaIntegral(margerita)))

    print(f'Minha pizza custará R${minhaSuperMargerita.preco()}')

if __name__ == '__main__':

    PizzariaDaNonna()