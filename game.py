import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

#Seleccionar nivel de dificultad
difficulty = input("Seleccione la dificultad del juego (Fácil, Media, Difícil): ").lower()

# Número máximo de intentos permitidos
max_failures= 6
failures= 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

#Mostrar palabra parcialmente adivinada segun dificultad elegida
word_displayed = ""
if difficulty == "fácil":
    for letter in secret_word:
        if letter in "aeiou":
            word_displayed += letter
        else:
            word_displayed += "_"
elif difficulty == "media":
    word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word [-1]
else: 
    word_displayed = "_" * len(secret_word)

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while failures < max_failures:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #Verificar si no se ingreso ninguna letra
    if not letter:
        print("Ingrese una letra valida.")
        continue
    
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures+= 1
        print(f"Numeros de fallos: {failures}/{max_failures}")

    # Mostrar la palabra parcialmente adivinada
    word_displayed = ""
    for letter in secret_word:
        if letter in guessed_letters:
             word_displayed += letter
        elif difficulty == "fácil" and letter in "aeiou":
            word_displayed += letter
        elif difficulty == "media" and (letter == secret_word[0] or letter == secret_word[-1]):
            word_displayed += letter
        else:
            word_displayed += "_"

    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado el numero maximo de fallos.")
    print(f"La palabra secreta era: {secret_word}")