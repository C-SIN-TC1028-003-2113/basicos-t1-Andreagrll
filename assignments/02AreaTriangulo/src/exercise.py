def main():
    #escribe tu código abajo de esta línea
    #Modifica el programa para que lea los datos tipo float: 
    #base (b) y altura (h), y muestre el área del triángulo.
    
    b= float(input('Dame la base: '))
    h= float(input('Dame la altura: '))

    area= (b*h)/2

    print('El área es: ' +str(area))

if __name__ == '__main__':
    main()
