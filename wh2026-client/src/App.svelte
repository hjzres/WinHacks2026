<script lang="ts">
    import { v4 as uuidv4 } from 'uuid';
  import JoinHost from './lib/JoinHost.svelte'
  import Lobby from './lib/Lobby.svelte' 
  import Game from './lib/Game.svelte'

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
  let inLobby : boolean = $state(false);
  let gameCode : string = $state("");
  let isHost : boolean = $state(false);
  let gameStarted : boolean = $state(false);

  socket.on("players_updated", (data) => {
      console.log(data);
      players = data;
  });

  socket.on("game_started", (data) => {
      console.log(data);
      gameStarted = true;
      console.log(gameStarted);
  })

  function HostLobby(){
    socket.emit("create_game", (data) => {
      console.log(data);
      gameCode = data.game_code;
      inLobby = true;
      isHost = true;
    });
  }

  function JoinLobby(game_code : string){
    socket.emit("join_game", game_code, (data) => {
      console.log(data);
      gameCode = game_code;
      inLobby = true;
    })
  }

  function updateQuestionTypes(questions: {[index: string]: number|undefined}){
    socket.emit("update_question_types", questions)
  }
  
  function startGame(){
    socket.emit("start_game");
  }

</script>

<main>
  {#if !inLobby}
    <JoinHost HostLobby={HostLobby} JoinLobby={JoinLobby} />
  {:else if !gameStarted}
    <Lobby players={players} gameCode={gameCode} isHost={isHost} updateQuestionData={updateQuestionTypes} startGame={startGame}/>
  {:else}
    <Game />
  {/if}
</main>

<style>
  
</style>
