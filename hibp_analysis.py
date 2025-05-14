from statistics import mean
from statistics import mode
from statistics import median
from statistics import stdev
import re

def turn_to_dict(texto):
    result = {}
    match = re.search(r'Counter\(\{(.+)\}\)', texto)
    if match:
        data = match.group(1)
    else:
        data = texto.strip().strip('{}')
    pairs = data.split(",")
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(":", 1)
            key = key.strip().strip("'\"")
            value = value.strip().strip("})")
            result[key] = int(value)
    return result

def turn_to_list_tuples(data):
    result = []
    data = data.strip().strip("[]")
    elements = data.split("),")
    for element in elements:
        element = element.strip().strip("()").replace("'", "")
        if ',' in element:
            year, times = element.split(",", 1)
            result.append((year.strip(), int(times.strip())))
    return result

def rearrange_by_value(tupla):
    return tupla[1]

with open("hibp_cleaned.txt", "r") as file:
    lines = file.readlines()
count_dict = {}
sorted_years = []
data_classes = {}
for i in range(len(lines)):
    line = lines[i]
    if "Breaches by name" in line:
        count_dict = turn_to_dict(lines[i+1])
    elif "Breaches by date" in line:
        sorted_years = turn_to_list_tuples(lines[i+1])
    elif "Data types leaked" in line:
        data_classes = turn_to_dict(lines[i+1])

sorted_by_freq = sorted(sorted_years, key=rearrange_by_value, reverse=True)
top_3_years = sorted_by_freq[:3]
bottom_3_years = sorted_by_freq[-3:]

sorted_pages = sorted(count_dict.items(), key=rearrange_by_value, reverse=True)
top_pages = sorted_pages[:5]
bottom_pages = sorted_pages[-5:]

# Estadísticas
valores = list(count_dict.values())
promedio = mean(valores)
mediana = median(valores)
moda = mode(valores)
desviacion = stdev(valores)

# Tipo de dato más vulnerable
datos_vulnerables = sorted(data_classes.items(), key=rearrange_by_value, reverse=True)
top_3_data_type = datos_vulnerables[:3]

# Mostrar resultados
print("Tres años con más filtraciones:")
for year, times in top_3_years:
    print(f"Año: {year} , {times} filtraciones")

print("\nTres años con menos filtraciones:")
for year, times in bottom_3_years:
    print(f"Año: {year} , {times} filtraciones")

print("\nSitios con más cuentas comprometidas:")
for page, times in top_pages:
    print(f"{page} : {times:,} cuentas")

print("\nSitios con menos cuentas comprometidas:")
for page, times in bottom_pages:
    print(f"{page} : {times:,} cuentas")

print(f"\nPromedio de cuentas comprometidas por sitio: {promedio:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:}")
print(f"Desviación estándar: {desviacion:.2f}")

print(f"\nTop tres tipos de datos más vulnerable:")
for data, times in top_3_data_type:
    print(f"tipo de dato: {data}, filtraciones: {times}")
