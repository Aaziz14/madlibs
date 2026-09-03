def madlib():
    adjective1 = input("Adjectif : ")
    opponent = input("Nom de l'adversaire : ")
    place = input("Lieu : ")
    noun1 = input("Nom commun : ")
    verb1 = input("Verbe : ")
    strategy = input("Nom d'une stratégie : ")
    adjective2 = input("Adjectif : ")
    noun2 = input("Nom commun : ")
    verb2 = input("Verbe : ")
    plural_noun = input("Nom pluriel : ")

    story = f"""
Dans la Chine ancienne, un stratège {adjective1} nommé Sun Zi
réfléchit profondément à l'art de conduire une armée.

Pour lui, gagner une bataille ne signifie pas simplement posséder
plus de soldats ou plus d'armes.

Lorsqu'un commandant doit affronter {opponent} près de {place},
il commence par étudier attentivement son adversaire.

Il observe son {noun1}, ses habitudes, ses forces et ses faiblesses.

Plutôt que de se précipiter dans le combat, il cherche d'abord
à {verb1} les conditions qui pourraient lui donner l'avantage.

Une bonne stratégie, comme {strategy}, peut parfois permettre
de remporter une victoire sans livrer une bataille longue et coûteuse.

Le commandant doit rester {adjective2} et contrôler ses émotions.

Il doit également comprendre l'importance de l'information,
de la discipline et du {noun2}.

Son objectif n'est pas seulement de {verb2}, mais de créer une
situation dans laquelle l'adversaire perd progressivement
sa capacité à résister.

Ainsi, la connaissance, la préparation et l'intelligence peuvent
être plus importantes que la force brute.

Le véritable stratège sait également reconnaître le moment où
il faut avancer et celui où il faut attendre.

Dans la guerre comme dans de nombreuses situations de la vie,
les {plural_noun} et la réflexion peuvent parfois être plus
puissants que la confrontation directe.
"""

    print(story)
