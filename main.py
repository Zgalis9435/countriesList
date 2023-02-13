countriesList=list()
closeProgram=False

def inputCountry():
    userCountry=input('Introduce el país que quieras:')
    return userCountry


while(closeProgram==False):
    userOption=int(input('Introduce una opción'
                     '\n1.Introducir un país'
                     '\n2.Imprimir los paises'
                     '\n3.Salir del programa'))
    match(userOption):
        case 1:
            countriesList.append(inputCountry().lower())
        case 2:
            countriesList.sort()
            printableList=set(countriesList)
            print(printableList)
        case 3:
            closeProgram=True
            break

