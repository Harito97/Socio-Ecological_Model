import sys
import numpy as np
from src.models.models import GSSEMModel
from src.utils.plot_utils import plot

def main():
    model = GSSEMModel(time=100)

    if len(sys.argv) != 2:
        print("Argv != 2")
        print("Usage: python main.py [show_params|show_docs|run_simulation]")
        sys.exit(1)

    elif sys.argv[1] == "show_params":
        print()
        model.params.print_params()
        sys.exit(0)
    
    elif sys.argv[1] == "show_docs":
        print("Model documentation:")
        model.simulation_docs()
        sys.exit(0)

    elif sys.argv[1] == "run_simulation":
        # Run simulation
        x, y = model.run_simulation()
        print("Simulation completed.")
        x = np.array(x)
        y = np.array(y)
        print("x: ", x)
        print(x.shape)
        print("y: ", y)
        print(y.shape)
        plot(x, y)
        sys.exit(0)
        
    else:
        print("Invalid command.")
        print("Usage: python main.py [show_params|show_docs|run_simulation]")
        sys.exit(1)


if __name__ == "__main__":
    main()