import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🎉 Happy Birthday Arpita", layout="centered")

birthday_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Happy Birthday Arpita</title>

<style>
body {
  margin:0;
  background:black;
  font-family:'Comic Sans MS', cursive;
  overflow:hidden;
  text-align:center;
}

/* INTRO */
#intro {
  position:fixed;
  inset:0;
  background:black;
  display:flex;
  justify-content:center;
  align-items:center;
  z-index:999;
  color:#00fff7;
  font-size:2.2rem;
  text-shadow:0 0 20px #00fff7,0 0 40px #ff00ff;
  animation:pulse 1.5s infinite alternate;
  cursor:pointer;
}
@keyframes pulse {from{opacity:.6}to{opacity:1}}

h1 {
  margin-top:40px;
  font-size:3.5rem;
  color:#00fff7;
  text-shadow:0 0 10px #00fff7,0 0 40px #ff00ff;
}
h2 {
  color:#ff66ff;
  margin-bottom:25px;
  text-shadow:0 0 15px #ff00ff;
}

/* WISH */
#wish {
  max-width:600px;
  margin: 0 auto 60px auto;
  color:white;
  font-size:1.1rem;
  line-height:1.6;
  text-shadow:0 0 10px rgba(255,255,255,0.6);
}

/* CAKE */
.cake {
  position:relative;
  width:240px;
  height:240px;
  margin:auto;
  animation:float 3s ease-in-out infinite;
}
@keyframes float {50%{transform:translateY(-15px)}}

/* CAKE GLOW */
@keyframes cakeGlow {
  from { box-shadow: 0 0 10px rgba(255,255,255,0.4); }
  to   { box-shadow: 0 0 35px rgba(255,255,255,1); }
}

.layer {
  position:absolute;
  height:70px;
  border-radius:15px;
  animation:cakeGlow 2s infinite alternate;
}

.l1 {
  bottom:0;
  width:240px;
  background:linear-gradient(45deg,#ff0080,#ff8c00);
  box-shadow:0 0 25px #ff0080,0 0 45px #ff8c00;
}
.l2 {
  bottom:70px;
  width:190px;
  left:25px;
  background:linear-gradient(45deg,#00f260,#0575e6);
  box-shadow:0 0 25px #00f260,0 0 45px #0575e6;
}
.l3 {
  bottom:140px;
  width:140px;
  left:50px;
  background:linear-gradient(45deg,#8e2de2,#4a00e0);
  box-shadow:0 0 25px #8e2de2,0 0 45px #4a00e0;
}

/* CANDLE */
.candle {
  position:absolute;
  top:-50px;
  left:110px;
  width:22px;
  height:50px;
  background:white;
  border-radius:6px;
  animation:candleGlow 1.5s infinite alternate;
}
@keyframes candleGlow {
  from { box-shadow:0 0 10px white; }
  to   { box-shadow:0 0 30px white,0 0 50px #ffff99; }
}

/* FLAME */
.flame {
  position:absolute;
  top:-28px;
  left:4px;
  width:14px;
  height:26px;
  background:radial-gradient(circle,yellow,orange,red);
  border-radius:50%;
  animation:flicker .35s infinite alternate;
  box-shadow:0 0 25px orange,0 0 45px red;
}
@keyframes flicker {to{transform:scale(1.5)}}

/* STARS */
.star {
  position:fixed;
  width:3px;
  height:3px;
  background:white;
  border-radius:50%;
  animation:twinkle 2s infinite alternate;
}
@keyframes twinkle {from{opacity:.3}to{opacity:1}}

/* HEARTS */
.heart {
  position:fixed;
  font-size:20px;
  color:#ff66ff;
  animation:floatHeart 3s linear forwards;
  text-shadow:0 0 10px #ff00ff;
}
@keyframes floatHeart {
  from { transform:translateY(0); opacity:1; }
  to { transform:translateY(-150px); opacity:0; }
}

/* BUTTON */
.play-btn {
  margin-top:25px;
  padding:10px 22px;
  border-radius:20px;
  background:#ff00ff;
  color:white;
  border:none;
  font-size:16px;
  box-shadow:0 0 15px #ff00ff;
  cursor:pointer;
}
</style>
</head>

<body>

<div id="intro">✨ Tap to Start ✨</div>

<h1>🎉 Happy Birthday Arpita 🎂</h1>
<h2>@_.bubblixie._ 💖</h2>

<div id="wish">
  May your birthday be as bright and magical as your smile,<br>
  and may every dream you carry find its way to reality.<br>
  May this year bring you love, laughter, and endless joy,<br>
  with success lighting your path wherever you go.<br>
  Keep shining — the world is better with you in it. ✨
</div>

<div class="cake">
  <div class="layer l3"></div>
  <div class="layer l2"></div>
  <div class="layer l1"></div>
  <div class="candle"><div class="flame"></div></div>
</div>

<button class="play-btn" onclick="playMusic()">🎵 Play Music</button>

<!-- SAME MUSIC AS SUMEET -->
<audio id="song" loop controls style="display:none">
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
</audio>

<script>
const song = document.getElementById("song");

/* INTRO CLICK */
document.getElementById("intro").onclick = async () => {
  document.getElementById("intro").style.display="none";
  await playMusic();
};

/* PLAY MUSIC */
async function playMusic() {
  try {
    song.volume = 1;
    await song.play();
  } catch (e) {
    console.log("Playback blocked:", e);
  }
}

/* STARS */
for(let i=0;i<120;i++){
  let s=document.createElement("div");
  s.className="star";
  s.style.left=Math.random()*innerWidth+"px";
  s.style.top=Math.random()*innerHeight+"px";
  s.style.animationDuration=(1+Math.random()*2)+"s";
  document.body.appendChild(s);
}

/* HEARTS */
setInterval(()=>{
  let h=document.createElement("div");
  h.className="heart";
  h.innerHTML="💖";
  h.style.left=Math.random()*innerWidth+"px";
  h.style.top=innerHeight+"px";
  document.body.appendChild(h);
  setTimeout(()=>h.remove(),3000);
},800);
</script>

</body>
</html>
"""

components.html(birthday_html, height=1300, scrolling=False)
