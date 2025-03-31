
from countries_data import countries_data
#1
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

#resultadosordenados
print("Países ordenados por nombre:")
for country in sorted_by_name:
    print(country['name'])

print("\nPaíses ordenados por capital:")
for country in sorted_by_capital:
    print(country['name'], country['capital'])

print("\nPaíses ordenados por población:")
for country in sorted_by_population:
    print(country['name'], country['population'])

#2
languages = {}

for country in countries_data:
    for language in country['languages']:
        if language not in languages:
            languages[language] = 0
        languages[language] += 1

#Ordena los idiomas 
sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

#10 idiomas mas hablados
print("\nLos 10 idiomas más hablados por ubicación:")
for language, count in sorted_languages[:10]:
    print(f"{language}: {count} países")

#3
top_10_population = sorted_by_population[:10]

#10 maspoblados
print("\nLos 10 países más poblados:")
for country in top_10_population:
    print(f"{country['name']}: {country['population']}")
