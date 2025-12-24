import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🎉 Happy Birthday Arpita",
    layout="centered"
)

birthday_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Happy Birthday Arpita</title>

<style>
body {
    margin: 0;
    padding: 0;
    background: radial-gradient(circle at bottom, #0f2027, #203a43, #2c5364);
    font-family: 'Comic Sans MS', cursive;
    text-align: center;
    overflow: hidden;
}

/* Neon Text */
h1 {
    margin-top: 30px;
    font-size: 3.2rem;
    color: #00fff7;
    text-shadow:
        0 0 5px #00fff7,
        0 0 10px #00fff7,
        0 0 20px #00fff7,
        0 0 40px #ff00ff;
    animation: neonPulse 2s infinite alternate;
}

@keyframes neonPulse {
    from { opacity: 0.8; }
    to { opacity: 1; }
}

h2 {
    color: #ffb6ff;
    text-shadow: 0 0 10px #ff00ff;
}

/* Cake */
.cake {
    position: relative;
    width: 220px;
    height: 220px;
    margin: 50px auto;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.layer {
    position: absolute;
    width: 220px;
    height: 65px;
    border-radius: 12px;
}

.layer1 { bottom: 0; background: linear-gradient(45deg, #ff0080, #ff8c00); }
.layer2 { bottom: 65px; width: 180px; left: 20px; background: linear-gradient(45deg, #00f260, #0575e6); }
.layer3 { bottom: 130px; width: 140px; left: 40px; background: linear-gradient(45deg, #8e2de2, #4a00e0); }

/* Candle */
.candle {
    position: absolute;
    top: -40px;
    left: 100px;
    width: 20px;
    height: 40px;
    background: white;
    border-radius: 5px;
}

.flame {
    position: absolute;
    top: -22px;
    left: 3px;
    width: 14px;
    height: 22px;
    background: radial-gradient(circle, yellow, orange, red);
    border-radius: 50%;
    animation: flicker 0.4s infinite alternate;
}

@keyframes flicker {
    from { transform: scale(1); opacity: 0.7; }
    to { transform: scale(1.3); opacity: 1; }
}

/* Button */
button {
    padding: 14px 30px;
    font-size: 18px;
    background: linear-gradient(45deg, #ff00ff, #00ffff);
    color: black;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    box-shadow: 0 0 20px #00ffff;
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
    to { transform: translateY(110vh) rotate(360deg); }
}

/* Fireworks */
.firework {
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    animation: explode 1.5s infinite;
}

@keyframes explode {
    0% { transform: scale(0); opacity: 1; }
    100% { transform: scale(8); opacity: 0; }
}
</style>
</head>

<body>

<h1>🎉 Happy Birthday Arpita 🎂</h1>
<h2>@_.bubblixie._ ✨</h2>

<div class="cake">
    <div class="layer layer3"></div>
    <div class="layer layer2"></div>
    <div class="layer layer1"></div>
    <div class="candle"><div class="flame"></div></div>
</div>

<button onclick="document.getElementById('song').play()">▶ Play Birthday Song</button>

<audio id="song">
    <source src="https://www.soundjay.com/human/sounds/happy-birthday-song-01.mp3" type="audio/mp3">
</audio>

<script>
// Confetti
for (let i = 0; i < 150; i++) {
    let c = document.createElement("div");
    c.className = "confetti";
    c.style.left = Math.random() * window.innerWidth + "px";
    c.style.backgroundColor = `hsl(${Math.random()*360},100%,50%)`;
    c.style.animationDuration = (Math.random()*3+2) + "s";
    document.body.appendChild(c);
}

// Fireworks
setInterval(() => {
    let f = document.createElement("div");
    f.className = "firework";
    f.style.left = Math.random() * window.innerWidth + "px";
    f.style.top = Math.random() * window.innerHeight + "px";
    f.style.background = `hsl(${Math.random()*360},100%,50%)`;
    document.body.appendChild(f);
    setTimeout(() => f.remove(), 1500);
}, 500);
</script>

</body>
</html>
"""

components.html(birthday_html, height=1000, scrolling=False)
