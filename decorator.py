class Component:
    def getDescription(self):
        return self.__class__.__name__
    def getCost(self):
        return self.__class__.cost 
    
class Base(Component):
    cost = 4.90

class Decorator(Component):
    def __init__(self, component):
        self.component = component
    def getCost(self):
        return self.component.getCost() + Component.getCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' ' + Component.getDescription(self)
    
class Mussarela(Decorator):
    cost = 5.00
    def __init__(self, component):
        Decorator.__init__(self, component)

class Calabresa(Decorator):
    cost = 6.00
    def __init__(self, component):
        Decorator.__init__(self, component)

class Presunto(Decorator):
    cost = 5.50
    def __init__(self, component):
        Decorator.__init__(self, component)

class Tomate(Decorator):
    cost = 3.00
    def __init__(self, component):
        Decorator.__init__(self, component)

class Cebola(Decorator):
    cost = 2.50
    def __init__(self, component):
        Decorator.__init__(self, component)

class Bacon(Decorator):
    cost = 7.00
    def __init__(self, component):
        Decorator.__init__(self, component)

class Frango(Decorator):
    cost = 6.50
    def __init__(self, component):
        Decorator.__init__(self, component)

class Milho(Decorator):
    cost = 2.00
    def __init__(self, component):
        Decorator.__init__(self, component)

class Azeitona(Decorator):
    cost = 3.50
    def __init__(self, component):
        Decorator.__init__(self, component)

class Palmito(Decorator):
    cost = 5.50
    def __init__(self, component):
        Decorator.__init__(self, component)

pizza1 = Presunto(Mussarela(Tomate(Base())))
print(pizza1.getDescription() + ": R$" + str(pizza1.getCost()))
pizza2 = Frango(Milho(Palmito(Base())))
print(pizza2.getDescription() + ": R$" + str(pizza2.getCost()))