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
      background: radial-gradient(circle at center, #1c0202 0%, #050000 100%);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      position: relative;
    }

    /* Rayos iniciales en pantalla */
    .lightning-bg {
      position: absolute;
      inset: 0;
      background: #ffe600;
      opacity: 0;
      pointer-events: none;
      animation: lightning 0.3s ease-out 0.5s 2;
    }

    @keyframes lightning {
      0% { opacity: 0; }
      50% { opacity: 0.85; }
      100% { opacity: 0; }
    }

    /* Estela de velocidad inicial */
    .speed-trail {
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 8px;
      background: linear-gradient(90deg, transparent, #ffea00, #ff1e00, transparent);
      opacity: 0;
      box-shadow: 0 0 25px #ffea00, 0 0 50px #ff1e00;
      animation: trail 1.2s ease-out 0.5s forwards;
    }

    /* 1. Primera pasada rápida de Flash */
    .runner-first-pass {
      position: absolute;
      top: calc(50% - 30px);
      left: -150px;
      font-size: 3.5rem;
      z-index: 10;
      filter: drop-shadow(0 0 15px #ffea00) drop-shadow(-30px 0 10px #e50914);
      animation: sprintAcross 1.1s cubic-bezier(0.25, 1, 0.5, 1) 0.4s forwards;
    }

    @keyframes sprintAcross {
      0% {
        left: -150px;
        transform: skewX(-25deg);
      }
      100% {
        left: 130vw;
        transform: skewX(-35deg);
      }
    }

    @keyframes trail {
      0% { opacity: 0; }
      40% { opacity: 1; transform: scaleY(2); }
      100% { opacity: 0; transform: scaleY(0.5); }
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
      background: rgba(255, 234, 0, 0.12);
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
      text-shadow: 0 0 15px rgba(255, 30, 0, 0.75), 0 0 30px rgba(255, 234, 0, 0.4);
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

    /* 2. Flash vuelve por abajo y se queda moviéndose */
    .flash-bottom-container {
      position: absolute;
      bottom: -100px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10;
      display: flex;
      flex-direction: column;
      align-items: center;
      /* Entra deslizándose desde abajo a los 2.2 segundos */
      animation: enterFromBottom 1s cubic-bezier(0.2, 0.8, 0.2, 1) 2.2s forwards;
    }

    @keyframes enterFromBottom {
      to {
        bottom: 45px;
      }
    }

    /* Movimiento continuo de Flash patrullando / trotando */
    .flash-character {
      font-size: 3.2rem;
      filter: drop-shadow(0 0 15px #ffea00) drop-shadow(0 0 25px #ff1e00);
      animation: runningMotion 0.45s infinite alternate ease-in-out 3.2s,
                 patrolPacing 4s infinite alternate ease-in-out 3.2s;
    }

    /* Animación de carrera rápida en su lugar */
    @keyframes runningMotion {
      0% {
        transform: translateY(0px) rotate(-3deg) scale(1);
      }
      100% {
        transform: translateY(-10px) rotate(4deg) scale(1.08);
      }
    }

    /* Se desplaza suavemente de izquierda a derecha en la zona inferior */
    @keyframes patrolPacing {
      0% {
        margin-left: -50px;
      }
      100% {
        margin-left: 50px;
      }
    }

    .energy-sparks {
      font-size: 1.2rem;
      color: #ffea00;
      letter-spacing: 6px;
      animation: sparkFlicker 0.25s infinite alternate 3.2s;
      text-shadow: 0 0 8px #ffea00;
    }

    @keyframes sparkFlicker {
      0% { opacity: 0.3; transform: scaleX(0.85); }
      100% { opacity: 1; transform: scaleX(1.15); }
    }
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>

  <!-- Primer Flash que pasa volando y deja el mensaje -->
  <div class="runner-first-pass">⚡🏃💨</div>

  <!-- Mensaje central -->
  <div class="card">
    <div class="badge">A la velocidad de la luz</div>
    <div class="text">
      te amo muuuucho<br>mi amor
    </div>
    <div class="heart">♥</div>
  </div>

  <!-- Flash que regresa por abajo y se queda moviéndose con electricidad -->
  <div class="flash-bottom-container">
    <div class="flash-character">⚡🏃⚡</div>
    <div class="energy-sparks">⚡ ⚡ ⚡</div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)