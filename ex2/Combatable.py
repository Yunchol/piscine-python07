from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: str) -> Dict:
        """
        対象を攻撃する
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """
        攻撃を受けて防御する
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """
        戦闘能力の情報を返す
        """
        pass
