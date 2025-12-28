from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana: int
    ):
        #ここはCardのclassのsuper()
        #そうなるのは、combatableとmagicalに__init__がないから（これがあったら危険になる）
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.mana = mana

    # ===== Card =====
    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters the battlefield"
        }

    # ===== Combatable =====
    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(self.attack_power, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    # ===== Magical =====
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        mana_cost = len(targets) * 2
        self.mana -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "mana": self.mana
        }
