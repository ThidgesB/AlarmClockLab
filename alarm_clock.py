class alarm_clock:
    def __init__(self):
        self.current_time = ''
        self.alarm_on = False
        self.alarm_off = True
        self.alarm_time = ''

    def set_time(self):
        self.current_time = input('Current time is not set. Please set the desired time.')
        self.alarm_time = input('Please set the desired alarm time.')

    def alarm_check(self):
        if self.alarm_time != '':
            self.alarm_on = True
            self.alarm_off = False
        else:
            self.alarm_off = True
            self.alarm_on = False
