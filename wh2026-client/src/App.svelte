<script lang="ts">
  import JoinHost from './lib/JoinHost.svelte'
  import Lobby from './lib/Lobby.svelte' 

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

<main>
  <JoinHost />
</main>

<style>
  
</style>
