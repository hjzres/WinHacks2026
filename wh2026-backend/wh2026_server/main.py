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
async def connect(sid, environ, auth):
    id = auth["id"]
    connections[sid] = ConnectionData(id)

    print("connect ", sid)
    print(connections)


@sio.event
async def create_game(sid):
    game_code = generate_unique_game_code()
    game = games[game_code] = Game(
        game_code,
    )

    player = Player(connections[sid].id, is_host=True)
    game.players[connections[sid].id] = player
    await sio.enter_room(sid, game_code)

    connections[sid].game_code = game_code

    print(games)

    return {"status": "OK", "game_code": game_code, "name": player.name}


@sio.event
async def join_game(sid, data):
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

    return {"status": "OK"}


@sio.event
async def set_name(sid, data):
    new_name = data
    conn_data = connections[sid]

    if not validate_name(new_name):
        return {"status": "ERROR", "message": "Invalid name."}

    game = games[conn_data.game_code]
    player = game.players[conn_data.id]

    print(f"Old name: {player.name}, New name: {new_name}")

    player.name = new_name


@sio.event
async def disconnect(sid, reason):
    del connections[sid]

    print("disconnect ", sid, reason)


app = socketio.ASGIApp(sio)
