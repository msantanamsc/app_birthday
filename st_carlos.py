import streamlit as st
import folium
import os
from streamlit_folium import folium_static

# Load image
#image = Image.open("spain_map.jpg")
#st.image(image, caption="Click on the cities", use_column_width=True)

st.title("Juego de cumpleaños")
st.write("¡Feliz cumpleaños! Hoy es un día muy especial para ti y tu novia quiere sorprenderte con un " 
         "regalo increíble. Pero no será fácil conseguirlo. Tendrás que demostrar tu ingenio y habilidad "
         "en este juego lleno de enigmas. Cada acertijo que encuentres en tu habitación te dará una pista sobre lo que es tu regalo. "
         "Si logras resolverlos todos, podrás abrir tu regalo y disfrutar de tu sorpresa. "
         "¿Estás listo para el desafío? ¡Que empiece el juego!")
image = os.path.abspath("carlos_room.jpeg")

# Define coordinates of markers
cuadro_cantante = [42.0095, -4.524006]
foto_nuestra = [40.07039, -2.13741]
reloj = [41.65606, -0.87734]
radio = [38.90673, 1.42059]
foto_mochete = [41.55032, -8.42005]
ps5 = [40.20564, -8.41955]
messi = [39.5, -6.34407]
cama = [38.98626, -3.92907]
caja = [36.68645, -6.34407]
coche = [37.00864, -8.94311]
# Create map with image overlay
m = folium.Map(location=[40, -4], zoom_start=5, tiles= None)

tooltip = "Haz click para investigar"

folium.raster_layers.ImageOverlay(
    image=image,
    bounds=[[35.6, -10.8], [43.3, 2.6]],
    opacity=1,
    interactive=True,
    cross_origin=False
).add_to(m)
# Add markers to map
popup_1 = folium.Popup("<b>Enigma 2</b>:<br>¿Cuál es el nombre de este chico?.<br><font color = 'blue'><b>Pista</b>: Es el nombre del protagonista de una serie, en la que sueña con ser un gran futbolista y tiene un balón muy especial.</font>", max_width= 300)
folium.map.Marker(
    cuadro_cantante,
    popup=popup_1,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_2 = folium.Popup("Una foto en la que salimos guapos", max_width= 300)
folium.map.Marker(
    foto_nuestra,
    popup=popup_2,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_3 = folium.Popup("Tic-tac, continúa buscando por otro lado", max_width= 300)
folium.map.Marker(
    reloj,
    popup=popup_3,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_4 = folium.Popup("<b>Enigma 3</b>:<br>Para finalizar tu investigación deberás arreglar la radio, esta solo funcionará si aciertas el género musical que debe sonar.<br><font color = 'blue'><b>Pista</b>: Género musical que escuchas a menudo </font>", max_width= 300)
folium.map.Marker(
    radio,
    popup=popup_4,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_5 = folium.Popup("Observas una foto de una palmera, pero esto no es ninguna pista. ¡Sigue buscando!", max_width= 300)
folium.map.Marker(
    foto_mochete,
    popup=popup_5,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_6 = folium.Popup("La ps5 no podía faltar en una simulación de tu habitación", max_width= 300)
folium.map.Marker(
    ps5,
    popup= popup_6,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_7 = folium.Popup("Hay una cama, pero no es hora de dormir. ¡Sigue buscando!", max_width= 300)
folium.map.Marker(
    cama,
    popup=popup_7,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_8 = folium.Popup("<b>Enigma 1</b>:<br>Encuentras una caja pero está cerrada. Para abrirla deberás introducir un código numérico.<br><font color = 'blue'><b>Pista</b>: Es el resultado del siguiente problema de estadística:<br><i>La incidencia de hepatocarcinoma en un determinado país, en sujetos alcohólicos, es de 1307 casos nuevos por cada 10000 bebedores. Sin embargo, el riesgo de hepatocarcinoma es de 2 por cada 20000 bebedores. ¿Cuál es el riesgo relativo de padecer hepatocarcinoma por alcoholismo? </i></font>", max_width= 300)
folium.map.Marker(
    caja,
    popup= popup_8,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_9 = folium.Popup("Vas caminando y te tropiezas con una maqueta de un Porsche GT3RS. Y te preguntas ¿será un Porsche GT3RS mi regalo? Le das la vuelta a la maqueta y ves que hay una nota que dice así:<br><i>Soñar es gratis pero un Porsche no.</i><br>Desilusionado, dejas la maqueta en el suelo y continuas tu búsqueda.", max_width= 300)
folium.map.Marker(
    coche,
    popup= popup_9,
    icon=folium.Icon(icon="search", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

popup_10 = folium.Popup("¿Qué mirás bobo? Andá para investigar bobo", max_width= 300)
folium.map.Marker(
    messi,
    popup= popup_10,
    icon=folium.Icon(icon="question", color = "green", prefix = "fa"),
    tooltip = tooltip
).add_to(m)

folium_static(m, width= 700, height= 500)

# Create sidebar with enigmas
sidebar = st.sidebar
sidebar.title("Resuelve los enigmas")

#DEfine the correct answer
codigo = 1307
nombre = "oliver"
genero = "rock"

codigo_usuario = sidebar.number_input("Enigma 1", min_value=0, max_value= 20000, step = 1)
if codigo_usuario == codigo:
    sidebar.success("¡Has acertado el código!")
else:
    sidebar.error("Incorrecto")
    
nombre_usuario = sidebar.text_input("Enigma 2")
if nombre_usuario.lower() == nombre:
    sidebar.success("¡Has acertado el nombre!")
else:
    sidebar.error("Incorrecto")
    
genero_usuario = sidebar.text_input("Enigma 3")
if genero_usuario.lower() == genero:
    sidebar.success("¡Has acertado el género musical!")
else:
    sidebar.error("Incorrecto")

if codigo_usuario == codigo and nombre_usuario == nombre and genero_usuario == genero:
    sidebar.success("¡Has resuelto los 3 enigmas! Felicidades. Ahora puedes recibir tu regalo, ¿sabes ya que es?.")

# Show map in streamlit
#st.write(m)