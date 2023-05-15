import random

def generate_data(size):
    list = []
    for i in range(size):
        list.append(random.randint(50,500))
    return list


# data = generate_data(500)
# print(data)
