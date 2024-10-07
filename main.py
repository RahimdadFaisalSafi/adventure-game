from ast import main
from game_utils import  solve_riddle, end_game
PUZZLES = ['Ich habe eine Seite, aber keinen Rand. Ich kann sprechen, \
    aber keinen Mund. Ich kann fliegen, aber habe keine Flügel. Ich\
        kann gefallen, aber bin kein Regen.', ]

# Begrüßungsfunktion
def greeting():
    print("Willkommen zum Abenteuer 'Die verlorene Schatzsuche'!")
    print("Du wirst durch verschiedene Räume navigieren und Rätsel lösen müssen, um den Schatz zu finden.")
    print("Gib die Himmelsrichtungen ('norden', 'süden', 'osten', 'westen') ein, um dich zu bewegen.")
    print("Viel Erfolg!\n")

def enter_room(room):
    if room == 'norden':
        return solve_riddle(PUZZLES[0])
    elif room == 'süden':
        pass
    elif room == 'osten':
        pass
    elif room == 'westen':
        pass
    else:
        pass
    
def main():
    greeting()
    current_room = "start"
    
    while current_room != 'ende':
        direction = input("\nWohin möchtest du gehen? (norden/süden/osten/westen): ").lower()
        if direction == "norden":
            current_room = "norden"
            result = enter_room("norden")
            if isinstance(result, str):
                print(result)
            
        
if __name__ == '__main__':
    main()
    
    