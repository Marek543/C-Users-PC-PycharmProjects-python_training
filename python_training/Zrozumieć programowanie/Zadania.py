
Oceny_szkolne = {
    "Matematyka": 5,
    "Biologia": 4,
    "Chemia": 3,
    "Polski": 2
}

# print("Przedmioty i oceny", Oceny_szkolne)

my_family = {
    "Ja": "name: Marek, surname: Madzia, birthday: 14.06.2001",
    "Brat 1": "name: Mateusz, surname: Madzia, birthday: 15.02.2010",
    "Brat 2": "name: Tomasz, surname: Madzia, birthday: 15.02.2010",
    "Rodzice": [
        {
        "Tata": "name: Krzysztof, surname: Trojak, birthday: 20.10.1974",
        "Rodzice": [
            {
            "Dziadek1": 1,
            "Babcia1": 2
            }
        ],
        "Mama": "name: Magdalena, surname: Madzia, birthday: 10.04.1973",
        "Parents": [
            {
            "Dziadek2": 1,
            "Babcia2": 1
            }
        ]
        }
    ]
}

# print(my_family)

wydatki_procentowo = {}

food = float(input("Ile miesięcznie wydajesz na jedzenie? "))
fun = float(input("Ile miesięcznie wydajesz na rozrywkę? "))
media = float(input("Ile miesięcznie wydajesz na opłaty? "))
other = float(input("Ile miesięcznie wydajesz na inne? "))

Total = food + fun + media + other

Jedzenie = food * 100 / Total
Rozrywka = fun * 100 / Total
Opłaty = media * 100 / Total
Inne = other * 100 / Total

wydatki_procentowo["Jedzenie"] = Jedzenie
wydatki_procentowo["Rozrywka"] = Rozrywka
wydatki_procentowo["Opłaty"] = Opłaty
wydatki_procentowo["Inne"] = Inne

selected_category = input("Wybierz jedną z powyższych kategorii. ")

print(f'Na {selected_category} wydajesz {wydatki_procentowo[selected_category]:.2f}% wszystkich wydatków.')

# Kategoria = input("Wpisz nazwę kategorii żeby poznać jej procentowy udział w wydatkach. " )
