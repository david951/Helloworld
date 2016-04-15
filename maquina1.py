if __name__ == "__main__":
  
    dinero = 0
    opcion = 0
    dinero = input('Inserte el dinero:  ')
    m500 = 0
    m200 = 0
    m100 = 0
    if ((dinero >= 200) and (dinero <= 2500)):
        print 'MENU'
        print '1 Papas Fritas 1200'
        print "2 Sandwich Combinado 2500"
        print "3 Pescadito 1800"
        print "4 Empanada 1700"
        print "5 Arepa 2000"
        print "6 Gaseosa 1600"
        print "7 Vaso de Te 1000"
        print "8 Dulce 200"
        print "9 Salir" 
        opcion = input('Escoja opcion  ')
        if opcion == 1:
            costo = 1200
        elif opcion == 2:
            costo = 2500
        elif opcion == 3:
            costo = 1800
        elif opcion == 4:
            costo = 1700
        elif opcion == 5:
            costo = 2000
        elif opcion == 6:
            costo = 1600
        elif opcion == 7:
            costo = 1000
        elif opcion == 8:
            costo = 200
        elif opcion == 9:
            costo = 0
        else:
            costo = 0
        print "Costo: ", costo
        vueltas = dinero - costo
        print "Vueltas: ", vueltas
        m500=int(vueltas/500)
        print "El nro en monedas de 500:",m500
        vueltas=vueltas-m500*500
        m200=int(vueltas/200)
        print "El nro en monedas de 200:",m200
        vueltas=vueltas-m200*200
        m100=int(vueltas/100)
        print "El nro en monedas de 100:",m100
    else:
        print 'valor invalido' 
        