from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        """
        スペルを発動する（1回使い切り）
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Spell activated: {self.effect_type}"
        }

    def resolve_effect(self, targets: List[str]) -> Dict:
        """
        スペル効果の解決
        """
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }
