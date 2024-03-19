from collections import Counter
from typing import Dict, Sequence
from pathlib import Path
import json
import argparse


def count_words(text: str) -> Dict[str, int]:
    """Count the number of times each word appears in a
    file and save the 10 most common words.
    """
    delimiters = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()

    counts = Counter()

    for line in text.split("\n"):

        # replace all delimiters with spaces
        for delimiter in delimiters:
            line = line.replace(delimiter, " ")

        counts.update(line.split())

    # grab the 10 most common words
    return dict(counts.most_common(10))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=count_words.__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=None)
    args = vars(parser.parse_args(argv))

    # count the words
    if not args["path"].is_file():
        print(f"{args['path']} is not a file")
        return 1
    counts = count_words(args["path"].read_text())
    output = json.dumps(counts, indent=4)
    print(output)

    # save the output
    if args["output"] is not None:
        args["output"].parent.mkdir(parents=True, exist_ok=True)
        args["output"].write_text(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
