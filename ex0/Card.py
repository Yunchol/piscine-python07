from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """
        カードをプレイしたときの処理
        各カードで必ず実装させる
        """
        pass

    def get_card_info(self) -> Dict:
        """
        カードの基本情報を返す
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", "")
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        マナが足りているか判定
        """
        return available_mana >= self.cost
