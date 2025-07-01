import pandas as pd
import streamlit as st


def preprocess_dataframe(dataframe: pd.DataFrame) -> tuple[pd.DataFrame, list[int]]:
    dataframe["Website"] = dataframe["Website"].map(lambda x: x.capitalize())

    stats: list[int] = [0 for _ in range(3)]

    for index, name in enumerate(["Website", "Password", "Username"]):
        stats[index] = max([len(_) for _ in dataframe[name].dropna()])

    return dataframe, stats
