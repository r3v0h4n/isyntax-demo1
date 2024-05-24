def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception as e:
            return "Unexpected error"
    return inner