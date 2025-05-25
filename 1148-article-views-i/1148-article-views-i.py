import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[views["author_id"] == views["viewer_id"]].rename(columns={'author_id': 'id'})
    result = filtered[["id"]].drop_duplicates().sort_values("id")
    return result
    