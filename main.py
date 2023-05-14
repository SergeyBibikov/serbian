from jinja2 import Environment, FileSystemLoader
import csv
from transl import tt, substitute


def read_new_words():
    with open('nwords.csv') as f:
        words = csv.reader(f, delimiter=':')
        next(words)

        words = {substitute(w[0].translate(tt)): w[1] for w in words}
        return words


def get_known_words() -> dict[str, list[str]]:
    from bs4 import BeautifulSoup
    with open("words.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        a = soup.body.div.find_all('div', class_="wordPair")  # type:ignore

        known_words = {}
        for w in a:
            srb = w.find('div', class_="srb").text
            ru = w.find('div', class_="rus").text
            if known_words.get(srb):
                known_words[srb].append(ru)
            else:
                known_words[srb] = [ru]

        return known_words


def generate_words_addition():
    new_words = read_new_words()
    known_words = get_known_words()
    kw_list = known_words.keys()
    nw_list = new_words.keys()
    for w in nw_list:
        if w in kw_list:
            print(
                f"Word {w} is known. Known translations are: {known_words[w]}, new translation is {new_words[w]}")
            del new_words[w]
    with open(f"addition.html", mode="w") as f:
        env = Environment(loader=FileSystemLoader('.'))
        content = env.get_template(
            "new_words_template.txt").render(words=sorted(new_words.items()))
        f.write(content)


def generate_exercises():
    """Generates the html files with 70 words for a week"""

    w = read_new_words()
    w = list(w.items())
    count = 1
    while len(w) > 0:

        tmp = w[:70]
        w = w[70:]
        with open(f"./words_learning/ex{count}.html", mode="w") as f:
            env = Environment(loader=FileSystemLoader('./words_learning/'))
            content = env.get_template(
                "template.txt").render(words=tmp)
            f.write(content)
            count += 1


def main():

    generate_exercises()
    generate_words_addition()


main()
