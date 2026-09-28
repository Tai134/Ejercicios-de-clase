def sumar (num_1: int, num_2: int) -> int:
    """
    Esta función suma dos números enteros.

    Args:
    num_1 (int): El primer número.
    num_2 (int): El segundo número.

    return:
    int: La suma de los dos números.
    """
    suma = num_1 + num_2
    return suma

def restar (num_1: int, num_2: int) -> int:
    """
    Esta función resta dos números enteros.

    Args:
    num_1 (int): El primer número.
    num_2 (int): El segundo número.

    return:
    int: La resta de los dos números.
    """
    resta = num_1 - num_2
    return resta

def producto (num_1: int, num_2: int) -> int:
    """
    Esta función multiplica dos números enteros.

    Args:
    num_1 (int): El primer número.
    num_2 (int): El segundo número.

    return:
    int: La multiplicación de los dos números.
    """
    multiplicacion = num_1 * num_2
    return multiplicacion

def dividir (num_1: float, num_2: float) -> float:
    """
    Esta función divide dos números enteros.

    Args:
    num_1 (float): El primer número.
    num_2 (float): El segundo número.

    return:
    float: La división de los dos números.
    """

    retorno = None

    if num_2 != 0:
        division = num_1 / num_2
        retorno = division
        return retorno
