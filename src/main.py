from modulo1 import Modulo1
from modulo2 import Modulo2

modulo1 = Modulo1(2, 3)
modulo2 = Modulo2(10)

print(modulo1.multiplicar())
print(modulo2.sumar(modulo1.x, modulo1.y))
