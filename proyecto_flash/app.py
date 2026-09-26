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
      background: radial-gradient(circle at center, #1b0000 0%, #050000 100%);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      position: relative;
    }

    /* Destello inicial de relámpago */
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
      background: rgba(255, 230, 0, 0.15);
      border: 1px solid #ffe600;
      border-radius: 999px;
      color: #ffe600;
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

    /* 2. Flash vuelve por abajo y se queda patrullando */
    .flash-bottom-zone {
      position: absolute;
      bottom: -160px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10;
      display: flex;
      flex-direction: column;
      align-items: center;
      animation: enterBottom 0.9s cubic-bezier(0.2, 0.8, 0.2, 1) 2.2s forwards;
    }

    @keyframes enterBottom {
      to {
        bottom: 25px;
      }
    }

    .flash-avatar {
      width: 125px;
      height: 125px;
      filter: drop-shadow(0 0 12px #ffe600) drop-shadow(0 0 25px #c62828);
      animation: patrol 3.5s infinite alternate ease-in-out 2.8s;
    }

    /* Movimiento de patrulla de izquierda a derecha */
    @keyframes patrol {
      0% {
        transform: translateX(-45px) scaleX(1);
      }
      48% {
        transform: translateX(45px) scaleX(1);
      }
      50% {
        transform: translateX(45px) scaleX(-1);
      }
      98% {
        transform: translateX(-45px) scaleX(-1);
      }
      100% {
        transform: translateX(-45px) scaleX(1);
      }
    }

    .speedforce-aura {
      width: 130px;
      height: 4px;
      margin-top: -6px;
      background: radial-gradient(circle, #ffe600 0%, #c62828 60%, transparent 100%);
      box-shadow: 0 0 15px #ffe600, 0 0 30px #c62828;
      animation: auraPulse 0.3s infinite alternate ease-in-out 2.8s;
    }

    @keyframes auraPulse {
      0% { opacity: 0.4; transform: scaleX(0.7); }
      100% { opacity: 1; transform: scaleX(1.3); }
    }

    /* Animación de carrera para las extremidades */
    .leg-back {
      transform-origin: 48px 62px;
      animation: legBackMove 0.26s infinite alternate ease-in-out;
    }
    .leg-front {
      transform-origin: 52px 62px;
      animation: legFrontMove 0.26s infinite alternate ease-in-out;
    }
    .arm-back {
      transform-origin: 46px 42px;
      animation: armBackMove 0.26s infinite alternate ease-in-out;
    }
    .arm-front {
      transform-origin: 58px 40px;
      animation: armFrontMove 0.26s infinite alternate ease-in-out;
    }
    .body-bob {
      animation: bobbing 0.13s infinite alternate ease-in-out;
    }
    .lightning-crack {
      animation: crackle 0.2s infinite alternate;
    }

    @keyframes legBackMove {
      0% { transform: rotate(-25deg); }
      100% { transform: rotate(35deg); }
    }
    @keyframes legFrontMove {
      0% { transform: rotate(30deg); }
      100% { transform: rotate(-30deg); }
    }
    @keyframes armBackMove {
      0% { transform: rotate(35deg); }
      100% { transform: rotate(-35deg); }
    }
    @keyframes armFrontMove {
      0% { transform: rotate(-35deg); }
      100% { transform: rotate(30deg); }
    }
    @keyframes bobbing {
      0% { transform: translateY(0px); }
      100% { transform: translateY(-3px); }
    }
    @keyframes crackle {
      0% { opacity: 0.2; }
      100% { opacity: 0.9; }
    }
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>

  <!-- Componente gráfico de Flash Barry Allen -->
  {% macro flash_figure() %}
  <svg viewBox="0 0 120 120" width="100%" height="100%">
    <!-- Rayos de electricidad Speed Force traseros -->
    <g class="lightning-crack" stroke="#ffe600" stroke-width="2" fill="none">
      <path d="M 25 45 L 35 52 L 28 60 L 40 68" />
      <path d="M 50 15 L 42 25 L 48 30" />
    </g>

    <!-- Pierna Trasera -->
    <g class="leg-back">
      <path d="M 46 62 Q 35 75 22 88" stroke="#9b0000" stroke-width="8" stroke-linecap="round" fill="none"/>
      <!-- Bota dorada -->
      <path d="M 22 88 L 12 90 L 18 96 Z" fill="#ffd700" stroke="#ffb300" stroke-width="1"/>
    </g>

    <!-- Brazo Trasero -->
    <g class="arm-back">
      <path d="M 46 42 Q 35 50 25 58" stroke="#9b0000" stroke-width="7" stroke-linecap="round" fill="none"/>
      <!-- Guantelete dorado -->
      <circle cx="25" cy="58" r="4" fill="#ffd700"/>
    </g>

    <!-- Torso y Cabeza atléticos -->
    <g class="body-bob">
      <!-- Torso rojo -->
      <path d="M 46 36 L 68 34 L 58 64 L 46 62 Z" fill="#d50000"/>

      <!-- Cinturón de rayo dorado en la cintura -->
      <path d="M 45 61 L 52 64 L 49 67 L 59 63" stroke="#ffd700" stroke-width="2.5" fill="none"/>

      <!-- Emblema de Flash en el pecho -->
      <circle cx="56" cy="46" r="8" fill="#ffffff" stroke="#ffd700" stroke-width="1.8"/>
      <!-- Rayo central -->
      <polygon points="57,40 51,47 55,47 53,53 60,45 56,45" fill="#ffd700"/>

      <!-- Cabeza: Máscara roja -->
      <ellipse cx="64" cy="24" rx="10" ry="12" fill="#d50000"/>
      <!-- Rostro expuesto (boca y barbilla humana) -->
      <path d="M 64 27 Q 70 28 68 34 Q 63 35 62 31 Z" fill="#ffd0b0"/>

      <!-- Alas de rayo horizontales a los lados de las orejas (diseño original Flash) -->
      <polygon points="56,23 48,19 53,26" fill="#ffd700"/>
      <polygon points="68,22 76,18 71,25" fill="#ffd700"/>

      <!-- Visor / hendidura del ojo -->
      <ellipse cx="66" cy="23" rx="2.5" ry="1.5" fill="#ffffff"/>
    </g>

    <!-- Pierna Delantera -->
    <g class="leg-front">
      <path d="M 54 62 Q 68 74 76 84" stroke="#d50000" stroke-width="8" stroke-linecap="round" fill="none"/>
      <!-- Bota dorada -->
      <path d="M 76 84 L 88 84 L 82 92 Z" fill="#ffd700" stroke="#ffb300" stroke-width="1"/>
    </g>

    <!-- Brazo Delantero -->
    <g class="arm-front">
      <path d="M 60 40 Q 75 36 84 32" stroke="#d50000" stroke-width="7" stroke-linecap="round" fill="none"/>
      <!-- Guantelete dorado -->
      <circle cx="84" cy="32" r="4" fill="#ffd700"/>
    </g>
  </svg>
  {% endmacro %}

  <!-- 1. Flash cruzando volando -->
  <div class="flash-first-pass">
    {{ flash_figure() }}
  </div>

  <!-- Mensaje de amor -->
  <div class="card">
    <div class="badge">Toda mi vida estuve buscando lo imposible, jamás pensé que contigo lo encontraría.</div>
    <div class="text">
      Ti amo muuuucho<br>Mi amor
    </div>
    <div class="heart">♥</div>
  </div>

  <!-- 2. Flash patrullando abajo -->
  <div class="flash-bottom-zone">
    <div class="flash-avatar">
      {{ flash_figure() }}
    </div>
    <div class="speedforce-aura"></div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)