import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for cyr, tr in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyr)] = tr
    TRANS[ord(cyr.upper())] = tr.upper()


def normalize_filename(file_name: str) -> str:
    name_list = file_name.split(".")
    i = 0
    for name in name_list[:-1]:
        name_list[i] = name.translate(TRANS)
        name_list[i] = re.sub(r"\W", "_", name_list[i])
        i += 1
    return '.'.join(name_list)
