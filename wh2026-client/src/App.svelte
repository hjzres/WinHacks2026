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

  interface PlayerData {
      name: string, 
      is_host: boolean, 
      id: string
  }

  let players : Array<PlayerData> = $state([]);
  let inLobby : boolean = $state(false);
  let gameCode : string = $state("");
  let isHost : boolean = $state(false);
  let gameStarted : boolean = $state(false);
  let question : string = $state("");
  let answer : string = $state("");
  let totalQuestions: number = $state(1);
  let currentQuestion = $state(1);
  let sabotageChance:number = $state(3);
  
  function sendSabotage(id: string){
    socket.emit("send_sabotage", id, (data) => {
        
    })
  }

  let gameComponent:Game;

  socket.on("players_updated", (data) => {
      console.log(data);
      players = data;
  });

  socket.on("question_updated", (data) => {
      console.log(data);
      players = data;

      question = data.question;
      answer = data.answer_template;
  });

  socket.on("game_started", (data) => {
      console.log(data);
      gameStarted = true;
      question = data.question;
      answer = data.answer_template;
      totalQuestions = data.total_questions;
      console.log(totalQuestions);
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
    socket.emit("update_question_types", questions);
  }
  
  function startGame(){
    socket.emit("start_game", (data) => {
      console.log("Started ", data);
    });
  }

  function submitAnswer(userAnswer) {
  socket.emit("submit_answer", userAnswer, (data) => {
    console.log(userAnswer);
    console.log(data);
    if(!data.is_correct) return;
    currentQuestion++;
    sabotageChance = Math.floor(Math.random() * 3);
    if(sabotageChance == 1){
        gameComponent.sabotage()
        sabotageChance = 2;
    }
    console.log(sabotageChance);
    question = data.next_question;
    answer = data.next_answer_template;
    console.log(question);
    console.log(answer);
  });
}

</script>

<main>
  {#if !inLobby}
    <JoinHost HostLobby={HostLobby} JoinLobby={JoinLobby} />
  {:else if !gameStarted}
    <Lobby players={players} gameCode={gameCode} isHost={isHost} updateQuestionData={updateQuestionTypes} startGame={startGame}/>
  {:else}
    <Game question={question} answer={answer} submitAnswer={submitAnswer} totalQuestions={totalQuestions} players={players} currentQuestion={currentQuestion} bind:this={gameComponent} sendSabotage={sendSabotage}/>
  {/if}
</main>

<style>
  
</style>
