def ReadDataset(filename):
    dataset = []
    with open(filename, 'r') as f:
        dataset = f.readlines()
        dataset = dataset.split('/n','')
    return dataset