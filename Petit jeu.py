import os

import random


def main():
    print("Bienvenue!")
    print("Il y a trois héros!")
    print("Vous pouvez choisir entre : Victor, Bob, Mickael!")
    hero = input("Choisissez un des héros! : ")
    hero_user = hero
    if hero_user != "Victor" and hero_user != "Bob" and hero_user != "Mickael":
        print("Erreur, veuillez verifier l'ortographe!")
        os.system("PAUSE")
        exit()
    print("Vous avez choisi " + hero_user + "!")
    if hero_user == "Victor":
        health_v = 35
        attack_v = 4
        print("Vous avez " + str(health_v) + " points de vie!")
        print("Vous infligez " + str(attack_v) + " points de dégat!")
    if hero_user == "Bob":
        health_b = 30
        attack_b = 5
        print("Vous avez " + str(health_b) + " points de vie!")
        print("Vous infligez " + str(attack_b) + " points de dégat!")
    if hero_user == "Mickael":
        health_m = 40
        attack_m = 3
        print("Vous avez " + str(health_m) + " points de vie!")
        print("Vous infligez " + str(attack_m) + " points de dégat!")
    print("Devant vous se trouve le donjon des ténèbres!")
    ch = input("Souhaitez vous entrez dans le donjon des ténèbres ou alors avant d'entrer dans le donjon, cherchez des objets qui pourait vous etre utile pour le donjon? [entrer / chercher] : ")
    if ch == "entrer":
        print("Un monstre se trouve devant vous!")
        health_ms = 20
        attack_ms = 5
        print("Il a " + str(health_ms) + " points de vie!")
        print("Il peut infliger " + str(attack_ms) + " points de dégat!")
        print("Il vous inflige " + str(attack_ms) + " points de dégat!")
        if hero_user == "Victor":
            while health_v > 0 and health_ms > 0:
                health_v -= attack_ms
                if health_v <= 0:
                    print("Vous êtes mort!")
                    os.system("PAUSE")
                    exit()
                print("Vous avez maintenant " + str(health_v) + " points de vie!")
                print("Vous lui infligez " + str(attack_v) + " points de dégat!")
                health_ms -= attack_v
                if health_ms <= 0:
                    print("Vous l'avez tué!")
                    os.system("PAUSE")
                else:
                    print("Il lui reste " + str(health_ms) + " points de vie!")
                    os.system("PAUSE")
        if hero_user == "Bob":
            while health_b > 0 and health_ms > 0:
                health_b -= attack_ms
                if health_b <= 0:
                    print("Vous êtes mort!")
                    os.system("PAUSE")
                    exit()
                print("Vous avez maintenant " + str(health_b) + " points de vie!")
                print("Vous lui infligez " + str(attack_b) + " points de dégat!")
                health_ms -= attack_b
                if health_ms <= 0:
                    print("Vous l'avez tué!")
                    os.system("PAUSE")
                else:
                    print("Il lui reste " + str(health_ms) + " points de vie!")
                    os.system("PAUSE")
        if hero_user == "Mickael":
            while health_m > 0 and health_ms > 0:
                health_m -= attack_ms
                if health_m <= 0:
                    print("Vous êtes mort!")
                    os.system("PAUSE")
                    exit()
                print("Vous avez maintenant " + str(health_m) + " points de vie!")
                print("Vous lui infligez " + str(attack_m) + " points de dégat!")
                health_ms -= attack_m
                if health_ms <= 0:
                    print("Vous l'avez tué!")
                    os.system("PAUSE")
                else:
                    print("Il lui reste " + str(health_ms) + " points de vie!")
                    os.system("PAUSE")
    if ch == "chercher":
        print("Vous chercher des objets qui pourait vous ameliorer!")
        print("Vous avez trouver un objet!")
        objects = ["un casque", "une épée"]
        user_object = random.choice(objects)
        print("Vous avez trouvé " + user_object + "!")
        if hero_user == "Victor":
            if user_object == "un casque":
                health_v += 5
                health_points = 5
                print("Vous avez gagner " + str(health_points) + " points de vie en plus!")
                print("Vous avez maintenant " + str(health_v) + " points de vie!")
            if user_object == "une épée":
                attack_v += 3
                attack_points = 3
                print("Vous infligez maintenant " + str(attack_points) + " points de dégat en plus!")
                print("Vous inligez maintenant " + str(attack_v) + " points de dégat!")
        if hero_user == "Bob":
            if user_object == "un casque":
                health_b += 5
                health_points = 5
                print("Vous avez gagner " + str(health_points) + " points de vie en plus!")
                print("Vous avez maintenant " + str(health_b) + " points de vie!")
            if user_object == "une épée":
                attack_b += 3
                attack_points = 3
                print("Vous infligez maintenant " + str(attack_points) + " points de dégat en plus!")
                print("Vous inligez maintenant " + str(attack_b) + " points de dégat!")
        if hero_user == "Mickael":
            if user_object == "un casque":
                health_m += 5
                health_points = 5
                print("Vous avez gagner " + str(health_points) + " points de vie en plus!")
                print("Vous avez maintenant " + str(health_m) + " points de vie!")
            if user_object == "une épée":
                attack_m += 3
                attack_points = 3
                print("Vous infligez maintenant " + str(attack_points) + " points de dégat en plus!")
                print("Vous inligez maintenant " + str(attack_m) + " points de dégat!")
        print("Maintenant que vous avez trouvez un objet, vous allez entrez dans le donjon des ténèbres!")
        os.system("PAUSE")
        print("Un monstre se trouve devant vous!")
        health_ms = 20
        attack_ms = 5
        print("Il a " + str(health_ms) + " points de vie!")
        print("Il peut infliger " + str(attack_ms) + " points de dégat!")
        print("Il vous inflige " + str(attack_ms) + " points de dégat!")
        if hero_user == "Victor":
            while health_v > 0 and health_ms > 0:
                health_v -= attack_ms
                if health_v <= 0:
                    print("Vous êtes mort!")
                    os.system("PAUSE")
                    exit()
                print("Vous avez maintenant " + str(health_v) + " points de vie!")
                print("Vous lui infligez " + str(attack_v) + " points de dégat!")
                health_ms -= attack_v
                if health_ms <= 0:
                    print("Vous l'avez tué!")
                    os.system("PAUSE")
                else:
                    print("Il lui reste " + str(health_ms) + " points de vie!")
                    os.system("PAUSE")
        if hero_user == "Bob":
            while health_b > 0 and health_ms > 0:
                health_b -= attack_ms
                if health_b <= 0:
                    print("Vous êtes mort!")
                    os.system("PAUSE")
                    exit()
                print("Vous avez maintenant " + str(health_b) + " points de vie!")
                print("Vous lui infligez " + str(attack_b) + " points de dégat!")
                health_ms -= attack_b
                if health_ms <= 0:
                    print("Vous l'avez tué!")
                    os.system("PAUSE")
                else:
                    print("Il lui reste " + str(health_ms) + " points de vie!")
                    os.system("PAUSE")
        if hero_user == "Mickael":
            while health_m > 0 and health_ms > 0:
                health_m -= attack_ms
                if health_m <= 0:
                    print("Vous êtes mort!")
                    os.system("PAUSE")
                    exit()
                print("Vous avez maintenant " + str(health_m) + " points de vie!")
                print("Vous lui infligez " + str(attack_m) + " points de dégat!")
                health_ms -= attack_m
                if health_ms <= 0:
                    print("Vous l'avez tué!")
                    os.system("PAUSE")
                else:
                    print("Il lui reste " + str(health_ms) + " points de vie!")
                    os.system("PAUSE")
    print("Vous avez trouver un objet!")
    objects_2 = ["un plastron", "une hache"]
    user_object_2 = random.choice(objects_2)
    print("Vous avez trouvé " + user_object_2 + "!")
    if hero_user == "Victor":
        if user_object_2 == "un plastron":
            health_v += 20
            health_points = 20
            print("Vous avez gagner " + str(health_points) + " points de vie en plus!")
            print("Vous avez maintenant " + str(health_v) + " points de vie!")
        if user_object_2 == "une hache":
            attack_v += 10
            attack_points = 10
            print("Vous infligez maintenant " + str(attack_points) + " points de dégat en plus!")
            print("Vous inligez maintenant " + str(attack_v) + " points de dégat!")
    if hero_user == "Bob":
        if user_object_2 == "un plastron":
            health_b += 20
            health_points = 20
            print("Vous avez gagner " + str(health_points) + " points de vie en plus!")
            print("Vous avez maintenant " + str(health_b) + " points de vie!")
        if user_object_2 == "une hache":
            attack_b += 10
            attack_points = 10
            print("Vous infligez maintenant " + str(attack_points) + " points de dégat en plus!")
            print("Vous inligez maintenant " + str(attack_b) + " points de dégat!")
    if hero_user == "Mickael":
        if user_object_2 == "un plastron":
            health_m += 20
            health_points = 20
            print("Vous avez gagner " + str(health_points) + " points de vie en plus!")
            print("Vous avez maintenant " + str(health_m) + " points de vie!")
        if user_object_2 == "une hache":
            attack_m += 10
            attack_points = 10
            print("Vous infligez maintenant " + str(attack_points) + " points de dégat en plus!")
            print("Vous inligez maintenant " + str(attack_m) + " points de dégat!")
    os.system("PAUSE")
    print("Un monstre se trouve devant vous!")
    health_ms = 20
    attack_ms = 5
    print("Il a " + str(health_ms) + " points de vie!")
    print("Il peut infliger " + str(attack_ms) + " points de dégat!")
    print("Il vous inflige " + str(attack_ms) + " points de dégat!")
    if hero_user == "Victor":
        while health_v > 0 and health_ms > 0:
            health_v -= attack_ms
            if health_v <= 0:
                print("Vous êtes mort!")
                os.system("PAUSE")
                exit()
            print("Vous avez maintenant " + str(health_v) + " points de vie!")
            print("Vous lui infligez " + str(attack_v) + " points de dégat!")
            health_ms -= attack_v
            if health_ms <= 0:
                print("Vous l'avez tué!")
                os.system("PAUSE")
            else:
                print("Il lui reste " + str(health_ms) + " points de vie!")
                os.system("PAUSE")
    if hero_user == "Bob":
        while health_b > 0 and health_ms > 0:
            health_b -= attack_ms
            if health_b <= 0:
                print("Vous êtes mort!")
                os.system("PAUSE")
                exit()
            print("Vous avez maintenant " + str(health_b) + " points de vie!")
            print("Vous lui infligez " + str(attack_b) + " points de dégat!")
            health_ms -= attack_b
            if health_ms <= 0:
                print("Vous l'avez tué!")
                os.system("PAUSE")
            else:
                print("Il lui reste " + str(health_ms) + " points de vie!")
                os.system("PAUSE")
    if hero_user == "Mickael":
        while health_m > 0 and health_ms > 0:
            health_m -= attack_ms
            if health_m <= 0:
                print("Vous êtes mort!")
                os.system("PAUSE")
                exit()
            print("Vous avez maintenant " + str(health_m) + " points de vie!")
            print("Vous lui infligez " + str(attack_m) + " points de dégat!")
            health_ms -= attack_m
            if health_ms <= 0:
                print("Vous l'avez tué!")
                os.system("PAUSE")
            else:
                print("Il lui reste " + str(health_ms) + " points de vie!")
                os.system("PAUSE")
    print("Vous avez terminé le donjon, félicitation!")
    print("Merci d'avoir joué!")
    os.system("PAUSE")


if __name__ == '__main__':
    main()
