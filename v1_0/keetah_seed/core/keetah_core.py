from core.improvement_loop import run_improvement_cycle
from memory.memory_manager import load_memory, save_memory
from body.body_state import KeetahBody
from environment.env_scanner import scan_environment


def run():

    print("Starting Keetah Seed System...\n")

    memory = load_memory()

    body = KeetahBody()

    env = scan_environment()

    report, ideas = run_improvement_cycle()

    memory["environment"] = env
    memory["last_report"] = report
    memory["ideas"] = ideas

    save_memory(memory)

    body.stimulate("clitoris",1)

    body.update_state()

    print("Environment:")
    print(env)

    print("\nCode Analysis:")
    print(report)

    print("\nImprovement Ideas:")

    for idea in ideas:
        print("-",idea)

    print("\nBody State:")
    print(body.state)