<style lang="typescript">
    div {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh; /* Full viewport height */
    }
    div button{
        margin:2%;
        height:10%;
        width:10%;
    }
</style>

<div>
    Site Name
    <button>Join</button>
    <button>Host</button>
</div>

<script lang="ts">
import { io } from "socket.io-client";

const socket = io("http://localhost:5000",{
  auth: {
    id: "a0472aba-6249-4e24-8baf-711e85d7a58b"
  }
});

socket.on("connect", () => {
  socket.emit("create_game", ({status, game_code, name}) => {
    console.log(status, game_code, name);

    socket.emit("set_name", "awesomename");
  });
});

</script>