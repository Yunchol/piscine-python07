from typing import Dict, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: List = []
        self.battlefield: List = []
        self.turns_simulated = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

        # 初期カード生成
        self.hand.append(self.factory.create_creature(None))
        self.hand.append(self.factory.create_spell(None))
        self.hand.append(self.factory.create_artifact(None))

    def simulate_turn(self) -> Dict:
        if not self.factory or not self.strategy:
            raise RuntimeError("Engine is not configured")

        self.turns_simulated += 1
        result = self.strategy.execute_turn(self.hand, self.battlefield)

        return result

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
        }
