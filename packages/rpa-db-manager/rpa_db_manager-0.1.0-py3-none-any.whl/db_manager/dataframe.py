import pandas as pd


class DataframeHandler:
    def __init__(self) -> None:
        pass

    def normalize_column_names(self, df:pd.DataFrame) -> pd.DataFrame:
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        return df

    def create_unique_key_column(self, df:pd.DataFrame, key_columns:list[str], new_column_name:str="unique_key") -> pd.DataFrame:
        df[new_column_name] = df[key_columns].astype(str).agg('_'.join, axis=1)
        return df
