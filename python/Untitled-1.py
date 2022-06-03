class calculadora:
  def __init__(self):
    self.numero1=int(input('Escriba su primer numero'))
    self.numero2=int(input('Escriba su primer numero'))

  def suma (self):
    totals = self.numero1 + self.numero2
    print('La suma de sus numeros es ' , totals)

  def resta (self):
    totalr = self.numero1 - self.numero2
    print('La resta de sus numeros es ' , totalr)

  def multiplicacion (self):
    totalm = self.numero1 * self.numero2
    print('La multiplicacion de sus numeros es ' , totalm)

  def division (self):
    totald = self.numero1 / self.numero2
    print('La division de sus numeros es ' , totald)

alumno1=calculadora()
alumno1.suma()
alumno1.resta()
alumno1.multiplicacion()
alumno1.division()