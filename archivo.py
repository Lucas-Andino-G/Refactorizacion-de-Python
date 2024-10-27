def ingresar_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                return point  # Devuelve la puntuación válida
            else:
                print('Por favor, introduzca un valor entre 1 y 5')
        else:
            print('Por favor, introduzca la puntuación en números')


def ingresar_comentario():
    print('Por favor, introduzca un comentario')
    comment = input()
    return comment  # Devuelve el comentario


def guardar_resultado(point, comment):
    post = f'punto: {point} comentario: {comment}'
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{post}\n')
    print('Puntuación y comentario guardados.')


def comprobar_resultados():
    print('Resultados hasta la fecha.')
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print("No hay resultados registrados.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos.")


def procesar_ingreso():
    point = ingresar_puntuacion()
    comment = ingresar_comentario()
    guardar_resultado(point, comment)


def mostrar_menu():
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprobar los resultados obtenidos hasta ahora.')
    print('3: Finalizar')


def main():
    while True:
        mostrar_menu()
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                procesar_ingreso()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Por favor, introduzca del 1 a 3')
        else:
            print('Por favor, introduzca del 1 a 3')


if __name__ == "__main__":
    main()