def madlib():
    adjective1 = input("Adjectif : ")
    noun1 = input("Nom commun : ")
    noun2 = input("Nom commun : ")
    place = input("Lieu : ")
    verb = input("Verbe : ")
    emotion = input("Émotion : ")
    adjective2 = input("Adjectif : ")
    plural_noun = input("Nom pluriel : ")
    adjective3 = input("Adjectif : ")

    story = f"""
Au XIXe siècle, dans une société profondément marquée par les
inégalités, un écrivain {adjective1} nommé Victor Hugo décide
de consacrer une partie de son œuvre aux personnes oubliées.

Il s'intéresse particulièrement à la justice, à la pauvreté,
à la dignité humaine et aux conséquences d'un système qui peut
transformer une simple faute en une longue condamnation.

Dans les rues d'un grand {place}, il imagine le parcours d'un homme
confronté à la misère et à la loi.

Cet homme cherche à {verb}, mais son passé continue de le poursuivre.

Autour de lui se trouvent des personnages confrontés à la faim,
à la pauvreté, à l'amour, à la violence et à l'espoir.

L'écrivain veut montrer qu'un être humain ne devrait pas être défini
uniquement par son {noun1} ou par les erreurs de son passé.

Il réfléchit alors au rôle de la loi, de la {noun2} et de la
compassion dans une société véritablement juste.

Son projet devient une immense fresque où la {emotion} côtoie
l'espoir.

À travers cette histoire, il dénonce les injustices qui frappent
les plus faibles et défend une vision plus {adjective2}
de la société.

Les personnages finissent par montrer que même dans les moments
les plus sombres, les {plural_noun} peuvent encore changer le destin.

C'est une histoire de souffrance, mais aussi de rédemption et
d'espérance humaine.

Une histoire profondément {adjective3}.
"""

    print(story)
