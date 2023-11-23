import pandas as pd
from tabulate import tabulate



df = pd.read_json("spotify-data/spotify-acc-data-2023/StreamingHistory0.json")



print("spotify analysis 2023")

print("\ntop artists by listen time")
print(tabulate(
    df.groupby("artistName")
      .sum("msPlayed")
      .sort_values("msPlayed", ascending=False)
      .rename({"msPlayed": "hoursPlayed"}, axis="columns")
      .head()
      /3600_000
, headers=["artistName", "hoursPlayed"], tablefmt="rounded_grid"
))

print("\ntop songs by listen time")
print(tabulate(
    df.groupby("trackName")
      .sum("msPlayed")
      .sort_values("msPlayed", ascending=False)
      .rename({"msPlayed": "hoursPlayed"}, axis="columns")
      .head()
      /3600_000
, headers=["trackName", "hoursPlayed"], tablefmt="rounded_grid"
))

print("\ntop artists by listen count")
print(tabulate(
    df[["artistName", "msPlayed"]]
      .groupby("artistName")
      .count()
      .sort_values("msPlayed", ascending=False)
      .rename({"msPlayed": "count"}, axis="columns")
      .head()
, headers=["artistName", "count"], tablefmt="rounded_grid"
))

print("\ntop songs by listen count")
print(tabulate(
    df[["trackName", "msPlayed"]]
      .groupby("trackName")
      .count()
      .sort_values("msPlayed", ascending=False)
      .rename({"msPlayed": "count"}, axis="columns")
      .head()
, headers=["trackName", "count"], tablefmt="rounded_grid"
))


