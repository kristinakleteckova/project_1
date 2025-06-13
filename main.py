"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kristina Kletečková
email: kleteckova.kristina@gmail.com
"""
texts = [
    '''Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive 
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
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
username = (input("Please enter your username: "))
password = (input("Please enter your password: "))
separator = "-" * 38
print(separator)
credentials = username, password
number_of_texts = len(texts)

if credentials in users.items():  # ověření uživatele a umožnění zvolit text
  print(f"Welcome to the app, {username}.")
  print(f"We have {number_of_texts} texts to be analyzed.")
  print(separator)
  number = input(f"Enter number btw. 1 and {number_of_texts} to select: ")

  if not number.isdigit():  # ověření, zda se jedná o číslo
    print("Non-exist text, terminating the program")
    exit()
  else:
    number = int(number)

  index = number - 1

  if number <= number_of_texts and number > 0:  # ověření, zda existuje takto očíslovaný text
    print("Start analysis the text:")
    analyzed_text = texts[index]
    words = analyzed_text.split() # rozdělení textu na slova
    text_cleaning = [
        word.replace(",", "").replace(".", "").replace("\n", "") 
        for word in words 
        ] # odstranění interpunkce a ukončených řádků
    text_cleaning = [word for word in text_cleaning if word != ""]  # vymazání prázdných prvků 
    word_count = len(text_cleaning) 
    word_titlecase = len([word for word in text_cleaning if word.istitle()])
    word_uppercase = len([word for word in text_cleaning if word.isupper()])
    word_lowercase = len([word for word in text_cleaning if word.islower()])
    numeric = [word for word in text_cleaning if word.isnumeric()]
    numeric_string = len(numeric)
    sum_numbers = sum([int(number) for number in numeric])
    print(separator)
    print(
        f"There are {word_count} in the selected text.",
        f"There are {word_titlecase} titlecase words.",
        f"There are {word_uppercase} uppercase words.",
        f"There are {word_lowercase} lowercase words.",
        f"There are {numeric_string} numeric strings.",
        f"The sum of all numbers is {sum_numbers}.",
        sep = "\n"
          )
    print(separator)
    header = ["LEN", "OCCURENCES", "NR."]
    print(f"{header[0]:<3} | {header[1]:<20} | {header[2]}")
    print(separator)
    counter = dict()  # vytvoření slovníku do kterého budou ukládány četnosti výskytu jednotlivých délek slov
    
    for word in text_cleaning: # cyklus prochází jednotlivá slova textu, určuje délku slova a tu ukládá jako klíč
      length = len(word)
      counter[length] = counter.get(length, 0) + 1
    
    for key, value in sorted(counter.items()): # seřazení slovníku podle klíče a převedení na dvojice
      print(f"{key:<3} | {value * '*':<20} | {value}")  # vytvoření sloupcového grafu  klíč - počet písmen, hodnota četnost - výskytu
      
    print(separator)
  
  else:
    print("Non-exist text, terminating the program")
    exit()
else:
  print("Wrong username or password")