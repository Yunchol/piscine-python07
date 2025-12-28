from typing import Dict
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power) -> CreatureCard:
        return CreatureCard(
            name="Fire Dragon",
            cost=5,
            rarity="Legendary",
            attack=7,
            health=5
        )

    def create_spell(self, name_or_power) -> SpellCard:
        return SpellCard(
            name="Fireball",
            cost=3,
            rarity="Common",
            effect_type="damage"
        )

    def create_artifact(self, name_or_power) -> ArtifactCard:
        return ArtifactCard(
            name="Mana Ring",
            cost=2,
            rarity="Rare",
            durability=3,
            effect="+1 mana per turn"
        )

    def create_themed_deck(self, size: int) -> Dict:
        cards = []
        for _ in range(size):
            cards.append(self.create_creature(None))
            cards.append(self.create_spell(None))
        return {
            "theme": "Fantasy",
            "cards": cards
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
