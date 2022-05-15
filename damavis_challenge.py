
def numberOfAvailableDifferentPaths(board, snake, depth):
    """
        Esta funcion calcula el numero de posibles caminos que la serpiente puede realizar en un tablero dado (board) con un numero de pasos dados (depth)

        Parameters
        ----------
        board: array.integer
            El tablero (board) es un array que contiene numeros enteros indicando las dimensiones del tablero
        snake: array.array.integer
            La serpiente (snake) es un array de arrays donde cada uno contiene dos elementos, uno indica la posicion en la fila y el otro en la columna.
            Cada array indica la posicion (x,y) de un cuadrado de la serpiente.
        depth: integer
            Es la profundidad en la que debemos buscar todos los posibles movimientos de la serpiente
        
        Returns
        -------
        integer
            Devuelve el numero de posibles caminos que puede hacer la serpiente de longitud depth
    """

    # Implementamos una funcion lambda que comprueba si la serpiente se ha salido de los bordes
    out_of_border = lambda board,snake: snake[0][0] < 0 or snake[0][0] >= board[0] or snake[0][1] < 0 or snake[0][1] >= board[1]

    # Implementamos una funcion lambda comprueba que si la serpiente se ha intersectado
    # Si se ha intersectado quiere decir que dos casillas de la serpiente tendran el mismo valor
    # Lo que hacemos entonces es obtener un conjunto de tuplas y comprobar su tamanyo
    # Si hay elementos iguales su tamanyo sera menor al de la serpiente original y por lo tanto la serpiente se habra intersectado
    self_intersection = lambda snake0, snake1: len(snake0)!=len(set(snake1))

    print(out_of_border((4,3),[(2,0),(1,2)]))
    print(self_intersection([(2,2),(3,2),(3,1)],[(3,1),(2,2),(2,2)]))


    return 1


if __name__=='__main__':
    board=(4,3)
    snake=[(2,2), (3,2), (3,1), (3,0), (2,0), (1,0), (0,0)]
    depth=3
    number_of_available_different_paths = numberOfAvailableDifferentPaths(board, snake, depth)
    print('numberOfAvailableDifferentPaths(board, snake, depth) =',number_of_available_different_paths)
    print(board,'\n')
    # board1=[(1,2),(3,2), (1, 2)]
    # print(board1)
    # board3 = set(board1)
    # print(board3)
    # print(len(board3)!=len(board1))
