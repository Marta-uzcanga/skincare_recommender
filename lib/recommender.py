def get_rec(name):
    import pandas as pd
    import load_csv
    df_filtered = load_csv.load_csv('recommender_data.csv')
    if name in list(df_filtered['names']):
        cluster = df_filtered[df_filtered.names == name].clusters
        sample = df_filtered[df_filtered.clusters == cluster.values[0]].sample()

    else:
        print("We don't recognise this product, but here is another one that we are sure you will love:")
        sample = df_filtered.sample()

    return sample['names']