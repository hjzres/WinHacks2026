<script lang="ts">
    let { players, gameCode } = $props();
</script>

<div id="parent-container">
    <div id="code-container">
        <div class="text-container">
            <p style="font-size: 2rem;">Join Code: {gameCode}</p>
        </div>
    </div>

    <div class="player-list-menu">
        <div style="width: 100%; height: 20%;">
            <div class="text-container">
                <p style="font-size: 2rem">Players:</p>
            </div>
        </div>

        <div style="width: 100%; height: 80%; background-color: green;">
            <div class="player-grid">
                {#each players as player (player.id ?? player.name)}
                <p style="margin: 0;">{player.name}</p>
                {/each}
            </div>
        </div>
    </div>

    <div class="info-menu-container">
        <div style="width: 100%; height: 20%;">
            <div style="display: flex; flex-direction: row; align-items: center;">
                <div style="width: 75%; height: 100%">    
                    <div class="text-container">
                        <p style="font-size: 2rem;">Question Types:</p>
                    </div>
                </div>

                <div style="width: 25%; height: 100%">
                    <div class="text-container">
                        <p style="font-size: 2rem;">Settings:</p>
                    </div>
                </div>
            </div>
        </div>

        <div style="width: 100%; height: 80%; display: flex; flex-direction: row; align-items: center;">
            <div style="width: 75%; height: 100%">
                <div id="questions-menu">
                    <!-- CATEGORY 1 -->
                    <div style="background-color: red; width: 33.4%; height: 100%;">
                        <p class="mathematical-subject-text"><input type="number" name="i" id="i" min=0 value=0 style="width: 70px; text-align: center;"> Integration</p>
                        <p class="mathematical-subject-text"><input type="number" name="d" id="d" min=0 value=0 style="width: 70px; text-align: center;"> Derivatives</p>
                        <p class="mathematical-subject-text"><input type="number" name="vc" id="vc" min=0 value=0 style="width: 70px; text-align: center;"> Vector Calculus</p>
                    </div>

                    <!-- CATEGORY 2 -->
                    <div style="background-color: orange; width: 33.3%; height: 100%;">
                        <p class="mathematical-subject-text"><input type="number" name="f" id="f" min=0 value=0 style="width: 70px; text-align: center;"> Functions</p>
                        <p class="mathematical-subject-text"><input type="number" name="ba" id="ba" min=0 value=0 style="width: 70px; text-align: center;"> Boolean Algebra</p>
                        <p class="mathematical-subject-text"><input type="number" name="la" id="la" min=0 value=0 style="width: 70px; text-align: center;"> Linear Algebra</p>
                    </div>

                    <!-- CATEGORY 3 -->
                    <div style="background-color: red; width: 33.3%; height: 100%;">
                        <p class="mathematical-subject-text"><input type="number" name="a" id="a" min=0 value=0 style="width: 70px; text-align: center;"> Arithmetic</p>
                        <p class="mathematical-subject-text"><input type="number" name="t" id="t" min=0 value=0 style="width: 70px; text-align: center;"> Trigonometry</p>
                        <p class="mathematical-subject-text"><input type="number" name="s" id="s" min=0 value=0 style="width: 70px; text-align: center;"> Statistics</p>
                    </div>
                </div>
            </div>

            <!-- SETTINGS -->
            <div style="width: 25%; height: 100%; background-color: purple;">
                <p style="margin-top: 13%;"><input type="number" name="time" id="time" min=30 value=120 style="width: 70px; text-align: center;"> s</p>
            </div>
        </div>

        
    </div>
</div>

<!-- <div id="parent-container">
    <div style="width: 100vw; height: 100vh;">
        <div>
            <div class="code-container" style="margin: 1vh 1vw 1vh 1vw; background-color: white;">
                <p class="title">Join Code: {gameCode}</p>
            </div>
        </div>
        






        <div class="player-list-menu" style="background-color: white;">
            <p class="title">Player:</p>
            <div class="player-grid">
                {#each players as player (player.id ?? player.name)}
                <p style="margin: 0;">{player.name}</p>
                {/each}
            </div>
        </div>






        <div class="info-menu-container" style="background-color: white;">
            <div class="question-types">
                <p class="title">Question Types:</p>
                <div class="sections">
                    <div class="section">
                        <p><input type="number" name="i" id="i" min=0 value=0> Integration</p>
                        <p><input type="number" name="d" id="d" min=0 value=0> Derivatives</p>
                        <p><input type="number" name="vc" id="vc" min=0 value=0> Vector Calculus</p>
                    </div>
                    <div class="section">
                        <p><input type="number" name="f" id="f" min=0 value=0> Functions</p>
                        <p><input type="number" name="ba" id="ba" min=0 value=0> Boolean Algebra</p>
                        <p><input type="number" name="la" id="la" min=0 value=0> Linear Algebra</p>
                    </div>
                    <div class="section">
                        <p><input type="number" name="a" id="a" min=0 value=0> Arithmetic</p>
                        <p><input type="number" name="t" id="t" min=0 value=0> Trigonometry</p>
                        <p><input type="number" name="s" id="s" min=0 value=0> Statistics</p>
                    </div>
                </div>
            </div>





            <div class="settings">
                <p class="title">Settings:</p>
                <p style="margin-top: 13%;"><input type="number" name="time" id="time" min=30 value=120>s</p>
            </div>
        </div>
    </div>
</div> -->

<style>
    * {
        font-size: 1.5rem;
    }

    #parent-container {
        background-color: black;
        width: 100vw;
        height: 100vh;
    }

    .player-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr)); /* max 4 per row */
        gap: 12px; /* space between rows/cols */
        
    }

    @media (max-width: 800px) {
        .player-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    @media (max-width: 450px) {
        .player-grid { grid-template-columns: 1fr; }
    }

    #code-container {
        display:flex;
        justify-content: center;
        align-items: center;
        width: 98vw;
        height: 10vh;
        background-color: white;
        margin-left: 1vw;
        transform: translateY(1vh);
    }

    .player-list-menu {
        width: 98vw;
        height: 40vh;
        margin-left: 1vw;
        background-color: white;
        transform: translateY(2vh);
    }

    .info-menu-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 98vw;
        height: 46vh;
        margin-left: 1vw;
        background-color: white;
        transform: translateY(3vh);
    }

    #questions-menu {
        width: 100%; 
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .text-container {
        background-color: red; 
        width: 30%; 
        height: 80%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .mathematical-subject-text {
        margin: 15% 0 15% 0;
    }

    .info-menu-container .sections {
        margin-left: 10px;
        display: flex;
        flex-direction: row;
    }

    .info-menu-container .section{
        width: 33%;
        height: 100%;
    }

    .info-menu-container .section p {
        margin: 13% 0 25% 13%;
    }

    input {
        width: 3vw;
    }

    .settings {
        width: 25vw;
        height: 100%;
    }

    #time {
        width: 4vw;
    }
</style>
