import matplotlib.pyplot as plt
from typing import Dict, Sequence, Optional
import json
import argparse
from pathlib import Path


def plot(data: Dict[str, int], filename: Optional[Path] = None):
    # Create figure folder if not exists

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(data.keys(), data.values())
    ax.set_title("10 most common words")
    if filename is not None:
        filename.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(filename)
    else:
        plt.show()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Plot bar chart of word counts")
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=None)
    args = vars(parser.parse_args(argv))

    # count the words
    if not args["path"].is_file():
        print(f"{args['path']} is not a file")
        return 1
    data = json.loads(args["path"].read_text())
    plot(data, args["output"])
    print(f"Figure saved to {args['output']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
