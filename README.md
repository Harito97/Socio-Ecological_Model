# Socio-Ecological Model

## Introduction

This paper presents a Python implementation of a comprehensive Generalized Sustainability Socio-Ecological Model (GSSEM) that integrates economic, social, and climate change factors.

The original model was developed in MATLAB (the source code is available at [Generalized Sustainability Socio-Ecological Model GSSEM](https://github.com/TenochRdz/-Generalized-Sustainability-Socio-Ecological-Model-GSSEM-)). However, MATLAB's limitations in accessibility and the lack of modularity in the original code - the authors of the paper coded poorly, making the code difficult to read - prompted me to create this Python version.

This Python implementation emphasizes:

  - **Modularity:** The code is well-structured with distinct modules, promoting readability and maintainability.
  - **Functionality Separation:** Different functionalities are separated into dedicated functions, improving organization and clarity.

While the complete code might reside within a single file for simplicity, the modular structure ensures better organization and understanding.

## Running the Model

**Prerequisites:**

- Python 3.x installed ([https://www.python.org/downloads/](https://www.google.com/url?sa=E&source=gmail&q=https://www.python.org/downloads/))

- Needed library: numpy, matplotlib
  
**Steps:**

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Harito97/Socio-Ecological_Model.git
    ```

2.  **View Model Parameters (Optional):**

    Before running the simulation, explore the available parameters that can be adjusted to customize the model's behavior:

    ```bash
    python main.py show_params
    ```

3.  **Explore Model Documentation (Optional):**

    To understand the structure and functions of the model, generate documentation:

    ```bash
    python main.py show_docs
    ```

4.  **Run the Simulation:**

    Execute the following command to initiate the simulation. The results will be stored in the `results` directory:

    ```bash
    python main.py run_simulation
    ```
