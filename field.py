class Field:
    def __init__(self, value: str) -> None:
        self._value = None
        self.value = value

    def __str__(self) -> str:
        return str(self._value)
    
    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, value: str) -> None:
        self._value = value