import json
import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Corazón Giratorio Personalizado", layout="centered")

# Estilos visuales
st.markdown("""
     <style>
        .stApp { background-color: #000000; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ff3366;'> Corazón Giratorio Interactivo</h1>", unsafe_allow_html=True)

# Cuadro para que cualquier persona pued cambiar la frase desde la web
palabra = st.text_input("Escribe tu palabra o frase:", "I love you")
if not palabra:
    palabra = "I love you"

# Generación del componente visual optimizado para la web
html_template = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    background-color: #000000;
    margin: 0;
    padding: 20px;
    text-align: center;
  }
  canvas {
    background-color: #000000;
    display: block;
    margin: 0 auto;
  }
</style>
</head>
<body>
<canvas id="canvas" width="500" height="500"></canvas>
<script>
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  const customText = USER_TEXT_JSON;
  let angle = 0;

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.save();
    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate(angle);

    let numPoints = 35;
    ctx.font = "bold 18px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = #ffffff";
    ctx.shadowBlur = 10;
    ctx.shadowColor = "#ff3366";
    
    for (let i = 0; i < numPoints; i++) {
      let t = (i / numPoints) * 2 * Math.PI;
      // Ecuaciones matemáticas del corazón de tu código
      let x = 16 * Math.pow(Math.sin(t),3);
      let y = -(13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t));

      x *= 15;
      y *= 15;

      let char = customText[i % customText.length];
      ctx.fillText(char, x, y);
    }
    ctx.restore();

    angle += 0.01; //Velocidad de rotación similar a tu script
    requestAnimationFrame(animate);
  }
  animate();
</script>
</body>
</html>
"""

html_code = html_template.replace("USER_TEXT_JSON", json.dumps (palabra))
st.components.v1.html(html_code, height=560, scrolling=False)
