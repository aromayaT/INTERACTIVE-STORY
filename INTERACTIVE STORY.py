scenario = {
    "Foyer": {
        "description": "Vous êtes dans le foyer.",
        "choix": {0 : "Escalier",
                  1 : "Salon",
                  2 : "Salle à manger",
                  3 : "Salle des invités"}
    },
    "Salon": {
        "description": "Vous êtes dans le salon.",
        "choix": {0 : "Foyer",
                  1 : "Salle à manger"}
    },
    "Cuisine": {
        "description": "Vous êtes dans la cuisine.",
        "choix": {0 : "Foyer",
                  1 : "Salon"}
    },
    "Salle à manger": {
        "description": "Vous êtes dans la salle à manger.",
        "choix": {0 : "Foyer",
                  1 : "Salon",
                  2 : "Cuisine",
                  3 : "Toilettes"}
    },
    "Toilettes": {
        "description": "Vous êtes dans les toilettes.",
        "choix": {0 : "Salle à manger"}
    },
    "Escalier": {
        "description": "Vous êtes en face des escaliers. Monter au premier étage ?",
        "choix": {0 : "Foyer",
                  1 : "Couloir"}
    },
    "Salle des invités": {
        "description": "Vous êtes dans la salle des invités.",
        "choix": {0 : "Foyer"}
    },
    "2ème étage": {
        "description": "Vous êtes au deuxième étage. Voulez vous descendre ou accéder au couloir ?",
        "choix": {0 : "Escalier",
                  1 : "Couloir"}
    },
    "Couloir": {
        "description": "Vous êtes au premier étage.",
        "choix": {0 : "Escalier",
                  1 : "Salle de bain",
                  2 : "Chambre des parents",
                  3 : "Votre chambre"}
    },
    "Salle de bain": {
        "description": "Vous êtes dans la salle de bain.",
        "choix": {0 : "Couloir"}
    },
    "Chambre des parents": {
        "description": "Vous êtes dans la chambre des parents.",
        "choix": {0 : "Couloir",
                  1 : "Salle de bain des parents"}
    },
    "Votre chambre": {
        "description": "Vous êtes dans votre chambre. Que voulez-vous faire ?",
        "choix": {0 : "Couloir"}
    },
    "Salle de bain des parents": {
        "description": "Vous êtes dans la salle de bain des parents.",
        "choix": {0 : "Chambre des parents"}
    }
}

salle = "Votre chambre"
while True:
    print(scenario[salle]["description"])
    for numero, destination in scenario[salle]["choix"].items():
        print(f"{numero}: {destination}")
        
    choix = int(input("Où aller ? : "))
    salle = scenario[salle]["choix"][choix]
    
    
    
    
    
    
