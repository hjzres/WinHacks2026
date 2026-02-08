<script lang="ts">
    let { HostLobby, JoinLobby } = $props();
    let code = $state();
</script>

<div id="body">
    <div id="container">
        <div style="width: 100%; height: 10%;">
             <p id="site-name">Site Name</p>
             <p id="site-description">Harness the potential of competitive group studying to solidify your mathematical foundations! Choose an option below:</p>
        </div>

        <div style="width: 100%; height: 90%;">
            <div style="width: 100%; height: 100%; display: flex; flex-direction: row; align-items: center;">
                <div style="width: 50%; height: 100%;">
                    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center;">
                        <div style="width: 100%; height: 50%; display: flex; justify-content: center; align-items: flex-end;">
                            <input type="text" name="code" id="code" maxlength=4 placeholder="Enter the code" bind:value={code}>
                        </div>
                            
                        <div style="width: 100%; height: 50%; display: flex; justify-content: center; align-items: flex-start;">
                            <button class="menu-buttons" onclick={() => {JoinLobby(code)}}>Join Lobby</button>
                        </div>
                    </div>
                </div>

                <div style="width: 50%; height: 100%;">
                    <div style="width: 100%; height: 100%; display: flex; flex-direction: row; align-items: center;">
                        <div style="width: 100%; height: 50%; display: flex; justify-content: center; align-items: center;">
                            <button class="menu-buttons" style="height: 215px;" onclick={HostLobby}>Host Lobby</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<head>
    <link rel="stylesheet" href = "https://fonts.googleapis.com/css2?family=Inter|SN+Pro">
</head>
<style>
    
    #body {
        background-image: url("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.wallpapersden.com%2Fimage%2Fdownload%2Fabstract-wave-hd-blue_bWZnbm6UmZqaraWkpJRoaWprrWdnaGk.jpg&f=1&nofb=1&ipt=98a6a5de7c02caa8d4320c8166d916e52e7e383d4bd86c46b61b3477f8762847");
        background-size: cover;
        width: 100vw; 
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    #container {
        width: 80%; 
        height: 80%; 
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(30px);
    }

    #code {
        width: 350px;
        height: 100px;
        font-size: 30px;
        text-align: center;
        margin-bottom: 10px;
        border-radius: 15px;
    }

    #site-name {
        margin: 5% 0 2% 0;
        font-size: 85px;
        text-align: center;
    }

    #site-description {
        margin: 0 10% 3% 10%;
        text-align: center;
        font-family: "Montserrat";
        font-size: 35px;
    }
    
    .menu-buttons {
        background-color: rgb(124,185,232);
        border-color: rgb(36, 23, 1);
        border-style: solid;
        border-radius: 20px;
        width: 350px;
        height: 100px;
        bottom: 0px;
        position: relative;
        transition: 
            background-color ease 0.3s, 
            box-shadow ease-out 0.15s,
            bottom ease-out 0.1s;
        outline: none;
        font-family: "Montserrat", sans-serif;
        font-size: 30px;
    }

    .menu-buttons:hover {
        background-color: rgb(201,255,229);
        box-shadow: 0 8px 15px rgb(161,161,161);
        bottom: 3px;
    }
</style>
