import flet as ft 

def main(page: ft.Page):
    BACKGROUNDCOLOR = "#464236"
    TEXTBUTTONCOLOR = "#D3C9C9"
    INPUTTEXTCOLOR = "#D9D9D9"
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

    container = ft.Container( content=
        ft.Column(
            [
                ft.Row(
                    controls=[
                        ft.Text(
                            text_align=ft.TextAlign.CENTER,
                            value=f"Generate melody",
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
                            # weight=ft.FontWeight.W_100,
                            font_family="YanoneMedium"
                        )
                    ],
                    width=80,
                    height = 200,
                    aligment = ft.alignment.top_center,
                    # alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                         ft.CupertinoButton(
                            content=ft.Text("Сгенерировать", color="#000000", font_family="YanoneMedium"),
                            bgcolor=TEXTBUTTONCOLOR,
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(0),
                            opacity_on_click=0.5,
                            on_click=lambda e: print("Filled CupertinoButton clicked!"),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
           
            
        ),
        alignment=ft.alignment.center
    )
    page.add(container )
    # container = ft.Container(
    #     width=300, 
    #     height= 300,
    #     content = ft.Stack(
    #         controls=[
    #             mainText = ft.Text('Генератор мелодий'),
    #             descriptionText = ft.Text("генератор позволяющий создавать мелодий с помощью нейросети"),
    #             mainButton = ft.CupertinoButton(content=ft.Text("Normal CupertinoButton", color=ft.cupertino_colors.DESTRUCTIVE_RED),
    #             opacity_on_click=0.3,
    #             on_click=lambda e: print("Normal CupertinoButton clicked!"),)
    #         ]
    #     )
    # )
    # page.add(container)

ft.app(target = main)
