PUZZLES = ['Ich habe eine Seite, aber keinen Rand. Ich kann sprechen, \
    aber keinen Mund. Ich kann fliegen, aber habe keine Flügel. Ich\
        kann gefallen, aber bin kein Regen.', ]
def solve_riddle(riddle):
    print(f"Rätsel: {riddle}")
    answer = input("Deine Antwort: ").lower()
    if riddle == PUZZLES[0] and answer == "buch":
        return "Richtig! Du kannst weitergehen."
    else:
        return False

def end_game():
    exit()