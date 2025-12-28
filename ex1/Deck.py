import random
from typing import List, Dict
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """
        デッキにカードを追加
        """
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        名前でカードを削除
        """
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """
        デッキをシャッフル
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        デッキの一番上を引く
        """
        if not self.cards:
            raise IndexError("Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        """
        デッキの統計情報
        """
        total = len(self.cards)
        if total == 0:
            return {
                "total_cards": 0,
                "avg_cost": 0
            }

        total_cost = sum(card.cost for card in self.cards)

        return {
            "total_cards": total,
            "avg_cost": total_cost / total
        }
