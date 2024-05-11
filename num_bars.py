from flet import *
import flet as ft

class numBars(UserControl):
   BACKGROUNDCOLOR = "#464236"
   TEXTBUTTONCOLOR = "#D3C9C9"
   INPUTTEXTCOLOR = "#D9D9D9"
   def __init__(self,page):
      super().__init__()
      self.page = page
   def build(self):
      
      return ft.Column(
               [
                  ft.Row(
                  controls=[
                     ft.Text(
                           text_align=ft.TextAlign.CENTER,
                           value=f"Генератор мелодий",
                           size=25,
                           weight=ft.FontWeight.BOLD,
                           font_family="YanoneBold"
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
                  #asda
               ),
               ft.Row(
                  controls=[
                     ft.Text(
                           text_align=ft.TextAlign.CENTER,
                           value=f"Введите количество тактов(Длина мелодии):",
                           size=12,
                           weight=ft.FontWeight.W_100,
                           font_family="YanoneMedium"
                     )
                  ],
            
                  # aligment = ft.alignment.top_center,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        ft.TextField(
                        label="От 0 до 8",
                        bgcolor ="#969490",
                        border_color="#413E3E"
                     )
                  ],
            
                  # aligment = ft.alignment.top_center,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        ft.CupertinoButton(
                           content=ft.Text("Отправить", color="#000000", font_family="YanoneMedium"),
                           bgcolor= "#D3C9C9",
                           alignment=ft.alignment.center,
                           border_radius=ft.border_radius.all(0),
                           opacity_on_click=0.5,
                           on_click=route_to_numNotes,
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               )
               ],alignment=ft.MainAxisAlignment.CENTER)
         
   
