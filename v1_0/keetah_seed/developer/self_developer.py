import os

def create_module(module_name: str, description: str) -> str:
    """
    Auto-generate a Python module for Keetah's self-development.
    Stores templates in generated_modules/
    """
    folder = "generated_modules"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, f"{module_name}.py")
    if os.path.exists(file_path):
        return f"Module {module_name} already exists."

    template = f'''"""
Auto-generated module by Keetah

Purpose:
{description}
"""

class {module_name.capitalize()}:

    def __init__(self):
        print("Module {module_name} initialized")

    def run(self):
        print("Running {module_name}")
'''
    with open(file_path, "w") as f:
        f.write(template)

    return f"Created module: {module_name}"