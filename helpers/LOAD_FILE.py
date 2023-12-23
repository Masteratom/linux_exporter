class LOADFILE:

    def load(self, directory):
        with open(directory, encoding="utf-8") as f:
            read_data = f.read()
        return read_data
