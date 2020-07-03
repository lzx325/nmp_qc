import datasets
if __name__=="__main__":
    root='./data/qm9/dsgdb9nsd/'
    train_ids=["dsgdb9nsd_133880.xyz"]
    data_train = datasets.Qm9(root, train_ids, edge_transform=datasets.utils.qm9_edges, e_representation='raw_distance')
    print(data_train[0])