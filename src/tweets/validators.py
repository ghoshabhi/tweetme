from django.core.exceptions import ValidationError

# implement validation for curse words
# custom validation
def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("Content cannot be blank")
    return value
