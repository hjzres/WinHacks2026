<script lang="ts">

</script>

<div class="container">
    <div class="code">
        <p class="title">CODE :######</p>
    </div>
    <div class="players-menu">
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
    <div class=menu>
        <div class="question-types">
            <p class="title">Question Types:</p>
            <div class="sections">
                <div class="section">
                    <p><input type="number" name="vc" id="vc" min=0 value=0>Vector Calculus</p>
                    <p><input type="number" name="i" id="i" min=0 value=0>Integration</p>
                    <p><input type="number" name="d" id="d" min=0 value=0>Derivatives</p>
                </div>
                <div class="section">
                    <p><input type="number" name="f" id="f" min=0 value=0>Functions</p>
                    <p><input type="number" name="ba" id="ba" min=0 value=0>Boolean Algebra</p>
                    <p><input type="number" name="la" id="la" min=0 value=0>Linear Algebra</p>
                </div>
                <div class="section">
                    <p><input type="number" name="a" id="a" min=0 value=0>Arithmetic</p>
                    <p><input type="number" name="t" id="t" min=0 value=0>Trigonometry</p>
                    <p><input type="number" name="s" id="s" min=0 value=0>Statistics</p>
                </div>
            </div>
        </div>
        <div class="settings">
            <p class="title">Settings:</p>
            <p><input type="number" name="time" id="time" min=30 value=120>s</p>
        </div>
    </div>
</div>

<style>
    .container{
        width:100vw;
        height: 100vh;
    }

    .code{
        display:flex;
        justify-content: center;
        width:100vw;
        height:10vh;
    }

    .players-menu{
        width:100vw;
        height:40vh;
    }

    .players-menu .sections{
        display: flex;
        justify-content: space-around;
        flex-direction: column;
        gap:40px;
    }

    .players-menu .section{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        width: 100vw;
    }

    .players-menu .section p{
        display:flex;
        width: 25vw;
        justify-content: center;
    }

    .menu{
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

    .menu .sections{
        margin-left: 10px;
        display:flex;
        flex-direction: row;
    }

    .menu .section{
        width:33%;
        height:100%;
    }

    .menu .section p:not(:last-child){
        margin-bottom: 33%;
    }

    input{
        width:2vw;
    }

    .settings{
        width:25vw;
        height:100%;
    }

    #time{
        width: 3vw;
    }
</style>