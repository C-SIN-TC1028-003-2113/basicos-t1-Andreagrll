def main():
    #escribe tu código abajo de esta línea
    #Modifica el programa para que realice lo siguiente: 
    #En una universidad cada estudiante cursa 4 materias en el semestre. 
    #Desarrolla un programa que reciba la calificación de cada materia (tipo float), 
    #calcula el promedio de las 4 materias y lo despliega.

    cali1= float(input('Calificación de la materia: '))
    cali2= float(input('Calificación de la materia: '))
    cali3= float(input('Calificación de la materia: '))
    cali4= float(input('Calificación de la materia: '))

    promedio= (cali1+cali2+cali3+cali4)/4

    print('El promedio es: '+ str(promedio))
    
if __name__ == '__main__':
    main()
