import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby('class').size()
    result = result[result >= 5].reset_index()
    return result[['class']]
    