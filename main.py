from sample_madlibs import chronique, une_vie_de_boy, miserables, art_de_la_guerre
import random


if __name__ == "__main__":
    stories = {
        "Chronique des temps obscurs": chronique,
        "Une vie de boy": une_vie_de_boy,
        "Les Misérables": miserables,
        "L'Art de la guerre": art_de_la_guerre
    }

    title, story = random.choice(list(stories.items()))

    print("\n" + "=" * 50)
    print(f"        🎭 MAD LIBS - {title}")
    print("=" * 50 + "\n")

    story.madlib()
