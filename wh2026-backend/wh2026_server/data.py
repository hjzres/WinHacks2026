import datetime
import random
from uuid import UUID

from attrs import define, field

from .questions import Question, generate_questions


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
    "Brain"
]

NOUNS = ["Dog", "Cat", "Bird", "Lizard", "Fox", "Rat", "Storm", "Needle"]


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
class Player:
    id: UUID = field()
    is_host: bool = field(default=False)
    name: str = field(factory=random_name)
    question_number: int = field(default=0)
    question_overrides: dict[int, str] = field(factory=dict)

    def get_display_data(self) -> dict:
        return {"name": self.name, "is_host": self.is_host, "id": self.id}


@define
class Game:
    code: str = field()
    time_created: datetime.datetime = field(factory=datetime.datetime.now)
    time_started: datetime.datetime | None = field(default=None)
    started: bool = field(default=False)
    players: dict[UUID, Player] = field(factory=dict)

    questions: list[Question] = field(factory=generate_questions)
    question_types: dict[str, int] = field(factory=dict)

    def get_player_list(self) -> list[dict]:
        return [p.get_display_data() for p in self.players.values()]

