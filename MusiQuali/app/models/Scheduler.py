class Schedule:
    def __init__(self,planning):
        self.start_time= planning["start_time"]
        self.monday= planning["monday"]
        self.tuesday= planning["tuesday"]
        self.wednesday= planning["wednesday"]
        self.thursday= planning["thursday"]
        self.friday= planning["friday"]
        self.saturday= planning["saturday"]
        self.sunday= planning["sunday"]
    
    def add_task(self, day, music, index):
        day_list = getattr(self, day)
        hour_test = 0
        # On ignore le premier élément qui est l'heure de début (str)
        for i in day_list[1:]:
            hour_test += i.length
        if hour_test + music.length > 86400:
            return False
        day_list.insert(index + 1, music)
        return True

    def move_task(self, from_day, from_idx, to_day, to_idx):
        source = getattr(self, from_day)
        dest = getattr(self, to_day)
        # +1 car l'index 0 est l'heure de début
        item = source.pop(from_idx + 1)
        dest.insert(to_idx + 1, item)

    def get_day_data(self, day_name):
        """Calcule les positions et horaires pour l'affichage adaptatif."""
        day_list = getattr(self, day_name)
        start_time_str = day_list[0]
        h, m = map(int, start_time_str.split(':'))
        current_sec = h * 3600 + m * 60
        
        musics = []
        for m_obj in day_list[1:]:
            start_str = f"{current_sec//3600:02d}:{(current_sec%3600)//60:02d}"
            musics.append({
                'obj': m_obj,
                'time': start_str,
                'start_sec': current_sec,
                'duration': m_obj.length
            })
            current_sec += m_obj.length
        return {
            'start_offset_min': h * 60 + m,
            'musics': musics
        }

    def update_day(self, day, musics, start_time=None):
        day_list = getattr(self, day)
        if start_time is None:
            start_time = day_list[0]
        # On reconstruit la liste : heure de début + nouvelles musiques
        setattr(self, day, [start_time] + musics)

