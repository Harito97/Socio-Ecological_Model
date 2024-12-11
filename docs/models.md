**Model documentation**:
```
        Run the simulation over the specified time period.

        Simulate a complex ecological system over time. It involves multiple interacting components, including:

            Populations: Different species or populations (P1, P2, H1, H2, etc.)
            Resources: Resources like food, energy, and space (RP, IRP, ERP)
            Human population: Human population and its interaction with the ecosystem
            Economic factors: Industrial production, consumption, and economic growth
            Environmental factors: Temperature, CO2 levels, and carrying capacity

        Key Components and Functionality

            Initialization:
                Sets initial values for various populations, resources, and parameters.
                Defines time steps and simulation duration.

            Time Loop:
                Iterates over each time step.
                Calculates various rates and flows based on current state and parameters.
                Updates the state of the system for the next time step.

            Population Dynamics:
                Models growth and decline of populations based on factors like birth rates, death rates, and resource availability.
                Includes logistic growth models and interactions between species.

            Resource Dynamics:
                Simulates the dynamics of resources, including consumption by populations and regeneration.
                Models the impact of human activity on resource depletion.

            Economic Model:
                Incorporates economic factors such as production, consumption, and wages.
                Models the impact of economic activity on the ecosystem.

            Environmental Model:
                Simulates changes in environmental factors like temperature and CO2 levels.
                Models the impact of human activities on the climate.

            Human Population Model:
                Models the growth and decline of the human population based on factors like birth rates, death rates, and resource availability.
                Includes the impact of economic factors and environmental changes on human population.

        Specific Calculations and Variables

            Population growth: Calculated based on birth rates, death rates, and carrying capacity.
            Resource consumption: Determined by the demands of different populations.
            Economic production: Calculated based on factors like labor, capital, and technology.
            Environmental impact: Assessed by tracking changes in CO2 levels and temperature.
            Human behavior: Modeled through consumption patterns, economic decisions, and policy choices.

        Key Equations and Concepts

            Logistic growth: A common model for population growth that accounts for carrying capacity.
            Predator-prey models: Describe the interactions between predator and prey populations.
            Economic models: Based on supply and demand, production functions, and utility maximization.
            Climate models: Simulate the Earth's climate system and its response to greenhouse gas emissions.
```