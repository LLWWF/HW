class AlarmClock:
    def __init__(self):
        self._current_time = "00:00"
        self._alarm_time = "00:00"
    
    @property
    def current_time(self):
        return self._current_time
    
    def current_time(self, time_str):
        if self._validate_time_format(time_str):
            self._current_time = time_str
        else:
            print("Неверный формат времени. Используйте ЧЧ:ММ")
    
    @property
    def alarm_time(self):
        return self._alarm_time
    
    @alarm_time.setter
    def alarm_time(self, time_str):
        if self._validate_time_format(time_str):
            self._alarm_time = time_str
        else:
            print("Неверный формат времени. Используйте ЧЧ:ММ")
    
    def _validate_time_format(self, time_str):
        if not isinstance(time_str, str) or len(time_str) != 5:
            return False
        
        if time_str[2] != ':':
            return False
        
        hours, minutes = time_str.split(':')
        
        if not (hours.isdigit() and minutes.isdigit()):
            return False
        
        h = int(hours)
        m = int(minutes)
        
        return 0 <= h <= 23 and 0 <= m <= 59
    
    def set_time(self, time_str):
        self.current_time = time_str
    
    def set_alarm(self, time_str):
        self.alarm_time = time_str
    
    def check_alarm(self):
        return self._current_time == self._alarm_time