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
      background: radial-gradient(circle at center, #220002 0%, #050000 100%);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      position: relative;
    }

    /* Destello de relámpago inicial */
    .lightning-bg {
      position: absolute;
      inset: 0;
      background: #ffe600;
      opacity: 0;
      pointer-events: none;
      animation: lightning 0.35s ease-out 0.4s 2;
    }

    @keyframes lightning {
      0% { opacity: 0; }
      50% { opacity: 0.9; }
      100% { opacity: 0; }
    }

    /* Estela de velocidad roja y dorada */
    .speed-trail {
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 8px;
      background: linear-gradient(90deg, transparent, #ffe600, #c62828, transparent);
      opacity: 0;
      box-shadow: 0 0 25px #ffe600, 0 0 50px #c62828;
      animation: trail 1.1s ease-out 0.4s forwards;
    }

    @keyframes trail {
      0% { opacity: 0; }
      40% { opacity: 1; transform: scaleY(2.2); }
      100% { opacity: 0; transform: scaleY(0.5); }
    }

    /* 1. Flash cruzando volando a toda velocidad */
    .flash-first-pass {
      position: absolute;
      top: calc(50% - 65px);
      left: -200px;
      width: 135px;
      height: 135px;
      z-index: 10;
      filter: drop-shadow(0 0 15px #ffe600) drop-shadow(-35px 0 10px #c62828);
      animation: sprintAcross 1s cubic-bezier(0.25, 1, 0.5, 1) 0.3s forwards;
    }

    @keyframes sprintAcross {
      0% {
        left: -200px;
        transform: skewX(-20deg) scale(0.95);
      }
      100% {
        left: 130vw;
        transform: skewX(-30deg) scale(1.1);
      }
    }

    /* Mensaje central */
    .card {
      text-align: center;
      padding: 24px;
      max-width: 90%;
      opacity: 0;
      transform: scale(0.6);
      animation: popMessage 0.9s cubic-bezier(0.175, 0.885, 0.32, 1.275) 1.2s forwards;
      z-index: 5;
    }

    .badge {
      display: inline-block;
      margin-bottom: 16px;
      padding: 8px 18px;
      background: rgba(255, 230, 0, 0.12);
      border: 1px solid #ffe600;
      border-radius: 999px;
      color: #ffe600;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 1px;
      line-height: 1.4;
      text-shadow: 0 0 10px rgba(255, 230, 0, 0.4);
    }

    .text {
      color: #ffffff;
      font-size: 2.2rem;
      font-weight: 800;
      line-height: 1.35;
      text-shadow: 0 0 15px rgba(229, 9, 20, 0.85), 0 0 30px rgba(255, 230, 0, 0.5);
    }

    .heart {
      display: inline-block;
      color: #ff1744;
      font-size: 3.2rem;
      margin-top: 10px;
      filter: drop-shadow(0 0 15px #ff1744);
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

    /* 2. Logo oficial de Flash abajo */
    .flash-logo-container {
      position: absolute;
      bottom: -150px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10;
      display: flex;
      flex-direction: column;
      align-items: center;
      animation: enterLogo 1s cubic-bezier(0.2, 0.8, 0.2, 1) 2s forwards;
    }

    @keyframes enterLogo {
      to {
        bottom: 30px;
      }
    }

    .flash-logo-svg {
      width: 75px;
      height: 75px;
      filter: drop-shadow(0 0 20px #ffe600) drop-shadow(0 0 35px #c62828);
      animation: logoPulse 2s infinite ease-in-out 3s;
    }

    @keyframes logoPulse {
      0%, 100% {
        transform: scale(1);
        filter: drop-shadow(0 0 15px #ffe600) drop-shadow(0 0 30px #c62828);
      }
      50% {
        transform: scale(1.1);
        filter: drop-shadow(0 0 25px #ffe600) drop-shadow(0 0 45px #ffe600);
      }
    }

    .energy-ring {
      width: 110px;
      height: 4px;
      margin-top: 6px;
      background: radial-gradient(circle, #ffe600 0%, #c62828 60%, transparent 100%);
      box-shadow: 0 0 15px #ffe600, 0 0 25px #c62828;
      animation: ringGlow 0.4s infinite alternate ease-in-out 3s;
    }

    @keyframes ringGlow {
      0% { opacity: 0.4; transform: scaleX(0.7); }
      100% { opacity: 1; transform: scaleX(1.3); }
    }
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>

  <!-- Flash cruzando a toda velocidad -->
  <div class="flash-first-pass">
    <svg viewBox="0 0 120 120" width="100%" height="100%">
      <!-- Rayos de energía -->
      <g stroke="#ffe600" stroke-width="2" fill="none">
        <path d="M 25 45 L 35 52 L 28 60 L 40 68" />
        <path d="M 50 15 L 42 25 L 48 30" />
      </g>
      <!-- Piernas y silueta veloz -->
      <path d="M 46 62 Q 35 75 22 88" stroke="#9b0000" stroke-width="8" stroke-linecap="round" fill="none"/>
      <path d="M 22 88 L 12 90 L 18 96 Z" fill="#ffd700"/>
      <path d="M 54 62 Q 68 74 76 84" stroke="#d50000" stroke-width="8" stroke-linecap="round" fill="none"/>
      <path d="M 76 84 L 88 84 L 82 92 Z" fill="#ffd700"/>
      <!-- Torso -->
      <path d="M 46 36 L 68 34 L 58 64 L 46 62 Z" fill="#d50000"/>
      <circle cx="56" cy="46" r="8" fill="#ffffff" stroke="#ffd700" stroke-width="1.8"/>
      <polygon points="57,40 51,47 55,47 53,53 60,45 56,45" fill="#ffd700"/>
      <!-- Máscara -->
      <ellipse cx="64" cy="24" rx="10" ry="12" fill="#d50000"/>
      <path d="M 64 27 Q 70 28 68 34 Q 63 35 62 31 Z" fill="#ffd0b0"/>
      <polygon points="56,23 48,19 53,26" fill="#ffd700"/>
      <polygon points="68,22 76,18 71,25" fill="#ffd700"/>
    </svg>
  </div>

  <!-- Mensaje de amor -->
  <div class="card">
    <div class="badge">Toda mi vida estuve buscando lo imposible, jamás pensé que contigo lo encontraría.</div>
    <div class="text">
      Ti amo muuuucho<br>Mi amor
    </div>
    <div class="heart">♥</div>
  </div>

  <!-- Logo oficial de Flash abajo con aura eléctrica -->
  <div class="flash-logo-container">
    <div class="flash-logo-svg">
      <svg viewBox="0 0 100 100" width="100%" height="100%">
        <!-- Círculo rojo exterior -->
        <circle cx="50" cy="50" r="46" fill="#c62828" stroke="#ffe600" stroke-width="4"/>
        <!-- Círculo interior blanco -->
        <circle cx="50" cy="50" r="38" fill="#ffffff"/>
        <!-- Rayo oficial de Flash atravesando el círculo -->
        <polygon points="53,10 32,52 48,50 42,90 73,42 54,44" fill="#ffd700" stroke="#f57f17" stroke-width="1.5"/>
      </svg>
    </div>
    <div class="energy-ring"></div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)