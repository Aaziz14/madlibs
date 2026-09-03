def madlib():
    age = input("Âge : ")
    animal = input("Animal : ")
    adjective1 = input("Adjectif : ")
    place = input("Lieu : ")
    noun1 = input("Nom commun : ")
    noun2 = input("Nom commun : ")
    verb = input("Verbe : ")
    body_part = input("Partie du corps : ")
    adjective2 = input("Adjectif : ")
    companion = input("Nom d'un compagnon : ")

    story = f"""
Il y a des milliers d'années, dans une {place} immense et mystérieuse,
un jeune garçon de {age} ans nommé Torak voit sa vie bouleversée
après une terrible rencontre avec un {animal}.

Désormais seul, il comprend qu'une ancienne prophétie le désigne
comme celui qui devra rétablir l'équilibre entre les humains,
la nature et les animaux.

Pour accomplir cette mission, il doit atteindre une montagne
{adjective1} et retrouver un mystérieux {noun1}.

Son voyage le conduit à travers une forêt où chaque arbre,
chaque rivière et chaque {noun2} semblent cacher un secret.

Accompagné d'un jeune loup et de {companion}, Torak doit
{verb} malgré la peur et les nombreux dangers.

Il découvre bientôt que son véritable courage ne vient pas
de la force de son {body_part}, mais de sa capacité à rester
{adjective2} face aux épreuves.

Son aventure ne fait que commencer...
"""

    print(story)
