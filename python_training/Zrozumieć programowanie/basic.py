# print("Kalkulator lokaty z roczną kapitalizacją")
# value_input = input("Jaka jest początkowa wartość kapitału? ")
# intrest_input = input("Jakie jest oprocentowanie? ")
# time_input = input("Ile lat będzie trwać lokata? ")
#
# wartość_pocz = float(value_input)
# oprocentowanie = float(intrest_input)
# liczba_lat = float(time_input)
#
# wartość = wartość_pocz * (1 + oprocentowanie/100) ** liczba_lat
#
# print(f"Po {liczba_lat} latach lokata będzie wynosić {wartość:.2f} złotych")

# name = input("Jak masz na imię? ")
# print(f"Twoje imię {name} zawiera {len(name)} liter")

# miasto = input("W jakim mieście mieszkasz? ")
# print(f"Jako miło że mieszkasz w {miasto.title()}")

ford = "ford=\t\t ab100100\n"
audi = "audi=\t\t EEE 123123\n"
citroen = "citroen=\t Zk-300300\n"
honda = "honda=\t\t AB210210"
rejestr = (ford + audi + citroen + honda)
rejestr = rejestr.upper()
rejestr = rejestr.replace(' ', '')
rejestr = rejestr.replace('-', '')
print(rejestr)
