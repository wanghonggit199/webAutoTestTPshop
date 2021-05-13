import json

from config import BASE_DIR


def read_cart_data():
    with open(BASE_DIR + "/data/cart_data.json", encoding="utf-8") as f:
        data = json.load(f)
        # 声明一个空列表
        data_list = list()
        for i in data.values():
            data_list.append((i.get('good_name'),
                              i.get('expect')))

        print(data_list)


read_cart_data()
