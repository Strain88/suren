from typing import TypeVar, Sequence

T = TypeVar("T")


def repeat(val: T, times: int) -> list[T]:
    return [val] * times


def get_first_element(items: Sequence[T]) -> T:
    if items:
        return items[0]
    else:
        raise ValueError("items is empty")


def main() -> None:
    values = repeat(7, 3)
    lines = repeat("spam and eggs", 2)
    print("values:\t", values)
    print("lines:\t", lines)

    # for line in lines:
    #     print(line.title())

    # for value in values:
    #     print(value.bit_count())

    value = get_first_element(values)
    line = get_first_element(lines)
    print("value:\t", value)
    print("line:\t", line.title())


if __name__ == "__main__":
    main()
