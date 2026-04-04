from director import Director
from builder import GamingComputerBuilder, OfficeComputerBuilder

if __name__ == "__main__":
    director = Director()
    
    print("Building a full-featured Gaming Computer:")
    gaming_builder = GamingComputerBuilder()
    director.builder = gaming_builder
    director.build_full_featured_computer()
    gaming_computer = gaming_builder.get_result()
    print(gaming_computer)
    
    print("\nBuilding a minimal viable Office Computer:")
    office_builder = OfficeComputerBuilder()
    director.builder = office_builder
    director.build_minimal_viable_computer()
    office_computer = office_builder.get_result()
    print(office_computer)
