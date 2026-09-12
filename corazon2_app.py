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
frase_usuario = st.text_input("Escribe tu palabra o frase:", "I love you")
if not frase_usuario:
    frase_usuario = "I love you"

# Generación del componente visual optimizado para la web
html_template = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    background-color: #000000;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 450vh;
    overflow: hidden;
  }
  canvas {
    background: #000000;
  }
</style>
</head>
<body>
<canvas id="canvas" width="600" height="600"></canvas>
<script>
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  const customText = "{frase_usuario}";
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
    ctx.fillStyle = #3399ff";
    ctx.shadowBlur = 6;
    ctx.shadowColor = "#00ffff";
    
    for (let i = 0; i < numPoints; i++) {
      let t = (i / numPoints) * 2 * Math.PI;
      // Ecuaciones matemáticas del corazón de tu código
      let x = 16 * Math.pow(Math.sin(t),3);
      let y = -(13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t));

      x *= 18;
      y *= 18;

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

st.components.v1.html(html_code, height=520)
st.markdown("<p style='text-align: center; color: #888;'>Sube este archivo a GitHub y conéctalo a Streamlit Cloud para obtener tu enlace web.</p>", unsafe_allow_html=True)
