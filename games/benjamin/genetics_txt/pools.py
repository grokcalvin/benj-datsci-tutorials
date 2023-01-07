import random

class Entry:
    def __init__(self,value,weight=int) -> None:
        self.weight = weight
        self.value = value

pool = [
    Entry(value=1,weight=1),
    Entry(value=2,weight=1),
    Entry(value=3,weight=1),
    Entry(value=4,weight=1),
    Entry(value=5,weight=1),
    Entry(value=6,weight=1),
    Entry(value=7,weight=10),
    Entry(value=8,weight=1),
    Entry(value=9,weight=1),
    Entry(value=10,weight=1),
]

total_wieght = 0
for i in pool:
    total_wieght += i.weight

role = random.randint(1,total_wieght)

index_value = 0

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
    return items
print((select_from_pool(pool,5)))