from abc import ABC, abstractmethod
from computer import Computer

class ComputerBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build_cpu(self):
        pass
        
    @abstractmethod
    def build_ram(self):
        pass
        
    @abstractmethod
    def build_storage(self):
        pass
        
    @abstractmethod
    def build_gpu(self):
        pass
        
    @abstractmethod
    def get_result(self):
        pass

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def reset(self):
        self.computer = Computer()
        
    def build_cpu(self):
        self.computer.cpu = "Intel Core i9"
        
    def build_ram(self):
        self.computer.ram = "32GB DDR5"
        
    def build_storage(self):
        self.computer.storage = "2TB NVMe SSD"
        
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"
        
    def get_result(self):
        result = self.computer
        self.reset()
        return result

class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def reset(self):
        self.computer = Computer()
        
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5"
        
    def build_ram(self):
        self.computer.ram = "16GB DDR4"
        
    def build_storage(self):
        self.computer.storage = "512GB SSD"
        
    def build_gpu(self):
        self.computer.gpu = "Integrated Graphics"
        
    def get_result(self):
        result = self.computer
        self.reset()
        return result
