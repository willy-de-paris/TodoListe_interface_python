import string
import tkinter as tk
import json

# Constantes
FICHIER_TODOLISTE = "todolist.json"

# Classe Todo
class Todo:
    def __init__(self, titre, faite):
        self.titre = titre
        self.faite = faite

# Méthode pour charger la todoliste depuis le fichier
def charger_todoliste():
    with open(FICHIER_TODOLISTE, "r") as f:
        todoliste = json.load(f)
    return todoliste

# Méthode pour sauvegarder la todoliste dans le fichier
def sauvegarder_todoliste(todoliste):
    with open(FICHIER_TODOLISTE, "w") as f:
        json.dump(todoliste, f)

# Fonction pour créer la première interface
def menu():
    # Créer une fenêtre principale
    fenetre = tk.Tk()
    fenetre.geometry("300x400")
    fenetre.title("Todo List")

     # Afficher un message
    label = tk.Label(fenetre, text="MENU TODO LISTE")

    # Placer le message
    label.pack()
    # Créer un bouton
    bouton1 = tk.Button(fenetre, text="Ajouter",bg='red', command=ajouter)
    bouton2 = tk.Button(fenetre, text="Suprimer",bg='blue', command=supprimer)
    bouton3 = tk.Button(fenetre, text="Consulter",bg='red', command=consulter)
    bouton4 = tk.Button(fenetre, text="Modifier",bg='blue', command=modifier)
    bouton5 = tk.Button(fenetre, text="Rechercher",bg='red', command=rechercher)
    bouton6 = tk.Button(fenetre, text="Filtrer",bg='blue', command=filtrer)
    bouton1.config(borderwidth=5)
    bouton1.config(width=12, height=1)
    bouton1.relief = tk.RIDGE
    bouton2.config(borderwidth=5)
    bouton2.config(width=12, height=1)
    bouton2.relief = tk.RIDGE
    bouton3.config(borderwidth=5)
    bouton3.config(width=12, height=1)
    bouton3.relief = tk.RIDGE
    bouton4.config(borderwidth=5)
    bouton4.config(width=12, height=1)
    bouton4.relief = tk.RIDGE
    bouton5.config(borderwidth=5)
    bouton5.config(width=12, height=1)
    bouton5.relief = tk.RIDGE
    bouton6.config(borderwidth=5)
    bouton6.config(width=12, height=1)
    bouton6.relief = tk.RIDGE


    # Placer le bouton
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()
    bouton4.pack()
    bouton5.pack()
    bouton6.pack()

    # Afficher la fenêtre
    fenetre.mainloop()

# Fonction pour créer la deuxième interface
def ajouter():
    # Créer une fenêtre principale
    fenetre = tk.Tk()

    # Afficher un message
    fenetre.title("Ajouter une tâche")

    # Placer le message
    label = tk.Label(fenetre, text="Nom de tache")
    label.pack()
    # entrée
    value = tk.StringVar() 
    task = tk.Entry(fenetre, textvariable=string, width=30)
    task.pack()
    value = tk.StringVar() 
    bouton1 = tk.Radiobutton(fenetre, text="Oui", variable=value, value=1)
    bouton2 = tk.Radiobutton(fenetre, text="Non", variable=value, value=2)
    bouton1.pack()
    bouton2.pack()
    # Afficher la fenêtre
    fenetre.mainloop()

def supprimer():
    # Créer une fenêtre principale
    fenetre = tk.Tk()

    # Afficher un message
    fenetre.title("Supprimer une tâche")

    # Placer le message
    

    # Afficher la fenêtre
    fenetre.mainloop()

def consulter():
    # Créer une fenêtre principale
    fenetre = tk.Tk()

    # Afficher un message
    fenetre.title("Consulter une tâche")

    # Placer le message
    

    # Afficher la fenêtre
    fenetre.mainloop()

def modifier():
    # Créer une fenêtre principale
    fenetre = tk.Tk()

    # Afficher un message
    label = tk.Label(fenetre, text="Modifier")

    # Placer le message
    label.pack()

    # Afficher la fenêtre
    fenetre.mainloop()

def rechercher():
    # Créer une fenêtre principale
    fenetre = tk.Tk()

    # Afficher un message
    label = tk.Label(fenetre, text="Rechercher")

    # Placer le message
   

    # Afficher la fenêtre
    fenetre.mainloop()
    
def filtrer():
    # Créer une fenêtre principale
    fenetre = tk.Tk()

    # Afficher un message
    label = tk.Label(fenetre, text="Filtrer")

    # Placer le message
    

    # Afficher la fenêtre
    fenetre.mainloop()
    
# Appeler la fonction pour créer la première interface
menu()
