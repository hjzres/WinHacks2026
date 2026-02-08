<script lang="ts">
    let { players, gameCode } = $props();
</script>

<div id="parent-container">
    <div id="code-container">
        <div style="width: 100%; height: 100%; display: flex; flex-direction: row; align-items: center;">
            <div style="width: 33.3%; height: 100%;">
                <p class="text-container">[HOST]</p>
            </div>

            <div id="code-text-container" style="width: 33.4%; height: 100%;">
                <p style="font-size: 2rem; font-weight: bold;">JOIN CODE: {gameCode}</p>
            </div>

            <div class="button-container" style="width: 33.3%; height: 100%;">
                <button id="start-button">Start Round</button>
            </div>
        </div>
    </div>

    <div class="player-list-menu">
        <div style="width: 100%; height: 20%;">
            <div class="text-container">
                <p style="font-size: 2rem;">Players:</p>
            </div>
        </div>

        <div style="width: 100%; height: 80%;">
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
                    <div style="width: 33.4%; height: 100%; margin-left: 15px;">
                        <p class="mathematical-subject-text"><input type="number" name="i" id="i" min=0 value=0 style="width: 70px; text-align: center;"> Integration</p>
                        <p class="mathematical-subject-text"><input type="number" name="d" id="d" min=0 value=0 style="width: 70px; text-align: center;"> Derivatives</p>
                        <p class="mathematical-subject-text"><input type="number" name="vc" id="vc" min=0 value=0 style="width: 70px; text-align: center;"> Vector Calculus</p>
                    </div>

                    <!-- CATEGORY 2 -->
                    <div style="width: 33.3%; height: 100%;">
                        <p class="mathematical-subject-text"><input type="number" name="f" id="f" min=0 value=0 style="width: 70px; text-align: center;"> Functions</p>
                        <p class="mathematical-subject-text"><input type="number" name="ba" id="ba" min=0 value=0 style="width: 70px; text-align: center;"> Boolean Algebra</p>
                        <p class="mathematical-subject-text"><input type="number" name="la" id="la" min=0 value=0 style="width: 70px; text-align: center;"> Linear Algebra</p>
                    </div>

                    <!-- CATEGORY 3 -->
                    <div style="width: 33.3%; height: 100%;">
                        <p class="mathematical-subject-text"><input type="number" name="a" id="a" min=0 value=0 style="width: 70px; text-align: center;"> Arithmetic</p>
                        <p class="mathematical-subject-text"><input type="number" name="t" id="t" min=0 value=0 style="width: 70px; text-align: center;"> Trigonometry</p>
                        <p class="mathematical-subject-text"><input type="number" name="s" id="s" min=0 value=0 style="width: 70px; text-align: center;"> Statistics</p>
                    </div>
                </div>
            </div>

            <!-- SETTINGS -->
            <div style="width: 25%; height: 100%;">
                <p style="margin-left: 15px;"><input type="number" name="time" id="time" min=30 value=120 style="width: 70px; text-align: center;"> s</p>
            </div>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=SN+Pro:ital,wght@0,200..900;1,200..900&display=swap');

    * {
        font-size: 1.5rem;
        font-family: "Montserrat";
    }

    #parent-container {
        background-image: url(https://static.vecteezy.com/system/resources/previews/020/798/168/large_2x/subtle-gradient-blue-background-free-vector.jpg);
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
        border-radius: 15px;
    }

    .player-list-menu {
        width: 98vw;
        height: 40vh;
        margin-left: 1vw;
        background-color: white;
        transform: translateY(1vh);
        border-radius: 15px;
    }

    .info-menu-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 98vw;
        height: 46vh;
        margin-left: 1vw;
        background-color: white;
        transform: translateY(2vh);
        border-radius: 15px;
    }

    #questions-menu {
        width: 100%; 
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .text-container {
        width: 30%; 
        height: 80%;
        display: flex;
        justify-content: left;
        align-items: center;
        margin: 10px 0 0 15px;
    }

    #code-text-container {
        width: 30%; 
        height: 80%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .mathematical-subject-text {
        margin: 0 0 20% 0;
    }

    input {
        width: 3vw;
    }

    #time {
        width: 4vw;
    }

    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
