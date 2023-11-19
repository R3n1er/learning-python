import random


def main():
    player_health = 50
    enemy_health = 50
    player_potions = 3

    while player_health > 0 and enemy_health > 0:
        print(
            f"Your health: {player_health} ❤️, Enemy health: {enemy_health} ❤️, Potions: {player_potions} 🧪")

        choice = input("Do you want to attack (1) or use a potion (2)? ")

        if choice == "1":
            # Player attacks
            attack_damage = random.randint(5, 10)
            enemy_health -= attack_damage
            print(
                f"You attacked the enemy and dealt {attack_damage} damage! ⚔️")

        elif choice == "2":
            # Player uses a potion
            if player_potions > 0:
                potion_health = random.randint(15, 50)
                player_health += potion_health
                player_potions -= 1
                print(
                    f"You used a potion and restored {potion_health} health! 🌟")
            else:
                print("You don't have any potions left! 😟")

        # Enemy attacks
        enemy_attack_damage = random.randint(5, 15)
        player_health -= enemy_attack_damage
        print(
            f"The enemy attacked you and dealt {enemy_attack_damage} damage! 💔")

    # Game result
    if player_health <= 0:
        print("Game over. You lost! 😢")
    else:
        print("Congratulations! You defeated the enemy! 🎉")


if __name__ == "__main__":
    main()
