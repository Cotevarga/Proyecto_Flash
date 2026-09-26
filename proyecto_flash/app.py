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
      background: radial-gradient(circle at center, #200000 0%, #050000 100%);
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
      background: linear-gradient(90deg, transparent, #ffea00, #d50000, transparent);
      opacity: 0;
      box-shadow: 0 0 25px #ffea00, 0 0 50px #d50000;
      animation: trail 1.2s ease-out 0.4s forwards;
    }

    @keyframes trail {
      0% { opacity: 0; }
      40% { opacity: 1; transform: scaleY(2); }
      100% { opacity: 0; transform: scaleY(0.5); }
    }

    /* 1. Flash cruzando volando a toda velocidad */
    .flash-first-pass {
      position: absolute;
      top: calc(50% - 60px);
      left: -200px;
      width: 130px;
      height: 120px;
      z-index: 10;
      filter: drop-shadow(0 0 15px #ffe600) drop-shadow(-35px 0 10px #d50000);
      animation: sprintAcross 1.1s cubic-bezier(0.25, 1, 0.5, 1) 0.3s forwards;
    }

    @keyframes sprintAcross {
      0% {
        left: -200px;
        transform: skewX(-25deg) scale(0.95);
      }
      100% {
        left: 130vw;
        transform: skewX(-35deg) scale(1.1);
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
      text-shadow: 0 0 15px rgba(213, 0, 0, 0.8), 0 0 30px rgba(255, 230, 0, 0.5);
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

    /* 2. Flash vuelve por abajo y se queda corriendo */
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
      width: 120px;
      height: 110px;
      filter: drop-shadow(0 0 15px #ffe600) drop-shadow(0 0 25px #d50000);
      animation: runMotion 0.4s infinite alternate ease-in-out 2.8s,
                 patrol 3.6s infinite alternate ease-in-out 2.8s;
    }

    @keyframes runMotion {
      0% {
        transform: translateY(0px) rotate(-4deg);
      }
      100% {
        transform: translateY(-8px) rotate(4deg);
      }
    }

    @keyframes patrol {
      0% {
        margin-left: -50px;
      }
      100% {
        margin-left: 50px;
      }
    }

    /* Chispas y rayos de la Speed Force */
    .speedforce-aura {
      width: 140px;
      height: 4px;
      margin-top: -6px;
      background: radial-gradient(circle, #ffe600 0%, #d50000 60%, transparent 100%);
      box-shadow: 0 0 15px #ffe600, 0 0 25px #d50000;
      animation: auraPulse 0.3s infinite alternate ease-in-out 2.8s;
    }

    @keyframes auraPulse {
      0% { opacity: 0.4; transform: scaleX(0.8); }
      100% { opacity: 1; transform: scaleX(1.3); }
    }
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>

  <!-- SVG de Flash el superhéroe (traje rojo, rayos dorados, máscara y emblema) -->
  <div class="flash-first-pass">
    <svg viewBox="0 0 100 100" width="100%" height="100%">
      <!-- Rayos traseros -->
      <polygon points="5,50 30,42 22,55 45,46 15,68 28,57" fill="#ffe600" opacity="0.8"/>
      <!-- Piernas en carrera -->
      <line x1="38" y1="65" x2="15" y2="88" stroke="#b71c1c" stroke-width="9" stroke-linecap="round"/>
      <polygon points="10,88 20,86 12,96" fill="#ffe600"/>
      <line x1="48" y1="65" x2="72" y2="82" stroke="#d50000" stroke-width="9" stroke-linecap="round"/>
      <polygon points="72,82 85,82 78,92" fill="#ffe600"/>
      <!-- Torso inclinado hacia adelante -->
      <polygon points="35,38 65,34 56,68 38,68" fill="#d50000"/>
      <!-- Cinturón de rayo -->
      <polygon points="36,66 48,64 45,69 57,66 56,70 38,70" fill="#ffe600"/>
      <!-- Brazo derecho impulsándose -->
      <line x1="40" y1="42" x2="22" y2="52" stroke="#b71c1c" stroke-width="8" stroke-linecap="round"/>
      <polygon points="22,52 14,48 18,58" fill="#ffe600"/>
      <!-- Brazo izquierdo extendido -->
      <line x1="60" y1="40" x2="82" y2="35" stroke="#d50000" stroke-width="8" stroke-linecap="round"/>
      <polygon points="82,35 90,32 88,40" fill="#ffe600"/>
      <!-- Emblema de Flash en el pecho -->
      <circle cx="51" cy="48" r="8" fill="#ffffff" stroke="#ffe600" stroke-width="1.5"/>
      <polygon points="53,41 46,49 50,49 48,56 56,47 52,47" fill="#ffe600"/>
      <!-- Cabeza con máscara roja -->
      <circle cx="62" cy="25" r="13" fill="#d50000"/>
      <!-- Orejeras con alas de rayo amarillas -->
      <polygon points="62,18 72,13 67,22" fill="#ffe600"/>
      <polygon points="56,20 48,15 52,24" fill="#ffe600"/>
      <!-- Ojos blancos de la máscara -->
      <polygon points="65,22 71,25 65,26" fill="#ffffff"/>
    </svg>
  </div>

  <!-- Mensaje central -->
  <div class="card">
    <div class="badge">A la velocidad de la luz</div>
    <div class="text">
      te amo muuuucho<br>mi amor
    </div>
    <div class="heart">♥</div>
  </div>

  <!-- Flash corriendo en la parte inferior -->
  <div class="flash-bottom-zone">
    <div class="flash-avatar">
      <svg viewBox="0 0 100 100" width="100%" height="100%">
        <!-- Rayos de Speed Force -->
        <polygon points="5,50 30,42 22,55 45,46 15,68 28,57" fill="#ffe600" opacity="0.9"/>
        <!-- Piernas -->
        <line x1="38" y1="65" x2="15" y2="88" stroke="#b71c1c" stroke-width="9" stroke-linecap="round"/>
        <polygon points="10,88 20,86 12,96" fill="#ffe600"/>
        <line x1="48" y1="65" x2="72" y2="82" stroke="#d50000" stroke-width="9" stroke-linecap="round"/>
        <polygon points="72,82 85,82 78,92" fill="#ffe600"/>
        <!-- Torso -->
        <polygon points="35,38 65,34 56,68 38,68" fill="#d50000"/>
        <!-- Cinturón de rayo -->
        <polygon points="36,66 48,64 45,69 57,66 56,70 38,70" fill="#ffe600"/>
        <!-- Brazos -->
        <line x1="40" y1="42" x2="22" y2="52" stroke="#b71c1c" stroke-width="8" stroke-linecap="round"/>
        <polygon points="22,52 14,48 18,58" fill="#ffe600"/>
        <line x1="60" y1="40" x2="82" y2="35" stroke="#d50000" stroke-width="8" stroke-linecap="round"/>
        <polygon points="82,35 90,32 88,40" fill="#ffe600"/>
        <!-- Emblema -->
        <circle cx="51" cy="48" r="8" fill="#ffffff" stroke="#ffe600" stroke-width="1.5"/>
        <polygon points="53,41 46,49 50,49 48,56 56,47 52,47" fill="#ffe600"/>
        <!-- Cabeza y máscara -->
        <circle cx="62" cy="25" r="13" fill="#d50000"/>
        <!-- Rayos en la cabeza -->
        <polygon points="62,18 72,13 67,22" fill="#ffe600"/>
        <polygon points="56,20 48,15 52,24" fill="#ffe600"/>
        <!-- Ojos -->
        <polygon points="65,22 71,25 65,26" fill="#ffffff"/>
      </svg>
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