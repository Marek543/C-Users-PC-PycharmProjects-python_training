sklep = [
        {
            'produkt': 'chleb',
            'informacje': [
        {
            'ilość': 5,
            'cena': 10
        }
    ]
        },
        {
            'produkt': 'jabłka',
            'informacje': [
        {
            'ilość': 20,
            'cena': 3
        }
    ]
}
]

def znajdź_produkt(name):
    for nazwa in sklep:
        if nazwa['produkt'] == name:
            return nazwa

def czy_produkt_jest_w_sklepie(name):
    if not znajdź_produkt(name):
        return False
    return True
# print(znajdź_produkt('kabanosy'))
# print(czy_produkt_jest_w_sklepie('kabanosy'))

def znajdź_ilość(name):
   produkt_ze_sklepu = znajdź_produkt(name)
   for produkt in produkt_ze_sklepu['informacje']:
       return produkt['ilość']
# print(znajdź_ilość('chleb'))

def wyznacz_cene_jednostkową(name):
    produkt_ze_sklepu = znajdź_produkt(name)
    for produkt in produkt_ze_sklepu['informacje']:
        return produkt['cena']





