'''
author = Jan Hubáček
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

ODDELOVAC = "=" * 40
print(ODDELOVAC)
print("Ahoj, vítej v aplikaci. Prosím přihlaš se.")

uzivatele = {
"bob" : "123",
"ann" : "pass123",
"mike" : "password123 ",
"liz" : "pass123"
}

for prihlaseni in range(9999999999999):
    jmeno = input("Uživatelské jméno:")
    heslo = input("Heslo:")
    if uzivatele.get(jmeno) == heslo:
        print("Přihlášení proběhlo v pořádku. Můžete pokračovat")
        break
    else:
        print("Uživatelské jméno nebo heslo je špatně.")

print(ODDELOVAC)
print("Máme na výběr ze 3 textů.")
vyber = int(input("Vložte číslo mezi 1 a 3 pro výběr textu: "))
print(ODDELOVAC)
if vyber == 1:
    vybrany_text = TEXTS[vyber - 1]
elif vyber == 2:
    vybrany_text = TEXTS[vyber - 1]
elif vyber == 3:
    vybrany_text = TEXTS[vyber -1]
else:
    print("Prosím vyberte číslo v rozmezí od 1 do 3.")

slova = vybrany_text.split()
slovo_s_velkym_pismenem = 0
slovo_velka_pismena = 0
slovo_mala_pismena = 0
cislo = 0
soucet_cisel = []
delky_slov = {}

ocistena_slova = []
for slovo in slova:
    ocistena_slova.append(slovo.strip(",."))

for slovo in ocistena_slova:
    if slovo.istitle():
        slovo_s_velkym_pismenem = slovo_s_velkym_pismenem + 1
    if slovo.isupper():
        slovo_velka_pismena = slovo_velka_pismena + 1
    if slovo.islower():
        slovo_mala_pismena = slovo_mala_pismena + 1
    if slovo.isnumeric():
        cislo = cislo + 1
        soucet_cisel.append(int(slovo))
    delka_slova = len(slovo)
    delky_slov[delka_slova] = delky_slov.get(delka_slova, 0) + 1

print("Počet slov v textu:", len(ocistena_slova))
print("Počet slov začínající velkým písmenem:",slovo_s_velkym_pismenem)
print("Počet slov psaných velkými písmeny:",slovo_velka_pismena)
print("Počet slov psaných malými písmeny:",slovo_mala_pismena)
print("Počet číšel v textu:",cislo)
print(ODDELOVAC)

delky_slov_list = list(delky_slov)
delky_slov_list.sort()

for delka in delky_slov_list:
    print(delka, delky_slov[delka] * "*", delky_slov[delka])

print(ODDELOVAC)
print("Pokud sečteme všechna čísla v tomto textu, dostaneme hodnotu:",(sum(soucet_cisel)))
