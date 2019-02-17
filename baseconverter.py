#  *__author__*  Gaetan Jonathan

def base(base, nombre):
    base_list = []
    stringBase = ''

    while nombre > 0:
        reste = nombre % base 
        base_list.append(reste)

        nombre //= base

    for sb in base_list[::-1]:
        if sb == 10:
            sb = 'A'
        elif sb == 11:
            sb = 'B'
        elif sb == 12:
            sb = 'C'
        elif sb == 13:
            sb = 'D'
        elif sb == 14:
            sb = 'E'
        elif sb == 15:
            sb = 'F'
            
        stringBase += f' {sb}'

    return stringBase


def decimal(base, base_nombre):
    base_nombre = str(base_nombre)
    nombre_list = list(base_nombre)
    n = 0
    base_nombre = 0

    for entier in nombre_list[::-1]:
        if entier == 'A':
            entier = 10
        elif entier == 'B':
            entier = 11
        elif entier == 'C':
            entier = 12
        elif entier == 'D':
            entier = 13
        elif entier == 'E':
            entier = 14
        elif entier == 'F':
            entier = 15
        else:
            entier = int(entier)

        base_nombre = base_nombre + (entier*(base**n))

        n += 1 

    return base_nombre


def base_to_base(base_initial, base_finale, nombre):
    dec = decimal(base_initial, nombre)
    return base(base_finale, dec)