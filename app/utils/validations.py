def validate(schema: dict, data: dict):
    errors = []

    fields = schema["fields"] if schema["fields"] is not None else schema.keys()
    required = schema.get("required", [])

    for field in required:
        if field not in data:
            errors.append({
                "code": "REQUIRED_FIELD_MISSING",
                "message": f"{field} es obligatorio",
                "level": "error",
                "description": None
            })

    for field, rules in fields.items():
        value = data.get(field)

        if value is None:
            continue

        expected_type = rules.get("type")
        if expected_type and not isinstance(value, expected_type):
            errors.append({
                "code": "INVALID_TYPE",
                "message": f"{field} tipo inválido",
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