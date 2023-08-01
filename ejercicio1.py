from experta import *
import random 

class Rutina (Know.ledgeEngine): #class crea una clase 

    opciones = ["a", "b"] #declara una variable, los valores a y b

    @DefFacts()
    def _initial_action(self): #se configura un hecho como valido
        yield Fact(noche="noche") 
        yield Fact(tarde="tarde")
        yield Fact(mañana="mañana")

    x1= Fact(a= "Me levanto y leo 10 minutos un libro",
             b= "Me levanto y chequeo mi telefono")
    x2= Fact(a="Cargo los bizcochuelos en mi tupper", 
             b="Antes de salir le saludo a Olivia")
    x3= Fact(a="Voy al gimnasio para relajarme",
             b="Preparo unos mates y los tomo con mi hermana")

    @Rule(Fact(mañana="mañana"))
    def m1(self):
        print(self.x1[random.choice(self.opciones)])

     @Rule(Fact(mañana="tarde"))
    def t1(self):
        print(self.x2[random.choice(self.opciones)])

     @Rule(Fact(mañana="noche"))
    def t2(self):
        print(self.x3[random.choice(self.opciones)])

    engine = Rutina()
    engine.reset() #Prepare the engine for the execution.
    engine.run() #Run it!

    


