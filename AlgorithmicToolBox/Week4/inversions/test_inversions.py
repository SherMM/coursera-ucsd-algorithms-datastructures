from random import randrange

def generate_dataset(n, low=0, high=(10**9)+1):
    dataset = []
    for i in range(n):
        dataset.append(randrange(low, high))
    return dataset
