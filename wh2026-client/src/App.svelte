<script lang="ts">
    import { v4 as uuidv4 } from 'uuid';
  import JoinHost from './lib/JoinHost.svelte'
  import Lobby from './lib/Lobby.svelte' 

  import { io } from "socket.io-client";

  if(localStorage.getItem("uuid") === null){
    localStorage.setItem("uuid", uuidv4());
  }

  const socket = io("http://localhost:5000",{
  auth: {
    id: localStorage.getItem("uuid")
  }
  });

  let players : Array<string> = $state([]);

  socket.on("players_updated", (data) => {
      console.log(data);
      players = data;
  });

  function HostLobby(){
    socket.emit("create_game", (data) => {
      console.log(data);
    });
  }

  function JoinLobby(game_code : string){
    socket.emit("join_game", game_code, (data) => {
      console.log(data);
    })
  }

</script>

<main>
  <JoinHost HostLobby={HostLobby} JoinLobby={JoinLobby} />
</main>

<style>
  
</style>
