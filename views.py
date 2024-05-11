from flet import *
from pages.num_bars import numBars
from pages.num_notes import numNotes
import flet as ft
from pages.main import data

def views_hadler(page):
   # data = {"num_bars":"num_bars","num_notes":"num_notes","num_steps ":"num_steps ","key":"key","scale":"scale"}
   num_bars = ft.TextField(
                        label="От 0 до 8",
                        bgcolor ="#969490",
                        border_color="#413E3E"
                     )
   num_notes = ft.TextField(
                        label="От 0 до 4",
                        bgcolor ="#969490",
                        border_color="#413E3E"
                     )
   # num_steps = ft.TextField(label="Введите количество высот в ноте:",width =400)
   # pauses = ft.TextField(label="Добавить паузы:",width =400)
   # key = ft.TextField(
   #                      label="От 0 до 4",
   #                      bgcolor ="#969490",
   #                      border_color="#413E3E",

   #                   )
   keey = ft.Text("pass", color="#000000", font_family="YanoneMedium",size = 16)
   # def key(i):
   #    return ft.Text(i, color="#000000", font_family="YanoneMedium",size = 16)
   scale = ft.Text("pass", color="#000000", font_family="YanoneMedium",size = 16)
   root = ft.TextField(label="Введите высоту тона гаммы:",width =400)
   population_size = ft.TextField(label="Введите размер популяции(количество мелодий):",width =400)
   num_mutations = ft.TextField(label="Введите количество мутаций(Максимальное количество мутаций):",width =400)
   mutation_probability = ft.TextField(label="Введите вероятность возникновения мутации:",width =400)
   x=0



   def key_row():
      keys=["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#"]
      items = []
      for i in keys:
         print(i)
         print(keey.value)
         keey.value = i
         print(i)
         print(keey.value)
         items.append(
            ft.Container(content = ft.CupertinoButton(
                           content=ft.Text(i, color="#000000", font_family="YanoneMedium",size = 16),
                           data=i,
                           # bgcolor= "#D3C9C9",
                           # alignment=ft.alignment.top_left,
                           # border_radius=ft.border_radius.all(0),
                           opacity_on_click=0.5,
                           on_click=route_to_Scales,), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",)
         )
      return items
   def key_row2():
      keys=["Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
      items = []
      for i in keys:
         items.append(
            ft.Container(content = ft.CupertinoButton(
                           content=ft.Text(i, color="#000000", font_family="YanoneMedium",size = 16),
                           # bgcolor= "#D3C9C9",
                           # alignment=ft.alignment.top_left,
                           # border_radius=ft.border_radius.all(0),
                           opacity_on_click=0.5,
                           on_click=route_to_Scales,), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",)
         )
      
      return items


   def scale_row():
      scales=["major", "minorM", "dorian", "phrygian", "lydian", "mixolydian", "majorBlues", "minorBlues"]
      items = []
      for i in scales:
         scale.value = i
         items.append(
            ft.Container(content = ft.CupertinoButton(
                           content=keey,
                           data=i,
                           # bgcolor= "#D3C9C9",
                           # alignment=ft.alignment.top_left,
                           # border_radius=ft.border_radius.all(0),
                           opacity_on_click=0.5,
                           on_click=route_to_Scales,), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",)
         )
      return items










   def route_change(e):
      print(page.route)
      page.views.clear()
      page.views.append(
         views_hadler(page)[page.route]
      )
      
   def route_to_numNotes(e):
      data["num_bars"] = num_bars.value
      page.on_route_change = route_change
      page.go('/num_notes')
      page.update()
      print(data)
   def route_to_Keys(e):
      data["num_notes"] = num_notes.value
      page.on_route_change = route_change
      page.go('/keys')
      page.update()
      print(data)
   def route_to_Scales(e):
      data["key"] = keey.value
      page.on_route_change = route_change
      page.go('/scales')
      page.update()
      print(data)
   def route_to_numBars(e):
      page.on_route_change = route_change
      page.go('/num_bars')
      page.update()
   def route_to_main(e):
      page.on_route_change = route_change
      page.go('/')
      page.update()
   # page.on_route_change = route_change
   # page.go('/num_notes')
   # page.update()
   return {
      

      '/':View(
         
         route="/",
         controls = [
            Container(
               height = 800,
               width = 350,
               bgcolor = 'blue'
            )
         ]
         ),
#Длина мелодии
      '/num_bars':View(
         route="/",
         controls = [
            # Container( content = [numBars(page)], bgcolor = '#464236', width=800,height=440)
            Container(content=ft.Column(
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
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        num_bars
                  ],
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
               ],alignment=ft.MainAxisAlignment.CENTER),bgcolor = '#464236', width=800,height=440)]),

#Нот в такте
      '/num_notes':View(
         route="/",
         controls = [
            Container(content=ft.Column(
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
               ),
               ft.Row(
                  controls=[
                     ft.Text(
                           text_align=ft.TextAlign.CENTER,
                           value=f"Введите количество нот в такте:",
                           size=12,
                           weight=ft.FontWeight.W_100,
                           font_family="YanoneMedium"
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        num_notes
                  ],
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
                           on_click=route_to_Keys,
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               )
               ],alignment=ft.MainAxisAlignment.CENTER),bgcolor = '#464236', width=800,height=440)]
      ),



#Тональность
      '/keys':View(
         route="/",
         controls = [
            # Container( content = [numBars(page)], bgcolor = '#464236', width=800,height=440)
            Container(content=ft.Column(
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
                           value=f"Выберите тональность гаммы::",
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
                        num_bars
                  ],
            
                  # aligment = ft.alignment.top_center,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=key_row(),width=page.window_width,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=key_row2(),width=page.window_width,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ],alignment=ft.MainAxisAlignment.CENTER),bgcolor = '#464236', width=800,height=440)]),

#Тип гаммы
      '/scales':View(
         route="/",
         controls = [
            # Container( content = [numBars(page)], bgcolor = '#464236', width=800,height=440)
            Container(content=ft.Column(
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
                           value=f"Выберите тип гаммы::",
                           size=12,
                           weight=ft.FontWeight.W_100,
                           font_family="YanoneMedium"
                     )
                  ],
            
                  # aligment = ft.alignment.top_center,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               # ft.Row(
               #    controls=[
               #          num_bars
               #    ],
            
               #    # aligment = ft.alignment.top_center,
               #    alignment=ft.MainAxisAlignment.CENTER
               # ),
               ft.Row(
                  controls=scale_row(),width=page.window_width,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
            
               ],alignment=ft.MainAxisAlignment.CENTER),bgcolor = '#464236', width=800,height=440)]),
         
         
      
   }
