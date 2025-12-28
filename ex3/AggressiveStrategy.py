from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        played = []
        mana_used = 0

        # 低コスト優先でカードを出す
        sorted_hand = sorted(hand, key=lambda c: c.cost)

        for card in sorted_hand:
            played.append(card.name)
            mana_used += card.cost

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": played,
            "mana_used": mana_used
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        # プレイヤー優先
        return sorted(available_targets, reverse=True)
