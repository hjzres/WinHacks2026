<script lang="ts">
   let { question, answer, submitAnswer, totalQuestions, players, currentQuestion, sendSabotage } = $props();

  

  let renderedVersion: HTMLElement;
  let renderedAnswer: HTMLElement;

  let sabotageOpen = $state(false); 

  function sabotagePlayer(id: string) {
    console.log("Sabotaged:", id);
    sendSabotage(id);
    sabotageOpen = false; 
  }

  export function sabotage(){
    sabotageOpen = true;
    console.log("test");
  }

  $effect(() => {
    
    question;
    answer;
    currentQuestion;
    if (!renderedVersion || !renderedAnswer) return;
    // @ts-ignore
    window.MathJax?.typesetClear([renderedVersion, renderedAnswer]);
    renderedVersion.innerHTML = "$$" + question + "$$";
    renderedAnswer.innerHTML = answer;
    window.MathJax?.typeset([renderedVersion, renderedAnswer]);
  });

  function next() {
    let inputs = renderedAnswer.parentElement!.querySelectorAll<HTMLInputElement>('input');
    let data: { [index: string]: number | undefined } = {};

    for (let input of inputs) {
      if (input.value === "") return;
      data[input.name] = Number(input.value);
    }

    submitAnswer(data);
  }
</script>
<div class="bg">
    <main>
    <header>
        <span class="qLabel">Question #{currentQuestion}:</span>
        <span class="qMath" bind:this={renderedVersion}>$${question}$$</span>
    </header>

    <div class="workArea">
        <span bind:this={renderedAnswer}>{answer}</span>
    </div>

    <footer>
        <div class="progress">{currentQuestion} / {totalQuestions}</div>
        <button class="nextBtn" onclick={next}>Next →</button>
    </footer>

    {#if sabotageOpen}
        <div class="overlay">
        <div class="modal">
            <div class="modalTitle">Choose someone to sabotage</div>

            <div class="playerList">
            {#each players as p}
                <div class="playerItem" onclick={() => sabotagePlayer(p.id)}>
                {p.name}
                </div>
            {/each}
            </div>
        </div>
        </div>
    {/if}
    
    </main>
</div>
<style>
  main {
    margin: 0 auto;
    width: min(1000px, 92%);
    height: 84%;

    border-radius: 18px;
    border: 1px solid rgba(0,0,0,0.10);
    background: linear-gradient(
        180deg,
        rgba(120,140,255,0.08),
        transparent 40%
      ),
      #fff;
    box-shadow: 0 18px 60px rgba(0,0,0,0.12);

    display: flex;
    flex-direction: column;
    overflow: hidden;

    transform: translateY(8vh);
  }

  header {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    padding: 20px 18px;
    border-bottom: 1px solid rgba(0,0,0,0.08);
    font-size: 2rem;
  }

  .qLabel {
    font-weight: 800;
    color: rgba(0,0,0,0.75);
  }

  .qMath {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .workArea {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 24px;

    margin: 22px;
    border-radius: 16px;
    border: 2px solid rgba(0,0,0,0.10);
    background: rgba(0,0,0,0.02);

    font-size: 1.6rem;
  }

  footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 18px;
    border-top: 1px solid rgba(0,0,0,0.08);
  }

  .progress {
    font-weight: 800;
    color: rgba(0,0,0,0.65);
    font-size: 1.05rem;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(0,0,0,0.05);
  }

  .nextBtn {
    border: none;
    border-radius: 12px;
    padding: 10px 16px;
    font-weight: 900;
    cursor: pointer;

    background: #4f6bff;
    color: white;
    box-shadow: 0 10px 24px rgba(79,107,255,0.25);
  }

  .nextBtn:hover {
    filter: brightness(1.03);
  }
  .nextBtn:active {
    transform: translateY(1px);
  }

  .overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    display: grid;
    place-items: center;
    z-index: 1000;
  }

  .modal {
    width: min(420px, 90vw);
    background: white;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  }

  .modalTitle {
    font-weight: 900;
    margin-bottom: 14px;
    text-align: center;
  }

  .playerList {
    display: grid;
    gap: 10px;
  }

  .playerItem {
    padding: 12px;
    border-radius: 12px;
    border: 1px solid rgba(0,0,0,0.15);
    font-weight: 800;
    cursor: pointer;
    text-align: center;
  }

  .playerItem:hover {
    background: rgba(79,107,255,0.08);
  }

  span {
    margin: 0;
  }

  .bg{
    width:100vw;
    height: 100vh;
    background-image: url(https://static.vecteezy.com/system/resources/previews/013/894/763/non_2x/minimalist-blue-wavy-with-halftone-background-gradient-free-vector.jpg);
    background-size: cover;
  }
</style>
