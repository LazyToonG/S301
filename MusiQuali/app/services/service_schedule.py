from app.DAO.ScheduleDAO import ScheduleDAO
from app.models.Scheduler import Schedule
from app.models.Music import Music
import io

class ScheduleService:
    def __init__(self):
        self.schedule_dao = ScheduleDAO()
        self.schedule_dao.init_db()
        self.planning_model = self._load_planning()

    def _load_planning(self):
        planning_data = {"start_time": "00:00"}
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        for day in days:
            start_time = self.schedule_dao.get_start_time(day)
            items = self.schedule_dao.get_items_by_day(day)
            musics = []
            for item in items:
                musics.append(Music(item['title'], item['path'], item['duration'], item['artist']))
            planning_data[day] = [start_time] + musics
        return Schedule(planning_data)

    def get_planning(self):
        return self.planning_model

    def sync_day(self, day, tasks, start_time):
        # Mise à jour du Modèle en mémoire
        new_musics = []
        for t in tasks:
            new_musics.append(Music(t['title'], t.get('path', ''), int(t['duration']), t['artist']))
        self.planning_model.update_day(day, new_musics, start_time)

        # Mise à jour de la Base de Données via DAO
        self.schedule_dao.update_start_time(day, start_time)
        self.schedule_dao.clear_day_items(day)
        for i, t in enumerate(tasks):
            self.schedule_dao.add_item(day, i, t['title'], t['artist'], int(t['duration']), t.get('path', ''))

    def move_task(self, from_day, from_index, to_day, to_index):
        self.planning_model.move_task(from_day, from_index, to_day, to_index)

    def export_planning(self):
        days_order = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        mem_file = io.BytesIO()
        for day in days_order:
            day_data = getattr(self.planning_model, day)
            if not day_data: continue
            start_time = day_data[0]
            music_names = [m.titre for m in day_data[1:]]
            line = f"{day.capitalize()} : {start_time}, " + ", ".join(music_names) + "\n"
            mem_file.write(line.encode('utf-8'))
        mem_file.seek(0)
        return mem_file

service_schedule = ScheduleService()