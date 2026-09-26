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
      background: linear-gradient(90deg, transparent, #ffe600, #e50914, transparent);
      opacity: 0;
      box-shadow: 0 0 25px #ffe600, 0 0 50px #e50914;
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
      width: 130px;
      height: 130px;
      z-index: 10;
      filter: drop-shadow(0 0 15px #ffe600) drop-shadow(-35px 0 10px #e50914);
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
      filter: drop-shadow(0 0 12px #ffe600) drop-shadow(0 0 25px #d50000);
      animation: patrol 3.5s infinite alternate ease-in-out 2.8s;
    }

    /* Patrulla de izquierda a derecha */
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

    /* Rayos vivos de la Speed Force */
    .speedforce-aura {
      width: 130px;
      height: 4px;
      margin-top: -6px;
      background: radial-gradient(circle, #ffe600 0%, #e50914 60%, transparent 100%);
      box-shadow: 0 0 15px #ffe600, 0 0 30px #e50914;
      animation: auraPulse 0.3s infinite alternate ease-in-out 2.8s;
    }

    @keyframes auraPulse {
      0% { opacity: 0.4; transform: scaleX(0.7); }
      100% { opacity: 1; transform: scaleX(1.3); }
    }

    /* Animación de carrera para las extremidades */
    .leg-back {
      transform-origin: 40px 65px;
      animation: legBackMove 0.28s infinite alternate ease-in-out;
    }
    .leg-front {
      transform-origin: 50px 65px;
      animation: legFrontMove 0.28s infinite alternate ease-in-out;
    }
    .arm-back {
      transform-origin: 40px 42px;
      animation: armBackMove 0.28s infinite alternate ease-in-out;
    }
    .arm-front {
      transform-origin: 55px 40px;
      animation: armFrontMove 0.28s infinite alternate ease-in-out;
    }
    .body-bob {
      animation: bobbing 0.14s infinite alternate ease-in-out;
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
      0% { transform: rotate(30deg); }
      100% { transform: rotate(-35deg); }
    }
    @keyframes armFrontMove {
      0% { transform: rotate(-35deg); }
      100% { transform: rotate(30deg); }
    }
    @keyframes bobbing {
      0% { transform: translateY(0px); }
      100% { transform: translateY(-4px); }
    }
    @keyframes crackle {
      0% { opacity: 0.2; transform: scale(0.85); }
      100% { opacity: 1; transform: scale(1.15); }
    }
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>

  <!-- Componente gráfico de Flash -->
  {% macro flash_figure() %}
  <svg viewBox="0 0 110 110" width="100%" height="100%">
    <!-- Rayos de fondo -->
    <g class="lightning-crack">
      <polygon points="10,48 35,40 26,55 52,44 20,68 34,56" fill="#ffe600" opacity="0.85"/>
      <polygon points="50,20 62,8 58,24 72,12" fill="#ffe600" opacity="0.9"/>
    </g>

    <!-- Pierna trasera con bota dorada -->
    <g class="leg-back">
      <line x1="40" y1="65" x2="22" y2="88" stroke="#b71c1c" stroke-width="10" stroke-linecap="round"/>
      <polygon points="16,88 28,84 20,96" fill="#ffe600"/>
    </g>

    <!-- Brazo trasero -->
    <g class="arm-back">
      <line x1="42" y1="42" x2="25" y2="54" stroke="#b71c1c" stroke-width="8" stroke-linecap="round"/>
      <polygon points="25,54 17,50 20,60" fill="#ffe600"/>
    </g>

    <!-- Cuerpo y Cabeza articulados -->
    <g class="body-bob">
      <!-- Torso rojo carmesí con inclinación de carrera -->
      <polygon points="36,36 66,32 58,68 38,68" fill="#e50914"/>
      
      <!-- Cinturón de rayo dorado -->
      <polygon points="37,66 48,63 45,69 57,65 56,70 38,70" fill="#ffe600"/>

      <!-- Emblema de Flash en el pecho -->
      <circle cx="52" cy="48" r="9" fill="#ffffff" stroke="#ffe600" stroke-width="2"/>
      <polygon points="54,40 46,49 51,49 48,58 57,47 52,47" fill="#ffe600"/>

      <!-- Cabeza con máscara de Flash -->
      <circle cx="64" cy="24" r="14" fill="#e50914"/>
      
      <!-- Rayos/alas doradas de la máscara -->
      <polygon points="64,16 75,10 69,21" fill="#ffe600"/>
      <polygon points="57,18 48,13 53,23" fill="#ffe600"/>
      
      <!-- Ojo blanco definido de la capucha -->
      <polygon points="67,21 74,24 67,26" fill="#ffffff"/>
    </g>

    <!-- Pierna delantera con bota dorada -->
    <g class="leg-front">
      <line x1="50" y1="65" x2="72" y2="82" stroke="#e50914" stroke-width="10" stroke-linecap="round"/>
      <polygon points="72,82 86,81 78,92" fill="#ffe600"/>
    </g>

    <!-- Brazo delantero lanzado al correr -->
    <g class="arm-front">
      <line x1="58" y1="40" x2="80" y2="34" stroke="#e50914" stroke-width="8" stroke-linecap="round"/>
      <polygon points="80,34 90,30 87,40" fill="#ffe600"/>
    </g>
  </svg>
  {% endmacro %}

  <!-- 1. Flash cruzando volando -->
  <div class="flash-first-pass">
    {{ flash_figure() }}
  </div>

  <!-- Mensaje de amor -->
  <div class="card">
    <div class="badge">A la velocidad de la luz</div>
    <div class="text">
      te amo muuuucho<br>mi amor
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