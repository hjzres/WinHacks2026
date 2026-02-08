<script lang="ts">
    let { question, answer } = $props();

    let test = "\\int_{1}^{10}x^2 dx"

    let renderedVersion: HTMLElement;

    $effect(function renderMath() {
        // @ts-ignore
        window.MathJax?.typesetPromise([renderedVersion]);
    });

    

    // window.MathJax.typeset(renderedVersion);
</script>

<main>
    <header>
        Question #X: <span bind:this={renderedVersion} >$${test}$$</span>
    </header>
   <footer>
        ANSWER BOX
   </footer>
</main>

<style>
    main{
        margin: 10vh 10vw;
        height:80vh;
        width:80vw;

    }
    header{
        display:flex;
        justify-content: center;
        height:20%;
        width:100%;
        font-size: 2rem;
    }
    footer{
        display:flex;
        justify-content: center;
        height: 60%;
        width:80%;
        margin: 0% 0 10% 10%;
        border: 5px solid black;
        font-size: 2rem;
    }
</style>