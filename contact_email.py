'''module provides functionality for email'''
import re
from field import Field

class Email(Field):
    '''class for email'''
    def _check_email(self, email):
        '''validate string for email'''
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Is not valid email!")
        return email

    @Field.value.setter
    def value(self, value: str) -> None:
        try:
            self._value = self._check_email(value)
        except ValueError as e:
            raise e
