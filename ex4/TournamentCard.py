from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ):
        super().__init__(name, cost, rarity)

        self.card_id = card_id
        self.attack_power = attack
        self.health = health

        # ランキング用
        self.wins = 0
        self.losses = 0
        self.base_rating = 1200

    # ===== Card =====
    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "effect": "Tournament card enters the match"
        }

    # ===== Combatable =====
    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> Dict:
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    # ===== Rankable =====
    def calculate_rating(self) -> int:
        return self.base_rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> Dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }

    def get_tournament_stats(self) -> Dict:
        return self.get_rank_info()
