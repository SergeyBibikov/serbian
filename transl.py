let = {
    "А": "А",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Ђ": "Đ",
    "Е": "E",
    "Ж": "Ž",
    "З": "Z",
    "И": "I",
    "Ј": "J",
    "К": "K",
    "Л": "L",
    "Љ": "Lj",
    "М": "M",
    "Н": "N",
    "Њ": "Nj",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "Ћ": "Ć",
    "У": "U",
    "Ф": "F",
    "Х": "H",
    "Ц": "C",
    "Ч": "Č",
    "Џ": "Dž",
    "Ш": "Š",

    "а": "а",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "ђ": "đ",
    "е": "e",
    "ж": "ž",
    "з": "z",
    "и": "i",
    "ј": "j",
    "к": "k",
    "л": "l",
    "љ": "lj",
    "м": "m",
    "н": "n",
    "њ": "nj",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "ћ": "ć",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "č",
    "џ": "dž",
    "ш": "š"
}

tt = {1040: 'А', 1041: 'B', 1042: 'V', 1043: 'G', 1044: 'D', 1026: 'Đ', 1045: 'E', 1046: 'Ž', 1047: 'Z', 1048: 'I', 1032: 'J', 1050: 'K', 1051: 'L', 1033: 'Lj', 1052: 'M', 1053: 'N', 1034: 'Nj', 1054: 'O', 1055: 'P', 1056: 'R', 1057: 'S', 1058: 'T', 1035: 'Ć', 1059: 'U', 1060: 'F', 1061: 'H', 1062: 'C', 1063: 'Č', 1039: 'Dž', 1064: 'Š',
      1072: 'а', 1073: 'b', 1074: 'v', 1075: 'g', 1076: 'd', 1106: 'đ', 1077: 'e', 1078: 'ž', 1079: 'z', 1080: 'i', 1112: 'j', 1082: 'k', 1083: 'l', 1113: 'lj', 1084: 'm', 1085: 'n', 1114: 'nj', 1086: 'o', 1087: 'p', 1088: 'r', 1089: 's', 1090: 't', 1115: 'ć', 1091: 'u', 1092: 'f', 1093: 'h', 1094: 'c', 1095: 'č', 1119: 'dž', 1096: 'š'}


def substitute(word: str):
    word = word.replace("[", '<span class="stress">')
    return word.replace("]", '</span>')