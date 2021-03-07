#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:53:19 2021

@author: daniellapretorius
"""


from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string("""
<LoginScreen>:
    canvas.before:
        Color:
            rgb: 0x66 / 255.0, 0x85 / 255.0, 0x80 / 255.0     
        Rectangle:
            pos: self.pos
            size: self.size
        
    BoxLayout:
        id: login_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50
        
        Image:
            source: "Carbon.png"

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Username'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20

            TextInput:
                id: login
                multiline:False
                font_size: 28

        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 18
                text_size: root.width-20, 20

            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 28

        Button:
            text: 'Login'
            size_hint: (1, 0.4)
            font_size: 24
            on_press:  root.manager.current = 'menu'

<MenuScreen>:
    canvas.before:
        Color:
            rgb: 0x66 / 255.0, 0x85 / 255.0, 0x80 / 255.0     
        Rectangle:
            pos: self.pos
            size: self.size
            
    Image:
        source: "foot2.png"
    
    BoxLayout:
        Button:
            text: 'Homescreen'
            size_hint: (1, 0.3)
        Button:
            text: 'Challenges'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'challenges'
        Button:
            text: 'Scanner'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Inbox'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'inbox'
        Button:
            text: 'Quit'
            size_hint: (1, 0.3)
            on_press: app.stop()


<SettingsScreen>:
    #:import ZBarCam kivy_garden.zbarcam.ZBarCam
    #:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
    BoxLayout:
        orientation: 'vertical'
        ZBarCam:
            id: zbarcam
            # optional, by default checks all types
            code_types: ZBarSymbol.QRCODE, ZBarSymbol.EAN13
            Button:
                background_color: 0, 0.3, 0.2, 0.5 
                size_hint: (0.7, 0.1)
                pos_hint : {'x':1, 'bottom':.2}
                size: self.texture_size[0], 50
                text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
                on_press: root.manager.current = 'stats'
                
<StatScreen>:
    canvas.before:
        Color:
            rgb: 0x66 / 255.0, 0x85 / 255.0, 0x80 / 255.0     
        Rectangle:
            pos: self.pos
            size: self.size
            
    Image:
        source: "kiwi.png"
    
    BoxLayout:
        id: stat_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50

    Button:
        text: 'Back' 
        on_press: root.manager.current = 'menu'  
        size_hint: (1, 0.2)


<ChalScreen>:
    canvas.before:
        Color:
            rgb: 0x66 / 255.0, 0x85 / 255.0, 0x80 / 255.0     
        Rectangle:
            pos: self.pos
            size: self.size
            
    Image:
        source: "award.png"
            
    BoxLayout:
        Button:
            text: 'Homescreen'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Challenges'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'challenges'
        Button:
            text: 'Scanner'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Inbox'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'inbox'
        Button:
            text: 'Quit'
            size_hint: (1, 0.3)
            on_press: app.stop()         

<InboxScreen>:
    canvas.before:
        Color:
            rgb: 0x66 / 255.0, 0x85 / 255.0, 0x80 / 255.0     
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        Button:
            text: 'Homescreen'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Challenges'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'challenges'
        Button:
            text: 'Scanner'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Inbox'
            size_hint: (1, 0.3)
            on_press: root.manager.current = 'inbox'
        Button:
            text: 'Quit'
            size_hint: (1, 0.3)
            on_press: app.stop()        
    """)

            

# Declare all screens
class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class StatScreen(Screen):
    pass

class ChalScreen(Screen):
    pass

class InboxScreen(Screen):
    pass


class TestApp(App):  

    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(StatScreen(name='stats'))
        sm.add_widget(ChalScreen(name='challenges'))
        sm.add_widget(InboxScreen(name='inbox'))

        return sm

if __name__ == '__main__':
    TestApp().run()
