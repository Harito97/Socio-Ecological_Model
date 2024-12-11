from math import exp, log, sqrt, ceil
import numpy as np
from src.models.parameters import Parameters


class GSSEMModel:
    """
    Generalized Socio-Economic-Ecological Model (GSSEM).
    This model is adapted from Cabezas & Whitmore and incorporates energy
    concepts from Kotecha's work.
    """

    def __init__(self, time: int = 100):
        """
        Parameters:
        - time (int): Simulation time period.
        """

        # Initialize model parameters
        self.params = Parameters(time)
        print("Model parameters initialized. For details, see src/models/parameters.py")

    def simulation_docs(self):
        docs = """
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
        """

        print(docs)

    def run_simulation(self):
        # x = np.zeros(self.params.time)
        x = []
        y = []

        for i in range(0, self.params.time):
            if i == self.params.time - 1:
                i = self.params.time - 2
            # Weighting factors for total population variables
            alfa1 = self.params.numHH1[0] / (
                self.params.numHH1[0] + self.params.numHH2[0]
            )
            alfa2 = self.params.numHH2[0] / (
                self.params.numHH1[0] + self.params.numHH2[0]
            )

            # Demographic params due current trends (2014)
            mHH1 = (
                -3.25 * log(i + 55) + 20.536
            ) / 1000 + self.params.sigmam * self.params.epsilonm1[i] * sqrt(1)
            mHH2 = (
                -0.0103 * (i + 55) + 9.4329
            ) / 1000 + self.params.sigmam * self.params.epsilonm2[i] * sqrt(1)
            aa = mHH1
            bb = mHH2
            mHH = mHH1 * alfa1 + mHH2 * alfa2
            cc = mHH
            etaa1 = (41.975 * exp(-0.013 * (i + 55)) + 3) / 1000
            etab1 = self.params.etab
            etaa2 = (20.831 * exp(-0.012 * (i + 55)) + 3) / 1000
            etab2 = self.params.etab

            # RPP1 RPP2 RPP3 MATERIAL FLOW as a function of temperature
            # Plants
            gRPP1 = self.params.gRPP1p * exp(
                -((self.params.temp[i] - self.params.tempo) ** 2) / 100
            )
            gRPP2 = self.params.gRPP2p * exp(
                -((self.params.temp[i] - self.params.tempo) ** 2) / 100
            )
            gRPP3 = self.params.gRPP3p * exp(
                -((self.params.temp[i] - self.params.tempo) ** 2) / 100
            )

            # Humans
            mHH = -(
                mHH * exp(-((self.params.temp[i] - self.params.tempo) ** 2) / 100)
            ) + (2.0 * mHH)

            # Assigning values for further calculations
            dd = mHH1
            ee = mHH2
            ff = mHH

            # -----TEMPERATURE CALCULATION-----
            self.params.atemp[i + 1] = 0.010008 * self.params.CO2eq[i] - 3.21675
            self.params.temp[i + 1] = self.params.tempo + self.params.atemp[i + 1]

            # I. Economic calculations
            W1 = max(
                self.params.aw1
                + self.params.cw1
                * (
                    self.params.ISbar
                    - (self.params.ISmassdeficit[i] + self.params.ISmass[i])
                )
                / (self.params.theta + self.params.lambda_)
                - self.params.dw1 * self.params.numHH[i],
                0,
            )
            W2 = max(
                self.params.aw2
                + self.params.cw2
                * (
                    self.params.ISbar
                    - (self.params.ISmassdeficit[i] + self.params.ISmass[i])
                )
                / (self.params.theta + self.params.lambda_)
                - self.params.dw2 * self.params.numHH[i],
                0,
            )
            W = W1 * alfa1 + W2 * alfa2

            # Economic Mobility Factor
            EMF = self.params.psi * (
                (self.params.Wgid - W * self.params.numHH[i]) / self.params.Wgid
            )
            if EMF * self.params.numHH[i] > self.params.numHH1[i]:
                EMF = self.params.numHH1[i] / self.params.numHH[i]
            if EMF * self.params.numHH[i] < (-self.params.numHH2[i]):
                EMF = self.params.numHH2[i] / self.params.numHH[i]

                # Pricing and Production calculations
            if self.params.P1[i] == 0:
                pP1 = 0
                P1production = 0
            else:
                pP1 = max(
                    self.params.aP1
                    + self.params.bP1 * W
                    - self.params.cP1
                    * (
                        (self.params.P1massdeficit[i] + self.params.P1[i])
                        - self.params.P1bar
                    ),
                    0,
                )
                P1production = max(
                    self.params.aP1p
                    - self.params.bP1p * W
                    - self.params.cP1p
                    * (
                        (self.params.P1massdeficit[i] + self.params.P1[i])
                        - self.params.P1bar
                    ),
                    0,
                )

            if self.params.H1[i] == 0:
                pH1 = 0
                H1production = 0
            else:
                pH1 = max(
                    self.params.aH1
                    + self.params.bH1 * W
                    - self.params.cH1
                    * (
                        (self.params.H1massdeficit[i] + self.params.H1[i])
                        - self.params.H1bar
                    ),
                    0,
                )
                H1production = max(
                    self.params.aH1p
                    - self.params.bH1p * W
                    - self.params.cH1p
                    * (
                        (self.params.H1massdeficit[i] + self.params.H1[i])
                        - self.params.H1bar
                    ),
                    0,
                )

            if self.params.HH[i] == 0 or self.params.numHH[i] < 20:
                pIS = 0
                ISproduction = 0
            else:
                pIS = max(
                    self.params.aIS
                    + self.params.bIS * W
                    + self.params.cIS
                    * (
                        self.params.ISbar
                        - (self.params.ISmassdeficit[i] + self.params.ISmass[i])
                    )
                    / (self.params.theta + self.params.lambda_),
                    0,
                )
                ISproduction = max(
                    self.params.aISp
                    - self.params.bISp * W
                    + self.params.cISp
                    * (
                        self.params.ISbar
                        - (self.params.ISmassdeficit[i] + self.params.ISmass[i])
                    )
                    / (self.params.theta + self.params.lambda_),
                    0,
                )

            if self.params.HH[i] == 0 or self.params.numHH[i] < 20:
                pEE = 0
            else:
                pEE = max(
                    self.params.aEE
                    + self.params.bEE * W
                    + (self.params.cEE / self.params.ERP[i]),
                    0,
                )

                # II. Demanda
            if (
                self.params.H1[i] == 0
                or self.params.HH[i] == 0
                or self.params.numHH[i] < 20
            ):
                P1H1demand = 0
                P2H1 = 0
            else:
                P1H1demand = max(
                    self.params.dP1H1
                    - self.params.eP1H1 * W
                    - self.params.fP1H1 * pP1
                    - self.params.gP1H1
                    * (
                        (self.params.H1massdeficit[i] + self.params.H1[i])
                        - self.params.H1bar
                    ),
                    0,
                )
                P2H1 = self.params.khat

                # Demand calculations for P1HH, H1HH, and ISHH
            if self.params.HH[i] == 0 or self.params.numHH[i] < 20:
                P1HHdemand = 0
                H1HHdemand = 0
                ISHHdemand = 0
                EEHHdemand = 0
            else:
                P1HHdemand = (
                    max(
                        (
                            1
                            / (
                                -1
                                + self.params.zP1HH
                                + self.params.zH1HH
                                + self.params.zISHH
                            )
                        )
                        * (
                            -self.params.dP1HH
                            - self.params.mP1HH * pH1
                            - self.params.nP1HH * pIS
                            + self.params.kP1HH * pP1
                            - self.params.dH1HH * self.params.zP1HH
                            - self.params.dISHH * self.params.zP1HH
                            + self.params.mH1HH * pH1 * self.params.zP1HH
                            - self.params.mISHH * pH1 * self.params.zP1HH
                            - self.params.nH1HH * pIS * self.params.zP1HH
                            + self.params.nISHH * pIS * self.params.zP1HH
                            - self.params.kH1HH * pP1 * self.params.zP1HH
                            + self.params.dP1HH * self.params.zH1HH
                            + self.params.mP1HH * pH1 * self.params.zH1HH
                            + self.params.nP1HH * pIS * self.params.zH1HH
                            - self.params.kP1HH * pP1 * self.params.zH1HH
                            + self.params.dP1HH * self.params.zISHH
                            + self.params.mP1HH * pH1 * self.params.zISHH
                            + self.params.nP1HH * pIS * self.params.zISHH
                            - self.params.kP1HH * pP1 * self.params.zISHH
                        ),
                        0,
                    )
                    * 50
                )

                H1HHdemand = (
                    max(
                        (
                            1
                            / (
                                -1
                                + self.params.zP1HH
                                + self.params.zH1HH
                                + self.params.zISHH
                            )
                        )
                        * (
                            -self.params.dH1HH
                            + self.params.mH1HH * pH1
                            - self.params.nH1HH * pIS
                            - self.params.kH1HH * pP1
                            + self.params.dH1HH * self.params.zP1HH
                            - self.params.mH1HH * pH1 * self.params.zP1HH
                            + self.params.nH1HH * pIS * self.params.zP1HH
                            + self.params.kH1HH * pP1 * self.params.zP1HH
                            - self.params.dISHH * self.params.zH1HH
                            - self.params.dP1HH * self.params.zH1HH
                            - self.params.mISHH * pH1 * self.params.zH1HH
                            - self.params.mP1HH * pH1 * self.params.zH1HH
                            + self.params.nISHH * pIS * self.params.zH1HH
                            - self.params.nP1HH * pIS * self.params.zH1HH
                            - self.params.kISHH * pP1 * self.params.zH1HH
                            + self.params.kP1HH * pP1 * self.params.zH1HH
                            + self.params.dH1HH * self.params.zISHH
                            - self.params.mH1HH * pH1 * self.params.zISHH
                            + self.params.nH1HH * pIS * self.params.zISHH
                            + self.params.kH1HH * pP1 * self.params.zISHH
                        ),
                        0,
                    )
                    * 50
                )

                ISHHdemand = (
                    max(
                        -(
                            (
                                self.params.dISHH
                                + self.params.mISHH * pH1
                                - self.params.nISHH * pIS
                                + self.params.kISHH * pP1
                                - self.params.dISHH * self.params.zP1HH
                                - self.params.mISHH * pH1 * self.params.zP1HH
                                + self.params.nISHH * pIS * self.params.zP1HH
                                - self.params.kISHH * pP1 * self.params.zP1HH
                                - self.params.dISHH * self.params.zH1HH
                                - self.params.mISHH * pH1 * self.params.zH1HH
                                + self.params.nISHH * pIS * self.params.zH1HH
                                - self.params.kISHH * pP1 * self.params.zH1HH
                                + self.params.dH1HH * self.params.zISHH
                                + self.params.dP1HH * self.params.zISHH
                                - self.params.mH1HH * pH1 * self.params.zISHH
                                + self.params.mP1HH * pH1 * self.params.zISHH
                                + self.params.nH1HH * pIS * self.params.zISHH
                                + self.params.nP1HH * pIS * self.params.zISHH
                                + self.params.kH1HH * pP1 * self.params.zISHH
                                - self.params.kP1HH * pP1 * self.params.zISHH
                            )
                            / (
                                -1
                                + self.params.zP1HH
                                + self.params.zH1HH
                                + self.params.zISHH
                            )
                        ),
                        0,
                    )
                    * 50
                )

                EEHHdemand = (
                    max(
                        -(
                            (
                                self.params.dEEHH
                                + self.params.mEEHH * pH1
                                - self.params.nEEHH * pEE
                                + self.params.kEEHH * pP1
                                - self.params.dEEHH * self.params.zP1HH
                                - self.params.mEEHH * pH1 * self.params.zP1HH
                                + self.params.nEEHH * pEE * self.params.zP1HH
                                - self.params.kEEHH * pP1 * self.params.zP1HH
                                - self.params.dEEHH * self.params.zH1HH
                                - self.params.mEEHH * pH1 * self.params.zH1HH
                                + self.params.nEEHH * pEE * self.params.zH1HH
                                - self.params.kEEHH * pP1 * self.params.zH1HH
                                + self.params.dH1HH * self.params.zEEHH
                                + self.params.dP1HH * self.params.zEEHH
                                - self.params.mH1HH * pH1 * self.params.zEEHH
                                + self.params.mP1HH * pH1 * self.params.zEEHH
                                + self.params.nH1HH * pEE * self.params.zEEHH
                                + self.params.nP1HH * pEE * self.params.zEEHH
                                + self.params.kH1HH * pP1 * self.params.zEEHH
                                - self.params.kP1HH * pP1 * self.params.zEEHH
                            )
                            / (
                                -1
                                + self.params.zP1HH
                                + self.params.zH1HH
                                + self.params.zEEHH
                            )
                        ),
                        0,
                    )
                    * 50
                )

                # Demand scaling
            P1HHdemand1 = P1HHdemand * self.params.f2pc[0]
            P1HHdemand2 = P1HHdemand * self.params.f2pc[1]
            H1HHdemand1 = H1HHdemand * self.params.f2pc[0]
            H1HHdemand2 = H1HHdemand * self.params.f2pc[1]
            ISHHdemand1 = ISHHdemand * self.params.f2pd[0]
            ISHHdemand2 = ISHHdemand * self.params.f2pd[1]
            EEHHdemand1 = EEHHdemand * self.params.f2pd[0]
            EEHHdemand2 = EEHHdemand * self.params.f2pd[1]

            P1HHdemand = P1HHdemand1 * alfa1 + P1HHdemand2 * alfa2
            H1HHdemand = H1HHdemand1 * alfa1 + H1HHdemand2 * alfa2
            ISHHdemand = ISHHdemand1 * alfa1 + ISHHdemand2 * alfa2
            EEHHdemand = EEHHdemand1 * alfa1 + EEHHdemand2 * alfa2

            # Energy demands
            EEHHtotdemand = EEHHdemand * self.params.numHH[i]
            EEISdemand = ISproduction * self.params.gammaEEIS

            # Labor flows for P1H2 and H1C2
            if self.params.P1[i] == 0 or self.params.H2[i] == 0:
                P1H2 = 0
            else:
                P1H2 = max(
                    (
                        gRPP1 * self.params.P1[i] * self.params.RP[i]
                        - self.params.mP1 * self.params.P1[i]
                        - P1production
                    ),
                    0,
                )

            if self.params.H1[i] == 0 or self.params.C1[i] == 0:
                H1C1 = 0
            else:
                H1C1 = max(
                    (
                        P1H1demand
                        + P2H1
                        - self.params.mH1 * self.params.H1[i]
                        - H1production
                    ),
                    0,
                )

                # If there are no humans, consumption of P1H2 and H1C1 is natural (Lokta-Volterra)
            if self.params.HH[i] == 0 or self.params.numHH[i] < 20:
                P1H2 = self.params.gP1H2 * self.params.P1[i] * self.params.H2[i]
                H1C1 = self.params.gH1C1 * self.params.H1[i] * self.params.C1[i]

            P1ISdemand = self.params.theta * ISproduction
            RPISdemand = self.params.lambda_ * ISproduction

            # III. Calculate all but next state, according to system equations.

            # P1
            P1RP = max(self.params.mP1 * self.params.P1[i], 0)
            RPP1 = max(gRPP1 * self.params.P1[i] * self.params.RP[i], 0)
            P1H1 = P1H1demand
            P1IS = P1ISdemand
            P1HH = P1HHdemand * self.params.numHH[i]

            if self.params.P1[i] + RPP1 - P1RP - P1H2 - P1H1 - P1HH - P1IS < 0:
                if self.params.P1[i] + RPP1 - P1RP < 0:
                    P1RP = self.params.P1[i] + RPP1
                    P1H2 = 0
                    P1H1 = 0
                    P1HH = 0
                    P1IS = 0
                else:
                    totP1demand = P1H2 + P1H1 + P1HH + P1IS
                    P1avail = self.params.P1[i] + RPP1 - P1RP
                    P1H2 = P1avail * P1H2 / totP1demand
                    P1H1 = P1avail * P1H1 / totP1demand
                    P1HH = P1avail * P1HH / totP1demand
                    P1IS = P1avail - (P1H2 + P1H1 + P1HH)
            else:
                if self.params.P1massdeficit[i] < 0:
                    P1surplus = min(
                        self.params.P1[i] + RPP1 - P1RP - P1H2 - P1H1 - P1HH - P1IS,
                        -self.params.P1massdeficit[i],
                    )
                    P1H1 += (
                        P1surplus
                        * self.params.P1H1massdeficit[i]
                        / self.params.P1massdeficit[i]
                    )
                    P1IS += (
                        P1surplus
                        * self.params.P1ISmassdeficit[i]
                        / self.params.P1massdeficit[i]
                    )
                    P1HH += (
                        P1surplus
                        * self.params.P1HHmassdeficit[i]
                        / self.params.P1massdeficit[i]
                    )

                    # P2
            P2H2 = self.params.gP2H2 * self.params.P2[i] * self.params.H2[i]
            P2H3 = self.params.gP2H3 * self.params.P2[i] * self.params.H3[i]
            P2RP = max(self.params.mP2 * self.params.P2[i], 0)
            RPP2 = max(gRPP2 * self.params.RP[i] * self.params.P2[i], 0)
            IRPP2 = max(self.params.rIRPP2 * self.params.P2[i] * self.params.IRP[i], 0)
            P3RP = max(self.params.mP3 * self.params.P3[i], 0)
            P3H3 = self.params.gP3H3 * self.params.P3[i] * self.params.H3[i]
            RPP3 = max(gRPP3 * self.params.RP[i] * self.params.P3[i], 0)
            IRPP3 = max(self.params.rIRPP3 * self.params.P3[i] * self.params.IRP[i], 0)

            if self.params.IRP[i] <= 0:
                IRPP2 = 0
                IRPP3 = 0
            elif (
                self.params.IRP[i]
                - IRPP2
                - IRPP3
                - max(self.params.IRP[i] * self.params.mIRPRP, 0)
                + self.params.RPIRP
                < 0
            ):
                if self.params.P2[i] != 0:
                    IRPP2 = (
                        self.params.rIRPP2
                        * (
                            self.params.IRP[i]
                            - max(self.params.IRP[i] * self.params.mIRPRP, 0)
                            + self.params.RPIRP
                        )
                        / (self.params.rIRPP2 + self.params.rIRPP3)
                    )
                if self.params.P3[i] != 0:
                    IRPP3 = (
                        self.params.rIRPP3
                        * (
                            self.params.IRP[i]
                            - max(self.params.IRP[i] * self.params.mIRPRP, 0)
                            + self.params.RPIRP
                        )
                        / (self.params.rIRPP2 + self.params.rIRPP3)
                    )

            if (
                self.params.P2[i] + IRPP2 + RPP2 - P2RP - P2H2 - P2H3 - P2H1
                < self.params.belownoreproduction
            ):
                if (
                    self.params.P2[i] + IRPP2 + RPP2 - P2RP
                    < self.params.belownoreproduction
                ):
                    P2RP = self.params.P2[i] + IRPP2 + RPP2
                    P2H2 = 0
                    P2H3 = 0
                    P2H1 = 0
                else:
                    totP2demand = P2H2 + P2H3 + P2H1
                    P2avail = self.params.P2[i] + IRPP2 + RPP2 - P2RP
                    P2H2 = P2H2 * P2avail / totP2demand
                    P2H3 = P2H3 * P2avail / totP2demand
                    P2H1 = P2avail - (P2H2 + P2H3)

                    # P3
            if (
                self.params.P3[i] + IRPP3 + RPP3 - P3RP - P3H3
                < self.params.belownoreproduction
            ):
                if (
                    self.params.P3[i] + IRPP3 + RPP3 - P3RP
                    < self.params.belownoreproduction
                ):
                    P3RP = self.params.P3[i] + IRPP3 + RPP3
                    P3H3 = 0
                else:
                    totP3demand = P3H3
                    P3avail = self.params.P3[i] + IRPP3 + RPP3 - P3RP
                    P3H3 = P3H3 * P3avail / totP3demand

                    # H1
            H1RP = max(self.params.mH1 * self.params.H1[i], 0)
            H1HH = H1HHdemand * self.params.numHH[i]
            if self.params.H1[i] + P1H1 + P2H1 - H1RP - H1C1 - H1HH < 0:
                if self.params.H1[i] + P1H1 + P2H1 - H1RP < 0:
                    H1RP = self.params.H1[i] + P1H1 + P2H1
                    H1C1 = 0
                    H1HH = 0
                else:
                    totH1demand = H1C1 + H1HH
                    H1avail = self.params.H1[i] + P1H1 + P2H1 - H1RP
                    H1C1 = H1avail * H1C1 / totH1demand
                    H1HH = H1avail - H1C1
            else:
                if self.params.H1massdeficit[i] < 0:
                    H1HH += min(
                        self.params.H1[i] + P1H1 + P2H1 - H1RP - H1C1 - H1HH,
                        -self.params.H1massdeficit[i],
                    )

                    # H2
            H2C1 = self.params.gH2C1 * self.params.C1[i] * self.params.H2[i]
            H2C2 = self.params.gH2C2 * self.params.H2[i] * self.params.C2[i]
            H2RP = max(self.params.mH2 * self.params.H2[i], 0)
            if (
                self.params.H2[i] + P1H2 + P2H2 - H2RP - H2C1 - H2C2
                < self.params.belownoreproduction
            ):
                if (
                    self.params.H2[i] + P1H2 + P2H2 - H2RP
                    < self.params.belownoreproduction
                ):
                    H2RP = self.params.H2[i] + P1H2 + P2H2
                    H2C1 = 0
                    H2C2 = 0
                else:
                    totH2demand = H2C1 + H2C2
                    H2avail = self.params.H2[i] + P1H2 + P2H2 - H2RP
                    H2C1 = H2C1 * H2avail / totH2demand
                    H2C2 = H2avail - H2C1

                    # H3
            H3RP = max(self.params.mH3 * self.params.H3[i], 0)
            H3C2 = self.params.gH3C2 * self.params.H3[i] * self.params.C2[i]
            if (
                self.params.H3[i] + P2H3 + P3H3 - H3RP - H3C2
                < self.params.belownoreproduction
            ):
                if (
                    self.params.H3[i] + P2H3 + P3H3 - H3RP
                    < self.params.belownoreproduction
                ):
                    H3RP = self.params.H3[i] + P2H3 + P3H3
                    H3C2 = 0
                else:
                    totH3demand = H3C2
                    H3avail = self.params.H3[i] + P2H3 + P3H3 - H3RP
                    H3C2 = H3C2 * H3avail / totH3demand

                    # C1
            C1RP = max(self.params.mC1 * self.params.C1[i], 0)
            if self.params.C1[i] + H1C1 + H2C1 - C1RP < self.params.belownoreproduction:
                C1RP = self.params.C1[i] + H1C1 + H2C1

                # C2
            C2RP = max(self.params.mC2 * self.params.C2[i], 0)
            if self.params.C2[i] + H2C2 + H3C2 - C2RP < self.params.belownoreproduction:
                C2RP = self.params.C2[i] + H2C2 + H3C2

                # HH
            HHRP = (
                ceil(self.params.mHH * self.params.numHH[i]) * self.params.percapmass[i]
            )
            if HHRP > (self.params.HH[i] + P1HH + H1HH):
                HHRP = self.params.HH[i] + P1HH + H1HH

                # RP
            IRPRP = max(self.params.IRP[i] * self.params.mIRPRP, 0)
            RPIS = min(self.params.lambda_ * P1IS / self.params.theta, RPISdemand)
            stockRP = (
                self.params.RP[i]
                + P1RP
                + P2RP
                + P3RP
                + H1RP
                + H2RP
                + H3RP
                + C1RP
                + C2RP
                + HHRP
                + IRPRP
            )
            if stockRP < 0:
                stockRP = 0
            if (
                stockRP - (RPP1 + RPP2 + RPP3) - self.params.RPIRP - RPIS
            ) <= 0 and self.params.RPIRP == 0:
                RPdemand = RPP1 + RPP2 + RPP3 + RPISdemand
                RPP1 = RPP1 * stockRP / RPdemand
                RPP2 = RPP2 * stockRP / RPdemand
                RPP3 = RPP3 * stockRP / RPdemand
                if RPIS != 0:
                    RPIS = stockRP - (RPP1 + RPP2 + RPP3)
                else:
                    RPIS = 0
            P1IS = min(self.params.theta * RPIS / self.params.lambda_, P1IS)

            # ERP
            if self.params.ERP[i] > 0:
                EEproduction = EEHHtotdemand + EEISdemand
                EEHHmass = EEHHtotdemand * self.params.gammaEEIRP
                ERPEE = EEproduction * self.params.gammaEEIRP
                if (self.params.ERP[i] - ERPEE) < 0:
                    ERPEE = self.params.ERP[i]
                    self.params.ERP[i] = 0
                EEIRP = ERPEE
            else:
                pEE = 0
                EEproduction = 0
                EEHHmass = 0
                self.params.ERPIRP = 0
                EEHHtotdemand = 0
                EEISdemand = 0
                EEHHdemand = 0

                # III.A. make checks again, to balance flows

                # P1
            if self.params.P1[i] + RPP1 - P1RP - P1H2 - P1H1 - P1HH - P1IS < 0:
                if self.params.P1[i] + RPP1 - P1RP < 0:
                    P1RP = self.params.P1[i] + RPP1
                    P1H2 = 0
                    P1H1 = 0
                    P1HH = 0
                    P1IS = 0
                else:
                    totP1demand = P1H2 + P1H1 + P1HH + P1IS
                    P1avail = self.params.P1[i] + RPP1 - P1RP
                    P1H2 = P1avail * P1H2 / totP1demand
                    P1H1 = P1avail * P1H1 / totP1demand
                    P1HH = P1avail * P1HH / totP1demand
                    P1IS = P1avail - (P1H2 + P1H1 + P1HH)
            else:
                if self.params.P1massdeficit[i] < 0:
                    P1surplus = min(
                        self.params.P1[i] + RPP1 - P1RP - P1H2 - P1H1 - P1HH - P1IS,
                        -self.params.P1massdeficit[i],
                    )
                    P1H1 += (
                        P1surplus
                        * self.params.P1H1massdeficit[i]
                        / self.params.P1massdeficit[i]
                    )
                    P1IS += (
                        P1surplus
                        * self.params.P1ISmassdeficit[i]
                        / self.params.P1massdeficit[i]
                    )
                    P1HH += (
                        P1surplus
                        * self.params.P1HHmassdeficit[i]
                        / self.params.P1massdeficit[i]
                    )

                    # P2
            if self.params.IRP[i] <= 0:
                IRPP2 = 0
                IRPP3 = 0
            elif (
                self.params.IRP[i]
                - IRPP2
                - IRPP3
                - max(self.params.IRP[i] * self.params.mIRPRP, 0)
                + self.params.RPIRP
                < 0
            ):
                if self.params.P2[i] != 0:
                    IRPP2 = (
                        self.params.rIRPP2
                        * (
                            self.params.IRP[i]
                            - max(self.params.IRP[i] * self.params.mIRPRP, 0)
                            + self.params.RPIRP
                        )
                        / (self.params.rIRPP2 + self.params.rIRPP3)
                    )
                if self.params.P3[i] != 0:
                    IRPP3 = (
                        self.params.rIRPP3
                        * (
                            self.params.IRP[i]
                            - max(self.params.IRP[i] * self.params.mIRPRP, 0)
                            + self.params.RPIRP
                        )
                        / (self.params.rIRPP2 + self.params.rIRPP3)
                    )

            if (
                self.params.P2[i] + IRPP2 + RPP2 - P2RP - P2H2 - P2H3 - P2H1
                < self.params.belownoreproduction
            ):
                if (
                    self.params.P2[i] + IRPP2 + RPP2 - P2RP
                    < self.params.belownoreproduction
                ):
                    P2RP = self.params.P2[i] + IRPP2 + RPP2
                    P2H2 = 0
                    P2H3 = 0
                    P2H1 = 0
                else:
                    totP2demand = P2H2 + P2H3 + P2H1
                    P2avail = self.params.P2[i] + IRPP2 + RPP2 - P2RP
                    P2H2 = P2H2 * P2avail / totP2demand
                    P2H3 = P2H3 * P2avail / totP2demand
                    P2H1 = P2avail - (P2H2 + P2H3)

                    # P3
            if (
                self.params.P3[i] + IRPP3 + RPP3 - P3RP - P3H3
                < self.params.belownoreproduction
            ):
                if (
                    self.params.P3[i] + IRPP3 + RPP3 - P3RP
                    < self.params.belownoreproduction
                ):
                    P3RP = self.params.P3[i] + IRPP3 + RPP3
                    P3H3 = 0
                else:
                    totP3demand = P3H3
                    P3avail = self.params.P3[i] + IRPP3 + RPP3 - P3RP
                    P3H3 = P3H3 * P3avail / totP3demand

                    # H1
            if self.params.H1[i] + P1H1 + P2H1 - H1RP - H1C1 - H1HH < 0:
                if self.params.H1[i] + P1H1 + P2H1 - H1RP < 0:
                    H1RP = self.params.H1[i] + P1H1 + P2H1
                    H1C1 = 0
                    H1HH = 0
                else:
                    totH1demand = H1C1 + H1HH
                    H1avail = self.params.H1[i] + P1H1 + P2H1 - H1RP
                    H1C1 = H1avail * H1C1 / totH1demand
                    H1HH = H1avail - H1C1
            else:
                if self.params.H1massdeficit[i] < 0:
                    H1HH += min(
                        self.params.H1[i] + P1H1 + P2H1 - H1RP - H1C1 - H1HH,
                        -self.params.H1massdeficit[i],
                    )

                    # H2
            if (
                self.params.H2[i] + P1H2 + P2H2 - H2RP - H2C1 - H2C2
                < self.params.belownoreproduction
            ):
                if (
                    self.params.H2[i] + P1H2 + P2H2 - H2RP
                    < self.params.belownoreproduction
                ):
                    H2RP = self.params.H2[i] + P1H2 + P2H2
                    H2C1 = 0
                    H2C2 = 0
                else:
                    totH2demand = H2C1 + H2C2
                    H2avail = self.params.H2[i] + P1H2 + P2H2 - H2RP
                    H2C1 = H2C1 * H2avail / totH2demand
                    H2C2 = H2avail - H2C1

                    # H3
            if (
                self.params.H3[i] + P2H3 + P3H3 - H3RP - H3C2
                < self.params.belownoreproduction
            ):
                if (
                    self.params.H3[i] + P2H3 + P3H3 - H3RP
                    < self.params.belownoreproduction
                ):
                    H3RP = self.params.H3[i] + P2H3 + P3H3
                    H3C2 = 0
                else:
                    totH3demand = H3C2
                    H3avail = self.params.H3[i] + P2H3 + P3H3 - H3RP
                    H3C2 = H3C2 * H3avail / totH3demand

                    # C1
            if self.params.C1[i] + H1C1 + H2C1 - C1RP < self.params.belownoreproduction:
                C1RP = self.params.C1[i] + H1C1 + H2C1

                # C2
            if self.params.C2[i] + H2C2 + H3C2 - C2RP < self.params.belownoreproduction:
                C2RP = self.params.C2[i] + H2C2 + H3C2

                # HH
            HHRP = (
                ceil(self.params.mHH * self.params.numHH[i]) * self.params.percapmass[i]
            )
            if HHRP > (self.params.HH[i] + P1HH + H1HH):
                HHRP = self.params.HH[i] + P1HH + H1HH

                # IV. Demographic

            ISHHflow = max(
                (self.params.theta + self.params.lambda_)
                * ISHHdemand
                * self.params.numHH[i],
                0,
            )
            ISIRP = ISHHflow
            if self.params.ISmass[i] + P1IS + RPIS - ISIRP <= 0:
                ISIRP = self.params.ISmass[i] + P1IS + RPIS
            else:
                if (
                    self.params.ISmassdeficit[i] < 0 and self.params.numHH[i] >= 2
                ):  # if there is an accumulated deficit
                    ISIRP += min(
                        self.params.ISmass[i] + P1IS + RPIS - ISIRP,
                        -self.params.ISmassdeficit[i],
                    )
                    # only what you need to make up deficit

            if (P1HH + H1HH + ISIRP) == 0:
                weightedprice = 0
                percapbirths = 0
                percapbirths1 = 0
                percapbirths2 = 0
            elif (pP1 * P1HH + pH1 * H1HH + pIS * ISIRP) == 0:
                weightedprice = 0
                percapbirths = 0
                percapbirths1 = 0
                percapbirths2 = 0
            else:
                weightedprice = (
                    pP1 * P1HH + pH1 * H1HH + pIS * ISIRP + pEE * EEHHmass
                ) / (P1HH + H1HH + ISIRP + EEHHmass)
                percapbirths1 = max(
                    etaa1
                    - etab1 * sqrt(W / weightedprice)
                    + self.params.sigmab * self.params.epsilonb1[i] * sqrt(1),
                    0,
                )  # 2P-a
                percapbirths2 = max(
                    etaa2
                    - etab2 * sqrt(W / weightedprice)
                    + self.params.sigmab * self.params.epsilonb2[i] * sqrt(1),
                    0,
                )  # 2P-a
                percapbirths = percapbirths1 * alfa1 + percapbirths2 * alfa2

            # -----Next Step-----
            # Update state variables for the next time step

            self.params.P1[i + 1] = (
                self.params.P1[i] + RPP1 - P1RP - P1H2 - P1H1 - P1HH - P1IS
            )
            self.params.IP1[i + 1] = RPP1
            self.params.DP1[i + 1] = P1RP + P1H1 + P1H2 + P1HH + P1IS

            if self.params.P1[i] == 0:
                P1H1demand = 0
                P1ISdemand = 0
                P1HHdemand = 0
                P1HHdemand1 = 0
                P1HHdemand2 = 0

            self.params.P1H1massdeficit[i + 1] = (
                self.params.P1H1massdeficit[i] + P1H1 - P1H1demand
            )
            self.params.P1ISmassdeficit[i + 1] = (
                self.params.P1ISmassdeficit[i] + P1IS - P1ISdemand
            )
            self.params.P1HHmassdeficit[i + 1] = (
                self.params.P1HHmassdeficit[i]
                + P1HH
                - P1HHdemand * self.params.numHH[i]
            )
            self.params.P1massdeficit[i + 1] = (
                self.params.P1H1massdeficit[i + 1]
                + self.params.P1ISmassdeficit[i + 1]
                + self.params.P1HHmassdeficit[i + 1]
            )

            self.params.P2[i + 1] = (
                self.params.P2[i] + IRPP2 + RPP2 - P2RP - P2H2 - P2H3 - P2H1
            )
            self.params.IP2[i + 1] = RPP2 + IRPP2
            self.params.DP2[i + 1] = P2RP + P2H1 + P2H2 + P2H3

            self.params.P3[i + 1] = self.params.P3[i] + IRPP3 + RPP3 - P3RP - P3H3
            self.params.IP3[i + 1] = RPP3 + IRPP3
            self.params.DP3[i + 1] = P3RP + P3H3

            self.params.H1[i + 1] = self.params.H1[i] + P1H1 + P2H1 - H1RP - H1C1 - H1HH
            self.params.IH1[i + 1] = P1H1 + P2H1
            self.params.DH1[i + 1] = H1RP + H1C1 + H1HH

            if self.params.H1[i] == 0:
                H1HHdemand = 0
                H1HHdemand1 = 0
                H1HHdemand2 = 0

            self.params.H1massdeficit[i + 1] = (
                self.params.H1massdeficit[i] + H1HH - H1HHdemand * self.params.numHH[i]
            )

            self.params.H2[i + 1] = self.params.H2[i] + P1H2 + P2H2 - H2RP - H2C1 - H2C2
            self.params.IH2[i + 1] = P1H2 + P2H2
            self.params.DH2[i + 1] = H2RP + H2C1 + H2C2

            self.params.H3[i + 1] = self.params.H3[i] + P2H3 + P3H3 - H3RP - H3C2
            self.params.IH3[i + 1] = P2H3 + P3H3
            self.params.DH3[i + 1] = H3RP + H3C2

            self.params.C1[i + 1] = self.params.C1[i] + H1C1 + H2C1 - C1RP
            self.params.IC1[i + 1] = H1C1 + H2C1
            self.params.DC1[i + 1] = C1RP

            self.params.C2[i + 1] = self.params.C2[i] + H2C2 + H3C2 - C2RP
            self.params.IC2[i + 1] = H2C2 + H3C2
            self.params.DC2[i + 1] = C2RP

            self.params.HH[i + 1] = self.params.HH[i] + P1HH + H1HH - HHRP
            self.params.IHH[i + 1] = P1HH + H1HH
            self.params.DHH[i + 1] = HHRP

            self.params.HH1[i + 1] = self.params.HH[i + 1] * self.params.f2pe[0]  # 2P-e
            self.params.HH2[i + 1] = self.params.HH[i + 1] * self.params.f2pe[1]  # 2P-e

            self.params.ISmass[i + 1] = self.params.ISmass[i] + P1IS + RPIS - ISIRP
            self.params.ISmassdeficit[i + 1] = (
                self.params.ISmassdeficit[i] + ISIRP - ISHHflow
            )

            self.params.IRP[i + 1] = (
                self.params.IRP[i]
                - IRPP2
                - IRPP3
                + self.params.RPIRP
                + ISIRP
                - IRPRP
                + EEIRP
            )
            self.params.IIRP[i + 1] = self.params.RPIRP + ISIRP + EEIRP
            self.params.DIRP[i + 1] = IRPP2 + IRPP3 + IRPRP

            self.params.RP[i + 1] = (
                stockRP - (RPP1 + RPP2 + RPP3) - self.params.RPIRP - RPIS
            )
            self.params.INRP[i + 1] = stockRP
            self.params.DRP[i + 1] = RPP1 + RPP2 + RPP3 + self.params.RPIRP + RPIS

            self.params.ERP[i + 1] = self.params.ERP[i] - EEIRP  # En

            self.params.EE[i + 1] = self.params.EE[i] + ERPEE - EEIRP  # En

            self.params.numHH1[i + 1] = max(
                self.params.numHH1[i]
                + ceil(percapbirths1 * self.params.numHH1[i])
                - ceil(mHH1 * self.params.numHH1[i])
                - ceil(
                    self.params.numHH1[i]
                    * (self.params.phi - self.params.phi1)
                    * (self.params.percapmass1[i] - self.params.idealpercapmass) ** 2
                ),
                1,
            )

            self.params.numHH2[i + 1] = max(
                self.params.numHH2[i]
                + ceil(percapbirths2 * self.params.numHH2[i])
                - ceil(mHH2 * self.params.numHH2[i])
                - ceil(
                    self.params.numHH2[i]
                    * (self.params.phi - self.params.phi2)
                    * (self.params.percapmass2[i] - self.params.idealpercapmass) ** 2
                ),
                1,
            )

            self.params.numHH[i + 1] = max(
                self.params.numHH[i]
                + ceil(percapbirths * self.params.numHH[i])
                - ceil(mHH * self.params.numHH[i])
                - ceil(
                    self.params.numHH[i]
                    * (self.params.phi - self.params.phi1)
                    * (self.params.percapmass[i] - self.params.idealpercapmass) ** 2
                ),
                1,
            )

            self.params.percapmass1[i + 1] = (
                self.params.HH1[i + 1] / self.params.numHH1[i + 1]
            )  # 2P-a
            self.params.percapmass2[i + 1] = (
                self.params.HH2[i + 1] / self.params.numHH2[i + 1]
            )  # 2P-a
            self.params.percapmass[i + 1] = (
                alfa1 * self.params.percapmass1[i + 1]
                + alfa2 * self.params.percapmass2[i + 1]
            )

            yGHG = [
                self.params.P1[i],
                self.params.H1[i],
                self.params.numHH[i],
                P1production,
                H1production,
                ISproduction,
                EEproduction,
                self.params.P2[i],
                self.params.P3[i],
                self.params.RP[i],
            ]

            self.params.CO2eq[i + 1] = (
                self.params.CO2eq[i]
                + sum(yGHG * self.params.GtCO2eq) * self.params.ppmCO2eq
            )  # In ppm

            # Store results for the current step
            x.append(
                [
                    P1RP,
                    P1H1,
                    P1H2,
                    P1IS,
                    P1HH,
                    P2RP,
                    P2H1,
                    P2H2,
                    P2H3,
                    P3RP,
                    P3H3,
                    H1RP,
                    H1C1,
                    H1HH,
                    H2RP,
                    H2C1,
                    H2C2,
                    H3RP,
                    H3C2,
                    C1RP,
                    C2RP,
                    HHRP,
                    ISIRP,
                    RPP1,
                    RPP2,
                    RPP3,
                    RPIS,
                    IRPP2,
                    IRPP3,
                    IRPRP,
                    P1HHdemand,
                    H1HHdemand,
                    ISHHdemand,
                    P1ISdemand,
                    RPISdemand,
                    P1production,
                    H1production,
                    ISproduction,
                    pP1,
                    pH1,
                    pIS,
                    percapbirths,
                    weightedprice,
                    W,
                    W1,
                    W2,
                    P1HHdemand1,
                    P1HHdemand2,
                    H1HHdemand1,
                    H1HHdemand2,
                    ISHHdemand1,
                    ISHHdemand2,
                    EEHHdemand1,
                    EEHHdemand2,
                    pEE,
                    EEHHdemand,
                    EEHHtotdemand,
                    EEISdemand,
                    EEproduction,
                    EEHHmass,
                    EEIRP,
                    percapbirths1,
                    percapbirths2,
                    mHH1,
                    mHH2,
                    EMF,
                    round(EMF * self.params.numHH[i]),
                    gRPP1,
                    gRPP2,
                    gRPP3,
                    mHH,
                    aa,
                    bb,
                    cc,
                    dd,
                    ee,
                    ff,
                ]
            )

        # Prepare final results for output
        y = [
            self.params.P1,
            self.params.P2,
            self.params.P3,
            self.params.H1,
            self.params.H2,
            self.params.H3,
            self.params.C1,
            self.params.C2,
            self.params.HH,
            self.params.ISmass,
            self.params.RP,
            self.params.IRP,
            self.params.numHH,
            self.params.percapmass,
            self.params.P1H1massdeficit,
            self.params.P1ISmassdeficit,
            self.params.P1HHmassdeficit,
            self.params.H1massdeficit,
            self.params.ISmassdeficit,
            self.params.numHH1,
            self.params.numHH2,
            self.params.HH1,
            self.params.HH2,
            self.params.ERP,
            self.params.EE,
            self.params.CO2eq,
            self.params.temp,
            self.params.IP1,
            self.params.DP1,
            self.params.IP2,
            self.params.DP2,
            self.params.IP3,
            self.params.DP3,
            self.params.IH1,
            self.params.DH1,
            self.params.IH2,
            self.params.DH2,
            self.params.IH3,
            self.params.DH3,
            self.params.IC1,
            self.params.DC1,
            self.params.IC2,
            self.params.DC2,
            self.params.IH3,
            self.params.DH3,
            self.params.IIRP,
            self.params.DIRP,
            self.params.INRP,
            self.params.DRP,
        ]

        # Save y and x to 2 files
        # Convert y and x to numpy arrays for easy saving
        x_array = np.array(x)
        y_array = np.array([y])  # Wrap y in a list to ensure it has the correct shape

        # Save x and y to files
        np.save("results/x_results.npy", x_array)
        np.save("results/y_results.npy", y_array)

        return x, y
