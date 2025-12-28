from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Epic",
        attack=5,
        health=10,
        mana=5
    )

    print("\nPlaying Elite Card:")
    print(elite.play({}))

    print("\nCombat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(5))

    print("\nMagic phase:")
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", elite.channel_mana(3))

    print("\nStats:")
    print("Combat stats:", elite.get_combat_stats())
    print("Magic stats:", elite.get_magic_stats())

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
