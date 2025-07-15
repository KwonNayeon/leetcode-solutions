import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    df_filtered = df[
        (df['activity_date'] >= '2019-06-28') &
        (df['activity_date'] < '2019-07-28') &
        (df['activity_type'].notna())
        ]

    result = df_filtered.groupby('activity_date')['user_id'].nunique().reset_index()
    result.columns = ['day', 'active_users']
    return result
    