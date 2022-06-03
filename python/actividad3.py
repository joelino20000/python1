#se crea la clase padre que es alumno
class alumno:
  #declaramos el metodo init
  def __init__(self):
    self.nombre=input('Su nombre es')
    self.nota=int(input('su nota es'))
  
  def mostrar(self):
        print('Nombre: ',self.nombre)
        print('nota: ',self.nota)

  def notas(self):
    if self.nota >= 3 :
      print('Uste aprobo felicidades con una nota de ' , self.nota)
    else:
      print('Lo sentimos sigue estudiando desaprobo con ', self.nota)

alumno1 = alumno()
alumno1.mostrar()
alumno1.notas()