def madlib():
    adjective1 = input("Adjectif : ")
    place = input("Lieu : ")
    noun1 = input("Nom commun : ")
    verb = input("Verbe : ")
    adjective2 = input("Adjectif : ")
    emotion = input("Émotion : ")
    noun2 = input("Nom commun : ")
    adjective3 = input("Adjectif : ")
    verb2 = input("Verbe : ")
    plural_noun = input("Nom pluriel : ")

    story = f"""
Dans une petite ville de {place}, un jeune garçon nommé Toundi
quitte précipitamment sa famille après une dispute particulièrement
{adjective1}.

Il trouve refuge auprès du père Gilbert, un missionnaire qui lui
offre protection, éducation et une nouvelle perspective sur le monde.

Après la disparition du missionnaire, Toundi commence à travailler
comme domestique auprès de M. Decazy, un administrateur colonial.

Au début, il admire cette nouvelle vie et pense avoir découvert
un univers {adjective2}.

Il devient rapidement un observateur privilégié de la maison.
Chaque jour, il voit les habitudes, les conversations et les
relations entre les habitants de la résidence.

Peu à peu, Toundi comprend que derrière les apparences se cachent
des injustices, du racisme et beaucoup d'hypocrisie.

L'arrivée de Mme Decazy change encore davantage son quotidien.
Toundi découvre des secrets qu'il aurait préféré ne jamais connaître.

Pris entre la peur et la {emotion}, il doit apprendre à
{verb2} pour protéger sa propre vie.

Mais dans ce monde dominé par le pouvoir, même un simple
{noun1} peut devenir dangereux.

Toundi réalise alors que les {plural_noun} qu'il admirait autrefois
ne sont peut-être pas aussi {adjective3} qu'il le croyait.

Son histoire devient ainsi le témoignage d'une société profondément
marquée par les inégalités.
"""

    print(story)
  
