import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🎂 Happy Birthday", layout="centered")

birthday_html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background: radial-gradient(circle, #ff9a9e, #fad0c4);
    text-align: center;
    font-family: Comic Sans MS;
    overflow: hidden;
}

h1 {
    color: white;
    font-size: 3rem;
    text-shadow: 0 0 20px yellow;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px white; }
    to { text-shadow: 0 0 30px yellow; }
}

/* Cake */
.cake {
    position: relative;
    margin: 50px auto;
    width: 200px;
    height: 200px;
}

.layer {
    position: absolute;
    width: 200px;
    height: 60px;
    border-radius: 10px;
}

.l1 { bottom: 0; background: #ff6f61; }
.l2 { bottom: 60px; background: #ffcc5c; width: 170px; left: 15px; }
.l3 { bottom: 120px; background: #88d8b0; width: 140px; left: 30px; }

.candle {
    position: absolute;
    top: -40px;
    left: 90px;
    width: 20px;
    height: 40px;
    background: white;
}

.flame {
    position: absolute;
    top: -20px;
    left: 3px;
    width: 14px;
    height: 20px;
    background: orange;
    border-radius: 50%;
    animation: flicker 0.5s infinite alternate;
}

@keyframes flicker {
    from { transform: scale(1); opacity: 0.8; }
    to { transform: scale(1.2); opacity: 1; }
}

button {
    padding: 12px 25px;
    font-size: 18px;
    background: #ff4081;
    color: white;
    border: none;
    border-radius: 25px;
    cursor: pointer;
}

/* Confetti */
.confetti {
    position: fixed;
    width: 10px;
    height: 10px;
    animation: fall linear infinite;
}

@keyframes fall {
    from { transform: translateY(-100px) rotate(0deg); }
    to { transform: translateY(100vh) rotate(360deg); }
}
</style>
</head>

<body>

<h1>🎉 Happy Birthday Sayan 🎂</h1>

<div class="cake">
    <div class="layer l3"></div>
    <div class="layer l2"></div>
    <div class="layer l1"></div>
    <div class="candle"><div class="flame"></div></div>
</div>

<button onclick="document.getElementById('song').play()">▶ Play Birthday Song</button>

<audio id="song">
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3">
</audio>

<script>
for (let i = 0; i < 120; i++) {
    let c = document.createElement("div");
    c.className = "confetti";
    c.style.left = Math.random() * window.innerWidth + "px";
    c.style.backgroundColor = `hsl(${Math.random()*360},100%,50%)`;
    c.style.animationDuration = (Math.random()*3+2) + "s";
    document.body.appendChild(c);
}
</script>

</body>
</html>
"""

components.html(birthday_html, height=800, scrolling=False)
