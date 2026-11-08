import os
from nicegui import ui, app

# Para que Render sí encuentre los videos y el audio
app.add_static_files('/media', '.')

energia = 50
felicidad = 50
bateria = 50

audio_robot = ui.audio('/media/robot.mp3').style('display: none;')

def actualizar():
    barra_energia.value = energia / 100
    barra_felicidad.value = felicidad / 100
    barra_bateria.value = bateria / 100
    texto_energia.text = f'Energia: {energia}%'
    texto_felicidad.text = f'Felicidad: {felicidad}%'
    texto_bateria.text = f'Bateria: {bateria}%'

def iniciar():
    inicio.visible = False
    juego.visible = True

def jugar():
    global energia, felicidad, bateria
    inicio.visible = False
    energia = max(energia - 10, 0)
    felicidad = min(felicidad + 20, 100)
    bateria = max(bateria - 15, 0)
    estado.text = 'El robot esta jugando'
    video.set_source('/media/play.MP4')
    audio_robot.play()
    actualizar()

def alimentar():
    global energia, felicidad, bateria
    energia = min(energia + 20, 100)
    felicidad = min(felicidad + 5, 100)
    estado.text = 'El robot esta recibiendo energia'
    video.set_source('/media/eat.MP4')
    audio_robot.play()
    actualizar()

def dormir():
    global energia, felicidad, bateria
    bateria = min(bateria + 25, 100)
    energia = min(energia + 10, 100)
    felicidad = max(felicidad - 5, 0)
    estado.text = 'El robot esta descansando'
    video.set_source('/media/sleep.MP4')
    audio_robot.play()
    actualizar()

def esperar():
    estado.text = 'El robot esta esperando instrucciones'
    video.set_source('/media/idle.MP4')
    audio_robot.play()

with ui.column().classes('w-full items-center').style('background-color: #eaffff; min-height: 100vh; padding: 20px') as inicio:
    ui.label('🤖 Mi Robot Virtual').style('font-size: 36px; font-weight: bold')
    ui.label('Cuida a tu robot para mantenerlo feliz y con energia')
    ui.button('▶️ Iniciar Robot', on_click=iniciar)

with ui.column().classes('w-full items-center').style('background-color: #eaffff; min-height: 100vh; padding: 20px') as juego:
    ui.label('🤖 Mi Robot Virtual').style('font-size: 36px; font-weight: bold')
    with ui.card().style('width: 520px; padding: 15px'):
        texto_energia = ui.label('Energia: 50%')
        barra_energia = ui.linear_progress(value=0.5)
        estado = ui.label('El robot esta esperando instrucciones').style('font-size: 22px')
        texto_felicidad = ui.label('Felicidad: 50%')
        barra_felicidad = ui.linear_progress(value=0.5)
        texto_bateria = ui.label('Bateria: 50%')
        barra_bateria = ui.linear_progress(value=0.5)
        video = ui.video('/media/idle.MP4', autoplay=True, loop=True, muted=False).style('width: 520px; border-radius: 20px')
        with ui.row():
            ui.button('🎮 Jugar', on_click=jugar)
            ui.button('🍔 Alimentar', on_click=alimentar)
            ui.button('😴 Dormir', on_click=dormir)
            ui.button('⏳ Esperar', on_click=esperar)

juego.visible = False

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        title="Mi Robot",
        reload=False
    )