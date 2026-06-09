# Si alguien esta viendo esto hice este proyecto gracias al aburrimiento
elige = 0
import time
import random

time.sleep(elige)

monedas = 0
reputacion = 5
texto_amigo = "Robarle el dinero a tu amigo"
texto_opcion = "Di :robar: para robar a su amigo o di :vender: para vender frutas en su emprendimiento "

time.sleep(1)
Nombre = input("¿Cual es tu nombre? ")

while True:
    print(
        "hola",
        Nombre,
        "este es tu Dinero:",
        monedas,
        "y esta es tu reputacion",
        reputacion,
        "\n Estas vendiendo frutas",
    )

    time.sleep(6)

    print(
        "puedes \n",
        texto_amigo,
        "\n Vender frutas en tu nuevo emprendimiento donde vendes frutas en el cual gastaste 100 pesos",
    )
    elige = input(texto_opcion)

    print("Cargando.")
    time.sleep(1)
    print("Cargando..")
    time.sleep(1)
    print("Cargando...")
    time.sleep(1)
    print("Cargando.")
    time.sleep(1)
    print("Cargando..")
    time.sleep(1)
    print("Cargando...")

    time.sleep(1)

    elige_random = random.randint(1, 6)
    clientes = random.randint(1, 8)
    clientes1 = random.randint(20, 30)
    clientes2 = random.randint(10, 20)
    monedas1 = random.randint(30, 50)
    monedas2 = random.randint(10, 25)
    monedas3 = random.randint(5, 10)
    reputacion1 = random.randint(1, 5)

    if elige == "vender" and clientes >= 1 and clientes <= 3:
        monedas += monedas1
        reputacion += 2
        print(
            "Tu negocio le fue muy bien tuviste ",
            clientes1,
            " clientes este dia y solo es el primero ganaste",
            monedas1,
            "monedas, tus monedas ahora son:",
            monedas,
            "ademas tu reputacion subio un",
            reputacion1,
            ",de reputacion:",
        )

    elif elige == "vender" and clientes >= 4 and clientes <= 6:
        monedas += monedas2
        reputacion += reputacion1
        print(
            "Tu negocio le fue normal tuviste ",
            clientes2,
            "clientes este dia y solo es el primero igual no es tanto es poco, ganaste",
            monedas2,
            "monedas, tus monedas ahora son:",
            monedas,
            "ademas tu reputacion subio un",
            reputacion1,
            "de reputacion:",
        )

    elif elige == "vender" and clientes >= 7 and clientes <= 8:
        monedas += monedas2
        reputacion += reputacion1
        print(
            "Tu negocio le fue muy mal obtuviste ",
            clientes2,
            "no es tanto es muy poco, ganaste",
            monedas3,
            "monedas, tus monedas ahora son:",
            monedas,
            "ademas tu reputacion subio un",
            reputacion1,
            "de reputacion:",
        )

    if (
        elige == "robar"
        and elige_random == 1
        or elige == "robar"
        and elige_random == 2
        or elige == "robar"
        and elige_random == 3
    ):
        print(
            "Te encontraron quedas arrestado Estas arrestado por 30 segundos Si esperas podras seguir el juego"
        )
        time.sleep(24)
        print("Cargando.")
        time.sleep(1)
        print("Cargando..")
        time.sleep(1)
        print("Cargando...")
        time.sleep(1)
        print("Cargando.")
        time.sleep(1)
        print("Cargando..")
        time.sleep(1)
        print("Cargando...")
        monedas -= 50
        reputacion -= 5
        print(
            "Has salido de tu condena pero como castigo tienes una deuda de 50 pesos ademas tu amigo te abandono y has perdido 5 de reputacion",
            reputacion,
            " Ahora tus monedas son",
            monedas,
        )
        texto_amigo = "Robarle el dinero a un desconocido en la calle"
        texto_opcion = "Di :robar: para robar a un desconocido o di :vender: para vender frutas en su emprendimiento "

    elif (
        elige == "robar" and elige_random == 6 or elige == "robar" and elige_random == 5 or elige == "robar" and elige_random == 4
    ):
        monedas += 50
        print(
            "Uffff has tenido suerte no te han encontrado!!! Con eso me referia a suerte, ahora tus monedas son",
            monedas,
        )

    if monedas >= 500:
        break

    if monedas <= -150:
        break
