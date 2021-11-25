questionaire1 = (
                 ("Quelle est la capitale de la France ?", ("Marseille", "Nantes", "Paris", "Lille"), "Paris"),
                 ("Quelle est la capitale de l'Italie ?", ("Naples", "Rome", "Milan", "Florence"), "Rome"),
                 ("Quelle est la capitale de l'Espagne ?", ("Madrid", "Seville", "Barcelone", "Valence"), "Madrid"),
                 ("Quelle est la capitale de la Belgique ?", ("Namur", "Antwerp", "Ghent", "Brussels"), "Brussels")
                )


def demander_nombre(nb_min, nb_max):
    nb_donner_str = input(f"Votre réponse (entre {nb_min} et {nb_max}): ")
    try:
        nb_donner_int = int(nb_donner_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer un nombre. Réessayez. ")
        return demander_nombre(nb_min, nb_max)
    else:
        if nb_donner_int > nb_max or nb_donner_int < nb_min:
            print(f"ERREUR: Le nombre doit être compris entre {nb_min} et {nb_max}. Réessayez.")
            return demander_nombre(nb_min, nb_max)
    return nb_donner_int


def poser_question(question):
    answer_counter = 0
    print(f"{question[0]}")
    for choix in question[1]:
        answer_counter += 1
        print(f"{answer_counter} - {choix}")
    print()
    user_answer = demander_nombre(1, len(question[1]))
    print()
    if question[1][user_answer-1] == question[2]:
        print("Bonne réponse.")
        return True
    else:
        print("Mauvaise réponse.")
    print()


def lancer_questionaire(questionaire):
    score = 0
    for question in questionaire:
        if poser_question(question):
            score += 1
    print()
    print(f"Score : {score}/{len(questionaire)}")


lancer_questionaire(questionaire1)
