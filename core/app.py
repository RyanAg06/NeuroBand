
# Imports
from time import sleep
from random import random
from pynput import keyboard
from pynput.keyboard import Key
from core.logic_manager import logic_manager
from threading import Thread

# App
class App:

    # Constructor
    def __init__(self):
        self.__logic = logic_manager()
        self.__running = False
        self.__listener = None
        self.__pressing = False
        self.__maximum_frecuency = 0

    # Generate normal cardiac frecuency
    def normal_frecuency(self):
        while(self.__running):
            sleep(1)

            # If not pressing
            if not self.__pressing:
            
                # Decrease frecuency if max-frec > 87
                if self.__maximum_frecuency > 87:
                    self.__logic.set_frecuency(self.__maximum_frecuency-1)
                    self.__maximum_frecuency -= 1
                    print(self.__logic.get_frecuency())

                # Generate normal frecuency
                else:
                    frecuency = 80 + int(random() * 9)
                    self.__maximum_frecuency = frecuency
                    self.__logic.set_frecuency(frecuency)
                    print(frecuency)


    # Start app
    def start(self):

        # Verification if already running
        if self.__running:
            print(f"Ya esta corriendo")
            return
        
        self.__running = True
        
        # Generate normal cardiac frecuency
        hilo = Thread(target=self.normal_frecuency, daemon=True)
        hilo.start()
        
        # Create and start listener
        self.__listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release)
        self.__listener.start()
        self.__listener.join()

    # Stop app
    def stop(self):

        # Verification is not running
        if not self.__running:
            print(f"No se esta ejecutando")
            return
        
        # Stop listener
        self.__running = False
        self.__listener.stop()

    # On-Press event
    def __on_press(self, key):

        # Get current key
        char = getattr(key, "char", None)
        self.__pressing = True

        # Stop key
        if key == Key.esc:
            print("App detenida")
            self.stop()

        # Increse Frecuency Cardiac
        if char == 'a':
            self.__logic.increase_frecuency()
            self.__maximum_frecuency = self.__logic.get_frecuency()

        # Increase Gyroscope
        if char == 's':
            self.__logic.increase_gyroscope()

        # Increase Both
        if char == "d":
            self.__logic.increase_both()

        # Toggle Alarm
        if char == "w":
            self.__logic.toggle_alarm()

    # On_Release event
    def __on_release(self, key):
        self.__pressing = False