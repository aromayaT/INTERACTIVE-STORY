import json

def ouvre_scenario(fichier):
    # Ouvre le fichier en mode lecture
    with open(fichier, 'r', encoding='utf-8') as fichier:
        # Charge le contenu JSON dans un dictionnaire
        dictionnaire = json.load(fichier)
    return dictionnaire

scenario = ouvre_scenario("scenario.json")
salle = "Votre chambre"
mum = True
dad = True

etat_Dad = 0
Dad = {0 : ([1], "Enfin reveillé ? J'ai préparé à manger. Va t'asseoir devant la télé, je t'amène le tout."),
       1 : ([2], '____'),
       2 : ([3], '_____'),
       3 : ([4], '_____'),
       4 : ([4], '_____')
       }

etat_Mum = 0
Mum = {0 : ([1], "Coucou, chéri. Bien dormi ? Va rejoindre ton père dans la cuisine."),
       1 : ([2], "Mon fils.. va te préparer ou tu risques d'être en retard.."),
       2 : ([3], "_____"),
       3 : ([4], "_____"),
       4 : ([2], "_____")
       }





while True:
    
    print(scenario[salle]["description"])
    if "action" in scenario[salle].keys():
        for commande in scenario[salle]["action"]:
            exec(commande)
        
    for numero, destination in scenario[salle]["choix"].items():
        print(f"{numero}: {destination}")
        
    choix =input("Où aller ? : ")
    salle = scenario[salle]["choix"][choix]
    
    
    