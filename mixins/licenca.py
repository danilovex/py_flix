# Mixins, que são apenas classes que podem ser herdadas mas que não devem ser instanciadas
# Servem para disponibilizar comportamentos para outras classes
class Licenca:
    def direitos_autorais(self):
        return f'Marvel Studios 2000 ({self.nome} Producao)'