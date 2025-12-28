from abc import ABC, abstractmethod
from typing import List, Dict


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """
        1ターンの行動を実行する
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        戦略名を返す
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        """
        攻撃対象の優先順位を決める
        """
        pass
