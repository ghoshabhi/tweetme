from django.core.exceptions import ValidationError

# custom validation
def validate_content(value):
    content = value
    if content == "abc":
        raise ValidationError("Content cannot be 'abc'")
    return value
