from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=10
    )

    wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Epic",
        attack=5,
        health=8
    )

    platform.register_card(dragon)
    platform.register_card(wizard)

    print("\nCreating match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, start=1):
        print(f"{i}. {entry['name']} - Rating: {entry['rating']} ({entry['wins']}-{entry['losses']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")


if __name__ == "__main__":
    main()
