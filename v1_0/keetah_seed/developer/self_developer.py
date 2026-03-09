import os

def create_module(module_name, description):

    folder = "generated_modules"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, module_name + ".py")

    if os.path.exists(file_path):
        return f"Module {module_name} already exists."

    template = f'''
"""
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

    with open(file_path,"w") as f:
        f.write(template)

    return f"Created module: {module_name}"