import math
import random
import string
from collections.abc import Callable

from attrs import define, field


class MathTemplate(string.Template):
    delimiter = "$"


@define
class QuestionTemplate:
    question_template: MathTemplate = field()
    answer_template: MathTemplate = field()
    constants: list[str] = field()
    placeholders: list[str] = field()
    check_answer: Callable[[dict[str, int], dict[str, int]], bool] | None = field(
        default=None
    )

    def render_answer_template(self) -> str:
        return self.answer_template.substitute(
            {
                p: f'<tex-html><input type="number" name="{p}"/></tex-html>'
                for p in self.placeholders
            }
        )


def lowest_terms(num: int, den: int) -> tuple[int, int]:
    is_negative = False

    if num < 0:
        is_negative = not is_negative
        num = -num

    if den < 0:
        is_negative = not is_negative
        den = -den

    gcd = math.gcd(num, den)

    num //= gcd
    den //= gcd

    if is_negative:
        return -num, den

    return num, den


def check_quadratic_factoring(
    solution: dict[str, int], submitted: dict[str, int]
) -> bool:
    sol_r = solution["r"]
    sol_s = solution["s"]
    sub_r = submitted["r"]
    sub_s = submitted["s"]

    if sub_r == sol_r and sub_s == sol_s:
        return True

    sub_r, sub_s = sub_s, sub_r

    return sub_r == sol_r and sub_s == sol_s

SABOTAGE_PLAYER = QuestionTemplate(
    MathTemplate(r"x^2 + $b x + $c"),
    MathTemplate(r"( x + $r )( x + $s )"),
    constants=["b", "c"],
    placeholders=["r", "s"],
    check_answer=check_quadratic_factoring,
)


QUADRATIC_FACTORING = QuestionTemplate(
    MathTemplate(r"x^2 + $b x + $c"),
    MathTemplate(r"( x + $r )( x + $s )"),
    constants=["b", "c"],
    placeholders=["r", "s"],
    check_answer=check_quadratic_factoring,
)


def check_power_definite_integral(
    solution: dict[str, int], submitted: dict[str, int]
) -> bool:
    sol_num = solution["num"]
    sol_den = solution["den"]
    sub_num = submitted["num"]
    sub_den = submitted["den"]

    sub_num, sub_den = lowest_terms(sub_num, sub_den)

    return sol_num == sub_num and sol_den == sub_den


POWER_DEFINITE_INTEGRAL = QuestionTemplate(
    MathTemplate(r"\int_{ $a }^{ $b } x^{ $n } dx "),
    MathTemplate(r"\frac{ $num }{ $den }"),
    constants=["a", "b", "n"],
    placeholders=["num", "den"],
    check_answer=check_power_definite_integral,
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

    def check_answers(self, answers: dict[str, int]):
        for p in self.template.placeholders:
            if answers[p] != self.placeholder_solutions[p]:
                return False
        return True


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

    num, den = lowest_terms(num, den)

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
