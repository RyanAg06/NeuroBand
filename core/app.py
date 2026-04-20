
# Imports
from pynput import keyboard
from pynput.keyboard import Key
from core.logic_manaeger import logic_manager
from threading import Thread

# App
class App:

    # Import logic
    logic = logic_manager()

    # Constructor
    def __init__(self):
        self.__running = False
        self.__listener = None

    # Start app
    def start(self):

        # Verification if already running
        if self.__running:
            print(f"Ya esta corriendo")
            return
        
        # Create and start listener
        self.__running = True
        self.__listener = keyboard.Listener(on_press=self.__on_press)
        self.__listener.start()
        self.__listener.join()

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
        print(str(key).replace("'",""))

        # Stop key
        if key == Key.esc:
            print("App detenida")
            self.stop()