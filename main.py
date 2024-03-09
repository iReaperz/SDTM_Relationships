import plotly.graph_objects as go
import json
import colorlover as cl

# Загрузка данных из файла JSON
with open('graph_data.json') as json_file:
    data = json.load(json_file)

# Генерация градиента цветов для связей
colors = cl.scales['9']['qual']['Paired']

# Создание диаграммы Sankey
fig = go.Figure(data=[go.Sankey(
    valueformat=".0f",  # Формат значений
    valuesuffix="TWh",  # Суффикс значений
    node=dict(
        pad=15,  # Отступ узлов
        thickness=15,  # Толщина узлов
        line=dict(color="black", width=0.5),  # Цвет и ширина линий узлов
        label=data['data'][0]['node']['label'],  # Метки узлов
        color=data['data'][0]['node']['color'],  # Цвета узлов
    ),
    link=dict(
        source=data['data'][0]['link']['source'],  # Источники связей
        target=data['data'][0]['link']['target'],  # Цели связей
        value=data['data'][0]['link']['value'],  # Значения связей
        color=[colors[i % len(colors)] for i in data['data'][0]['link']['source']]  # Применение градиента цветов к связям
    ))])

# Отображение диаграммы Sankey
fig.show()


# import json

# # Исходные данные о связях между главными и побочными узлами
# connections = [
#     ("raw_dm", "dm"),
#     ("raw_dm", "ae"),
#     ("raw_dm", "sv"),
#     ("raw_dm", "tu"),
#     ("raw_dm", "tr"),
#     ("raw_dm", "lb"),
#     ("raw_dm", "pp"),
#     ("raw_dm", "rp"),
#     ("raw_dm", "vs"),
#     ("raw_dm", "se"),
#     ("raw_dm", "tv"),
#     ("raw_dm", "ta"),
#     ("raw_vs", "ta"),
#     ("raw_vs", "sv"),
#     ("raw_vs", "dm"),
#     ("raw_vs", "ae"),
#     ("raw_vs", "lb"),
#     ("raw_vs", "pp"),
#     ("raw_vs", "vs"),
#     ("raw_ae", "ae"),
#     ("raw_ae", "lb"),
#     ("raw_ae", "sv"),
#     ("raw_ae", "vs"),
#     ("raw_ae", "dm"),
#     ("raw_lb", "lb"),
#     ("raw_lb", "pp"),
#     ("raw_lb", "dm"),
#     ("raw_lb", "ae"),
#     ("raw_lb", "vs")
# ]

# # Создаем структуру данных для JSON
# graph_data = {
#     "data": [{
#         "node": {
#             "label": [],
#             "color": []
#         },
#         "link": {
#             "source": [],
#             "target": [],
#             "value": []
#         }
#     }]
# }

# # Заполняем структуру данными
# for main, sub in connections:
#     if main not in graph_data["data"][0]["node"]["label"]:
#         graph_data["data"][0]["node"]["label"].append(main)
#         graph_data["data"][0]["node"]["color"].append("blue")  # Присваиваем цвет главным узлам
#     if sub not in graph_data["data"][0]["node"]["label"]:
#         graph_data["data"][0]["node"]["label"].append(sub)
#         graph_data["data"][0]["node"]["color"].append("green")  # Присваиваем цвет побочным узлам
#     # Индексы узлов для создания связей
#     source_index = graph_data["data"][0]["node"]["label"].index(main)
#     target_index = graph_data["data"][0]["node"]["label"].index(sub)
#     graph_data["data"][0]["link"]["source"].append(source_index)
#     graph_data["data"][0]["link"]["target"].append(target_index)
#     # Значения связей (произвольные значения, так как они не были предоставлены)
#     graph_data["data"][0]["link"]["value"].append(100)  

# # Преобразуем структуру данных в JSON формат
# json_data = json.dumps(graph_data, indent=4)

# # Выводим JSON
# with open('graph_data.json', 'w') as json_file:
#     # Записываем JSON в файл
#     json.dump(graph_data, json_file, indent=None, separators=(',', ':'))

