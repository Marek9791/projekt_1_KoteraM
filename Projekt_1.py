# HLAVIČKA
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marek Kotěra
email: marek.kotera@gmail.com
discord: marekk.0755
""")

print("-" *40)

# Vytvoření databáze uživatelů
registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Vyžádání přihlašovacího jména a hesla
username = input("Zadej přihlašovací jméno: ")
password = input("Zadej heslo: ")

import sys

# Ověření uživatele
if username in registered_users and registered_users[username] == password:
    # Uživatel je registrovaný
    print("Welcome to the app,", username, "\n""We have 3 texts to be analyzed.")
    print("-" *40)
else:
    # Uživatel není registrovaný
    print("Unregistered user, terminating the program..")
    sys.exit()

# Výběr textů uložených v proměnné TEXTS
TEXTS = ['''
1. Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 febet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''2. At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''3. The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
selected_text = TEXTS
choice = input("Enter a number btw. 1 and 3 to select: ")
if choice.isdigit():
    choice = int(choice)
    if choice < 1 or choice > 3:
        print("Invalid number, the program will be terminated.")
        sys.exit()
    else:
        selected_text = TEXTS[choice - 1]
else:
    print("Invalid input, the program will be terminated.")
    sys.exit()

# Tvorba statistik
words = selected_text.split()
total_words = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numbers_count = 0
numbers_sum = 0

for word in words:
    total_words += 1
    if word.istitle():
        titlecase_words += 1
    elif word.isupper():
        uppercase_words += 1
    elif word.islower():
        lowercase_words += 1
    elif word.isdigit():
        numbers_count += 1
        numbers_sum += int(word)

# Výpis statistik
print("There are", titlecase_words, "titlecase words.")
print("There are", uppercase_words, "uppercase words.")
print("There are", lowercase_words, "lowercase words.")
print("There are", numbers_count, "numeric strings.")
print("The sum of all the numbers", numbers_sum)
print("-" * 40)  

print("LEN|  OCCURENCES  |NR.")
print("-"*40)

# Vytvoření slovníku pro ukládání délek slov a jejich četností
word_length_frequency = {}

# Rozdělení textu na slova a počítání délek slov
words = TEXTS[0].split()
for word in words:
    word_length = len(word.strip(".,"))
    if word_length in word_length_frequency:
        word_length_frequency[word_length] += 1
    else:
        word_length_frequency[word_length] = 1

sorted_word_length_frequency = sorted(word_length_frequency.items())

# Výpis sloupcového grafu
for length, occurrences in sorted_word_length_frequency:
    print(f"{length:2}| {'*' * occurrences} {occurrences}")








