from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca

if __name__ == "__main__":
    # marca1 = Marca("Semsung")
    # marca2 = Marca("Lj")

    # tv1 = TV(marca1, True)
    # tv2 = TV(marca2, False)

    # tv1.setPrecio(2000)
    # tv2.setCanal(90)
    # tv1.setCanal(121)
    # tv2.setVolumen(7)

    # control1 = Control()
    # control1.enlazar(tv1)
    # control1.turnOff()
    # control1.setCanal(50)
    # control1.turnOn()
    # control1.canalUp()
    # control1.volumenUp()

    # print(tv2.getCanal())
    # print(tv1.getPrecio())
    # print(tv1.getMarca().getNombre())
    # print(tv1.getCanal())
    
    
    marca = Marca("Semsung")
    tv1 = TV(marca, True)
    
    tv1.setCanal(100)
    tv1.canalDown()

    tv2 = TV(marca, False)
    control = Control()
    control.enlazar(tv2)
    control.setCanal(50)
    control.turnOn()
    #print(tv2.getEstado())
    control.canalUp()
    #print(tv2.getCanal())
    tv3 = TV(marca, False)
    tv2.setCanal(121)
    
    print(tv1.getCanal())
    print(tv2.getCanal())
    print(tv3.getCanal())
