import streamlit as st
import streamlit.components.v1 as components

# CSS content from your style.css file
css_content = """
body {
    text-align: center;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    background-color: #f0f0f0;
}
.game-container {
    margin: auto;
    width: 60%;
    padding: 10px;
}
.door-container {
    display: inline-block;
    margin: 10px;
}
.door {
    cursor: pointer;
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
}
.door-label {
    margin-top: 8px;
}
#restart-button {
    margin-top: 20px;
    font-size: 20px;
    padding: 10px 20px;
    background-color: #008CBA; /* Blue */
}
"""

# JavaScript content for game logic
js_content = """
let prizeDoor = Math.floor(Math.random() * 3) + 1;
let selectedDoor = 0;
let goatRevealed = false;

function chooseDoor(doorNumber) {
    if (!goatRevealed) {
        for (let i = 1; i <= 3; i++) {
            if (i !== prizeDoor && i !== doorNumber) {
                document.getElementById('door' + i).children[0].src = "goat.jpg";
                goatRevealed = true;
                break;
            }
        }
        selectedDoor = doorNumber;
        document.getElementById('game-message').innerText = "Would you like to switch your choice?";
    } else {
        revealAllDoors();
        if (doorNumber === prizeDoor) {
            document.getElementById('game-message').innerText = "You won a car!";
        } else {
            document.getElementById('game-message').innerText = "Sorry, it's a goat. You lose!";
        }
        document.getElementById('restart-button').style.display = 'block';
    }
}

function revealAllDoors() {
    for (let i = 1; i <= 3; i++) {
        let imgSrc = i === prizeDoor ? "car.jpg" : "goat.jpg";
        document.getElementById('door' + i).children[0].src = imgSrc;
    }
}

function restartGame() {
    window.location.reload();
}
"""

# Embedding the CSS and JS within the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monty Hall Game for Kids</title>
    <style>
        {css_content}
    </style>
</head>
<body>
    <h1>Monty Hall Game for Kids</h1>
    <div class="game-container">
        <div class="door-container">
            <div class="door" id="door1" onclick="chooseDoor(1)">
                <img src="door.jpg" alt="Door 1" class="door-image">
                <div class="door-label">Door 1</div>
            </div>
            <div class="door" id="door2" onclick="chooseDoor(2)">
                <img src="door.jpg" alt="Door 2" class="door-image">
                <div class="door-label">Door 2</div>
            </div>
            <div class="door" id="door3" onclick="chooseDoor(3)">
                <img src="door.jpg" alt="Door 3" class="door-image">
                <div class="door-label">Door 3</div>
            </div>
        </div>
    </div>
    <div id="game-message"></div>
    <button id="restart-button" onclick="restartGame()" style="display:none;">Restart Game</button>
    <script>{js_content}</script>
</body>
</html>
"""

def main():
    # Display the HTML content with embedded CSS and JS
    components.html(html_content, width=None, height=None, scrolling=True)

if __name__ == "__main__":
    main()
