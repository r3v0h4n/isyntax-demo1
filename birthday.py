from field import Field
from datetime import datetime

class Birthday(Field):  

    @property
    def value(self) -> datetime:
        return self.__value

    @Field.value.setter
    def value(self, value: str) -> None:
        try:            
            self._value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self) -> str: 
        return self._value.strftime('%d.%m.%Y')