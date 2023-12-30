from helpers.LOAD_FILE import LOADFILE
import os


class CPUMETRICSE():

    def load_cpu(self):
        # TODO: wyciągnoąć dane c CPU. Zrobić tak by nie trzeba było pobierać za każdym razem ile jest CPU. Zrobić to raz i koniec. Zbezpieczyć to.
        cpu_list = []
        USER_HZ = os.sysconf(os.sysconf_names['SC_CLK_TCK'])
        quantity_cpu = LOADFILE.load(self, directory='/sys/devices/system/cpu/present')
        quantity_cpu = quantity_cpu.split('-')
        quantity_cpu = quantity_cpu[1].replace('\n', '')
        file = LOADFILE.load(self, directory='/proc/stat')
        file_parse = file.split('\n')
        for x in file_parse:
            print(x)


# #Obliczenie:
#
#     zsumuj wszystkie kolumny w pierwszej linii „ cpu ”:
#     ( user + nice + system + idle + iowait + irq + softirq )
#     zapewni to 100% czasu procesora
#     oblicz średni procent całkowitego „ bezczynności ” ze 100% czasu procesora: ( user + nice + system + idle + iowait + irq + softirq ) = 100%( idle ) = X %
#     stąd
#     average idle percentage X % = ( idle * 100 ) / ( user + nice + system + idle + iowait + irq + softirq )
#
#     Bazując na powyższym przykładzie :
#     average idle percentage X % = ( 842486413 * 100 ) / ( 79242 + 0 + 74306 + 842486413 + 756859 + 6140 + 67701 + 0 ) = ( 842486413100 ) / ( 843470661 ) = 99.8833 %


# https://stackoverflow.com/questions/23367857/accurate-calculation-of-cpu-usage-given-in-percentage-in-linux
# https://medium.com/@yogita088/how-to-calculate-cpu-usage-proc-stat-vs-top-e74f99f02d08