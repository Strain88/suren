import random
from typing import TypeVar, Sequence, reveal_type

S = TypeVar("S", bound=str)


class MoveTitle(str):
    @property
    def featuring(self) -> str:
        return f"Now playing {self!r}"


def get_and_show_random_element(lines: Sequence[S]) -> S:
    random_line: S = random.choice(lines)
    print("chosen line:", random_line.title())
    return random_line


def main() -> None:
    elements = ["foo", "bar", "spam and eggs"]
    line = get_and_show_random_element(elements)
    print("got line:", line)

    movies = [
        MoveTitle("foo"),
        MoveTitle("fizz buzz"),
        MoveTitle("spam and eggs"),
    ]

    movie = get_and_show_random_element(movies)
    print(reveal_type(movie))
    print("movie:", movie.featuring)


if __name__ == "__main__":
    main()
