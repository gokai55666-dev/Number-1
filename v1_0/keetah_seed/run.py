from core.keetah_core import KeetahCore
from developer.self_developer import create_module

if __name__ == "__main__":
    # Initialize main Keetah core
    keetah = KeetahCore()
    print("Keetah Core initialized")

    # Example: generate a module
    result = create_module("gpu_manager", "Manages GPU allocation and workload")
    print(result)

    # Run one step of Keetah (simplified example)
    keetah.step()