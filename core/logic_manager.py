
# Main logic
class logic_manager:

    # Constructor
    def __init__(self):
        self.__cardiac_frecuency = 0
        self.__x_gyroscope = 0
        self.__y_gyroscope = 0
        self.__z_gyroscope = 0
        self.__alarm_flag = False

    def set_frecuency(self, frecuency: int):
        self.__cardiac_frecuency = frecuency

    def get_frecuency(self) -> int:
        return self.__cardiac_frecuency
    
    def get_x(self) -> int:
        return self.__x_gyroscope
    
    def get_y(self) -> int:
        return self.__y_gyroscope
    
    def get_z(self) -> int:
        return self.__z_gyroscope

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
        
        if (self.__alarm_flag):
            print("[!] Alarma activada")
        else:
            print("[-] Alarma desactivada")

    # Verification
    def verification_flags(self, max_frecuency, x,y,z):

        if (self.get_frecuency() >= max_frecuency and
            self.get_x() >= x and
            self.get_y() >= y and
            self.get_z() >= z and
            not self.__alarm_flag):

            self.__alarm_flag = True
            print("[!] Alarma Activada")
        elif self.__alarm_flag and self.get_frecuency() <= 90:
            self.__alarm_flag = False
            print("[!] Alarma Desactivada")

#  \____/\
#  /\``/\
# -byRyanAg...