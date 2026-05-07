
# Imports
from time import sleep
from random import random
from pynput import keyboard
from pynput.keyboard import Key
from core.logic_manager import logic_manager
from threading import Thread

# Keys detector
class keys_detector_manager:

    # Constructor
    def __init__(self):
        self.logic = None
        self.__listener = None
        self.__running = False
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
                    self.logic.set_frecuency(self.__maximum_frecuency - 1)
                    self.__maximum_frecuency -= int(random() * 4)

                # Generate normal frecuency
                else:
                    frecuency = 80 + int(random() * 9)
                    self.__maximum_frecuency = frecuency
                    self.logic.set_frecuency(frecuency)

    def get_maximun(self):
        return self.__maximum_frecuency

    # Start app
    def start(self):

        # Verification if already running
        if self.__running:
            print(f"Ya esta corriendo")
            return
        
        # Start
        self.logic = logic_manager()
        self.__running = True

        # Create Therad for simulate cardiac frecuency
        hilo = Thread(target=self.normal_frecuency, daemon=True)
        hilo.start()
        
        # Create and start listener
        self.__listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release)
        self.__listener.start()

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

        # Increse Frecuency Cardiac
        if char == 'a':
            self.logic.increase_frecuency()
            self.__maximum_frecuency = self.logic.get_frecuency()

        # Increase Gyroscope
        if char == 's':
            self.logic.increase_gyroscope()

        # Increase Both
        if char == "d":
            self.logic.increase_both()

        # Toggle Alarm
        if char == "w":
            self.logic.toggle_alarm()

    # On_Release event
    def __on_release(self, key):
        self.__pressing = False

#  \____/\
#  /\``/\
# -byRyanAg...