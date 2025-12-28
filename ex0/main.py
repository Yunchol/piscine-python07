from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print()

    available_mana = 6
    print(f"Playing Fire Dragon with {available_mana} mana available:")
    print("Playable:", fire_dragon.is_playable(available_mana))

    if fire_dragon.is_playable(available_mana):
        result = fire_dragon.play({})
        print("Play result:", result)

    print()
    print("Fire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target("Goblin Warrior")
    print("Attack result:", attack_result)

    print()
    low_mana = 3
    print(f"Testing insufficient mana ({low_mana} available):")
    print("Playable:", fire_dragon.is_playable(low_mana))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
