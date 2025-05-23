import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, how = 'left', left_on= 'id', right_on= 'customerId')
    no_orders = df[df['customerId'].isna()]
    result = no_orders[['name']].copy()
    result.columns = ['Customers']

    return result

    