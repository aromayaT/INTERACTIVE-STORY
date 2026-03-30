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

while True:
    
    print(scenario[salle]["description"])
    if "action" in scenario[salle].keys():
        for commande in scenario[salle]["action"]:
            exec(commande)
        
    for numero, destination in scenario[salle]["choix"].items():
        print(f"{numero}: {destination}")
        
    choix =input("Où aller ? : ")
    salle = scenario[salle]["choix"][choix]
    
    
    