class schedule : 
    def __init__(self,planning):
        self.monday= planning["monday"]
        self.tuesday= planning["tuesday"]
        self.wednesday= planning["wednesday"]
        self.thursday= planning["thursday"]
        self.friday= planning["friday"]
        self.saturday= planning["saturday"]
        self.sunday= planning["sunday"]
    
    def add_task(self,day,music,index):
        day_mapping = {
        "monday": self.monday,
        "tuesday": self.tuesday,
        "wednesday": self.wednesday,
        "thursday": self.thursday,
        "friday": self.friday,
        "saturday": self.saturday,
        "sunday": self.sunday
                        }
        
        hour_test=0
        for i in day_mapping[day]:
            hour_test+=i.lenght
        if hour_test+music.lenght>86400: #vérifie si le temps des musiques est supérieur au temps d'une journée
             return False
        else:
            day_mapping[day].insert(index,music)
    

