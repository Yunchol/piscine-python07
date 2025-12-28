from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        """
        魔法を使う
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """
        マナをチャージする
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """
        魔法関連の情報を返す
        """
        pass
