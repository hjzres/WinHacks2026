<script lang="ts">
    import { v4 as uuidv4 } from 'uuid';
  import JoinHost from './lib/JoinHost.svelte'
  import Lobby from './lib/Lobby.svelte' 

  import { io } from "socket.io-client";

  if(localStorage.getItem("uuid") === null){
    localStorage.setItem("uuid", uuidv4());
  } else {
    console.log("Reconnected");
  }

  const socket = io("http://localhost:5000",{
  auth: {
    id: localStorage.getItem("uuid")
  }
  });

  socket.on("connect", () => {
      
  });

  function HostLobby(){
    socket.emit("create_game", (data) => {
      console.log(data.status, data.game_code, data.name);
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
