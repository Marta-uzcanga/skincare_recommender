def filter_df(data, vegan, gluten_free, cruelty_free):
    df2 = data.copy()
    df2 = df2[df2.vegan == vegan]
    df2 = df2[df2.gluten_free == gluten_free]
    df2 = df2[df2.cruelty_free == cruelty_free]
    return df2