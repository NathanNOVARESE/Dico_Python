import os
import re
import matplotlib.pyplot as plt

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

def modify_word(filename):
    word = input("Entrez le mot à modifier : ").strip()
    dictionary = load_dictionary(filename)
    
    if word in dictionary:
        new_word = input("Entrez le nouveau mot (ou appuyez sur Entrée pour conserver le mot actuel) : ").strip()
        new_definition = input("Entrez la nouvelle définition (ou appuyez sur Entrée pour conserver la définition actuelle) : ").strip()
        
        if new_word:
            dictionary[new_word] = dictionary.pop(word)
        if new_definition:
            dictionary[new_word or word] = new_definition
        
        save_dictionary(dictionary, filename)
        print(f"Le mot '{word}' a été modifié avec succès.")
    else:
        print("Erreur : le mot n'existe pas dans le dictionnaire.")

def graphic(filename):
    dictionary = load_dictionary(filename)
    if dictionary:
        words = list(dictionary.keys())
        lengths = [len(definition.split()) for definition in dictionary.values()]

        plt.figure(figsize=(10, 50))
        plt.bar(words, lengths, color='skyblue')
        plt.xlabel('Mots', fontsize=12)
        plt.ylabel('Nombre de mots dans la définition', fontsize=12)
        plt.title('Dictionnaire', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(range(0, max(lengths) + 1))
        plt.tight_layout()
        plt.show()
    else:
        print("Le dictionnaire est vide.")

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
        print("\n" + "="*80)
        print(" " * 10 + "Gestion d'un dictionnaire fichier")
        print("="*40)
        print(f"Le dictionnaire comporte pour le moment {len(load_dictionary(filename))} mot(s).")
        print("-" * 40)
        print("1. Ajout d'un mot")
        print("2. Suppression d'un mot")
        print("3. Recherche d'un mot")
        print("4. Affichage de tout le dictionnaire")
        print("5. Modification d'un mot")
        print("6. Graphique")
        print("0. Fin du programme")
        print("="*40)
        choice = input("\nVotre choix : ").strip()

        if choice == '1':
            add_word(filename)
        elif choice == '2':
            remove_word(filename)
        elif choice == '3':
            search_word(filename)
        elif choice == '4':
            display_dictionary(filename)
        elif choice == '5':
            modify_word(filename)
        elif choice == '6':
            graphic(filename)
        elif choice == '0':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()