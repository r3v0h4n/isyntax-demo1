from field import Field

class Phone(Field):

    @Field.value.setter
    def value(self, value: str) -> None:
        if not value.isdigit():
            raise ValueError("Phone must be numeric!")
        
        if len(value) != 10:
            raise ValueError("Phone must have 10 digits!")    
        self._value = value