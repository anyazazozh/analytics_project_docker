import csv
import requests
import pandas as pd
import json


df = pd.read_csv('../data/all_df.csv', encoding='utf-8', sep=',')
sellers = df['Контрагент'].unique()
brands = df['ТМ'].unique()
report_type = df['Тип'].unique()
#print(df)


sellers_d = requests.get('http://127.0.0.1:8000/api/sellers/?format=json').json()
sellers_dict = dict((elem['name'], elem['id']) for elem in sellers_d)

for elem in sellers:
    if elem not in sellers_dict.values():
        requests.post('http://127.0.0.1:8000/api/sellers/?format=json', data={'name': elem})


brands_d = requests.get('http://127.0.0.1:8000/api/brands/?format=json').json()
brands_dict = dict((elem['name'], elem['id']) for elem in brands_d)

for elem in brands:
    if elem not in brands_dict.values():
        requests.post('http://127.0.0.1:8000/api/brands/?format=json', data={'name': elem})


report_type_d = requests.get('http://127.0.0.1:8000/api/report-types/?format=json').json()
report_type_dict = dict((elem['name'], elem['id']) for elem in report_type_d)

for elem in report_type:
    if elem not in report_type_dict.values():
        requests.post('http://127.0.0.1:8000/api/report-types/?format=json', data={'name': elem})


reports_d = json.loads(json.dumps(list(df.T.to_dict().values())))
sellers_d = requests.get('http://127.0.0.1:8000/api/sellers/?format=json').json()
sellers_dict = dict((elem['name'], elem['id']) for elem in sellers_d)

brands_d = requests.get('http://127.0.0.1:8000/api/brands/?format=json').json()
brands_dict = dict((elem['name'], elem['id']) for elem in brands_d)

report_type_d = requests.get('http://127.0.0.1:8000/api/report-types/?format=json').json()
report_type_dict = dict((elem['name'], elem['id']) for elem in report_type_d)

for elem in reports_d:
    # print(elem, elem.get('Контрагент'))
    for key_elem in sellers_dict.keys():
        # print(key_elem)
        if elem.get('Контрагент') == key_elem:
            # print(elem, elem.get('Контрагент'))
            elem['Контрагент'] = sellers_dict.get(key_elem)
            # print(sellers_dict.get('key_elem'))


for elem in reports_d:
    # print(elem, elem.get('ТМ'))
    for key_elem in brands_dict.keys():
        # print(key_elem)
        if elem.get('ТМ') == key_elem:
            # print(elem, elem.get('ТМ'))
            elem['ТМ'] = brands_dict.get(key_elem)
            # print(brands_dict.get('key_elem'))


for elem in reports_d:
    # print(elem, elem.get('Тип'))
    for key_elem in report_type_dict.keys():
        # print(key_elem)
        if elem.get('Тип') == key_elem:
            # print(elem, elem.get('Тип'))
            elem['Тип'] = report_type_dict.get(key_elem)


for elem in reports_d:
    d = elem.get('Период')
    s = elem.get('Контрагент')
    b = elem.get('ТМ')
    rt = elem.get('Тип')
    t, m = elem.get('Стоимость'), elem.get('Валовый Доход')
    if len(requests.get(f'http://127.0.0.1:8000/api/reports/?format=json&seller={s}&brand={b}&date={d}&report_type={rt}').json()):
        requests.put(f'http://127.0.0.1:8000/api/reports/?format=json&seller={s}&brand={b}&date={d}&report_type={rt}',
                     data={'turnover': t, 'margin': m})

    requests.post('http://127.0.0.1:8000/api/reports/?format=json',
                  data={'date': d, 'seller': s, 'brand': b, 'turnover': t, 'margin': m, 'report type': rt})
print(requests.get('http://127.0.0.1:8000/api/reports/?format=json&seller'))