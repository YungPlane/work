import csv
import json

with open('file.csv', 'w', encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)

    csvWriter.writerow(['Объект', 'Значение'])
    csvWriter.writerow(['Ягода', 'Малина'])
    csvWriter.writerow(['Рыба', 'Килька'])
    csvWriter.writerow(['Дерево', 'Пихта'])

data = []

with open('file.csv', encoding="utf-8") as csvf:
    csvReader = csv.reader(csvf)
    for rows in csvReader:
        if rows and rows != ['Объект', 'Значение']:
            data.append({'Объект': rows[0], 'Значение': rows[1]})


with open('file.json', 'w', encoding="utf-8") as jsonf:
    jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))