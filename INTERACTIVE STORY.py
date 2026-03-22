scenario = {
    "Foyer": {
        "description": "Vous êtes dans le foyer.",
        "choix": {0 : "Escalier",
                  1 : "Salon",
                  2 : "Salle à manger",
                  3 : "Cuisine",
                  4 : "Toilettes",
                  5 : "Extérieur"}
    },
    "Salon": {
        "description": "Vous êtes dans le salon.",
        "choix": {0 : "Foyer",
                  1 : "Salle à manger",
                  2 : "Cuisine"}
    },
    "Cuisine": {
        "description": "Vous êtes dans la cuisine.",
        "choix": {0 : "Foyer",
                  1 : "Salon"}
    },
    "Salle à manger": {
        "description": "Vous êtes dans la salle à manger.",
        "choix": {0 : "Foyer",
                  1 : "Salon"}
    },
    "Toilettes": {
        "description": "Vous êtes dans les toilettes.",
        "choix": {0 : "Foyer"}
    },
    "Escalier": {
        "description": "Vous êtes en face des escaliers. Monter au premier étage ?",
        "choix": {0 : "Foyer",
                  1 : "1er étage"}
    }
}

salle = "Foyer"
while True:
    print(scenario[salle]["description"])
    for numero, destination in scenario[salle]["choix"].items():
        print(f"{numero}: {destination}")
        
    choix = int(input("Où aller ? : "))
    salle = scenario[salle]["choix"][choix]
    
    
    
    
    
    