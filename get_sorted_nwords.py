import csv
import sys
from sorting import sort_serbian_words


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'nwords.csv'
    with open(filename, encoding='utf-8') as f:
        words = csv.reader(f, delimiter=':')
        next(words)

        words_d = {}
        words_l: list[str] = []
        for w in words:
            words_d[w[0]] = w[1]
            words_l.append(w[0])

        words_l = sort_serbian_words(words_l)
    
    with open('sorted_nwords.csv', 'w+', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter=':')
        w.writerow(("serb", "rus"))
        for wo in words_l:
            w.writerow((wo, words_d[wo]))


main()
