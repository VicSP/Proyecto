import dearpygui.dearpygui as dpg
import model

dpg.create_context()

dpg.create_viewport(title='Algoritmo A*',width=900,height=450)

def button_callback(initLocation):
    model.aStarSearch(initLocation)

with dpg.window(label='Probando...',width=900,height=450):
    dpg.add_text("Este es el programa para evaluar distacias",color=[255,0,0])
    dpg.add_combo(model.locations,default_value="Arad",label='Punto de partida',width=250,tag='locations')
    initLocation = dpg.get_value('locations')
    dpg.add_button( label='Obtener ruta óptima',callback=button_callback,tag='btnSearch')
    dpg.add_text("La ruta optima es ",color=[223,0,0])
    dpg.set_item_callback('btnSearch',callback=button_callback)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

