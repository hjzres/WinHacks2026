import random
import string
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


r"\frac{}{}"
[r"\frac{", 12, r"}{", 34, r"}"]


class MathTemplate(string.Template):
    delimiter = "$"


@define
class QuestionTemplate:
    question_template: MathTemplate = field()
    solution_template: MathTemplate = field()
    constants: list[str] = field()
    placeholders: list[str] = field()


QUADRATIC_FACTORING = QuestionTemplate(
    MathTemplate(r"x^2 + bx + c"),
    MathTemplate(r"(x+r)(x+s)"),
    constants=["b", "c"],
    placeholders=["r", "s"],
)


@define
class Question:
    template: QuestionTemplate
    constants: dict[str, int]
    placeholder_solutions: dict[str, int]

    def render_question(self) -> str:
        return self.template.question_template.substitute(self.constants)


def make_random_qf():
    r = random.randint(1, 10)
    s = random.randint(1, 10)
    return Question(QUADRATIC_FACTORING, {"b": r + s, "c": r * s}, {"r": r, "s": s})


def generate_questions():
    return [make_random_qf() for _ in range(10)]


@define
class Game:
    code: str = field()
    started: bool = field(default=False)
    players: dict[UUID, Player] = field(factory=dict)

    questions: list[Question] = field(factory=generate_questions)

    def get_player_list(self) -> list[dict]:
        return [p.get_display_data() for p in self.players.values()]


@define
class Player:
    id: UUID = field()
    is_host: bool = field(default=False)
    name: str = field(factory=random_name)
    points: int = field(default=0)
    question_number: int = field(default=0)

    def get_display_data(self) -> dict:
        return {"name": self.name, "is_host": self.is_host}
