<script lang="ts">
    import { io } from "socket.io-client";

    const socket = io("http://localhost:5000",{
    auth: {
        id: "a0472aba-6249-4e24-8baf-711e85d7a58b"
    }
    });

    socket.on("connect", () => {
    socket.emit("create_game", ({status, game_code, name}) => {
        console.log(status, game_code, name);

        socket.emit("set_name", "awesomename");
    });
    });

</script>

<div id="body">
    <div id="site-modal">
        <div class="column-layout">
            <p id="site-name">Site Name</p>
            <p id="site-description">Harness the potential of competitive group studying to solidify your mathematical foundations! Choose an option below:</p>
        </div>

        <div id="site-buttons">
            <div class="site-rows">
                <div class="column-layout">
                    <input type="text" name="code" id="code" placeholder="Enter the code">
                </div>
                <div class="column-layout">
                    <button class="menu-buttons">Join Lobby</button>
                </div>
            </div>

            <div class="site-rows">
                <button class="menu-buttons">Host Lobby</button>
            </div>
        </div>

        <!-- <div id="site-components">
            <p id="site-name">Site Name</p>
            <p id="site-description">Harness the potential of competitive group studying to solidify your mathematical foundations! Choose an option below:</p>
        </div>
        <div id="site-components">
            <button class="menu-buttons">Join Lobby</button>
            <button class="menu-buttons">Host Lobby</button>
        </div> -->
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    #body {
        background-image: url("https://www.hdwallpapers.in/download/aerial_view_of_ocean_foam_waves_coast_white_beach_sand_hd_ocean-1920x1080.jpg");
        width: 100vw; 
        height: 100vh;
    }

    #site-modal {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: auto;
        width: 85vw;
        height: 80vh;
        transform: translateY(10vh);
        background-color: rgba(255,255,255,0.15);
        backdrop-filter: blur(30px);
        outline: solid;
        outline-width: 3px;
        border-radius: 15px;
    }
    
    /* 
    #site-components {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 50vw;
    } */

    .column-layout {
        width: 100%; 
        height: 50%;
        display: flex;
        flex-direction: column;
    }

    #site-buttons {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
    }
    
    .site-rows {
        width: 50%;
        height: 100%;
    }

    #site-name {
        margin: 5% 0 2% 0;
        font-size: 65px;
        text-align: center;
    }

    #site-description {
        margin: 0 0 3% 0;
        text-align: center;
        font-family: "Montserrat";
        font-size: 25px;
    }
    
    .menu-buttons {
        background-color: rgb(124,185,232);
        width: 350px;
        height: 100px;
        position: relative;
        bottom: 0px;
        transition: 
            background-color ease 0.3s, 
            box-shadow ease-out 0.15s,
            bottom ease-out 0.1s;
        outline: none;
        font-family: "Montserrat", sans-serif;
        font-size: 30px;
        display: block;
        margin: 0 auto 20% auto;
    }

    .menu-buttons:hover {
        background-color: rgb(201,255,229);
        box-shadow: 0 8px 15px rgb(161,161,161);
        bottom: 3px;
    }
</style>