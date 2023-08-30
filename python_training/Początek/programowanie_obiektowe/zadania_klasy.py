class Product:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass
if __name__ == '__main__':

    Jabłko = Apple()
    Japko = Apple()
    Ziemniak = Potato()
    Kartofel = Potato()
    print(type(Ziemniak))
    print(type(Kartofel))
    print(type(Japko))
    print(type(Jabłko))

    lista_zamówień = [Order(),Order(),Order(),Order(),Order(),Order(),]
    print(lista_zamówień)

    lista_zakupów = {
        'mleko': Product(),
        'ser': Product(),
        'jajka': Product(),
        'szynka': Product(),
        'marchewki': Product(),
    }
    print(lista_zakupów)