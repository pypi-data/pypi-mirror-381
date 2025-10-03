from .Token import Token


class NumToken(Token):
    def __init__(self, value: str, min_value: int | float, max_value: int | float, key: str | None = None,
                 desc: str | None = None):
        """
        Initializes a NumToken instance.

        A NumToken is a subclass of Token that includes an additional 'num' attribute
        to indicate if the token is associated with a numerical value.

        :param value: The string representing the token's value.
        :param min_value: The minimum numerical value the token can represent.
        :param max_value: The maximum numerical value the token can represent.
        :param key: Optional key associated with the token, a symbol, emoji, or short string.
        :param desc: Optional description of the token. Extends the value to contextualize its use.
        """
        super().__init__(value, key, desc)
        self.num: int = 1
        self.min_value = min_value
        self.max_value = max_value
        self.protocol_representation: str = f"<Number between {min_value} and {max_value}>"

    def __eq__(self, other):
        """Equality comparison for NumToken."""
        if not isinstance(other, NumToken):
            return False
        return self.value == other.value and self.key == other.key and self.desc == other.desc and self.num == other.num and self.protocol_representation == other.protocol_representation and self.min_value == other.min_value and self.max_value == other.max_value

    def __hash__(self):
        """Hash based on the string representation of the NumToken."""
        return hash((self.value, self.key, self.desc, self.num, self.min_value, self.max_value, self.protocol_representation))