
# Main logic
class logic_manager:

    # Constructor
    def __init__(self):
        self.__cardiac_frecuency = 0
        self.__x_gyroscope = 0
        self.__y_gyroscope = 0
        self.__z_gyroscope = 0
        self.__frecency_flag = False
        self.__gyroscope_flag = False
        self.__alarm_flag = False

    def set_frecuency(self, frecuency: int):
        self.__cardiac_frecuency = frecuency

    def get_frecuency(self):
        return self.__cardiac_frecuency

    # increase frecuency
    def increase_frecuency(self, increase=1):
        self.__cardiac_frecuency += increase
        print(f"Frecuencia actual: {self.__cardiac_frecuency}")

    # increase gyroscope values
    def increase_gyroscope(self, increase=1):
        self.__x_gyroscope += increase
        self.__y_gyroscope += increase
        self.__z_gyroscope += increase
        print(f"X={self.__x_gyroscope}     Y={self.__y_gyroscope}     Z={self.__z_gyroscope}")

    def increase_both(self, value=1):
        self.increase_frecuency(increase=value)
        self.increase_gyroscope(increase=value)
    
    # Toggle alarm
    def toggle_alarm(self):
        self.__alarm_flag = not self.__alarm_flag
        print(f"Estado alarma: {self.__alarm_flag}")

    # Verification
    def verification_flags(self):
        if self.__frecency_flag and self.__gyroscope_flag:
            self.__alarm_flag = True
            print("[!] Alarma Activada")