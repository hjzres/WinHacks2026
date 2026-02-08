<script lang="ts">

</script>

<div style="background-color: black;">
    <div style="width: 100vw; height: 100vh; margin: 1vh 1vw 1vh 1vw;">
        <div class="code-container" style="margin: 1vh 1vw 1vh 1vw;">
            <p class="title">Join Code: ######</p>
        </div>

        <div class="player-list-menu" style="background-color: white;">
            <p class="title">Player:</p>
            <div class="sections">
                <div class="section">
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                </div>
                <div class="section">
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                </div>
                <div class="section">
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                    <p>---</p>
                </div>
            </div>
        </div>
        <div class="info-menu-container">
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
                <p><input type="number" name="time" id="time" min=30 value=120>s</p>
            </div>
        </div>
    </div>
</div>

<style>
    * {
        font-size: 1.5rem;
    }

    .code-container {
        display:flex;
        justify-content: center;
        align-items: center;
        width: 100vw;
        height: 10vh;
    }

    .player-list-menu{
        width:100vw;
        height:40vh;
    }

    .player-list-menu .sections{
        display: flex;
        justify-content: space-around;
        flex-direction: column;
        gap:40px;
    }

    .player-list-menu .section{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        width: 100vw;
    }

    .player-list-menu .section p{
        display:flex;
        width: 25vw;
        justify-content: center;
    }

    .info-menu-container{
        display:flex;
        flex-direction: row;
        width:100vw;
        height:50vh;
    }

    .question-types{
        width:75vw;
        height:100%;
    }

    .title{
        font-size: 2rem;
    }

    .info-menu-container .sections{
        margin-left: 10px;
        display:flex;
        flex-direction: row;
    }

    .info-menu-container .section{
        width:33%;
        height:100%;
    }

    .info-menu-container .section p:not(:last-child){
        margin-bottom: 33%;
    }

    input{
        width:3vw;
    }

    .settings{
        width:25vw;
        height:100%;
    }

    #time{
        width: 4vw;
    }
</style>