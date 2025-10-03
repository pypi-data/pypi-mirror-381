import json
import os

from . import Token
from ._internal.ProtocolFile import ProtocolFile
from ._internal.TemplateFile import TemplateFile
from .common.constants import BOS_TOKEN, EOS_TOKEN, RUN_TOKEN, PAD_TOKEN, UNK_TOKEN
from .common.instructions.Instruction import Instruction
from .common.tokens.SpecialToken import SpecialToken
from .common.util import get_possible_emojis, hash_string, validate_string_set


class Protocol:
    """Model Training Protocol (MTP) class for creating the training configuration."""

    def __init__(self, name: str, context_lines: int, encrypt: bool = True):
        """
        Initialize the Model Training Protocol (MTP)

        :param name: The name of the protocol.
        :param context_lines: The number of lines in each instruction sample. Must be at least 2.
        :param encrypt: Whether to encrypt Tokens with unspecified with hashed keys. Default is True.
        """
        self.name: str = name
        self.context_lines: int = context_lines  # Number of lines in instruction samples
        self.encrypt: bool = encrypt
        if self.context_lines < 2:
            raise ValueError("A minimum of 2 context lines is required for all instructions.")
        self.context: list[str] = []
        self.tokens: set[Token] = set()
        self.instructions: set[Instruction] = set()
        self.guardrails: dict[str, list[str]] = dict()
        self.numbers: dict[str, str] = dict()
        self.none = None
        self.special_tokens: set[Token] = set()
        self.possible_emoji_keys: set[str] = get_possible_emojis()
        self.used_keys: set[str] = set()

    def add_context(self, context: str):
        """Adds a line of context to the model."""
        if not isinstance(context, str):
            raise TypeError("Context must be a string.")

        self.context.append(context)

    def add_instruction(self, instruction: Instruction):
        """
        Adds an Instruction (and its components) to the protocol.

        Asserts that all samples in the instruction match the defined sample line size.
        """
        if instruction in self.instructions:
            raise ValueError("Instruction already added to the protocol.")

        if len(instruction.samples) == 0:
            raise ValueError("Instruction must have at least three samples.")

        # Assert all samples match the defined sample line size
        for sample in instruction.samples:
            if not len(sample.context) == self.context_lines:
                raise ValueError(
                    f"Sample context lines ({len(sample.context)}) does not match defined context_lines count ({self.context_lines})"
                    f"\n{sample}."
                )

        # Add all tokens
        for token in instruction.get_tokens():
            if token not in self.tokens:
                self._add_token(token)

        # Add the instruction to the protocol
        self.instructions.add(instruction)

    def save(self, name: str | None = None, path: str | None = None):
        """
        Saves the protocol to a JSON file. This file can be submitted to Databiomes for model training.

        :param name: The name of the file (without extension). If None, uses the protocol's name.
        :param path: The directory path where the file will be saved. If None, saves in the current directory.
        """
        if name is None:
            name = self.name
        if path is None:
            path = os.getcwd()
        os.makedirs(path, exist_ok=True)
        filename = f"{path}\\{name}_model.json"

        self._prep_protocol()
        protocol_file: ProtocolFile = ProtocolFile(
            name=self.name, context=self.context, context_lines=self.context_lines,
            tokens=self.tokens, special_tokens=self.special_tokens, instructions=self.instructions,
        )

        print(f"Saving Model Train Protocol to {filename}...")
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(protocol_file.to_json(), file, indent=4, ensure_ascii=False)

    def template(self, path: str | None = None):
        """
        Create a template JSON file for the model training protocol.

        The template json file includes example usage and all possible combinations of model inputs and
        outputs based on the defined tokens and instructions.

        :param path: The directory path where the template file will be saved. If None, saves in the current directory.
        """
        if path is None:
            path = os.getcwd()
        filename = f"{path}\\{self.name}_template.json"

        self._prep_protocol()
        template_file: TemplateFile = TemplateFile(
            instructions=list(self.instructions),
            context_lines=self.context_lines
        )

        print(f"Saving Model Train Protocol Template to {filename}...")
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(template_file.to_json(), file, indent=4, ensure_ascii=False)

    def _assign_key(self, token: Token):
        """
        Assigns a key to a Token based on the protocol's encryption setting.

        :param token: The Token to assign the key of.
        """
        # If the user has assigned a key, use this key
        if token.key is not None:
            return

        if self.encrypt:
            # Generate a random key for the token if encrypting and no key is set
            token.key = hash_string(key=token.value, output_char=6)
        else:
            # Use the value as the key if not encrypting. I.e. Token 'Continue_' has key 'Continue_'
            token.key = token.value

    def _add_token(self, token: Token):
        """
        Adds a unique token to the protocol.

        Validates that the token's value and key are unique.
        :param token: The Token instance to add.
        """
        if token in self.tokens:
            raise ValueError(f"Token value '{token.value}' already used.")

        if token.key in self.used_keys:
            raise ValueError(f"Token key '{token.key}' already used.")

        self._assign_key(token=token)

        self.tokens.add(token)
        self.used_keys.add(token.key)

        if isinstance(token, SpecialToken):
            self.special_tokens.add(token)

    def _set_guardrails(self):
        """Sets all guardrails from TokenSets into the protocol."""
        # Add all guardrails to the protocol
        for instruction in self.instructions:
            if instruction.response.guardrail is not None:
                # instruction.response is the user TokenSet
                self.guardrails[instruction.response.key] = instruction.response.guardrail.format_samples()

    def _add_default_special_tokens(self):
        """Adds all special tokens to the protocol."""
        self.special_tokens.add(BOS_TOKEN)
        self.special_tokens.add(EOS_TOKEN)
        self.special_tokens.add(RUN_TOKEN)
        self.special_tokens.add(PAD_TOKEN)
        if len(self.guardrails) > 0:
            self.special_tokens.add(UNK_TOKEN)

    def _prep_protocol(self):
        """
        Sets all elements in the protocol before serialization.

        Raises errors if any validation checks fail.

        Setups up all necessary components in the protocol before saving or templating.

        This includes setting guardrails from their TokenSets and creating default special tokens.
        """
        if len(self.instructions) == 0:
            raise ValueError("No instructions have been added to Protocol. Call protocol.add_instruction() to add instructions.")

        self._set_guardrails()
        self._add_default_special_tokens()
        used_values: set[str] = {token.value for token in self.tokens}
        validate_string_set(used_values)
        validate_string_set(self.used_keys)
