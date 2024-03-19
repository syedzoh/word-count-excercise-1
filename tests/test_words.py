from pathlib import Path
import sys

here = Path(__file__).parent
sys.path.append((here / ".." / "code").as_posix())

from count import count_words


def test_word_count():
    assert count_words("well well fuck you") == {"well": 2, "fuck": 1, "you": 1}
    assert count_words("hello hello world") == {"hello": 2, "world": 1}