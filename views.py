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
   population_size = ft.TextField(
                        label="От 0 до 10",
                        bgcolor ="#969490",
                        border_color="#413E3E"
                     )
   # num_steps = ft.TextField(label="Введите количество высот в ноте:",width =400)
   # pauses = ft.TextField(label="Добавить паузы:",width =400)
   key = ft.TextField(
                        
                        bgcolor ="#969490",
                        border_color="#413E3E",

                     )
   keys = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#","Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
   keys_text = []
   for i in keys:
      keys_text.append(ft.Text(i, color="#000000", font_family="YanoneMedium",size = 14))

   scale = ft.TextField(
                        
                        bgcolor ="#969490",
                        border_color="#413E3E",

                     )
   scales=["major", "minorM", "dorian", "phrygian", "lydian", "mixolydian", "majorBlues", "minorBlues"]
   scales_text=[]
   for i in scales:
      scales_text.append(ft.Text(i, color="#000000", font_family="YanoneMedium",size = 14))

   root = ft.TextField(
                        label="От 0 до 4",
                        bgcolor ="#969490",
                        border_color="#413E3E"
                     )
   # population_size = ft.TextField(label="Введите размер популяции(количество мелодий):",width =400)
   num_mutations = ft.TextField(label="Введите количество мутаций(Максимальное количество мутаций):",width =400)
   mutation_probability = ft.TextField(label="Введите вероятность возникновения мутации:",width =400)
   


   # def scale_row():
   #    scales=["major", "minorM", "dorian", "phrygian", "lydian", "mixolydian", "majorBlues", "minorBlues"]
   #    items = []
   #    for i in scales:
   #       scale.value = i
   #       items.append(
   #          ft.Container(content = ft.CupertinoButton(
   #                         content=(),
   #                         data=i,
   #                         # bgcolor= "#D3C9C9",
   #                         # alignment=ft.alignment.top_left,
   #                         # border_radius=ft.border_radius.all(0),
   #                         opacity_on_click=0.5,
   #                         on_click=route_to_Scales,), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
            
   #       )
   #    return items

   def change_key1(e):
      key.value = keys[0]
      page.update()
   def change_key2(e):
      key.value = keys[1]
      page.update()
   def change_key3(e):
      key.value = keys[2]
      page.update()
   def change_key4(e):
      key.value = keys[3]
      page.update()
   def change_key5(e):
      key.value = keys[4]
      page.update()
   def change_key6(e):
      key.value = keys[5]
      page.update()
   def change_key7(e):
      key.value = keys[6]
      page.update()
   def change_key8(e):
      key.value = keys[7]
      page.update()
   def change_key9(e):
      key.value = keys[8]
      page.update()
   def change_key10(e):
      key.value = keys[9]
      page.update()
   def change_key11(e):
      key.value = keys[10]
      page.update()
   def change_key12(e):
      key.value = keys[11]
      page.update()
   def change_key13(e):
      key.value = keys[12]
      page.update()
   def change_key14(e):
      key.value = keys[13]
      page.update()
   def change_key15(e):
      key.value = keys[14]
      page.update()
   def change_key16(e):
      key.value = keys[15]
      page.update()
   def change_key17(e):
      key.value = keys[16]
      page.update()

   def change_scale1(e):
      scale.value = scales[0]
      page.update()
   def change_scale2(e):
      scale.value = scales[1]
      page.update()
   def change_scale3(e):
      scale.value = scales[2]
      page.update()
   def change_scale4(e):
      scale.value = scales[3]
      page.update()
   def change_scale5(e):
      scale.value = scales[4]
      page.update()
   def change_scale6(e):
      scale.value = scales[5]
      page.update()
   def change_scale7(e):
      scale.value = scales[6]
      page.update()
   def change_scale8(e):
      scale.value = scales[7]
      page.update()
      


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
      data["key"] = key.value
      page.on_route_change = route_change
      page.go('/scales')
      page.update()
      print(data)
   def route_to_PopulationSize(e):
      data["root"] = root.value
      page.on_route_change = route_change
      page.go('/populationSize')
      page.update()
      print(data)
   def route_to_root(e):
      data["scale"] = scale.value
      page.on_route_change = route_change
      page.go('/root')
      page.update()
      print(data)
   def route_to_result(e):
      pass


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
                           value=f"Выберите тональность гаммы:",
                           size=12,
                           weight=ft.FontWeight.W_100,
                           font_family="YanoneMedium"
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        key
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=
                  [ft.Container(content = ft.CupertinoButton(
                           content=keys_text[0],
                           opacity_on_click=0.5,
                           on_click= change_key1), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[1],
                           opacity_on_click=0.5,
                           on_click= change_key2), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[2],
                           opacity_on_click=0.5,
                           on_click= change_key3), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[3],
                           opacity_on_click=0.5,
                           on_click= change_key4), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[4],
                           opacity_on_click=0.5,
                           on_click= change_key5), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[5],
                           opacity_on_click=0.5,
                           on_click= change_key6), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[6],
                           opacity_on_click=0.5,
                           on_click= change_key7), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[7],
                           opacity_on_click=0.5,
                           on_click= change_key8), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[8],
                           opacity_on_click=0.5,
                           on_click= change_key9), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",)
                  ],width=page.window_width,
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[9],
                           opacity_on_click=0.5,
                           on_click= change_key10), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[10],
                           opacity_on_click=0.5,
                           on_click= change_key11), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[11],
                           opacity_on_click=0.5,
                           on_click= change_key12), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[12],
                           opacity_on_click=0.5,
                           on_click= change_key13), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[13],
                           opacity_on_click=0.5,
                           on_click= change_key14), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[14],
                           opacity_on_click=0.5,
                           on_click= change_key15), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[15],
                           opacity_on_click=0.5,
                           on_click= change_key16), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=keys_text[16],
                           opacity_on_click=0.5,
                           on_click= change_key17), width=70,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",)
                  ],width=page.window_width,
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
                           on_click=route_to_Scales,
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               )
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
               ),
               ft.Row(
                  controls=[
                     ft.Text(
                           text_align=ft.TextAlign.CENTER,
                           value=f"Выберите тип гаммы:",
                           size=12,
                           weight=ft.FontWeight.W_100,
                           font_family="YanoneMedium"
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        scale
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=
                  [
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[0],
                           opacity_on_click=0.5,
                           on_click= change_scale1), width=125,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[1],
                           opacity_on_click=0.5,
                           on_click= change_scale2), width=125,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[2],
                           opacity_on_click=0.5,
                           on_click= change_scale3), width=125,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[3],
                           opacity_on_click=0.5,
                           on_click= change_scale4), width=125,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ],alignment=ft.MainAxisAlignment.CENTER),
                  
               ft.Row(
                  controls=[
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[4],
                           opacity_on_click=0.5,
                           on_click= change_scale5), width=120,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[5],
                           opacity_on_click=0.5,
                           on_click= change_scale6), width=120,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[6],
                           opacity_on_click=0.5,
                           on_click= change_scale7), width=120,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",),
                  ft.Container(content = ft.CupertinoButton(
                           content=scales_text[7],
                           opacity_on_click=0.5,
                           on_click= change_scale8), width=120,height=70,  padding=10, alignment=ft.alignment.center, bgcolor= "#D3C9C9",)
                  ],alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        ft.CupertinoButton(
                           content=ft.Text("Отправить", color="#000000", font_family="YanoneMedium"),
                           bgcolor= "#D3C9C9",
                           alignment=ft.alignment.center,
                           border_radius=ft.border_radius.all(0),
                           opacity_on_click=0.5,
                           on_click=route_to_root,
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               )
            
               ],alignment=ft.MainAxisAlignment.CENTER),bgcolor = '#464236', width=800,height=440)]),
#Корень гаммы(Высота тона гамы)
      '/root':View(
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
                           value=f"Введите корень гаммы(Высота тона гамы)",
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
                           on_click=route_to_PopulationSize,
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               )
               ],alignment=ft.MainAxisAlignment.CENTER),bgcolor = '#464236', width=800,height=440)]
      ),


#Размер популяции(Длина мелодий) 
      '/populationSize':View(
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
                           value=f"Введите размер популяции(количество мелодий):",
                           size=12,
                           weight=ft.FontWeight.W_100,
                           font_family="YanoneMedium"
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               ),
               ft.Row(
                  controls=[
                        population_size
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
                           on_click=route_to_result,
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               )
            
               ],alignment=ft.MainAxisAlignment.CENTER),bgcolor = '#464236', width=800,height=440)]),
         
      # populationSize
   }
