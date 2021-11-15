from random import randint, choice


try:
    soubor1 = input("Zadejte název prvního souboru pro čtení: \n")
    soubor2 = input("Zadejte název druhého souboru pro zápis: \n")
    f1 = open(soubor1, "r")
    f2 = open(soubor2, "w")
except FileNotFoundError:
    print("Neplatný soubor.")

volba = int(input("Prosím, vyberte funkci: \n 1 - Převod souboru na malá písmena \n 2 - Náhrada znaku jiným znakem \n 3 - Statistika textu \n 4 - Generátor textu \n"))

if volba == 1:
    for line in f1:
        f2.write(line.lower())

if volba == 2:
    znak1 = input("Zadej znak, který chcete převést: ")
    znak2 = input("Zadej znak, na který se bude převádět: ")
    while True:
        char = f1.read(1)
        if char == "":
            break
        else:
            if char.upper() == znak1.upper():  #Ošetření malých/velkých písmen
                f2.write(znak2)
            else:
                f2.write(char)

if volba == 3:
    text = f1.read()
    print(text)
    f1.close()
    pocet = {}

    for pismeno in text:
        if pismeno.isalpha():
            if pismeno not in pocet.keys():
                pocet[pismeno] = 1
            else:
                pocet[pismeno] +=1

    print()
    nej = max(pocet.values())
    for key in sorted(pocet.keys()):
        print("({0}) -> {1:4} | {2}".format(key, pocet[key], 50 *  pocet[key]//nej * "#"))

if volba == 4:
    samohlasky = 'aeiyou'
    souhlasky = 'qwertzuiopasdfghjklyxcvbnm'
    def word_gen(minchars=1, maxchars=10):
        vysledek = ''
        pocet = randint(minchars, maxchars)
        if pocet == 1: #aby jednopísmenková slova byli vždy samohlásky
            zacatek = 0
        zacatek = randint(0,1)
        for i in range(pocet):
            if i % 2 == zacatek:
                vysledek = vysledek + choice(samohlasky)
            else:
                vysledek = vysledek + choice(souhlasky)
                if randint(1,10) == 1: #2 souhlásky vedle sebe
                    vysledek = vysledek + choice(souhlasky)

        return vysledek

    print(word_gen())

    def sentence_gen(minwords=3, maxwirds=12):
        vysledek = ''
        for i in range(randint(minwords,maxwords)):
            vysledek = vysledek + word_gen() + ' '

        return vysledek.capitalize()[0:-1] + '.'

    def prumer(a,b,c):
        return (a+b+c)/3

f1.close()
f2.close()
