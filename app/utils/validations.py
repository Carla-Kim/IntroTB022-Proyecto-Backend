from datetime import datetime
import re

TYPE_MAP = {
    "string": str,
    "integer": int,
    "float": float,
    "boolean": bool
}

def is_valid_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_email(value):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value) is not None

FORMAT_VALIDATORS = {
    "date": is_valid_date,
    "email": is_valid_email
}

def validate_schema(schema: dict, **data):
    errors = []

    for field, rules in schema.items():
        value = data.get(field)

        if value is None:
            continue

        expected_type = rules.get("type")
        if expected_type:
            py_type = TYPE_MAP.get(expected_type)

            if py_type and not isinstance(value, py_type):
                errors.append({
                    "code": "INVALID_TYPE",
                    "message": f"{field} tipo inválido",
                    "level": "error",
                    "description": None
                })
                continue

        format_type = rules.get("format")
        if format_type:
            validator = FORMAT_VALIDATORS.get(format_type)

            if validator and not validator(value):
                errors.append({
                    "code": "INVALID_FORMAT",
                    "message": f"{field} formato inválido ({format_type})",
                    "level": "error",
                    "description": None
                })

        if "min" in rules and value < rules["min"]:
            errors.append({
                "code": "MIN_VALUE",
                "message": f"{field} debe ser >= {rules['min']}",
                "level": "error",
                "description": None
            })

        if "enum" in rules and value not in rules["enum"]:
            errors.append({
                "code": "INVALID_VALUE",
                "message": f"{field} valor no permitido.",
                "level": "error",
                "description": None
            })

    return errors
