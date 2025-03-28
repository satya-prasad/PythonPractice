import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")

window = sg.Window("To-Do List App", layout=[[label],[input_box, add_button]])
window.read()
window.close()