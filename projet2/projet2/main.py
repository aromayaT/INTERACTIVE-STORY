import json
import random
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from colorama import Fore, Style, init

init()

ITALIC = '\x1B[3m'

def ouvre_scenario(fichier):
    # Ouvre le fichier en mode lecture
    with open(fichier, 'r', encoding='utf-8') as fichier:
        # Charge le contenu JSON dans un dictionnaire
        dictionnaire = json.load(fichier)
    return dictionnaire

scenario = ouvre_scenario("scenario.json")
salle = "Votre chambre"
mode = "chambre"
root = tk.Tk()
root.withdraw()

def intro():
    print("Vous ouvrez les yeux dans une chambre inconnue.")
    print("L'air est lourd, comme si elle n'avait pas été ouverte depuis longtemps.")
    print("À votre réveil, vous êtes immédiatement attiré par la porte qui se trouve en face de vous.") 
    print("Vous tentez de sortir mais la chambre est fermée à clé.")
    print("Vous voyez des meubles autour de vous..\n")

def post_porte():
    print("Vous êtes désormais dans le couloir du 2ème étage.")
    print("L'entièreté de cette maison est silencieuse.")
    print("Le bois grince légèrement et un léger courant d'air vient caresser votre cou.")
    print("\n...\n")
    print("À présent, que faire ?\n")
    
def chambre(etat):
    objets = {
        "0": "bureau",
        "1": "tiroir",
        "2": "armoire",
        "3": "lit",
        "4": "ordinateur"
        }
    
    message_vide = ["Rien d'intéressant ici.\n",
                    "Juste de la poussière.\n",
                    "Vide...\n",
                    "Vous ne trouvez rien.\n",
                    "Ce meuble semble ne pas avoir été ouvert depuis longtemps.\n",
                    "Une légère odeur de renfermé s’en échappe.\n",
                    "Il n’y a rien d’utile ici.\n",
                    "Seulement quelques objets sans importance.\n",
                    "Le meuble grince légèrement.\n",
                    "Vous fouillez sans succès.\n",
                    "Quelqu’un a peut-être déjà cherché ici.\n",
                    "Le silence devient presque oppressant.\n",
                    "Rien... encore.\n",
                    "Vous avez l’impression de perdre votre temps.\n",
                    "Tout semble étrangement vide.\n",
                    "Vous ne découvrez rien de particulier.\n",
                    "Une couche de poussière recouvre l’intérieur.\n",
                    "Le meuble est complètement vide.\n",
                    "Vous espériez trouver quelque chose.\n",
                    "Toujours rien.\n"
                    ]
    
    for key, obj in objets.items():
        print(f"{key} : {obj}")
        
    choix = input("\nOù voulez-vous chercher ? : ")
            
    if choix in objets:
        print("\nVous inspectez un " + objets[choix] + ".")
        
        if objets[choix] == etat["cle_objet"]:
            if not etat["ordi"]:
                print("Vous ressentez une présence étrange...")
            else:    
                print("Vous avez trouvé une clé.")
                etat["porte_ouverte"] = True
        elif objets[choix] == "ordinateur":
            if not etat["ordi"]:
                print("Étrangement, vous avez l'impression que cet ordinateur se détache des autres éléments de cette maison.")
                print("Sa présence vous laisse inconfortable, mais vous n'arrivez pas à détourner le regard.")
                print("Plus vous le fixez, et plus vous avez l'impression qu'il vous regarde en retour.")
                etat["ordi"] = True    
            else:
                print("L'écran reste noir... mais vous n'êtes pas rassuré...")
    
    
        else:
            print(random.choice(message_vide))
                
    else:
        print("Vous restez immobile...")
        
    return etat

def inventory(etat):
    print("\n=== INVENTAIRE ===")
    
    if len(etat["inventaire"]) == 0:
        print("Un peu vide...")
    else:
        for obj in etat["inventaire"]:
            print("- " + obj)
    print("==================\n")
    
def inspecter(salle):
    choix = input("Voulez-vous inspecter cette salle ? (oui/non): ")
    if choix.lower() not in ["oui", "o"]:
        return None
    
    print(choix)
                  
    if salle == "Votre chambre":
        print("Vous entrez lentement dans votre chambre. L’air y est étonnamment glacé, bien plus que dans le reste de la maison. La pièce est plongée dans une obscurité presque totale, seulement traversée par une faible lumière provenant d’une horloge numérique figée sur 19:47. Les meubles vous semblent familiers… mais quelque chose paraît profondément anormal.")
                  
    if salle == "Salle de bain des parents":
        print("Vous poussez la porte de la salle de bain. Une légère odeur d’humidité flotte dans l’air et le miroir couvert de traces ternes déforme vaguement votre reflet. Au-dessus du lavabo, une petite horloge murale arrêtée sur 19:47 émet un faible grésillement avant de retomber dans le silence.")
                  
    if salle == "Salle de bain":
        print("La salle de bain des parents paraît étrangement propre, presque inutilisée. Les carreaux froids réfléchissent la faible lumière de la pièce et rendent l’atmosphère encore plus vide. Près de la baignoire, une horloge blanche semble bloquée sur 19:47, comme si le temps lui-même avait cessé d’avancer ici.")

