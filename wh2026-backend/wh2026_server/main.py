from typing import Any

import socketio

from .data import ConnectionData, Game, Player, generate_game_code, validate_name

sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=[
        "http://localhost:5000",
        "http://localhost:5173",
    ],
)

games: dict[str, Game] = {}
connections: dict[str, ConnectionData] = {}


def generate_unique_game_code() -> str:
    while True:
        game_code = generate_game_code()
        if game_code not in games:
            return game_code


@sio.event
async def connect(sid: str, environ: Any, auth: Any) -> None:
    id = auth["id"]
    connections[sid] = ConnectionData(id)

    print("connect ", sid)
    print(connections)


@sio.event
async def create_game(sid: str):
    game_code = generate_unique_game_code()
    conn_data = connections[sid]

    if conn_data.game_code is not None:
        return {"status": "ERROR", "message": "Already in game."}

    game = games[game_code] = Game(
        game_code,
    )

    player = Player(conn_data.id, is_host=True)
    game.players[conn_data.id] = player
    await sio.enter_room(sid, game_code)

    conn_data.game_code = game_code

    print(games)

    await sio.emit("players_updated", game.get_player_list(), room=conn_data.game_code)

    return {"status": "OK", "game_code": game_code, "name": player.name}


@sio.event
async def join_game(sid: str, data: str):
    game_code = data
    conn_data = connections[sid]

    if conn_data.game_code is not None:
        return {"status": "ERROR", "message": "Already in game."}

    try:
        game = games[game_code]
    except IndexError:
        return {"status": "ERROR", "message": "Game doesn't exist."}

    game.players[conn_data.id] = Player(conn_data.id)

    await sio.enter_room(sid, game_code)

    await sio.emit("players_updated", game.get_player_list(), room=game_code)

    return {"status": "OK"}


@sio.event
async def set_name(sid: str, data: str):
    new_name = data
    conn_data = connections[sid]

    if not validate_name(new_name):
        return {"status": "ERROR", "message": "Invalid name."}

    if conn_data.game_code is None:
        return {"status": "ERROR", "message": "Not in game."}

    game = games[conn_data.game_code]
    player = game.players[conn_data.id]

    print(f"Old name: {player.name}, New name: {new_name}")

    await sio.emit("players_updated", game.get_player_list(), room=conn_data.game_code)

    player.name = new_name


@sio.event
async def start_game(sid: str):
    """
    Client->Server event that should be sent from the host player when they
    press the "start game" button.

    It will automatically send the "game_started" event to every player in the
    game, in which the data object will have a "question" field and
    "answer_template" containing the question which can be rendered on the client.
    """
    conn_data = connections[sid]

    if conn_data.game_code is None:
        return {"status": "ERROR", "message": "Not in game."}

    game = games[conn_data.game_code]
    player = game.players[conn_data.id]

    if not player.is_host:
        return {"status": "ERROR", "message": "Player is not a host."}

    if game.started:
        return {"status": "ERROR", "message": "Game has already started."}

    game.started = True

    first_question = game.questions[0]

    await sio.emit(
        "game_started",
        {
            "question": first_question.render_question(),
            "answer_template": first_question.render_answer_template(),
        },
        room=conn_data.game_code,
    )

    return {"status": "OK"}


@sio.event
async def submit_answer(sid: str, data: dict[str, int]):
    """
    Client->Server event that should be sent from a player when they want to
    submit an answer to the current question.

    It should send an object with an integer value for each placeholder in the
    solution template.
    """
    conn_data = connections[sid]

    if conn_data.game_code is None:
        return {"status": "ERROR", "message": "Not in game."}

    game = games[conn_data.game_code]
    player = game.players[conn_data.id]

    if not game.started:
        return {"status": "ERROR", "message": "Game has not started."}

    question = game.questions[player.question_number]

    for p in question.template.placeholders:
        if p not in data:
            return {
                "status": "ERROR",
                "message": "Submitted answer doesn't contain all placeholders.",
            }

    for p in question.template.placeholders:
        if data[p] != question.placeholder_solutions[p]:
            return {"status": "OK", "is_correct": False}

    player.question_number += 1
    next_question = game.questions[player.question_number]

    return {
        "status": "OK",
        "is_correct": True,
        "next_question": next_question.render_question(),
        "next_answer_template": next_question.render_answer_template(),
    }


@sio.event
async def update_question_types(sid: str, data: dict[str, int]):
    conn_data = connections[sid]

    if conn_data.game_code is None:
        return {"status": "ERROR", "message": "Not in game."}

    game = games[conn_data.game_code]
    player = game.players[conn_data.id]

    if not player.is_host:
        return {"status": "ERROR", "message": "Player is not a host."}

    if game.started:
        return {"status": "ERROR", "message": "Game has already started."}

    game.question_types = data
    print(game.question_types)

    return {"status": "OK"}


@sio.event
async def disconnect(sid: str, reason: str):
    del connections[sid]

    print("disconnect ", sid, reason)


app = socketio.ASGIApp(sio)
