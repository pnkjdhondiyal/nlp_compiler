def generate_python_code(operation, variables):
    if len(variables) != 2:
        return "print('Error: Invalid number of operands')"

    var1, var2 = variables

    operation_map = {
        "add": f"print({var1} + {var2})",
        "subtract": f"print({var1} - {var2})",
        "multiply": f"print({var1} * {var2})",  # ✅ Add multiplication support
        "divide": f"print({var1} / {var2}) if {var2} != 0 else print('Error: Division by zero')"
    }

    return operation_map.get(operation, "print('Error: Unsupported operation')")  # ✅ Ensure "multiply" is mapped
