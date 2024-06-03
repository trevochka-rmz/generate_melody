import flet as ft
from views import views_hadler

def main(page: ft.Page):
   BACKGROUNDCOLOR = "#464236"
   TEXTBUTTONCOLOR = "#D3C9C9"
   INPUTTEXTCOLOR = "#D9D9D9"

   num_bars = ft.TextField(label="Введите количество тактов(Длина мелодии):",width =400)
   num_notes = ft.TextField(label="Введите количество нот в такте:",width =400)
   # num_steps = ft.TextField(label="Введите количество высот в ноте:",width =400)
   pauses = ft.TextField(label="Добавить паузы:",width =400)
   key = ft.TextField(label="Введите тональность гаммы:",width =400)
   scale = ft.TextField(label="Введите тип гаммы:",width =400)
   root = ft.TextField(label="Введите высоту тона гаммы:",width =400)
   population_size = ft.TextField(label="Введите размер популяции(количество мелодий):",width =400)
   num_mutations = ft.TextField(label="Введите количество мутаций(Максимальное количество мутаций):",width =400)
   mutation_probability = ft.TextField(label="Введите вероятность возникновения мутации:",width =400)

   page.fonts = {
      "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
      "YanoneBold":"https://github.com/yanone/kaffeesatz/blob/master/fonts/ttf/YanoneKaffeesatz-Bold.ttf",
      "YanoneSemiBold":"https://github.com/yanone/kaffeesatz/blob/master/fonts/ttf/YanoneKaffeesatz-SemiBold.ttf",
      "YanoneMedium":"https://github.com/yanone/kaffeesatz/blob/master/fonts/ttf/YanoneKaffeesatz-Medium.ttf",
      "YanoneRegular":"https://github.com/yanone/kaffeesatz/blob/master/fonts/ttf/YanoneKaffeesatz-Regular.ttf",
      "YanoneLight":"https://github.com/yanone/kaffeesatz/blob/master/fonts/ttf/YanoneKaffeesatz-Light.ttf"        
   }


   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.title = "Генератор мелодий"
   page.bgcolor = BACKGROUNDCOLOR
   page.window_width = 800
   page.window_height=500
   page.window_resizable = False  
   page.update()

   def route_change(e):
      print(page.route)
      page.views.clear()
      page.views.append(
         views_hadler(page)[page.route]
      )
      
   def route_to_numNotes(e):
      page.on_route_change = route_change 
      page.go('/num_notes')
      page.update()
   def route_to_numBars(e):
      page.on_route_change = route_change
      page.go('/num_bars')
      page.update()
   def route_to_main(e):
      page.on_route_change = route_change
      page.go('/')
      page.update()

   container = ft.Container( content=
      ft.Column(
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
                           value=f"генератор позволяющий создавать мелодий с помощью нейросети",
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
                        ft.CupertinoButton(
                           content=ft.Text("Сгенерировать", color="#000000", font_family="YanoneMedium"),
                           bgcolor=TEXTBUTTONCOLOR,
                           alignment=ft.alignment.center,
                           border_radius=ft.border_radius.all(0),
                           # opacity_on_click=0.5,
                           
                           on_click=route_to_numBars,
                        
                     )
                  ],
                  alignment=ft.MainAxisAlignment.CENTER
               )
         ],alignment=ft.MainAxisAlignment.CENTER
         
         
      ),
      alignment=ft.alignment.center, bgcolor = '#464236', width=800,height=440)
   page.add(container)
   page.on_route_change = route_change
   # page.go('/num_bars')
   page.update()
   # page.on_route_change = route_change
   # page.go('/num_bars')
   # page.update()
   

   # user = ft.Text("Info", color ="#fafafa")
   
   # page.add(
   #    ft.Container(margin=10,
   #                padding=10,
   #                width=400,
   #                height=400,
   #                content = ft.Column(
   #       [
   #          ft.Text("Генератор мелодий"),
   #          ft.Text("генератор позволяющий создавать мелодий с помощью нейросети"),
   #          ft.FilledButton("Сгенерировать", disabled=True)
   #       ],
         
   #    ))
      
      # ft.Row(
      #    [
      #       user,
      #       ft.TextField(value="0", width=150, text_align=ft.TextAlign.LEFT)
      #    ],
      #    alignment=ft.MainAxisAlignment.CENTER
      # ) 
   # )

   #
ft.app(target=main)