event_ordi = ["Vous restez intrigué par la présence de l'ordinateur.",
              "Vous repensez à l'ordinateur sans raison particulière.",
              "L'image de l'écran noir vous revient en tête.",
              "Vous vous demandez si l'ordinateur était vraiment allumé.",
              "Vous essayez d'oublier cet ordinateur, sans y parvenir.",
              "L'ordinateur vous intrigue encore, même loin de la pièce."
]

ambiance = ["Le silence est si profond qu’il en devient presque gênant.\n",
    "Chaque pas résonne légèrement sur le sol en bois.\n",
    "L’air est immobile, comme figé depuis longtemps.\n",
    "Rien ne bouge… mais tout semble attendre.\n",
    "La maison paraît habitée, mais étrangement vide.\n",
    "Un calme étrange enveloppe les lieux.\n",
    "Vous avez l’impression d’être observé, sans raison précise.\n",
    "Quelque chose cloche, sans que vous puissiez dire quoi.\n",
    "L’atmosphère semble plus lourde qu’elle ne devrait l’être.\n",
    "Un détail vous échappe, mais vous dérange déjà.\n",
    "La lumière paraît légèrement trop froide.\n",
    "Le silence n’est pas naturel.\n",
    "Vous avez du mal à vous détendre ici.\n",
    "La pièce semble normale… mais votre instinct dit l’inverse.\n",
    "Silence.\n",
    "Trop calme.\n",
    "Quelque chose ne va pas.\n",
    "Rien ne bouge.\n",
    "Une sensation étrange.\n",
    "Le temps semble arrêté.\n",
    "Vous continuez d’avancer.\n",
    "Rien à signaler… en apparence.\n"
]

evenements_rares = [
    "Vous entendez un léger craquement derrière vous.\n",
    "Un bruit sourd semble provenir du rez-de-chaussée.\n",
    "Quelque chose vient de tomber au loin.\n",
    "Le parquet grince alors que vous êtes immobile.\n",
    "Un frisson vous parcourt soudainement.\n",
    "Vous avez la désagréable impression d’être suivi.\n",
    "Pendant une seconde, vous retenez votre respiration.\n",
    "Une sensation étrange vous envahit rapidement.\n",
    "Vous êtes persuadé que cette porte était fermée auparavant.\n",
    "La température semble avoir chuté brutalement.\n",
    "Vous avez l’impression que quelque chose a changé dans la pièce.\n",
    "Le silence devient presque assourdissant.\n",
    "Vous croyez apercevoir un mouvement du coin de l’œil.\n",
    "Un courant d’air glacé traverse soudainement le couloir.\n",
    "Pendant un instant, vous avez cru entendre une respiration.\n",
    "Quelque chose semble vous observer dans le silence.\n",
    "Le bois craque lentement au-dessus de vous.\n",
    "Vous restez immobile quelques secondes.\n",
    "Une étrange sensation de malaise vous envahit.\n",
    "Tout semble normal... et pourtant.\n"
]


objets = ["bureau", "tiroir", "armoire", "lit", "ordinateur"]

etat = {
    "cle_objet": random.choice(objets),
    "porte_ouverte": False,
    "ordi": False,
    "post_affiche": False,
    "ordinateur_affiche": False,
    "rdc": False,
    "inventaire": []
    }

intro()   
    
while True:
    
    if mode == "chambre":
        etat = chambre(etat)
        
        if etat["porte_ouverte"]:
            print("\nMaintenant que la clé est en votre possession, vous pouvez désormais dévérouiller la porte.\n")
            mode = "maison"
            salle = "Couloir"
    
    elif mode == "maison":
        
        if not etat["post_affiche"]:
            post_porte()
            etat["post_affiche"] = True
        
        print("\n" + scenario[salle]["description"])
        
        if not salle == "Couloir":
            inspecter(salle)
        
        if random.random() < 0.3:
            print(random.choice(ambiance))
        if random.random() < 0.05:        
            print(random.choice(evenements_rares))

        if salle == "Chambre des parents":
            print("\nQuelque chose brille au fond de la salle.")
            print("Vous vous en approchez et comprenez alors que la seule source de lumière émanant de celle-ci est un ordinateur.")
            print("Il semblerait que quelqu'un l'ait utilisé récemment, mais sans succès...")
        
        if random.random() < 0.15 and salle != "Chambre des parents":
            texte = random.choice(event_ordi)

            print(
                Fore.LIGHTRED_EX +
                Style.DIM +
                ITALIC +
                texte +
                Style.RESET_ALL
            )
        
        for numero, destination in scenario[salle]["choix"].items():
            print(f"{numero}: {destination}")
        
        choix = input("Où aller ? : (I pour ouvrir l'inventaire) : ")
        if choix.lower() == "i":
            inventory(etat)
        else:
            if choix in scenario[salle]["choix"]:
                destination = scenario[salle]["choix"][choix]
                
                if salle == "Couloir" and destination == "Escalier" and not etat["rdc"]:
                    print("\nVous vous approchez lentement des escaliers.")
                    print("Il semblerait que l'accès au rez-de-chaussée est bloqué.")
                    print("La porte faisant office d'obstacle présente un digicode composé de 4 chiffres...")
                    
                else:
                    salle = destination
            else:
                print("\nVous tentez soudainement de passer à travers le mur, mais sans issue...\n")
            
            
            
            