import flet as ft
import time

# so we can add controls into the page by two ways, 'page.add( name_control)' or 'page.controls.append(name_control)' 
def main(page: ft.Page):
    
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))
    
    # adding more than 1 control to the page
    page.add(
        ft.Row(controls=[  # adding controls to the pages by rows
            ft.TextField(label="Your name"), # creating a textField and setting a placeholder
            ft.ElevatedButton(text="Say my name!", on_click= button_clicked) # creating a button
    ]))
            

ft.app(main)