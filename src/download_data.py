"""
Download Premier League results + bookmaker odds from football-data.co.uk.

Saves one CSV per season into data/raw/. Raw files are never edited by hand:
if we ever need fresh copies, we just rerun this script.

Run from the project folder:
    python src/download_data.py
"""

from pathlib import Path
from urllib.request import urlretrieve

# The last 5 *completed* seasons. football-data.co.uk names each season
# by the last two digits of its start and end years: 2021/22 -> "2122".
SEASONS = ["2122", "2223", "2324", "2425", "2526"]

# "E0" is the site's code for the English top division (the Premier League).
URL_TEMPLATE = "https://www.football-data.co.uk/mmz4281/{season}/E0.csv"

# Where the files go. Path(__file__) is this script's own location, so this
# works no matter which folder you run the script from.
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for season in SEASONS:
        url = URL_TEMPLATE.format(season=season)
        save_path = RAW_DIR / f"E0_{season}.csv"

        print(f"Downloading {season} from {url} ...")
        urlretrieve(url, save_path)
        print(f"  saved to {save_path.relative_to(RAW_DIR.parent.parent)}")

    print("Done.")


if __name__ == "__main__":
    main()
