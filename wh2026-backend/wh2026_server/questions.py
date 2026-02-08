import math
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

POWER_DEFINITE_INTEGRAL = QuestionTemplate(
    MathTemplate(r"\int_{ $a }^{ $b } x^{ $n } dx "),
    MathTemplate(r"\frac{ $num }{ $den }"),
    constants=["a", "b", "n"],
    placeholders=["num", "den"],
)

MATRIX_2X2 = QuestionTemplate(
    MathTemplate(r"""\left[\begin{array}{cc|c}
$a & $b & $c \\
$d & $e & $f
\end{array}\right]
"""),
    MathTemplate(r"""\left[\begin{array}{cc|c}
1 & 0 & $x \\
0 & 1 & $y
\end{array}\right]
"""),
    constants=["a", "b", "c", "d", "e", "f"],
    placeholders=["x", "y"],
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


def make_random_power_definite_integral():
    a = random.randint(-10, 9)
    b = random.randint(a + 1, 10)

    n = random.randint(2, 8)

    num = b ** (n + 1) - a ** (n + 1)
    den = n + 1

    gcd = math.gcd(num, den)

    num //= gcd
    den //= gcd

    return Question(
        POWER_DEFINITE_INTEGRAL, {"a": a, "b": b, "n": n}, {"num": num, "den": den}
    )


def make_random_matrix_2x2():
    solvable = False

    while not solvable:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)

        det = a * d - b * c

        solvable = det != 0

    return Question(
        MATRIX_2X2, {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f}, {"x": x, "y": y}
    )


question_generators = [make_random_qf, make_random_power_definite_integral]


def generate_questions():
    q = []
    for i in range(10):
        q.append(random.choice(question_generators)())
    return q
