
def numberOfAvailableDifferentPaths(board, snake, depth):
    """
        Esta funcion calcula el numero de posibles caminos que la serpiente puede realizar en un tablero dado (board) con un numero de pasos dados (depth).

        Parameters
        ----------
        board: array.integer
            El tablero (board) es un array que contiene numeros enteros indicando las dimensiones del tablero.
        snake: array.array.integer
            La serpiente (snake) es un array de arrays donde cada uno contiene dos elementos, uno indica la posicion en la fila y el otro en la columna.
            Cada array indica la posicion (x,y) de un cuadrado de la serpiente.
        depth: integer
            Es la profundidad en la que debemos buscar todos los posibles movimientos de la serpiente.
        
        Returns
        -------
        integer
            Devuelve el numero de posibles caminos que puede hacer la serpiente de longitud depth.
    """
    if depth==0:    # Caso base
        # Si se ha llegado hasta este punto entonces ha encontrado un posible camino y devolveremos 1
        return 1
    else:           # Caso recursivo

        # Implementamos una funcion lambda que comprueba si la serpiente se ha salido de los bordes
        out_of_border = lambda board,snake: snake[0][0] < 0 or snake[0][0] >= board[0] or snake[0][1] < 0 or snake[0][1] >= board[1]

        # Implementamos una funcion lambda comprueba que si la serpiente se ha intersectado
        # Si se ha intersectado quiere decir que dos casillas de la serpiente tendran el mismo valor
        # Lo que hacemos entonces es obtener un conjunto de tuplas y comprobar su tamanyo
        # Si hay elementos iguales su tamanyo sera menor al de la serpiente original y por lo tanto la serpiente se habra intersectado
        self_intersection = lambda snake0, snake1: len(snake0)!=len(set(snake1))

        # Realizar un movimiento significa eliminar la ultima coordenada (cola) y anyadir una coordenada mas (la nueva), el resto permanece inmutable
        
        # Creamos 4 copias de serpientes
        lsnake = snake.copy()
        rsnake = snake.copy()
        dsnake = snake.copy()
        usnake = snake.copy()

        # Movimiento hacia la izquierda, la nueva cabeza de la serpiente tendra la coordenada (x, y-1)
        lsnake.pop(-1) # eliminamos la coordenada de la cola
        lsnake.insert(0,(snake[0][0], snake[0][1]-1)) # Restamos 1 a la segunda componente

        # Movimiento hacia la derecha, la nueva cabeza de la serpiente tendra la coordenada (x, y+1)
        rsnake.pop(-1) # eliminamos la coordenada de la cola
        rsnake.insert(0,(snake[0][0], snake[0][1]+1)) # Restamos 1 a la segunda componente

        # Movimiento hacia abajo, la nueva cabeza de la serpiente tendra la coordenada (x+1, y)
        dsnake.pop(-1) # eliminamos la coordenada de la cola
        dsnake.insert(0,(snake[0][0]+1, snake[0][1])) # Restamos 1 a la segunda componente

        # Movimiento hacia arriba, la nueva cabeza de la serpiente tendra la coordenada (x-1, y)
        usnake.pop(-1) # eliminamos la coordenada de la cola
        usnake.insert(0,(snake[0][0]-1, snake[0][1])) # Restamos 1 a la segunda componente

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
    a=[1,2,3,4,5]
    a.pop(-1)
    print(a)
    # board1=[(1,2),(3,2), (1, 2)]
    # print(board1)
    # board3 = set(board1)
    # print(board3)
    # print(len(board3)!=len(board1))

    snake2=[(2,2), (3,2), (3,1), (3,0), (2,0), (1,0), (0,0)]
    print(snake2)
    snake3 = snake2.copy()
    snake3.pop(-1)
    snake3.insert(0,(snake2[0][0], snake2[0][1]-1))
    print(snake3)
    
