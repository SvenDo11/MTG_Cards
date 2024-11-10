
class Card:
    """Class representing a single mtg card.
    """
    def __init__(self) -> None:
        """Construct a new MTG Card
        """
        self.uuid: str = "None"
        self.base_uuid: str = "None"
        self.name: str = "None"
        self.lang: str = ""
        self.cost = None
        self.cmc: int = 0
        self.type = None
        self.description: str = "None"
        self.power: int = 0
        self.toughness: int = 0
        self.colors = None
