<script lang="ts">
    import { v4 as uuidv4 } from 'uuid';
  import JoinHost from './lib/JoinHost.svelte'
  import Lobby from './lib/Lobby.svelte' 

  // import { io } from "socket.io-client";

<<<<<<< HEAD
  if(localStorage.getItem("uuid") === null){
    localStorage.setItem("uuid", uuidv4());
  }

  const socket = io("http://localhost:5000",{
  auth: {
    id: localStorage.getItem("uuid")
  }
  });

  let players : Array<string> = $state([]);
  let inLobby : boolean = $state(false);
  let gameCode : string = $state("");

  socket.on("players_updated", (data) => {
      console.log(data);
      players = data;
  });
=======
  // const socket = io("http://localhost:5000",{
  // auth: {
  //   id: "a0472aba-6249-4e24-8baf-711e85d7a58b"
  // }
  // });

  // socket.on("connect", () => {
  // socket.emit("create_game", ({status, game_code, name}) => {
  //     console.log(status, game_code, name);
  //     socket.emit("set_name", "awesomename");
  // });
  // });
>>>>>>> origin/lobby-design

  function HostLobby(){
    socket.emit("create_game", (data) => {
      console.log(data);
      gameCode = data.game_code;
      inLobby = true;
    });
  }

  function JoinLobby(game_code : string){
    socket.emit("join_game", game_code, (data) => {
      console.log(data);
      gameCode = game_code;
      inLobby = true;
    })
  }

</script>

<main>
<<<<<<< HEAD
  {#if !inLobby}
    <JoinHost HostLobby={HostLobby} JoinLobby={JoinLobby} />
  {:else}
    <Lobby players={players} gameCode={gameCode} />
  {/if}
=======
  <Lobby />
>>>>>>> origin/lobby-design
</main>

<style>
  
</style>
