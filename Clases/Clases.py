import matplotlib.pyplot as plt
import math

class circulo:
  def __init__(self,radio):
    self.radio = radio
  def area(self):
    return (math.pi * self.radio ** 2)
  
  def perimetro(self):
    return 2.0*math.pi*self.radio

while True:
  radio = int(input("\nIntroduzca el Radio: \n"))
  c = circulo(radio)
  if radio <= 0 :
    print("¡Ups! Error: el radio es menor a 0 \n")
  else:
    print("\nArea: ", c.area())
    print("Perímetro: ",c.perimetro())
    print()
    
    ### PLOTEO ###

    figure, axes = plt.subplots()
    circulo_dibujado = plt.Circle((0,0), radio,color='pink')
    perimetro_dibujado = plt.Circle((0, 0), radio,fill=False,color='red')
    radio_dibujado = plt.hlines(0,0,radio,color="purple")
    axes.set_aspect(1)
    axes.set_xlim((0 - radio*1.3, 0 + radio*1.3))
    axes.set_ylim((0 - radio*1.3, 0 + radio*1.3))
    axes.add_artist(circulo_dibujado)
    axes.add_artist(perimetro_dibujado)
    axes.legend([radio_dibujado,perimetro_dibujado,circulo_dibujado], ["Radio","Perímetro","Area"],loc='upper left', bbox_to_anchor=(0.8, 1.007), fancybox=True, shadow=True)
    plt.title('Circulo')
    plt.show()

    ### ------ ###

    opcion = int(input("\n¿Desea multiplicar el radio? \n 1- Si \n 2- No \n\n"))
    if opcion == 1:
      n = int(input("\nIntroduzca el número por cual multiplicar: \n"))
      while n:
        if n <= 0:
          print("¡Ups! Error: Operación no válidad. Por favor introduzca un número mayor a 0")
          n = int(input("\nIntroduzca el número por cual multiplicar: \n"))
        else:
          radio = radio * n
          c = circulo(radio)
          print("\nRadio: ",radio)
          print("Area: ", c.area())
          print("Perímetro: ",c.perimetro())
          print()

          ### PLOTEO ###

          figure, axes = plt.subplots()
          circulo_dibujado = plt.Circle((0,0), radio,color='pink')
          perimetro_dibujado = plt.Circle((0, 0), radio,fill=False,color='red')
          radio_dibujado = plt.hlines(0,0,radio,color="purple")
          axes.set_aspect(1)
          axes.set_xlim((0 - radio*1.3, 0 + radio*1.3))
          axes.set_ylim((0 - radio*1.3, 0 + radio*1.3))
          axes.add_artist(circulo_dibujado)
          axes.add_artist(perimetro_dibujado)
          axes.legend([radio_dibujado,perimetro_dibujado,circulo_dibujado], ["Radio","Perímetro","Area"],loc='upper left', bbox_to_anchor=(0.8, 1.007), fancybox=True, shadow=True)
          plt.title('Circulo')
          plt.show()

          ### ------ ###

          break
    elif opcion == 2:
      pass
    else:
      pass