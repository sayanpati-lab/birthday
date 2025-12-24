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

/* INTRO SCREEN */
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
}
@keyframes pulse {from{opacity:.6}to{opacity:1}}

h1 {
  margin-top:50px;
  font-size:3.5rem;
  color:#00fff7;
  text-shadow:0 0 10px #00fff7,0 0 40px #ff00ff;
}
h2 {
  color:#ff66ff;
  margin-bottom:90px;
  text-shadow:0 0 15px #ff00ff;
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

.layer {
  position:absolute;
  height:70px;
  border-radius:15px;
}
.l1 {bottom:0;width:240px;background:linear-gradient(45deg,#ff0080,#ff8c00)}
.l2 {bottom:70px;width:190px;left:25px;background:linear-gradient(45deg,#00f260,#0575e6)}
.l3 {bottom:140px;width:140px;left:50px;background:linear-gradient(45deg,#8e2de2,#4a00e0)}

.candle {
  position:absolute;
  top:-50px;
  left:110px;
  width:22px;
  height:50px;
  background:white;
  border-radius:6px;
}
.flame {
  position:absolute;
  top:-28px;
  left:4px;
  width:14px;
  height:26px;
  background:radial-gradient(circle,yellow,orange,red);
  border-radius:50%;
  animation:flicker .35s infinite alternate;
}
@keyframes flicker {to{transform:scale(1.4)}}

/* CONFETTI */
.confetti {
  position:fixed;
  width:8px;
  height:8px;
  animation:fall linear infinite;
}
@keyframes fall {to{transform:translateY(110vh) rotate(360deg)}}

/* FIREWORK */
.firework {
  position:absolute;
  width:6px;
  height:6px;
  border-radius:50%;
  animation:boom 1.2s forwards;
}
@keyframes boom {to{transform:scale(9);opacity:0}}

/* HEART */
.heart {
  position:absolute;
  font-size:22px;
  animation:heart 2s forwards;
}
@keyframes heart {to{transform:translateY(-120px);opacity:0}}

#msg {
  position:fixed;
  bottom:20px;
  left:50%;
  transform:translateX(-50%);
  background:#111;
  color:#fff;
  padding:12px 25px;
  border-radius:20px;
  box-shadow:0 0 20px #ff00ff;
}
</style>
</head>

<body>

<div id="intro">✨ Tap to Start ✨</div>

<h1>🎉 Happy Birthday Arpita 🎂</h1>
<h2>@_.bubblixie._ 💖</h2>

<div class="cake" id="cake">
  <div class="layer l3"></div>
  <div class="layer l2"></div>
  <div class="layer l1"></div>
  <div class="candle"><div class="flame" id="flame"></div></div>
</div>

<div id="msg">🎁 May your life glow brighter every year 💫</div>

<audio id="song" loop>
  <source src="https://www.soundjay.com/human/sounds/happy-birthday-song-01.mp3">
</audio>

<script>
/* INTRO + MUSIC */
const song = document.getElementById("song");
document.getElementById("intro").onclick = () => {
  document.getElementById("intro").style.display="none";
  song.volume = 0;
  song.play();
  let v = 0;
  let fade = setInterval(() => {
    v += 0.05;
    song.volume = v;
    if (v >= 1) clearInterval(fade);
  }, 150);
};

/* CONFETTI */
for(let i=0;i<100;i++){
 let c=document.createElement("div");
 c.className="confetti";
 c.style.left=Math.random()*innerWidth+"px";
 c.style.background=`hsl(${Math.random()*360},100%,60%)`;
 c.style.animationDuration=3+Math.random()*3+"s";
 document.body.appendChild(c);
}

/* FIREWORKS ABOVE CAKE */
const cake=document.getElementById("cake");
setInterval(()=>{
 let r=cake.getBoundingClientRect();
 let f=document.createElement("div");
 f.className="firework";
 f.style.left=r.left+r.width/2+(Math.random()*200-100)+"px";
 f.style.top=r.top-150-Math.random()*120+"px";
 f.style.background=`hsl(${Math.random()*360},100%,60%)`;
 document.body.appendChild(f);
 setTimeout(()=>f.remove(),1200);
},600);

/* HEARTS */
setInterval(()=>{
 let h=document.createElement("div");
 h.className="heart";
 h.innerHTML="💖";
 h.style.left=Math.random()*innerWidth+"px";
 h.style.top=innerHeight-50+"px";
 document.body.appendChild(h);
 setTimeout(()=>h.remove(),2000);
},1200);

/* MIC BLOW TO TURN OFF CANDLE */
navigator.mediaDevices.getUserMedia({audio:true}).then(stream=>{
 const ctx=new AudioContext();
 const mic=ctx.createMediaStreamSource(stream);
 const analyser=ctx.createAnalyser();
 mic.connect(analyser);
 let data=new Uint8Array(analyser.frequencyBinCount);
 setInterval(()=>{
   analyser.getByteFrequencyData(data);
   if(Math.max(...data)>200){
     document.getElementById("flame").style.display="none";
   }
 },200);
});
</script>

</body>
</html>
"""

components.html(birthday_html, height=1200, scrolling=False)
