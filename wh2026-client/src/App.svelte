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
      
  });

  function HostLobby(){
    socket.emit("create_game", (data) => {
      console.log(data.status, data.game_code, data.name);
      socket.emit("set_name", "awesomename");
    });
  }

  function JoinLobby(game_code : string){
    socket.emit("join_game", game_code, (data) => {
      console.log(data);
    })

    let code : string;
  }

</script>

<main>
  <JoinHost HostLobby={HostLobby} JoinLobby={JoinLobby} />
</main>

<style>
  
</style>
