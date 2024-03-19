import subprocess as sp
import os
from pathlib import Path

here = Path(__file__).parent

DATADIR = Path(os.getenv("DATADIR", here / "data"))
RESULTSDIR = Path(os.getenv("RESULTSDIR", here / "results"))
FIGDIR = Path(os.getenv("FIGDIR", here / "figures"))


def main():
    RESULTSDIR.mkdir(exist_ok=True, parents=True)
    FIGDIR.mkdir(exist_ok=True, parents=True)

    for title in ["abyss", "isles", "last", "sierra"]:
        data_path = DATADIR / f"{title}.txt"
        results_path = RESULTSDIR / f"{title}.json"
        fig_path = FIGDIR / f"{title}.png"

        count_scipts = (here / "code" / "count.py").as_posix()
        plot_scripts = (here / "code" / "plot.py").as_posix()

        sp.run(["python3", count_scipts, data_path, "-o", results_path])
        sp.run(["python", plot_scripts, results_path, "-o", fig_path])


if __name__ == "__main__":
    raise SystemExit(main())