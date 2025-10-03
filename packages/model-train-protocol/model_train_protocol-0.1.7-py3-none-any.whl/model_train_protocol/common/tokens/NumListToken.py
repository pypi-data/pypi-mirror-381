from .NumToken import NumToken


class NumListToken(NumToken):
    def __init__(self, value: str, min_value: int | float, max_value: int | float, length: int,
                 key: str | None = None, desc: str | None = None):
        """
        Initializes a NumListToken instance.

        A NumListToken is a special type of NumToken that represents a list of numbers.

        :param value: The string representing the token's value.
        :param min_value: The minimum numerical value an element in the list can represent.
        :param max_value: The maximum numerical value an element in the list can represent.
        :param length: The number of elements in the list.
        :param key: Optional key associated with the token, a symbol, emoji, or short string.
        :param desc: Optional description of the token. Extends the value to contextualize its use.
        """
        super().__init__(value=value, key=key, min_value=min_value, max_value=max_value, desc=desc)
        self.num: int = length
        self.protocol_representation: str = f"<List of length {length} of numbers between {min_value} and {max_value}>"
