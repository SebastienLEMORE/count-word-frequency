def word_frequency(sentence: str, n: int) -> list[tuple[str, int]]:
    """
    Args:
        sentence (str): The sentence to analyze.
        n (int): The number of top words to return.
    Returns:
        list[tuple[str, int]]: A list of tuples where each tuple contains a word and its frequency in the sentence.
            The list is sorted by decreasing frequency and alphabetical order in case of tie.
    """
    words = sentence.lower().split()

    freq_dict: dict[str, int] = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    freq_list: list[tuple[str, int]] = [(word, freq_dict[word]) for word in freq_dict]

    freq_list.sort(key=lambda x: (-x[1], x[0]))

    return freq_list[:n]


def test_word_frequency():
    sentence = "baZ bAr foo fOo zblah zbLah zblah bAz Toto bar"
    n = 3
    expected_output: list[tuple[str, int]] = [
        ("zblah", 3),
        ("bar", 2),
        ("baz", 2),
    ]
    assert word_frequency(sentence, n) == expected_output

    sentence = "b b a a e e c c d d f f"
    n = 10
    expected_output: list[tuple[str, int]] = [
        ("a", 2),
        ("b", 2),
        ("c", 2),
        ("d", 2),
        ("e", 2),
        ("f", 2),
    ]
    assert word_frequency(sentence, n) == expected_output
