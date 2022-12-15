class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item): #fazendo Duck Typing e realizando composição/extensao em nossa classe
        return self._programas[item]

    def __len__(self): #fazendo Duck Typing e realizando composição/extensao em nossa classe
        return len(self._programas)