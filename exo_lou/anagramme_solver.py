import re
from typing import List

from unidecode import unidecode

non_word_pattern = re.compile(r'\W+')


def get_anagrams(text: str) -> List[List[str]]:
    words = [word for word in non_word_pattern.split(text) if len(word) > 1]
    words_keys = [tuple(sorted(unidecode(w.upper()))) for w in words]

    anagrams_di = dict()
    for key, word in zip(words_keys, words):
        anagrams_di.setdefault(key, list()).append(word)
    return list(groups for groups in anagrams_di.values() if len(groups) >= 2)


if __name__ == '__main__':
    base_text = "A Tanger, le gérant, sans argent, ne put lui acheter de " \
                "grenat. Le maire et Marie, à l'aube, lui en donnèrent un beau."
    print(get_anagrams(base_text))
