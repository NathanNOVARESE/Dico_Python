import os

def load_dictionary(filename):
    dictionary = {}
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                word, definition = line.strip().split(':')
                dictionary[word] = definition
    return dictionary

def add_word(filename):
    word = input("Entrez le mot à ajouter : ").strip()
    dictionary = load_dictionary(filename)
    if word in dictionary:
        print("Erreur : le mot existe déjà dans le dictionnaire.")
    else:
        definition = input("Entrez la définition du mot : ").strip()
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{word}:{definition}\n")
        print(f"Le mot '{word}' a été ajouté avec succès.")

def remove_word(filename):
    word = input("Entrez le mot à supprimer : ").strip()
    dictionary = load_dictionary(filename)
    if word in dictionary:
        del dictionary[word]
        save_dictionary(dictionary, filename)
        print(f"Le mot '{word}' a été supprimé avec succès.")
    else:
        print("Erreur : le mot n'existe pas dans le dictionnaire.")

def search_word(filename):
    word = input("Entrez le mot à rechercher : ").strip()
    dictionary = load_dictionary(filename)
    if word in dictionary:
        print(f"{word} : {dictionary[word]}")
    else:
        print("Erreur : le mot n'existe pas dans le dictionnaire.")

def display_dictionary(filename):
    dictionary = load_dictionary(filename)
    if dictionary:
        for word, definition in sorted(dictionary.items()):
            print(f"{word} : {definition}")
    else:
        print("Le dictionnaire est vide.")

def save_dictionary(dictionary, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for word, definition in sorted(dictionary.items()):
            file.write(f"{word}:{definition}\n")

def main():
    filename = 'dico.txt'

    while True:
        print("\nGestion d'un dictionnaire")
        print("Ajout d'un mot __________________________________1")
        print("Suppression d'un mot ____________________________2")
        print("Recherche d'un mot ______________________________3")
        print("Affichage de tout le dictionnaire _______________4")
        print("Fin du programme ________________________________0")
        choice = input("\nVotre choix : ").strip()

        if choice == '1':
            add_word(filename)
        elif choice == '2':
            remove_word(filename)
        elif choice == '3':
            search_word(filename)
        elif choice == '4':
            display_dictionary(filename)
        elif choice == '0':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()