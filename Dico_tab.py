def print_menu():
    print("\nGestion d'un dictionnaire")
    print("Le dictionnaire comporte pour le moment 25 mots.")
    print("Ajout d'un mot __________________________________1")
    print("Suppression d'un mot ____________________________2")
    print("Recherche d'un mot ______________________________3")
    print("Affichage de tout le dictionnaire _______________4")
    print("Fin du programme ________________________________0")
    return input("\nVotre choix : ")

def add_word(dictionnaire):
    mot = input("Entrez le mot à ajouter : ")
    definition = input("Entrez la définition du mot : ")
    if mot in dictionnaire:
        print("Erreur : le mot est déjà présent dans le dictionnaire.")
    else:
        dictionnaire[mot] = definition
        print(f"Le mot '{mot}' a été ajouté avec succès.")
    return dictionnaire

def del_word(dictionnaire):
    mot = input("Entrez le mot à supprimer : ")
    if mot in dictionnaire:
        del dictionnaire[mot]
        print(f"Le mot '{mot}' a été supprimé avec succès.")
    else:
        print("Erreur : le mot n'existe pas dans le dictionnaire.")
    return dictionnaire

def search_word(dictionnaire):
    mot = input("Entrez le mot à rechercher : ")
    if mot in dictionnaire:
        print(f"Définition de '{mot}' : {dictionnaire[mot]}")
    else:
        print("Erreur : le mot n'existe pas dans le dictionnaire.")

def display_dictionnary(dictionnaire):
    for mot, definition in sorted(dictionnaire.items()):
        print(f"{mot} : {definition}")

def main():
    dictionnaire = {}
    while True:
        choix = print_menu()
        if choix == '1':
            dictionnaire = add_word(dictionnaire)
        elif choix == '2':
            dictionnaire = del_word(dictionnaire)
        elif choix == '3':
            search_word(dictionnaire)
        elif choix == '4':
            display_dictionnary(dictionnaire)
        elif choix == '0':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()