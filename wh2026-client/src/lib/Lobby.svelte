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

    .settings{
        width:25vw;
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

    .menu .section p input{
        width:2vw;
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
                    <p><input type="number" name="vc" id="vc">Vector Calculus</p>
                    <p><input type="number" name="i" id="i">Integration</p>
                    <p><input type="number" name="d" id="d">Derivatives</p>
                </div>
                <div class="section">
                    <p><input type="number" name="f" id="f">Functions</p>
                    <p><input type="number" name="ba" id="ba">Boolean Algebra</p>
                    <p><input type="number" name="la" id="la">Linear Algebra</p>
                </div>
                <div class="section">
                    <p><input type="number" name="a" id="a">Arithmetic</p>
                    <p><input type="number" name="t" id="t">Trigonometry</p>
                    <p><input type="number" name="s" id="s">Statistics</p>
                </div>
            </div>
        </div>
        <div class="settings">
            <p class="title">Settings:</p>
            <p><input type="number" name="time" id="time">s</p>
            <p><input type="number" name="max-questions" id="max-questions"> questions</p>
        </div>
    </div>
</div>