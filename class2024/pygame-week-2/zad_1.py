import time


class Brewer:

    def brew(self, recepie):
        print(f'Brewing {str(recepie)}')

class Recepie:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return str(self.ingredients)

class RecepieFactory:
    def get_recepie(self):
        raise NotImplementedError()
    
class EspressoRecepieFactory(RecepieFactory):

    def get_recepie(self):
        return Recepie([('Coffe', 18), ('Water', 40)])
    
class CappuccinoRecepieFactory(RecepieFactory):

    def get_recepie(self):
        return Recepie([('Coffe', 18), ('Water', 100), ('Powdered Milk', 5)])
    
class App:

    def __init__(self):
        self.recepie_factory = None 
        self.brewer = Brewer()

    def set_recepie_factory(self, recepie_factory: RecepieFactory):
        self.recepie_factory = recepie_factory

    def make_bevrage(self):
        recepie = self.recepie_factory.get_recepie()
        self.brewer.brew(recepie)

        


if __name__ == '__main__':
    app = App() 
    inp = input()
    while  inp != '-1':
        if inp == '1':
            rf = EspressoRecepieFactory()
            app.set_recepie_factory(rf)
        elif inp == '2':
            app.set_recepie_factory(CappuccinoRecepieFactory())
        
        time.sleep(2)
        app.make_bevrage()
        inp = input()

        