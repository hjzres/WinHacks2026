<style lang="typescript">
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

<div class="container">
    <div class="code">
        <p class="title">CODE :######</p>
    </div>
    <div class="players-menu">
        <p class="title">Player:</p>
    </div>
    <div class=menu>
        <div class="question-types">
            <p class="title">Question Types:</p>
            <div class="sections">
                <div class="section">
                    <p><input type="number" name="vc" id="vc" value=0>Vector Calculus</p>
                    <p><input type="number" name="i" id="i" value=0>Integration</p>
                    <p><input type="number" name="d" id="d" value=0>Derivatives</p>
                </div>
                <div class="section">
                    <p><input type="number" name="f" id="f" value=0>Functions</p>
                    <p><input type="number" name="ba" id="ba" value=0>Boolean Algebra</p>
                    <p><input type="number" name="la" id="la" value=0>Linear Algebra</p>
                </div>
                <div class="section">
                    <p><input type="number" name="a" id="a" value=0>Arithmetic</p>
                    <p><input type="number" name="t" id="t" value=0>Trigonometry</p>
                    <p><input type="number" name="s" id="s" value=0>Statistics</p>
                </div>
            </div>
        </div>
        <div class="settings">
            <p class="title">Settings:</p>
            <p><input type="number" name="time" id="time" value=120>s</p>
            <p><input type="number" name="max-questions" id="max-questions" value=5> questions</p>
        </div>
    </div>
</div>