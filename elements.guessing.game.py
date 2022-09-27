

import random

def main():
    """Start an Elements guessing game."""
    print("Guess the elements!")

    elements = [
        "Hydrogen",
        "Heluim",
        "Lithium",
        "Beryllium",
        "Boron",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Fluorine",
        "Neon"
         ]

    x = random.choice(elements)
    if x == "Hydrogen":
        print("gas yang tidak berbau dan tidak berwarna")
    elif x == "Helium":
        print("kepadatan terendah,kelarutan yang rendah dan tidak reaktif")
    elif x == "Lithium":
        print("unsur penghantar panas dan listrik yang baik serta reaktif")
    elif x == "Beryllium":
        print("mempunyai konduktivitas panas yang sangat baik")
    elif x == "Boron":
        print("mempunyai sifat metaloid dan berwarna hitam")
    elif x == "Carbon":
        print("satu-satunya unsur yang atom-atomnya saling dapat berikatan satu sama lain")
    elif x == "Nitrogen":
        print("cairan yang penampilannya mirip dengan air")
    elif x == "Oxygen":
        print("bahagian penting dari atmosfer")
    elif x == "Fluorine":
        print("sangat beracun dan korosif")
    elif x == "Neon":
        print("tidak berwarna,tidak mempunyai rasa,tidak berbau dan tidak beracun")
    guess = None

    while x != guess:

        guess = str(input("Cuba teka elemen yang saya fikirkan ? "))

        if x == guess:
            print("You guessed {}. TAHNIAH! jawapan kamu tepat.".format(guess))
            break
        else:
            print("You guessed {}. Jawapan kamu salah. SILA CUBA LAGI!".format(guess))

main()
        
