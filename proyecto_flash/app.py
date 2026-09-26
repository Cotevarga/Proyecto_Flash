from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>⚡ Flash ⚡</title>
  <style>
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: radial-gradient(circle at center, #240002 0%, #060001 100%);
      min-height: 100vh;
      min-height: 100dvh; /* Altura dinámica exacta para navegadores móviles */
      width: 100%;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      padding: clamp(16px, 4vh, 32px) clamp(16px, 5vw, 24px);
      position: relative;
    }

    /* Destello inicial de relámpago */
    .lightning-bg {
      position: fixed;
      inset: 0;
      background: #ffe600;
      opacity: 0;
      pointer-events: none;
      animation: lightning 0.35s ease-out 0.4s 2;
      z-index: 1;
    }

    @keyframes lightning {
      0% { opacity: 0; }
      50% { opacity: 0.9; }
      100% { opacity: 0; }
    }

    /* Estela de velocidad roja y dorada */
    .speed-trail {
      position: absolute;
      top: 45%;
      left: 0;
      width: 100%;
      height: 6px;
      background: linear-gradient(90deg, transparent, #ffe600, #c62828, transparent);
      opacity: 0;
      box-shadow: 0 0 25px #ffe600, 0 0 50px #c62828;
      animation: trail 1s ease-out 0.4s forwards;
      z-index: 2;
    }

    @keyframes trail {
      0% { opacity: 0; }
      40% { opacity: 1; transform: scaleY(2.2); }
      100% { opacity: 0; transform: scaleY(0.5); }
    }

    /* 1. Flash cruzando volando a toda velocidad */
    .flash-first-pass {
      position: absolute;
      top: calc(45% - clamp(40px, 8vh, 60px));
      left: -180px;
      width: clamp(90px, 25vw, 130px);
      height: clamp(90px, 25vw, 130px);
      z-index: 10;
      filter: drop-shadow(0 0 15px #ffe600) drop-shadow(-30px 0 10px #c62828);
      animation: sprintAcross 1s cubic-bezier(0.25, 1, 0.5, 1) 0.3s forwards;
    }

    @keyframes sprintAcross {
      0% {
        left: -180px;
        transform: skewX(-20deg) scale(0.9);
      }
      100% {
        left: 125vw;
        transform: skewX(-30deg) scale(1.05);
      }
    }

    /* Espacio superior para balancear el contenido */
    .spacer-top {
      height: 10px;
      flex-shrink: 0;
    }

    /* Contenedor central del mensaje */
    .card {
      text-align: center;
      width: 100%;
      max-width: 480px;
      margin: auto 0;
      padding: 0 clamp(8px, 2vw, 16px);
      opacity: 0;
      transform: scale(0.7);
      animation: popMessage 0.9s cubic-bezier(0.175, 0.885, 0.32, 1.275) 1.2s forwards;
      z-index: 5;
    }

    /* Insignia / frase superior que se acomoda en varias líneas */
    .badge {
      display: inline-block;
      margin-bottom: clamp(14px, 3vh, 22px);
      padding: clamp(8px, 2vh, 12px) clamp(12px, 4vw, 20px);
      background: rgba(255, 230, 0, 0.12);
      border: 1px solid rgba(255, 230, 0, 0.7);
      border-radius: 20px;
      color: #ffe600;
      font-size: clamp(0.75rem, 3.4vw, 0.95rem);
      font-weight: 600;
      letter-spacing: 0.5px;
      line-height: 1.45;
      text-shadow: 0 0 8px rgba(255, 230, 0, 0.4);
      max-width: 100%;
      word-wrap: break-word;
    }

    /* Título principal adaptativo */
    .text {
      color: #ffffff;
      font-size: clamp(1.7rem, 7.5vw, 2.6rem);
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: 0.5px;
      text-shadow: 0 0 15px rgba(229, 9, 20, 0.85), 0 0 30px rgba(255, 230, 0, 0.45);
    }

    /* Corazón latiendo */
    .heart {
      display: inline-block;
      color: #ff1744;
      font-size: clamp(2.4rem, 9vw, 3.4rem);
      margin-top: clamp(8px, 2vh, 14px);
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
      50% { transform: scale(1.22); }
    }

    /* 2. Logo oficial de Flash abajo */
    .flash-logo-container {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transform: translateY(40px);
      animation: enterLogo 0.9s cubic-bezier(0.2, 0.8, 0.2, 1) 1.9s forwards;
      z-index: 5;
      margin-top: auto;
      padding-bottom: clamp(6px, 2vh, 16px);
      flex-shrink: 0;
    }

    @keyframes enterLogo {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .flash-logo-svg {
      width: clamp(55px, 15vw, 75px);
      height: clamp(55px, 15vw, 75px);
      filter: drop-shadow(0 0 15px #ffe600) drop-shadow(0 0 30px #c62828);
      animation: logoPulse 2s infinite ease-in-out 2.8s;
    }

    @keyframes logoPulse {
      0%, 100% {
        transform: scale(1);
        filter: drop-shadow(0 0 12px #ffe600) drop-shadow(0 0 25px #c62828);
      }
      50% {
        transform: scale(1.08);
        filter: drop-shadow(0 0 22px #ffe600) drop-shadow(0 0 40px #ffe600);
      }
    }

    .energy-ring {
      width: clamp(75px, 22vw, 110px);
      height: 3px;
      margin-top: 6px;
      background: radial-gradient(circle, #ffe600 0%, #c62828 60%, transparent 100%);
      box-shadow: 0 0 12px #ffe600, 0 0 20px #c62828;
      animation: ringGlow 0.4s infinite alternate ease-in-out 2.8s;
    }

    @keyframes ringGlow {
      0% { opacity: 0.35; transform: scaleX(0.7); }
      100% { opacity: 1; transform: scaleX(1.3); }
    }
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>

  <!-- Flash cruzando volando a toda velocidad -->
  <div class="flash-first-pass">
    <svg viewBox="0 0 120 120" width="100%" height="100%">
      <g stroke="#ffe600" stroke-width="2" fill="none">
        <path d="M 25 45 L 35 52 L 28 60 L 40 68" />
        <path d="M 50 15 L 42 25 L 48 30" />
      </g>
      <path d="M 46 62 Q 35 75 22 88" stroke="#9b0000" stroke-width="8" stroke-linecap="round" fill="none"/>
      <path d="M 22 88 L 12 90 L 18 96 Z" fill="#ffd700"/>
      <path d="M 54 62 Q 68 74 76 84" stroke="#d50000" stroke-width="8" stroke-linecap="round" fill="none"/>
      <path d="M 76 84 L 88 84 L 82 92 Z" fill="#ffd700"/>
      <path d="M 46 36 L 68 34 L 58 64 L 46 62 Z" fill="#d50000"/>
      <circle cx="56" cy="46" r="8" fill="#ffffff" stroke="#ffd700" stroke-width="1.8"/>
      <polygon points="57,40 51,47 55,47 53,53 60,45 56,45" fill="#ffd700"/>
      <ellipse cx="64" cy="24" rx="10" ry="12" fill="#d50000"/>
      <path d="M 64 27 Q 70 28 68 34 Q 63 35 62 31 Z" fill="#ffd0b0"/>
      <polygon points="56,23 48,19 53,26" fill="#ffd700"/>
      <polygon points="68,22 76,18 71,25" fill="#ffd700"/>
    </svg>
  </div>

  <div class="spacer-top"></div>

  <!-- Mensaje de amor responsivo -->
  <div class="card">
    <div class="badge">Toda mi vida estuve buscando lo imposible, jamás pensé que contigo lo encontraría.</div>
    <div class="text">
      Ti amo muuuucho<br>Mi amor
    </div>
    <div class="heart">♥</div>
  </div>

  <!-- Logo oficial de Flash abajo -->
  <div class="flash-logo-container">
    <div class="flash-logo-svg">
      <svg viewBox="0 0 100 100" width="100%" height="100%">
        <circle cx="50" cy="50" r="46" fill="#c62828" stroke="#ffe600" stroke-width="4"/>
        <circle cx="50" cy="50" r="38" fill="#ffffff"/>
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