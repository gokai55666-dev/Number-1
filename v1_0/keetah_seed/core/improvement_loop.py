from analysis.code_analyzer import scan_previous_code
from build.module_generator import suggest_modules

def run_improvement_cycle():

    folder = "user_code/previous_scripts"

    report = scan_previous_code(folder)

    ideas = suggest_modules(report)

    return report, ideas