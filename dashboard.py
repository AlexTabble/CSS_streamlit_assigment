import numpy as np
import pandas as pd
import plotly.express as px
import plotnine as p9
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("st_assignment.csv")

df["ts"] = pd.to_datetime(df["ts"])
df["date"] = pd.to_datetime(df["ts"])


def subset(
    start_yr: int, end_year: int, start_month: int, end_month: int
) -> pd.DataFrame:
    year_mask = (df["date"].dt.year >= start_yr) & (df["date"].dt.year <= end_year)
    month_mask = (df["date"].dt.month >= start_month) & (
        df["date"].dt.month <= end_month
    )
    sub = df[year_mask & month_mask]
    return sub


def top_artists(sub: pd.DataFrame, n: int) -> list[str]:
    top = sub["Artist"].value_counts().head(n).index.tolist()
    return top


def top_n(sub: pd.DataFrame, n: int) -> pd.DataFrame:
    top_artists_list = sub["Artist"].value_counts().head(n).index.tolist()
    return sub[sub["Artist"].isin(top_artists_list)]


def artist_grouped(sub: pd.DataFrame, artist: str) -> pd.DataFrame:
    return (
        sub[sub["Artist"] == artist]
        .groupby("TrackName", as_index=False)
        .size()
        .rename(columns={"size": "listened"})
    )


def features_summary(sub: pd.DataFrame) -> pd.DataFrame:
    cols = sub.select_dtypes(np.float64).columns.drop(columns=["ms_played"])
    return sub[cols].mean()


def groupby_date(subset: pd.DataFrame) -> pd.DataFrame:
    return subset.groupby("date", as_index=False).agg(
        {"TrackName": "count", "Artist": "count"}
    )


def most_impactful_artist_by_af(sub: pd.DataFrame) -> dict[str]:
    sub = sub.dropna()
    most_emotional = sub[sub["valence"] == sub["valence"].max()]["Artist"].values
    most_energetic = sub[sub["energy"] == sub["energy"].max()]["Artist"].values
    most_danceable = sub[sub["danceability"] == sub["danceability"].max()][
        "Artist"
    ].values
    most_speechy = sub[sub["speechiness"] == sub["speechiness"].max()]["Artist"].values
    most_acoustic = sub[sub["acousticness"] == sub["acousticness"].max()][
        "Artist"
    ].values

    return {
        "valence": most_emotional[0],
        "energy": most_energetic[0],
        "danceability": most_danceable[0],
        "speechiness": most_speechy[0],
        "acousticness": most_acoustic[0],
    }


def most_impactful_song_by_af(sub: pd.DataFrame) -> dict[str]:
    sub = sub.dropna()
    most_emotional = sub[sub["valence"] == sub["valence"].max()]["TrackName"].values
    most_energetic = sub[sub["energy"] == sub["energy"].max()]["TrackName"].values
    most_danceable = sub[sub["danceability"] == sub["danceability"].max()][
        "TrackName"
    ].values
    most_speechy = sub[sub["speechiness"] == sub["speechiness"].max()][
        "TrackName"
    ].values
    most_acoustic = sub[sub["acousticness"] == sub["acousticness"].max()][
        "TrackName"
    ].values

    return {
        "valence": most_emotional[0],
        "energy": most_energetic[0],
        "danceability": most_danceable[0],
        "speechiness": most_speechy[0],
        "acousticness": most_acoustic[0],
    }



__all__ = [
    "df",
    "subset",
    "top_artists",
    "top_n",
    "artist_grouped",
    "features_summary",
    "groupby_date",
    "most_impactful_artist_by_af",
    "most_impactful_song_by_af",
]
