#se crea la clase padre
class empresa:
  def __init__(self):
    self.nombre=input('Digite su nombre')
    self.edad=int(input('Digite su edad'))

      # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
#se crea la clase hija empleado
class empleado(empresa):
  def __init__(self):

        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 

  def pagar_salario(self):
    if self.sueldo > 3600000 :
      subtotal=3600000*0.035;
      total=self.sueldo-subtotal;
      print('Su descuento es de', subtotal)
      print('Su total es de', total , " Pesos")
    else:
      print('Usted no nescesita un descuento')

empresa1=empresa()
empleado1=empleado()
empleado1.pagar_salario()