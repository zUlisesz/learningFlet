import flet as ft

def main(page: ft.Page):
    page.title = 'My first app with flet' # setting the page's title
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # aligning the elements of the page in  'X'
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # aligning the elements of the app in 'Y'
    
    page.bgcolor = ft.Colors.BLUE_GREY_400 #setting the page's color
    
    text = ft.Text('Hi, its me on my new app') # creating a 'label'
    text.color = ft.Colors.WHITE
    
    
    def changeBackGround(event):
        page.bgcolor = ft.Colors.BLUE_GREY_900
        page.update()
        
    boton = ft.FilledButton(text ='Press me to get the screen darker', on_click= changeBackGround)
    page.add( text, boton) # adding my 'text' into the page

ft.app(target=main)  # Al correr la aplicación se ejecutará la función main
