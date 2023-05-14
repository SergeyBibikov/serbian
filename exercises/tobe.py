from random import choice

pronouns = ['я', 'ты', 'он', 'мы', 'вы', 'они']
negation = ['', 'не']
noun = ['инженер(ы)', 'студент(ы)', 'учитель(я)', 'программист(ы)', 'юрист(ы)']


def run(pronouns_list, tense, help):
    print("Type 'q' to quit, 'h' for grammar help, press any other key to continue")
    while True:
        inp = input()
        match inp:
            case 'q':
                break
            case 'h':
                help()
            case _:
                print(
                    f"{choice(pronouns_list)} {choice(negation)} {tense} {choice(noun)}\n")


def help_present():
    print(
        """
        Jednina | Množina
        --------|--------
        Ja sam  | Mi smo
        Ti si   | Vi ste
        On je   | Oni su
        """)


def present(): run(pronouns, '', help_present)
# def past(): run(pronouns, 'был(и)')


present()
