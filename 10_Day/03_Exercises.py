#1
countries = ["Finland", "Iceland", "Ireland", "Germany", "Thailand", "Denmark"]
for country in countries:
    if 'land' in country:
        print(country)
#2
frutas=['banana', 'orange', 'mango', 'lemon']
reverFrut = []
for frutas in frutas:
    reverFrut.insert(0, frutas)
print(reverFrut)
#3
dataPaises = {
    "USA": ["English", "Spanish"],
    "India": ["Hindi", "English", "Tamil"],
    "China": ["Mandarin"],
    "Germany": ["German"],
}
idioma = set()
for pais, langs in dataPaises.items():
    idioma.update(langs)

totalIdioma = len(idioma)
print(f"Total de idiomas: {totalIdioma}")
#4
from collections import Counter
contarIdioma = Counter()
for pais, idioma in dataPaises.items():
    for idioma in idioma:
        contarIdioma[idioma] += 1

idiomaComun = contarIdioma.most_common(10)
print("Los diez idiomas más hablados:", idiomaComun)
#5
topPaises = {
    "China": 1400000000,
    "India": 1360004380,
    "USA": 331002651,
    "Indonesia": 273523615,
    "Pakistan": 220892340,
    "Brazil": 212559417,
    "Nigeria": 206139589,
    "Bangladesh": 164689383,
    "Russia": 145934462,
    "Mexico": 128933262,
}
ordenPaises = sorted(topPaises.items(), key=lambda x: x[1], reverse=True)
topDiez = ordenPaises[:10]
for paises, top in topDiez:
    print(f"{paises}: {top}")
