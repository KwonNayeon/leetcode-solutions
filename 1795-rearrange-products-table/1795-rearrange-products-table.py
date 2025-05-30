# 3개 store 컬럼을 1개로 "녹여서" 세로로 길게 만들기
# store1, store2, store3 → store (컬럼명) + price (값)

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    df = pd.melt(products,
                id_vars=["product_id"],
                value_vars=["store1", "store2", "store3"],
                var_name="store",
                value_name="price")

    df = df.dropna(subset=["price"])

    return df
    