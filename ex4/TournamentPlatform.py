from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        self.matches_played += 1

        # シンプルに攻撃力で勝敗決定
        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[Dict]:
        return sorted(
            [card.get_rank_info() for card in self.cards.values()],
            key=lambda x: x["rating"],
            reverse=True
        )

    def generate_tournament_report(self) -> Dict:
        ratings = [card.calculate_rating() for card in self.cards.values()]
        avg_rating = sum(ratings) // len(ratings) if ratings else 0

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
