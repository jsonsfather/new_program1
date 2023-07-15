import PySimpleGUI as SG
label=SG.Text("Add your text")
input_box=SG.InputText(tooltip="Inter random text")
add_button=SG.Button("Add")
window=SG.Window('My new window', layout=[[label],[input_box,add_button]])
window.read()
window.close()