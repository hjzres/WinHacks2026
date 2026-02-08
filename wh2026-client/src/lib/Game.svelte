<script lang="ts">
  let { question, answer, submitAnswer } = $props();

  let renderedVersion: HTMLElement;
  let renderedAnswer: HTMLElement;

  $effect(() => {
    if(!renderedVersion || !renderedAnswer) return;
    // @ts-ignore
    window.MathJax?.typeset([renderedVersion, renderedAnswer]);
  });

  function next(){
    console.log("click1");
    let inputs = renderedAnswer.parentElement!.querySelectorAll<HTMLInputElement>('input');
    let data: {[index: string]: number|undefined} = {};
    
    for(let input of inputs){
        if (input.value === "") return;
        data[input.name] = Number(input.value);
    }
    console.log("click2");


    submitAnswer(data);
  }
</script>

<main>
  <header>
    <span class="qLabel">Question #X:</span>
    <span class="qMath" bind:this={renderedVersion}>$${question}$$</span>
  </header>

  <div class="workArea">
    <span bind:this={renderedAnswer}>$${answer}$$</span>
  </div>

  <footer>
    <div class="progress">2 / 5</div>
    <button class="nextBtn" on:click={next}>Next →</button>
  </footer>
</main>

<style>
  main{
    margin: 8vh auto;
    width: min(1000px, 92vw);
    height: 84vh;

    border-radius: 18px;
    border: 1px solid rgba(0,0,0,0.10);
    background: linear-gradient(180deg, rgba(120,140,255,0.08), transparent 40%), #fff;
    box-shadow: 0 18px 60px rgba(0,0,0,0.12);

    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  header{
    display:flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    padding: 20px 18px;
    border-bottom: 1px solid rgba(0,0,0,0.08);
    font-size: 2rem;
  }

  .qLabel{
    font-weight: 800;
    color: rgba(0,0,0,0.75);
  }

  .qMath{
    display:flex;
    justify-content:center;
    align-items:center;
  }

  .workArea{
    flex: 1;
    display:flex;
    justify-content: center;
    align-items: center;
    padding: 24px;

    margin: 22px;
    border-radius: 16px;
    border: 2px solid rgba(0,0,0,0.10);
    background: rgba(0,0,0,0.02);

    font-size: 1.6rem;
  }

  footer{
    display:flex;
    align-items:center;
    justify-content: space-between;
    padding: 16px 18px;
    border-top: 1px solid rgba(0,0,0,0.08);
  }

  .progress{
    font-weight: 800;
    color: rgba(0,0,0,0.65);
    font-size: 1.05rem;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(0,0,0,0.05);
  }

  .nextBtn{
    border: none;
    border-radius: 12px;
    padding: 10px 16px;
    font-weight: 900;
    cursor: pointer;

    background: #4f6bff;
    color: white;
    box-shadow: 0 10px 24px rgba(79,107,255,0.25);
  }

  .nextBtn:hover{ filter: brightness(1.03); }
  .nextBtn:active{ transform: translateY(1px); }

  span{
    margin: 0;
  }
</style>
