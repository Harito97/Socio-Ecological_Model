# Params

Dưới đây là phân loại các tham số chính:

1. **Giá trị khởi tạo:** 
   - `P1`, `P2`, `P3`, `H1`, `H2`, `H3`, `C1`, `C2`, `HH`, `ISmass`, `RP`, `IRP`, `numHH`, ...

2. **Tham số nhiệt độ:**
   - `atemp`, `temp`, `tempo`, `gRPP1p`, `gRPP2p`, `gRPP3p`, ...

3. **Tham số tự nhiên:**
   - `gP2H2`, `gP2H3`, `gH2C1`, `gH2C2`, `gH3C2`, `rIRPP2`, `rIRPP3`, `mP2`, `mP3`, `mH2`, `mH3`, `mC1`, `mC2`, `mIRPRP`, ...

4. **Tham số kinh tế:**
   - `aw`, `cw`, `dw`, `aP1`, `bP1`, `cP1`, `aH1`, `bH1`, `cH1`, `aIS`, `bIS`, `cIS`, ...

5. **Tham số khí nhà kính:**
   - `ppmCO2eq`, `GtCO2eqStb`, `percCO2eq`, `yGHGstb`, `GtCO2eq`, ...

6. **Tham số ngẫu nhiên (Ito Processes):**
   - `sigmam`, `sigmab`, `epsilonm1`, `epsilonm2`, `epsilonb1`, `epsilonb2`, ...

---

Model parameters initialized. For details, see src/models/parameters.py

Parameters:
```python
dict_keys(['time', 'Ito', 'Case', 'pais', 'belownoreproduction', 'P1', 'P2', 'P3', 'H1', 'H2', 'H3', 'C1', 'C2', 'HH', 'ISmass', 'RP', 'IRP', 'numHH', 'P1H1massdeficit', 'P1ISmassdeficit', 'P1HHmassdeficit', 'H1massdeficit', 'ISmassdeficit', 'P1massdeficit', 'percapmass', 'ERP', 'EE', 'CO2eq', 'IP1', 'DP1', 'IP2', 'DP2', 'IP3', 'DP3', 'IH1', 'DH1', 'IH2', 'DH2', 'IH3', 'DH3', 'IC1', 'DC1', 'IC2', 'DC2', 'IHH', 'DHH', 'IIRP', 'DIRP', 'INRP', 'DRP', 'atemp', 'temp', 'tempo', 'gRPP1p', 'gRPP2p', 'gRPP3p', 'gP2H2', 'gP2H3', 'gP3H3', 'gH2C1', 'gH2C2', 'gH3C2', 'rIRPP2', 'rIRPP3', 'mP2', 'mP3', 'mH2', 'mH3', 'mC1', 'mC2', 'mIRPRP', 'RPIRP', 'gP1H2', 'gH1C1', 'mP1', 'mH1', 'aw', 'cw', 'dw', 'aP1', 'bP1', 'cP1', 'aP1p', 'bP1p', 'cP1p', 'aH1', 'bH1', 'cH1', 'aH1p', 'bH1p', 'cH1p', 'aIS', 'bIS', 'cIS', 'aISp', 'bISp', 'cISp', 'dP1H1', 'eP1H1', 'fP1H1', 'gP1H1', 'dP1HH', 'zP1HH', 'kP1HH', 'mP1HH', 'nP1HH', 'dH1HH', 'zH1HH', 'kH1HH', 'mH1HH', 'nH1HH', 'dISHH', 'zISHH', 'kISHH', 'mISHH', 'nISHH', 'khat', 'theta', 'lambda_', 'mHH', 'P1bar', 'H1bar', 'ISbar', 'etaa', 'etab', 'phi', 'idealpercapmass', 'sigmam', 'sigmab', 'epsilonm1', 'epsilonb1', 'epsilonm2', 'epsilonb2', 'IEI', 'numHH1', 'numHH2', 'HH1', 'HH2', 'phi1', 'phi2', 'percapmass1', 'percapmass2', 'f2pb', 'f2pc', 'f2pd', 'f2pe', 'aw1', 'aw2', 'cw1', 'cw2', 'dw1', 'dw2', 'dEEHH', 'zEEHH', 'kEEHH', 'mEEHH', 'nEEHH', 'aEE', 'bEE', 'cEE', 'gammaEEIS', 'gammaEEIRP', 'Wid', 'Wgid', 'psi', 'ppmCO2eq', 'GtCO2eqStb', 'percCO2eq', 'yGHGstb', 'GtCO2eq'])
```

Number of parameters: **170**