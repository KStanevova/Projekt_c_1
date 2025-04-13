"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kateřina Stanevová
email: KStanevova@seznam.cz
"""
# Registrovaní uživatelé
uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
    }

# separátor
sep = "-" * 40

# Texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',

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

# Přihlášení uživatele
username = input("Zadej uživatelské jméno: ")
password = input("Zadej heslo: ")
print(sep)

# Ověření uživatele a případné ukončení programu
if uzivatele.get(username) != password:
    print(f"username:{username}")
    print(f"password:{password}")
    print("unregistered user, terminating the program..")
    exit()

# Pokud je přihlášení správné, pokračuje dál:
print(f"Welcome to the app, {username} \nWe have {len(TEXTS)} texts to be analyzed.")
print(sep)

# Výběr textu
vyber = input(f"Enter a number btw. 1-{len(TEXTS)} to select: ")
print(sep)

# Ověření, zda je vstup číslo v daném rozsahu a případné ukončení programu
if not vyber.isdigit():
    print(f"You entered a letter instead of a number! \nPlease enter a number btw. 1 and {len(TEXTS)}! \nThe program is terminated, try it again.")
    exit()

# Ověření, zda je vstup čísla v daném rozsahu a případné ukončení programu
vyber = int(vyber)

if not (1 <= vyber <= len(TEXTS)):
    print(f"You selected a number outside the offer! \nPlease enter a number btw. 1 and {len(TEXTS)}! \nThe program is terminated, try it again.")
    exit()
else:
    vybrany_text = TEXTS[vyber - 1]

    # Rozdělí text na jednotlivá slova
    slova = vybrany_text.split()

    # Počet slov v textu a print
    pocet_slov = len(slova)
    print(f"There are {pocet_slov} words in the selected text.")

    # Počet slov začínajících velkým písmenem a print
    pocet_titlecase = len([slovo for slovo in slova if slovo.istitle()])
    print(f"There are {pocet_titlecase} titlecase words.")

    # Počet slov psaných velkými písmeny a print
    pocet_upper = len([slovo for slovo in slova if slovo.isupper()])
    print(f"There are {pocet_upper} uppercase words.")

    # Počet slov psaných malými písmeny a print
    pocet_lower = len([slovo for slovo in slova if slovo.islower()])
    print(f"There are {pocet_lower} lowercase words.")

    # Počet čísel (ne cifer) a print
    pocet_cisel = len([slovo for slovo in slova if slovo.isdigit()])
    print(f"There are {pocet_cisel} numeric strings.")

    # Suma všech čísel (ne cifer) v textu a print
    suma_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())
    print(f"The sum of all the numbers {suma_cisel}.")

print(sep)
print(f"{'LEN':<4}| {'OCCURENCES':<14}| {'NR.'}")
print(sep)

# Počítání délky slov
delky = [len(slovo.strip('.,!?()[]{}"')) for slovo in slova]

# Počítání výskytů jednotlivých délek slov
delky_dict = {}

for delka in delky:
    if delka in delky_dict:
        delky_dict[delka] += 1
    else:
        delky_dict[delka] = 1

# Zobrazení sloupcového grafu
for delka, pocet in sorted(delky_dict.items()):
    print(f"{delka:<4}| {'*' * pocet:<13} | {pocet}")
      