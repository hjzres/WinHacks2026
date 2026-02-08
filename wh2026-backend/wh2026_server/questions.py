import random
import string

from attrs import define, field


class MathTemplate(string.Template):
    delimiter = "$"


@define
class QuestionTemplate:
    question_template: MathTemplate = field()
    answer_template: MathTemplate = field()
    constants: list[str] = field()
    placeholders: list[str] = field()

    def render_answer_template(self) -> str:
        return self.answer_template.substitute(
            {
                p: f'<tex-html><input type="number" name="{p}"/></tex-html>'
                for p in self.placeholders
            }
        )


QUADRATIC_FACTORING = QuestionTemplate(
    MathTemplate(r"x^2 + $b x + $c"),
    MathTemplate(r"( x + $r )( x + $s )"),
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

    def render_answer_template(self) -> str:
        return self.template.render_answer_template()


def make_random_qf():
    r = random.randint(1, 10)
    s = random.randint(1, 10)
    return Question(QUADRATIC_FACTORING, {"b": r + s, "c": r * s}, {"r": r, "s": s})


def generate_questions():
    return [make_random_qf() for _ in range(10)]
