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
      background: radial-gradient(circle at center, #1a0000 0%, #050000 100%);
      height: 100vh;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      touch-action: manipulation;
    }

    /* Rayos en pantalla */
    .lightning-bg {
      position: absolute;
      inset: 0;
      background: #ffe600;
      opacity: 0;
      pointer-events: none;
      animation: lightning 0.3s ease-out 0.6s 2;
    }

    @keyframes lightning {
      0% { opacity: 0; }
      50% { opacity: 0.85; }
      100% { opacity: 0; }
    }

    /* Estela de velocidad roja y amarilla */
    .speed-trail {
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 8px;
      background: linear-gradient(90deg, transparent, #ffea00, #ff1e00, transparent);
      opacity: 0;
      box-shadow: 0 0 20px #ffea00, 0 0 45px #ff1e00;
      animation: trail 1.2s ease-out 0.6s forwards;
    }

    /* Flash corriendo */
    .runner {
      position: absolute;
      top: calc(50% - 30px);
      left: -150px;
      font-size: 3.5rem;
      z-index: 10;
      filter: drop-shadow(0 0 15px #ffea00) drop-shadow(-30px 0 10px #e50914);
      animation: sprint 1.2s cubic-bezier(0.25, 1, 0.5, 1) 0.5s forwards;
    }

    @keyframes sprint {
      0% {
        left: -150px;
        transform: skewX(-25deg);
      }
      100% {
        left: 125vw;
        transform: skewX(-35deg);
      }
    }

    @keyframes trail {
      0% { opacity: 0; transform: scaleY(1); }
      40% { opacity: 1; transform: scaleY(2); }
      100% { opacity: 0; transform: scaleY(0.5); }
    }

    /* Contenedor del mensaje que aparece tras la carrera */
    .card {
      text-align: center;
      padding: 24px;
      opacity: 0;
      transform: scale(0.6);
      animation: popMessage 0.9s cubic-bezier(0.175, 0.885, 0.32, 1.275) 1.4s forwards;
      z-index: 5;
    }

    .badge {
      display: inline-block;
      margin-bottom: 15px;
      padding: 5px 16px;
      background: rgba(255, 234, 0, 0.12);
      border: 1px solid #ffea00;
      border-radius: 999px;
      color: #ffea00;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
    }

    .text {
      color: #ffffff;
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.35;
      text-shadow: 0 0 15px rgba(255, 30, 0, 0.7), 0 0 30px rgba(255, 234, 0, 0.4);
    }

    .heart {
      display: inline-block;
      color: #ff1e42;
      font-size: 3.5rem;
      margin-top: 15px;
      filter: drop-shadow(0 0 15px #ff1e42);
      animation: beat 1.1s infinite ease-in-out 2.2s;
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
  </style>
</head>
<body>
  <div class="lightning-bg"></div>
  <div class="speed-trail"></div>
  <div class="runner">⚡🏃💨</div>

  <div class="card">
    <div class="badge">Toda mi vida estuve buscando lo imposible, jamás pensé que contigo lo encontraría.</div>
    <div class="text">
      Te amo muuuucho <br>Rodrigo
    </div>
    <div class="heart">♥</div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)