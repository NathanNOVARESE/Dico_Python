def print_menu():
    print("\n" + "="*40)
    print(" " * 10 + "Gestion d'un dictionnaire")
    print("="*40)
    print("Le dictionnaire comporte pour le moment 25 mots.")
    print("-" * 40)
    print("1. Ajout d'un mot")
    print("2. Suppression d'un mot")
    print("3. Recherche d'un mot")
    print("4. Affichage de tout le dictionnaire")
    print("5. Modification d'un mot")
    print("0. Fin du programme")
    print("="*40)
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

def modify_word(dictionnaire):
    mot = input("Entrez le mot à modifier : ").strip()
    if mot in dictionnaire:
        nouveau_mot = input("Entrez le nouveau mot (ou appuyez sur Entrée pour conserver le mot actuel) : ").strip()
        nouvelle_definition = input("Entrez la nouvelle définition (ou appuyez sur Entrée pour conserver la définition actuelle) : ").strip()
        
        if nouveau_mot:
            dictionnaire[nouveau_mot] = dictionnaire.pop(mot)
        if nouvelle_definition:
            dictionnaire[nouveau_mot or mot] = nouvelle_definition
        
        print(f"Le mot '{mot}' a été modifié avec succès.")
    else:
        print("Erreur : le mot n'existe pas dans le dictionnaire.")
    return dictionnaire

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
        elif choix == '5':
            dictionnaire = modify_word(dictionnaire)
        elif choix == '0':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()