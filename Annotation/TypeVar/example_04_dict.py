from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


def set_default_value(
    data: dict[K, V],
    key: K,
    new_value: V,
) -> tuple[K, V]:
    value = data.get(key)
    if not value:
        data[key] = new_value
    return key, data[key]


def get_default_value(
    data: dict[K, V],
    key: K,
    default_value: V,
) -> V:

    if value := data.get(key):
        return value
    return default_value


def main() -> None:
    ages = {
        "John": 30,
        "Kate": 33,
        "Nick": 0,
    }

    name, age = set_default_value(ages, key="Kate", new_value=33)
    print("res:", name, age)
    print(ages)
    res = set_default_value(ages, "Bob", 22)
    print("res", res)
    print(ages)

    kyle_res = get_default_value(ages, key="Kyle", default_value=16)
    print("kyle_res", kyle_res)
    print(ages)
    bob_res = get_default_value(ages, key="Bob", default_value=25)
    print("bob_res", bob_res)
    print(ages)
    nick_res = get_default_value(ages, key="Nick", default_value=42)
    print("nick_res", nick_res)
    print(ages)

    res = set_default_value(ages, "Nick", 25)
    print("res", res)
    print(ages)


if __name__ == "__main__":
    main()
