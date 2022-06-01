import random, os


while True:
    print(' Menu de départ '.center(50, '='))
    print("""
    1. Je suis prêt !
    2. Je ne suis pas prêt
    """)

    options = input('Choisis le chiffre pour chaque action')

    if options in ['1', '2']:
        print('Séléctionne')
    else:
        break

    print('Fin du prgramme')


random_number = random.randint(1,100)

def main():
    number_asker = int(input("Votre nombre juste ici : "))
    if number_asker == random_number:
        print(f"Bien joué le nombre était bien {number_asker}")
    elif number_asker < random_number:
        os.system('cls')
        print(f"Le nombre est au dessus de {number_asker}")
        main()
    elif number_asker > random_number:
        os.system('cls')
        print(f"Le nombre est aux dessous de {number_asker}")
        main()
main()