class alarm_clock:
    def __init__(self):
        self.current_time = '0000'
        self.alarm_on = False
        self.alarm_time = '0000'

    def set_time(self):
        self.current_time = input(f'Current time is {self.current_time}. Please set your desired time.').lower().strip()
        if self.current_time != '0000':
            print(f'{self.current_time} is the set time.')
        
    def set_alarm_time(self):
        self.alarm_time = input(f'Alarm is set to {self.alarm_time}. Please enter your desired alarm time').lower().strip()
        if self.alarm_time != '0000':
            print(f'The alarm is set to {self.alarm_time}')
    
    def alarm_check(self):
        if self.alarm_time != '0000':
            self.alarm_on = True
        else:
            self.alarm_on = False

    def toggle_alarm(self):
        while self.alarm_on == True:
            user_input = input(f'Alarm is set to {self.alarm_time}, would you like to toggle the alarm off?').lower().strip()
            if user_input == 'no':
                print(f'The alarm will stay on and set to {self.alarm_time}')
                self.alarm_on = True
                break
            elif user_input == 'yes':
                print('The alarm is toggled off.')
                self.alarm_on = False
                return False
            else:
                print('Unrecognized input.')
                self.alarm_on = True