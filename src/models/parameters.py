import numpy as np


class Parameters:
    def __init__(self, time: int = 100):
        """
        Initialize the GSSEM model parameters and variables.
        """
        self.time = time
        # General parameters
        self.init_general_parameters()
        # Initial values for populations, resources, and other states
        self.init_pop_res_states()
        # Initial deficit values
        self.init_deficits()
        # Initial per capita mass and environmental variables
        self.init_capita_mass_env_var()
        # Initial inflow and outflow rates
        self.init_inflows_outflows()
        # Temperature parameters
        self.init_temperature()
        # Growth rates for plants
        self.init_growth_rates_plants()
        # Natural parameters
        self.init_natural_parameters()
        # Economic parameters
        self.init_economic_parameters()
        # Ito process parameters
        self.init_ito_process()

        # Add other initialization methods with idea model of other researches
        # Initialize Society Type A - Ideal parameters
        self.init_society_type_a()
        # Energy parameters
        self.init_energy_parameters()
        # Economic mobility factors
        self.init_economic_mobility_factors()
        # Greenhouse gas emission parameters
        self.init_greenhouse_gas_emissions()

    def init_general_parameters(self):
        """Initialize general model parameters."""
        self.Ito = 0  # Ito process activation flag
        self.Case = 3  # Case number
        self.pais = 0  # Country identifier
        self.belownoreproduction = 1e-4  # Reproduction threshold for natural ecosystems

    def init_pop_res_states(self):
        """Initialize initial values for populations, resources, and other states."""
        self.P1 = [0.127639522] * self.time
        self.P2 = [6.637479579] * self.time
        self.P3 = [1.181396149] * self.time
        self.H1 = [1.248945367] * self.time
        self.H2 = [0.065892868] * self.time
        self.H3 = [1.073417243] * self.time
        self.C1 = [1.358944396] * self.time
        self.C2 = [0.611883366] * self.time
        self.HH = [0.4507] * self.time  # Human households
        self.ISmass = [0.508187978] * self.time  # Industrial system mass
        self.RP = [20.10894289] * self.time  # Resource pool
        self.IRP = [0.881746274] * self.time  # Industrial resource pool
        self.numHH = [1000] * self.time  # Number of households

    def init_deficits(self):
        """Initialize initial deficit values."""
        self.P1H1massdeficit = [0] * self.time
        self.P1ISmassdeficit = [0] * self.time
        self.P1HHmassdeficit = [0] * self.time
        self.H1massdeficit = [0] * self.time
        self.ISmassdeficit = [0] * self.time
        self.P1massdeficit = [sum([0, 0, 0])] * self.time # Sum of all P1 deficits

    def init_capita_mass_env_var(self):
        """Initial per capita mass and environmental variables"""
        self.percapmass = [self.HH[0] / self.numHH[0]]  * self.time
        self.ERP = [800] * self.time # Environmental resource potential
        self.EE = [0] * self.time # Environmental efficiency
        self.CO2eq = [300] * self.time # CO2 equivalent in ppm

    def init_inflows_outflows(self):
        """Initialize inflow and outflow rates for all compartments."""
        self.IP1, self.DP1 = [0] * self.time, [0] * self.time
        self.IP2, self.DP2 = [0] * self.time, [0] * self.time
        self.IP3, self.DP3 = [0] * self.time, [0] * self.time
        self.IH1, self.DH1 = [0] * self.time, [0] * self.time
        self.IH2, self.DH2 = [0] * self.time, [0] * self.time
        self.IH3, self.DH3 = [0] * self.time, [0] * self.time
        self.IC1, self.DC1 = [0] * self.time, [0] * self.time
        self.IC2, self.DC2 = [0] * self.time, [0] * self.time
        self.IHH, self.DHH = [0] * self.time, [0] * self.time
        self.IIRP, self.DIRP = [0] * self.time, [0] * self.time
        self.INRP, self.DRP = [0] * self.time, [0] * self.time

    def init_temperature(self):
        """Initialize temperature parameters."""
        self.atemp = [-0.21] * self.time  # Temperature anomaly
        self.temp = [25] * self.time  # Initial temperature
        self.tempo = 25  # Optimal temperature

    def init_growth_rates_plants(self):
        """Initialize growth rates for plants."""
        self.gRPP1p = 0.003541127
        self.gRPP2p = 0.009933643
        self.gRPP3p = 0.000778772

    def init_natural_parameters(self):
        """Initialize natural growth and mortality parameters."""
        self.gP2H2 = 0.058687036
        self.gP2H3 = 0.0168
        self.gP3H3 = 0.125249403
        self.gH2C1 = 0.366996266
        self.gH2C2 = 0.052509103
        self.gH3C2 = 0.117534846
        self.rIRPP2 = 0.021472781
        self.rIRPP3 = 0.357331692
        self.mP2 = 0.197313146
        self.mP3 = 0.186325524
        self.mH2 = 0.0004
        self.mH3 = 0.196123663
        self.mC1 = 0.092105574
        self.mC2 = 0.171458886
        self.mIRPRP = 0
        self.RPIRP = 0.49337505
        self.gP1H2 = 0.079785
        self.gH1C1 = 0.19963
        self.mP1 = 0.001018295
        self.mH1 = 0.009838862

    def init_economic_parameters(self):
        """Initialize economic parameters."""
        self.aw = 0.43853
        self.cw = 0.135718104
        self.dw = 4.51e-06
        self.aP1 = 0.4968
        self.bP1 = 0.67631
        self.cP1 = 0.12318
        self.aP1p = 0.050392
        self.bP1p = 0.149737492
        self.cP1p = 0.033805381
        self.aH1 = 1.4359
        self.bH1 = 0.001
        self.cH1 = 0.252716513
        self.aH1p = 0.24182
        self.bH1p = 0.049912497
        self.cH1p = 0.26657
        self.aIS = 1.17
        self.bIS = 0.297210307
        self.cIS = 0.001

        self.aISp	=	0.3109	  
        self.bISp	=	0.0044	  
        self.cISp	=	0.3313	  
        self.dP1H1	=	0.000191077	   
        self.eP1H1	=	0.049912497	   
        self.fP1H1	=	0.81332	       
        self.gP1H1	=	2.9657	       
        self.dP1HH	=	4.00e-08       
        self.zP1HH	=	6.00e-08	   
        self.kP1HH	=	1.60e-07	   
        self.mP1HH	=	6.00e-08	   
        self.nP1HH	=	0	           
        self.dH1HH	=	6.00e-08	   
        self.zH1HH	=	3.13e-05	   
        self.kH1HH	=	6.00e-08	   
        self.mH1HH	=	6.00e-08	   
        self.nH1HH	=	0	           
        self.dISHH	=	6.00e-08	   
        self.zISHH	=	5.68e-05	   
        self.kISHH	=	6.00e-08	   
        self.mISHH	=	4.00e-08	   
        self.nISHH	=	2.00e-08	   
        self.khat	=	.1 #0.09	  
        self.theta	=	0.101991961	
        self.lambda_	=	0.676677233	 
        self.mHH = 0.01
        self.P1bar	=	0	       
        self.H1bar	=	0.4	       
        self.ISbar	=	0	       
        self.etaa	=	0.000271386*52
        self.etab	=	0.00010454*52 
        self.phi	=	10	   #valor de enfermedad           
        self.idealpercapmass	=	4.51e-05 * 10000 / self.numHH[0] 

    def init_ito_process(self):
        """Initialize Ito process parameters."""
        self.sigmam = 2.34e-05
        self.sigmab = 1.56e-03
        self.epsilonm1 = np.random.normal(0, 1, self.time)
        self.epsilonb1 = np.random.normal(0, 1, self.time)
        self.epsilonm2 = np.random.normal(0, 1, self.time)
        self.epsilonb2 = np.random.normal(0, 1, self.time)

        # Disable Ito process if not active
        if self.Ito == 0:
            self.sigmam = 0
            self.sigmab = 0

    # Add other initialization methods with idea model of other researches
    def init_society_type_a(self):
        """
        Initialize parameters for Society Type A - Ideal.
        % Based on data taken from International Labor Oragization
        % http://laborsta.ilo.org/STP/guest
        """
        # Based on data taken from International Labor Organization
        # SOCIETY TYPE A - IDEAL
        # Two Populations modifications (2P):
        # 2P)   IEI 1 Income Equality Index
        # 2P-a) 75-25 total population; 1 = poor, 2 = rich; 
        # 2P-b) 75-25 total wages
        # 2P-c) 75-25 total P1demand & H1demand 
        # 2P-d) 75-25 total ISdemand & EEdemand
        # 2P-e) 75-25 HH
        self.IEI = 1                            # Income Equality Index
        self.numHH1 = [0.75 * self.numHH[0]] * self.time    # 75% of total households
        self.numHH2 = [0.25 * self.numHH[0]] * self.time    # 25% of total households
        self.HH1 = [self.HH[0] * 0.75] * self.time          # 75% of total household income
        self.HH2 = [self.HH[0] * 0.25] * self.time          # 25% of total household income

        # Factors related to healthcare and nutritional issues
        # Rich people have better access to healthcare
        self.phi1 = self.phi  # Factor for poorer population
        self.phi2 = self.phi / 2  # Factor for richer population

        # Per capita mass calculations
        self.percapmass1 = [self.HH1[0] / self.numHH1[0]] * self.time  # Per capita mass for poor
        self.percapmass2 = [self.HH2[0] / self.numHH2[0]] * self.time  # Per capita mass for rich

        # Factors for modification in individual populations variables
        # Equations formed by:
        # 1) pop1 + pop2 = total pop
        # 2) pop1 - pop2 * (ratio of percentages) = 0
        total_numHH = self.numHH[0]
        Ab = np.array(
            [
                [self.numHH1[0] / total_numHH, self.numHH2[0] / total_numHH],
                [
                    self.numHH1[0] / total_numHH,
                    -(self.numHH2[0] / total_numHH) * (75 / 25),
                ],
            ]
        )  # 2P-b, d)
        Ac = np.array(Ab)  # Same as Ab for demo purposes (2P-c, e)
        Ad = np.array(Ab)  # Same as Ab for demo purposes (2P-b, d)
        bb = np.array([1, 0])

        # Solve for f2p values
        self.f2pb = np.linalg.inv(Ab).dot(bb)  # Solution for demand equations
        self.f2pc = np.linalg.inv(Ac).dot(bb)  # Solution for demand equations
        self.f2pd = np.linalg.inv(Ad).dot(bb)  # Solution for demand equations
        self.f2pe = [0.75, 0.25]  # Ratio of populations

        # Wages parameters
        self.aw1 = self.aw * self.f2pb[0]  # 2P-a) Adjusted wage for poor
        self.aw2 = self.aw * self.f2pb[1]  # 2P-a) Adjusted wage for rich
        self.cw1 = self.cw * self.f2pb[0]  # 2P-b) Adjusted wage for poor
        self.cw2 = self.cw * self.f2pb[1]  # 2P-b) Adjusted wage for rich
        self.dw1 = self.dw * self.f2pb[0]  # 2P-c) Adjusted wage for poor
        self.dw2 = self.dw * self.f2pb[1]  # 2P-c) Adjusted wage for rich

    def init_energy_parameters(self):
        """
        Initialize energy parameters based on Kotecha & Diwekar (2010).
        % Inclusion of energy concepts %En)
        % - Energy producer compartment (EE)
        % - Energy Resourse Pool compartment (ERP)
        """
        # Energy parameters
        self.dEEHH = 6.00e-08  # demand for energy households
        self.zEEHH = 5.68e-05  # demand for energy households
        self.kEEHH = 6.00e-08  # demand for energy households
        self.mEEHH = 4.00e-08  # demand for energy households
        self.nEEHH = 2.00e-08  # demand for energy households

        self.aEE = self.aP1  # price of energy
        self.bEE = self.bP1  # price of energy
        self.cEE = 5000 * self.cP1  # price of energy

        self.gammaEEIS = 1  # (unit of energy / unit of IS)
        self.gammaEEIRP = 0.2  # yield (mass/energy)

    def init_economic_mobility_factors(self):
        """Initialize economic mobility parameters."""
        self.Wid = 0.31  # Ideal wage from stable simulation without Economic Mobility Factor (EMF)
        self.Wgid = 0.31 * self.numHH[0]  # Ideal global wage
        self.psi = 1  # Richness distribution factor

    def init_greenhouse_gas_emissions(self):
        """
        Initialize greenhouse gas emission parameters based on global data.
        """

        # Conversion factor from GtCO2eq to ppm in the atmosphere
        """
        % Greenhouse Gas emission based on:
        %-https://www3.epa.gov/climatechange/ghgemissions/global.html and references
        %-Climate Change 2014 Mitigation of Climate Change Working Group III 
        % Contribution to the Fifth Assessment Report of the Intergovernmental 
        % Panel on Climate Change
        %-https://www.co2.earth/ and http://www.esrl.noaa.gov/gmd/aggi/aggi.html     

        % 1870-2015:    - CO2eq 300-485 ppm aprox, CO2ppm 290-400
        %               - 545 GtC = 2000 GtCO2 (42% air, 28% ocean, 29% land)
        %               - 840 GtCO2eq and 185 ppm ---> 0.22024 ppm/GtCO2eq
        % 2015:         - 400 ppm CO2, 485 ppm CO2eq
        %               - 10.1 GtC = 37 GtCO2eq aprox
        """
        self.ppmCO2eq = (
            0.22024  # factor to convert from GtCO2eq to ppm in the atmosphere
        )
        self.GtCO2eqStb = 37  # GtCO2eq approx emitted in 2015

        # Global emissions percentages based on various sectors'
        """
        % Global emissions 2010:    - 25% Energy and heat production (EE)
        %                           - 24% Agriculture forestry and other land use
        %                                 (P1, H1 & productions)
        %                           -  6% Buildings (numHH)
        %                           - 14% Transportation (numHH)
        %                           - 21% Industry (IS)
        %                           - 10% Other energy (EE)

        % Percentage of total emissions per stable value of yGHG
        %                 P1    H1  numHH   P1prod  H1prod  ISprod  EEprod  P2  P3  RP
        % with percCO2eq=[6     6   20      6       6       21      35      -24 -5  -28]
        % negatives came from distribution percentages of emissions been equals for
        % P1 and P2 %'s are equally weighted 
        """
        self.percCO2eq = np.array([6, 6, 20, 6, 6, 21, 35, -24, -5, -28])
        # Negative percentages come from distribution percentages of emissions being equal for P1 and P2

        # Stable value of variables producing GHG (yGHG)
        self.yGHGstb = np.array(
            [
                0.090108316273598,
                1.243569877687978,
                996,
                0.000770375203888207,
                0.001427446253809,
                0.006279712575167,
                0.012336856254033,
                5.247311054647068,
                1.112128665742525,
                22.415707968618005,
            ]
        )

        # Calculate gigatonnes of CO2 equivalent emitted by mass unit
        self.GtCO2eq = self.GtCO2eqStb * (self.percCO2eq / 100) / self.yGHGstb

    def print_params(self):
        print("Parameters:")
        print(self.__dict__.keys())
        print("\nNumber of parameters:", len(self.__dict__))


if __name__ == "__main__":
    params = Parameters()
    params.print_params()
