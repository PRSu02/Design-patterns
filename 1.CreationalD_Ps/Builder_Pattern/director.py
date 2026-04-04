class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_minimal_viable_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()

    def build_full_featured_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()
