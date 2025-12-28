from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        """
        現在のレーティングを計算する
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        勝利数を更新する
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        敗北数を更新する
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """
        ランキング情報を返す
        """
        pass
