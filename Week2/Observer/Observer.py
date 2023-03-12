class Subject(object):
#Maintain a list of observers and notifies them of state changes

  def __init__(self): #construtor
  #Initialize a list of observers
    #define 2 propriedades e adiciona ao dicionário do objeto __dict__
    self.__dict__['state'] = 0 
    self.__dict__['observers'] = set()

  #__setattr__ é um método que é chamado toda vez que alguem altera o valor de um atributo desse meu objeto, onde name é o nome do atributo e value o valor a ser setado
  def __setattr__(self, name, value):
  #Override to notify observers of state changes when the state is updated
    self.__dict__[name] = value #seto o valor no atributo
    if name == 'state': #se o nome do atributo for state eu chamo o método pra notificar os observadores
      self.notify_observers()

  def register(self, observer):
  #Add an observer to the list of observers to be notified of state changes
    self.observers.add(observer)

  def deregister(self, observer):
  #Remove an observer
    self.observers.remove(observer)

  def notify_observers(self):
  #Iterate though observers and call the update() method on each one
    for observer in self.observers:
      observer.update()

#Create an abstract base class for and concrete classes for observer class

class Observer(object): #classe abstrata
#Abstract class to respond to changes in the subject
  
  def update(self):
  #Update observer state
    raise NotImplementedError("update() is not implemented.") #essa excessão diz que update não deve ser chamado em classe abstrata, apenas nas concretas


class BinaryObserver(Observer):
#Observer that prints subject state in binary

  def __init__(self, subject): #construtor recebe como parametro o subject, que é o sujeito que ele está observando
  #Keep a reference to the subject
    self.subject = subject
    self.subject.register(self) #eu me registro como um observador

  def update(self):
    print("\t em binário: " + bin(self.subject.state))


class OctalObserver(Observer):
#Observer that prints subject state in octal

  def __init__(self, subject):
  #Keep a reference to the subject.
    self.subject = subject
    self.subject.register(self)

  def update(self):
    print("\t em octal: " + oct(self.subject.state))


class HexadecimalObserver(Observer):
#Observer that prints subject state in hexadecimal

  def __init__(self, subject):
  #Keep a reference to the subject.
    self.subject = subject
    self.subject.register(self)

  def update(self):
    print("\t em hexadecimal: " + hex(self.subject.state))


def main():
#Test the observer pattern implementation
  subject = Subject()
  BinaryObserver(subject)
  OctalObserver(subject)
  HexadecimalObserver(subject)

  print("\nPrimeira mudanća de estado:")
  subject.state = 1024

  print("\nSegunda mudanća de estado:")
  subject.state = 255

if __name__ == "__main__":
  main()  