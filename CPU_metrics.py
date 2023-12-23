from helpers.LOAD_FILE import LOADFILE


class CPUMETRICSE():

    def load_cpu(self):
        file = LOADFILE.load(self, directory='/proc/stat')
        file_parse = file.split('\n')
        for x in file_parse:
            if 'cpu' in x:
                parse_x = x.split()
                print(parse_x)

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