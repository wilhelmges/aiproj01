def count_words(sentence: str) -> int:
    """Повертає кількість слів у реченні."""
    return len(sentence.split())


def main() -> None:
    sentence = input("Введіть речення: ")
    print(f"Кількість слів: {count_words(sentence)}")


if __name__ == "__main__":
    main()
