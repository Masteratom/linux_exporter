from helpers.LOAD_FILE import LOADFILE
import datetime


class System():
    def uptime_system(self):
        file = LOADFILE.load(self, directory='/proc/uptime')
        print(float(file.split(' ')[0]))
     #   uptime = str(datetime.timedelta(seconds=float(file.split(' ')[0])))
        return float(file.split(' ')[0])
    def unsame_system(self):
        pass
