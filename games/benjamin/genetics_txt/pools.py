import random

class Entry:
    def __init__(self,value,weight=int) -> None:
        self.weight = weight
        self.value = value
        
def select_from_pool(pool,roles):
    total_wieght = 0
    for i in pool:
        total_wieght += i.weight

    items = []
    for ii in range(roles):
        role = random.randint(1,total_wieght)
        index_value = 0
        for i, item in enumerate(pool):
            index_value += item.weight
            if role <= index_value:
            # and role < (index_value+(pool[i+1].weight)):
                items.append(item.value)
                break
    one_list_items = []
    for i in range(len(items)):
        if type(items[i]) == list:
            for ii in items[i]:
                one_list_items.append(ii)
        else:
            one_list_items.append(items[i])

    return one_list_items

pool_1_5 = [
    Entry(value=1,weight=1),
    Entry(value=2,weight=1),
    Entry(value=3,weight=1),
    Entry(value=4,weight=1),
    Entry(value=5,weight=10)
]
pool_6_10= [
    Entry(value=6,weight=1),
    Entry(value=7,weight=1),
    Entry(value=8,weight=1),
    Entry(value=9,weight=1),
    Entry(value=10,weight=10)
]

pool_11_15= [
    Entry(value=11,weight=1),
    Entry(value=12,weight=1),
    Entry(value=13,weight=1),
    Entry(value=14,weight=1),
    Entry(value=15,weight=10)
]

pool_1_15 = [
    Entry(value=select_from_pool(pool_1_5,5),weight=5),
    Entry(value=select_from_pool(pool_6_10,5),weight=3),
    Entry(value=select_from_pool(pool_11_15,5),weight=10),
]
#weapon functions
#armor functions
#food items

print(select_from_pool(pool_1_15,5))