from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_string("""
<RainbowApp>:
    BoxLayout:
        size: (360,800)
        orientation: 'vertical'
        Label:
            id: labelColor
            text: 'Hello!'
            font_size: 20
        TextInput:
            id: textInputHEX
            font_size: 20
            padding_y: 30
            halign: 'center'
        Button:
            text: '#ff0000'
            font_size: 20
            background_normal: ''
            background_color: (1,0,0,1)
            on_press:
                labelColor.text = 'Красный'
                labelColor.color = (1,0,0,1)
                textInputHEX.text = '#ff0000'
        Button:
            text: '#ff8800'
            font_size: 20
            background_normal: ''
            background_color: (1,0.53,0,1)
            on_press:
                labelColor.text = 'Оранжевый'
                labelColor.color = (1,0.53,0,1)
                textInputHEX.text = '#ff8800'
        Button:
            text: '#ffff00'
            font_size: 20
            background_normal: ''
            background_color: (1,1,0,1)
            on_press:
                labelColor.text = 'Желтый'
                labelColor.color = (1,1,0,1)
                textInputHEX.text = '#ffff00'
        Button:
            text: '#00ff00'
            font_size: 20
            background_normal: ''
            background_color: (0,1,0,1)
            on_press:
                labelColor.text = 'Зелёный'
                labelColor.color = (0,1,0,1)
                textInputHEX.text = '#00ff00'
        Button:
            text: '#00ffff'
            font_size: 20
            background_normal: ''
            background_color: (0,1,1,1)
            on_press:
                labelColor.text = 'Голубой'
                labelColor.color = (0,1,1,1)
                textInputHEX.text = '#00ffff'
        Button:
            text: '#0000ff'
            font_size: 20
            background_normal: ''
            background_color: (0,0,1,1)
            on_press:
                labelColor.text = 'Синий'
                labelColor.color = (0,0,1,1)
                textInputHEX.text = '#0000ff'
        Button:
            text: '#ff00ff'
            font_size: 20
            background_normal: ''
            background_color: (1,0,1,1)
            on_press:
                labelColor.text = 'Фиолетовый'
                labelColor.color = (1,0,1,1)
                textInputHEX.text = '#ff00ff'
""")


class RainbowApp(BoxLayout):
    pass


class myApp(App):
    def build(self):
        Window.size = (360, 800)
        Window.top = 30
        Window.left = 600
        return RainbowApp()


if __name__ == "__main__":
    myApp().run()