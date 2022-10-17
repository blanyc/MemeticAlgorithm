from abc import abstractmethod, ABC

class Function(ABC):
    @abstractmethod
    def CalculateValue(self, parameterA, parameterB):
        pass

