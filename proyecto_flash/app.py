from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>⚡ Flash ⚡</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      background: radial-gradient(circle at center, #1e0002 0%, #060001 100%);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      position: relative;
    }

    /* Rayos en pantalla */
    .lightning-bg {
      position: absolute;
      inset: 0;
      background: #ffe600;
      opacity: 0;
      pointer-events: none;
      animation: lightning 0.35s ease-out 0.5s 2;
    }

    @keyframes lightning {
      0% { opacity: 0; }
      50% { opacity: 0.85; }
      100% { opacity: 0; }
    }

    /* Estela de velocidad roja y dorada */
    .speed-trail {
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 10px;
      background: linear-gradient(90deg, transparent, #ffea00, #ff1e00, transparent);
      opacity: 0;
      box-shadow: 0 0 30px #ffea00, 0 0 60px #ff1e00;
      animation: trail 1.2s ease-out 0.5s forwards;
    }

    /* 1. Flash cruzando volando a toda velocidad */
    .runner-first-pass {
      position: absolute;
      top: calc(50% - 70px);
      left: -200px;
      width: 140px;
      height: auto;
      z-index: 10;
      filter: drop-shadow(0 0 20px #ffea00) drop-shadow(-40px 0 15px #e50914);
      animation: sprintAcross 1.1s cubic-bezier(0.25, 1, 0.5, 1) 0.4s forwards;
    }

    @keyframes sprintAcross {
      0% {
        left: -200px;
        transform: skewX(-20deg) scale(0.9);
      }
      100% {
        left: 130vw;
        transform: skewX(-30deg) scale(1.1);
      }
    }

    @keyframes trail {
      0% { opacity: 0; }
      40% { opacity: 1; transform: scaleY(2.5); }
      100% { opacity: 0; transform: scaleY(0.5); }
    }

    /* Tarjeta del mensaje */
    .card {
      text-align: center;
      padding: 20px;
      opacity: 0;
      transform: scale(0.6);
      animation: popMessage 0.9s cubic-bezier(0.175, 0.885, 0.32, 1.275) 1.2s forwards;
      z-index: 5;
    }

    .badge {
      display: inline-block;
      margin-bottom: 12px;
      padding: 5px 16px;
      background: rgba(255, 234, 0, 0.15);
      border: 1px solid #ffea00;
      border-radius: 999px;
      color: #ffea00;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
    }

    .text {
      color: #ffffff;
      font-size: 2.1rem;
      font-weight: 800;
      line-height: 1.35;
      text-shadow: 0 0 15px rgba(255, 30, 0, 0.8), 0 0 35px rgba(255, 234, 0, 0.5);
    }

    .heart {
      display: inline-block;
      color: #ff1e42;
      font-size: 3.2rem;
      margin-top: 10px;
      filter: drop-shadow(0 0 15px #ff1e42);
      animation: beat 1.1s infinite ease-in-out 1.8s;
    }

    @keyframes popMessage {
      to {
        opacity: 1;
        transform: scale(1);
      }
    }

    @keyframes beat {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.25); }
    }

    /* 2. Flash vuelve por abajo y se queda patrullando */
    .flash-bottom-container {
      position: absolute;
      bottom: -150px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10;
      display: flex;
      flex-direction: column;
      align-items: center;
      animation: enterFromBottom 1s cubic-bezier(0.2, 0.8, 0.2, 1) 2.2s forwards;
    }

    @keyframes enterFromBottom {
      to {
        bottom: 25px;
      }
    }

    /* Flash corriendo animado */
    .flash-character-img {
      width: 130px;
      height: auto;
      filter: drop-shadow(0 0 15px rgba(255, 234, 0, 0.8)) drop-shadow(0 0 30px rgba(255, 30, 0, 0.6));
      animation: patrolRun 3s infinite alternate ease-in-out 3.2s;
    }

    /* Patrulla de lado a lado por la base */
    @keyframes patrolRun {
      0% {
        transform: translateX(-40px) scaleX(1);
      }
      48% {
        transform: translateX(40px) scaleX(1);
      }
      50% {
        transform: translateX(40px) scaleX(-1);
      }
      98% {
        transform: translateX(-40px) scaleX(-1);
      }
      100% {
        transform: translateX(-40px) scaleX(1);
      }
    }

    .speedforce-ground {
      width: 140px;
      height: 4px;
      margin-top: -6px;
      background: radial-gradient(circle, #ffe600 0%, #ff1e00 60%, transparent 100%);
      box-shadow: 0 0 15px #ffe600, 0 0 25px #ff1e00;
      animation: energyPulse 0.4s infinite alternate ease-in-out 3.2s;
    }

    @keyframes energyPulse {
      0% { opacity: 0.5; transform: scaleX(0.8); }
      100% { opacity: 1; transform: scaleX(1.3); }
    }
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>

  <!-- Primer Flash que pasa corriendo en el medio -->
  <img class="runner-first-pass" src="https://media.giphy.com/media/26hirEPeos6yugLDO/giphy.gif" alt="Flash corriendo">

  <!-- Mensaje de amor -->
  <div class="card">
    <div class="badge">A la velocidad de la luz</div>
    <div class="text">
      te amo muuuucho<br>mi amor
    </div>
    <div class="heart">♥</div>
  </div>

  <!-- Flash real que entra por abajo y se queda corriendo con estela -->
  <div class="flash-bottom-container">
    <img class="flash-character-img" src="https://media.giphy.com/media/26hirEPeos6yugLDO/giphy.gif" alt="Flash patrullando">
    <div class="speedforce-ground"></div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)