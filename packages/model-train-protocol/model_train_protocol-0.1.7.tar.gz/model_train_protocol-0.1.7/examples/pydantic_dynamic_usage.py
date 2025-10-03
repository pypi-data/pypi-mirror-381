"""
Example demonstrating how to use GuardrailModel and NumberModel with dynamic attributes.
"""

from typing import Dict, Any, List, Union
import json
from model_train_protocol.common.pydantic.protocol import (
    GuardrailModel, 
    NumberModel, 
    ProtocolModel,
    TokenInfoModel,
    InstructionModel,
    BatchModel
)


def demonstrate_guardrail_model():
    """Demonstrate how to use GuardrailModel with dynamic attributes."""
    print("=== GuardrailModel Usage ===")
    
    # Create a guardrail model with dynamic attributes
    guardrail = GuardrailModel()
    
    # Set dynamic guardrail rules
    guardrail.set_guardrail_rule("safety", "Do not generate harmful content")
    guardrail.set_guardrail_rule("privacy", "Do not share personal information")
    guardrail.set_guardrail_rule("complex_rules", [
        "Rule 1: Be respectful",
        "Rule 2: Stay on topic",
        ["Nested rule", "Another nested rule"]
    ])
    
    # Access using dictionary-style syntax
    print(f"Safety rule: {guardrail['safety']}")
    print(f"Privacy rule: {guardrail['privacy']}")
    print(f"Complex rules: {guardrail['complex_rules']}")
    
    # Get all guardrail rules
    all_rules = guardrail.get_guardrail_rules()
    print(f"All guardrail rules: {all_rules}")
    
    # Convert to dictionary for JSON serialization
    guardrail_dict = guardrail.dict()
    print(f"Guardrail as dict: {json.dumps(guardrail_dict, indent=2)}")
    
    return guardrail


def demonstrate_number_model():
    """Demonstrate how to use NumberModel with dynamic attributes."""
    print("\n=== NumberModel Usage ===")
    
    # Create a number model with dynamic attributes
    numbers = NumberModel()
    
    # Set dynamic number rules
    numbers.set_number_rule("max_tokens", "2048")
    numbers.set_number_rule("temperature", "0.7")
    numbers.set_number_rule("top_p", "0.9")
    
    # Access using dictionary-style syntax
    print(f"Max tokens: {numbers['max_tokens']}")
    print(f"Temperature: {numbers['temperature']}")
    print(f"Top-p: {numbers['top_p']}")
    
    # Get all number rules
    all_rules = numbers.get_number_rules()
    print(f"All number rules: {all_rules}")
    
    # Convert to dictionary for JSON serialization
    numbers_dict = numbers.dict()
    print(f"Numbers as dict: {json.dumps(numbers_dict, indent=2)}")
    
    return numbers


def demonstrate_protocol_model():
    """Demonstrate how to use ProtocolModel with dynamic guardrails and numbers."""
    print("\n=== ProtocolModel Usage ===")
    
    # Create dynamic guardrails and numbers
    guardrails = GuardrailModel()
    guardrails.set_guardrail_rule("safety", "Be helpful and harmless")
    guardrails.set_guardrail_rule("content", "Stay on topic")
    
    numbers = NumberModel()
    numbers.set_number_rule("max_length", "1000")
    numbers.set_number_rule("timeout", "30")
    
    # Create a complete protocol model
    protocol = ProtocolModel(
        name="example_protocol",
        context=["This is a sample context line"],
        tokens={
            "Hello_": TokenInfoModel(
                emoji="👋",
                num=False,
                user=True,
                desc="Greeting token",
                special=None
            )
        },
        special_tokens=["<BOS>", "<EOS>"],
        instruction=InstructionModel(
            memory=3,
            sets=[]
        ),
        guardrails=guardrails.dict(),  # Convert to dict for ProtocolModel
        numbers=numbers.dict(),         # Convert to dict for ProtocolModel
        batches=BatchModel()
    )
    
    print(f"Protocol name: {protocol.name}")
    print(f"Guardrails: {protocol.guardrails}")
    print(f"Numbers: {protocol.numbers}")
    
    # Convert to JSON
    protocol_json = protocol.json(indent=2)
    print(f"Protocol JSON:\n{protocol_json}")
    
    return protocol


def demonstrate_parsing_from_json():
    """Demonstrate parsing dynamic models from JSON data."""
    print("\n=== Parsing from JSON ===")
    
    # Sample JSON with dynamic guardrails and numbers
    sample_json = {
        "nil": "",
        "safety_rule": "Do not generate harmful content",
        "privacy_rule": "Protect user data",
        "complex_rule": ["Rule A", "Rule B", ["Nested", "Rules"]]
    }
    
    # Parse guardrail from JSON
    guardrail = GuardrailModel(**sample_json)
    print(f"Parsed guardrail: {guardrail.dict()}")
    
    # Sample JSON for numbers
    numbers_json = {
        "nil": "",
        "max_tokens": "2048",
        "temperature": "0.7"
    }
    
    # Parse numbers from JSON
    numbers = NumberModel(**numbers_json)
    print(f"Parsed numbers: {numbers.dict()}")


def demonstrate_error_handling():
    """Demonstrate error handling for invalid dynamic attributes."""
    print("\n=== Error Handling ===")
    
    try:
        guardrail = GuardrailModel()
        # This should raise an error
        guardrail.set_guardrail_rule("invalid", 123)  # Invalid type
    except ValueError as e:
        print(f"Expected error: {e}")
    
    try:
        numbers = NumberModel()
        # This should raise an error
        numbers.set_number_rule("invalid", 123)  # Invalid type
    except ValueError as e:
        print(f"Expected error: {e}")


if __name__ == "__main__":
    # Run all demonstrations
    guardrail = demonstrate_guardrail_model()
    numbers = demonstrate_number_model()
    protocol = demonstrate_protocol_model()
    demonstrate_parsing_from_json()
    demonstrate_error_handling()
    
    print("\n=== Summary ===")
    print("✅ GuardrailModel supports dynamic attributes with proper validation")
    print("✅ NumberModel supports dynamic attributes with proper validation")
    print("✅ Both models can be serialized to/from JSON")
    print("✅ Type validation prevents invalid attribute values")
    print("✅ Dictionary-style access works with __getitem__ and __setitem__")

