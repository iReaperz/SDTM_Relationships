# import plotly.graph_objects as go
# import json
# import colorlover as cl

# # Загрузка данных из файла JSON
# with open('graph_data_with_adam.json') as json_file:
#     data = json.load(json_file)

# # Генерация градиента цветов для связей
# colors = cl.scales['9']['qual']['Paired']

# # Создание диаграммы Sankey
# fig = go.Figure(data=[go.Sankey(
#     valueformat=".0f",  # Формат значений
#     valuesuffix="TWh",  # Суффикс значений
#     node=dict(
#         pad=40,  # Отступ узлов
#         thickness= 15,  # Толщина узлов
#         label=data['data'][0]['node']['label'],  # Метки узлов
#         color=data['data'][0]['node']['color'],  # Цвета узлов
#     ),
#     link=dict(
#         source=data['data'][0]['link']['source'],  # Источники связей
#         target=data['data'][0]['link']['target'],  # Цели связей
#         value=data['data'][0]['link']['value'],  # Значения связей
#         color=[colors[i % len(colors)] for i in data['data'][0]['link']['source']]  # Применение градиента цветов к связям
#     ))])

# # Отображение диаграммы Sankey
# fig.show()


# # import json

# # # Исходные данные о связях между узлами
# # connections = [
# #     ("raw", "sdtm"),
# #     ("sdtm", "adam"),
# #     ("raw_dm", "dm"),
# #     ("raw_dm", "adas"),
# #     ("raw_dm", "adfw"),
# #     ("raw_dm", "adpl"),
# #     ("raw_dm", "lb"),
# #     ("raw_dm", "adbc"),
# #     ("raw_dm", "adfr"),
# #     ("raw_dm", "adef"),
# #     ("raw_vs", "ta"),
# #     ("raw_vs", "adta"),
# #     ("raw_vs", "sv"),
# #     ("raw_vs", "adsv"),
# #     ("raw_vs", "dm"),
# #     ("raw_vs", "adsd"),
# #     ("raw_vs", "ae"),
# #     ("raw_vs", "adae"),
# #     ("raw_vs", "lb"),
# #     ("raw_vs", "adlb"),
# #     ("raw_vs", "pp"),
# #     ("raw_vs", "adpp"),
# #     ("raw_vs", "vs"),
# #     ("raw_vs", "advs"),
# #     ("raw_ae", "ae"),
# #     ("raw_ae", "adav"),
# #     ("raw_ae", "lb"),
# #     ("raw_ae", "adlb"),
# #     ("raw_ae", "sv"),
# #     ("raw_ae", "adsv"),
# #     ("raw_ae", "vs"),
# #     ("raw_ae", "advs"),
# #     ("raw_ae", "dm"),
# #     ("raw_ae", "adad"),
# #     ("raw_lb", "lb"),
# #     ("raw_lb", "adlb"),
# #     ("raw_lb", "pp"),
# #     ("raw_lb", "adpp"),
# #     ("raw_lb", "dm"),
# #     ("raw_lb", "addm"),
# #     ("raw_lb", "ae"),
# #     ("raw_lb", "adae"),
# #     ("raw_lb", "vs"),
# #     ("raw_lb", "advs")
# # ]

# # # Создаем структуру данных для JSON
# # graph_data = {
# #     "data": [{
# #         "node": {
# #             "label": [],
# #             "color": []
# #         },
# #         "link": {
# #             "source": [],
# #             "target": [],
# #             "value": []
# #         }
# #     }]
# # }

# # # Заполняем структуру данными
# # for main, sub in connections:
# #     if main not in graph_data["data"][0]["node"]["label"]:
# #         graph_data["data"][0]["node"]["label"].append(main)
# #         graph_data["data"][0]["node"]["color"].append("blue")  # Присваиваем цвет главным узлам
# #     if sub not in graph_data["data"][0]["node"]["label"]:
# #         graph_data["data"][0]["node"]["label"].append(sub)
# #         graph_data["data"][0]["node"]["color"].append("green")  # Присваиваем цвет побочным узлам
# #     # Индексы узлов для создания связей
# #     source_index = graph_data["data"][0]["node"]["label"].index(main)
# #     target_index = graph_data["data"][0]["node"]["label"].index(sub)
# #     graph_data["data"][0]["link"]["source"].append(source_index)
# #     graph_data["data"][0]["link"]["target"].append(target_index)
# #     # Значения связей (произвольные значения, так как они не были предоставлены)
# #     graph_data["data"][0]["link"]["value"].append(100)  

# # # Преобразуем структуру данных в JSON формат
# # json_data = json.dumps(graph_data, indent=None, separators=(',', ':'))

# # # Записываем JSON в файл
# # with open('graph_data_with_adam.json', 'w') as json_file:
# #     json_file.write(json_data)

import plotly.graph_objects as go

# Ваши данные
data = [
    ["raw_dm", "dm", "adas","adae"],
    ["raw_dm", "dm", "adae",],
    ["raw_dm", "dm", "adpl"],
    ["raw_dm", "lb", "adas"],
    ["raw_dm", "lb", "adfr"],
    ["raw_dm", "lb", "adef"],
    ["raw_vs", "ta", "adta"],
    ["raw_vs", "sv", "adsv"],
    ["raw_vs", "dm", "advs"],
    ["raw_vs", "lb", "adae"],
    ["raw_vs", "lb", "adlb"],
    ["raw_vs", "pp", "adpp"],
    ["raw_vs", "vs", "advs"],
    ["raw_ae", "ae", "adav"],
    ["raw_ae", "lb", "adlb"],
    ["raw_ae", "sv", "adsv"],
    ["raw_ae", "vs", "advs"],
    ["raw_ae", "dm", "adad"],
    ["raw_lb", "lb", "adlb"],
    ["raw_lb", "pp", "adpp"],
    ["raw_lb", "dm", "addm"],
    ["raw_lb", "ae", "adae"],
    ["raw_lb", "vs", "advs"]
]

# Создаем словарь для хранения узлов и связей
nodes = set()
links = []

# Добавляем узлы и связи на основе данных
for row in data:
    raw, sdtm, adam = row
    nodes.update([raw, sdtm, adam])
    links.append({"source": raw, "target": sdtm})
    links.append({"source": sdtm, "target": adam})

# Список цветов для связей
link_colors = ['rgba(50, 50, 50, 0.5)', 'rgba(214, 36, 36, 0.5)']
node_colors = ['blue', 'green', 'red']

# Создаем диаграмму Sankey
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        label=list(nodes),
        color=[node_colors[i % len(node_colors)] for i in range(len(nodes))]
    ),
    link=dict(
        source=[list(nodes).index(link['source']) for link in links],
        target=[list(nodes).index(link['target']) for link in links],
        value=[1] * len(links),
        color=[link_colors[i % len(link_colors)] for i in range(len(links))]  # Цвета связей
    )
)])

# Отображаем диаграмму
fig.show()

