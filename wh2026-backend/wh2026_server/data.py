import random
from uuid import UUID

from attrs import define, field


def generate_game_code() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(4))


ADJECTIVES = [
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Purple",
    "White",
    "Black",
]

NOUNS = ["Dog", "Cat", "Bird", "Lizard", "Fox", "Rat"]


def random_name() -> str:
    return random.choice(ADJECTIVES) + random.choice(NOUNS)


def validate_name(name: str) -> bool:
    if len(name) < 1 or len(name) > 20:
        return False
    return True


@define
class ConnectionData:
    id: UUID = field()
    game_code: str | None = field(default=None)


@define
class Game:
    code: str = field()
    players: dict[UUID, Player] = field(factory=dict)
    question_number: int = field(default=0)
    current_question: str = field(default="1+1")


@define
class Player:
    id: UUID = field()
    is_host: bool = field(default=False)
    name: str = field(factory=random_name)
    points: int = field(default=0)
