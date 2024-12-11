import numpy as np
import matplotlib.pyplot as plt

def plot(x, y):
    x = np.array(x)
    y = np.array(y)
    # Giả sử dữ liệu đã được chuẩn bị từ trước
    # time = length(x) và các mảng `y`, `yc`, `x` được cung cấp trước
    time = len(x)  # Thời gian, tương đương với số bước
    t = np.arange(time)  # thời gian cho các biến y
    t2 = np.arange(1, time + 1)  # thời gian cho các biến x

    # Các dữ liệu từ y và yc (lấy mẫu từ y và yc)
    P1 = y[0]
    P2 = y[1]
    P3 = y[2]
    H1 = y[3]
    H2 = y[4]
    H3 = y[5]
    C1 = y[6]
    C2 = y[7]
    RP = y[10]
    IRP = y[11]
    NumHH = y[12]
    ERP = y[23]

    # P1e = yc[:, 0]
    # P2e = yc[:, 1]
    # P3e = yc[:, 2]
    # H1e = yc[:, 3]
    # H2e = yc[:, 4]
    # H3e = yc[:, 5]
    # C1e = yc[:, 6]
    # C2e = yc[:, 7]
    # NumHHe = yc[:, 12]
    # RPe = yc[:, 10]
    # IRPe = yc[:, 11]
    # ERPe = yc[:, 23]

    # Escalamiento (chuẩn hóa dữ liệu)
    def scale_data(data):
        return (data - np.min(data)) / (np.max(data) - np.min(data))

    # P1e = scale_data(P1e)
    # P2e = scale_data(P2e)
    # P3e = scale_data(P3e)
    # H1e = scale_data(H1e)
    # H2e = scale_data(H2e)
    # H3e = scale_data(H3e)
    # C1e = scale_data(C1e)
    # C2e = scale_data(C2e)
    # RPe = scale_data(RPe)
    # IRPe = scale_data(IRPe)
    # ERPe = scale_data(ERPe)

    P1 = scale_data(P1)
    P2 = scale_data(P2)
    P3 = scale_data(P3)
    H1 = scale_data(H1)
    H2 = scale_data(H2)
    H3 = scale_data(H3)
    C1 = scale_data(C1)
    C2 = scale_data(C2)
    RP = scale_data(RP)
    IRP = scale_data(IRP)
    ERP = scale_data(ERP)

    # Biểu đồ Figure 15
    Temp = y[26]
    print(Temp.shape)
    mHHe = x[:, 73] * 1000
    mHHgw = x[:, 76] * 1000

    plt.figure(figsize=(14, 8))
    plt.subplot(111)
    plt.plot(t, Temp, '*b', linewidth=3, label='Temperature (°C)')
    plt.xlabel('Year', fontsize=24)
    plt.ylabel('Temperature (°C)', fontsize=24)
    plt.plot(t2, mHHe, 'r', linewidth=3, label='Baseline')
    plt.plot(t2, mHHgw, 'ro', linewidth=2, label='Study Case')
    plt.axis([1, 100, 5, 8.5])
    plt.legend(loc='best')
    plt.grid()
    plt.tight_layout()
    plt.savefig('figs/Figure_15.jpeg', dpi=300)

    # Biểu đồ Figure 16
    beta1 = x[:, 67] * 100
    beta2 = x[:, 68] * 100
    beta3 = x[:, 69] * 100

    plt.figure(figsize=(14, 8))
    plt.subplot(111)
    plt.plot(t, Temp, '*b', linewidth=3, label='Temperature (°C)')
    plt.xlabel('Year', fontsize=24)
    plt.ylabel('Temperature (°C)', fontsize=24)
    plt.plot(t2, beta1, 'r', linewidth=3, label='Growth Factor 1')
    plt.plot(t2, beta2, 'ro', t2, beta3, 'r+', linewidth=2)
    plt.axis([1, 100, 0, 1.1])
    plt.legend(loc='best')
    plt.grid()
    plt.tight_layout()
    plt.savefig('figs/Figure_16.jpeg', dpi=300)

    # Biểu đồ PLANTS
    plt.figure(figsize=(14, 8))
    plt.plot(t, P1, 'b-', label='P1', linewidth=3)
    plt.plot(t, P2, 'r-', label='P2', linewidth=3)
    plt.plot(t, P3, 'g-', label='P3', linewidth=3)
    # plt.plot(t, P1e, 'b--', label='P1 (scaled)', linewidth=3)
    # plt.plot(t, P2e, 'r--', label='P2 (scaled)', linewidth=3)
    # plt.plot(t, P3e, 'g--', label='P3 (scaled)', linewidth=3)
    plt.axis([1, 100, -0.1, 1])
    plt.xlabel('Year', fontsize=24)
    plt.ylabel('Mass units', fontsize=24)
    plt.legend(loc='best')
    plt.grid()
    plt.tight_layout()
    plt.savefig('figs/Figure_17.jpeg', dpi=300)

    # Biểu đồ HERBIVORES
    plt.figure(figsize=(14, 8))
    plt.plot(t, H1, 'b-', label='H1', linewidth=3)
    plt.plot(t, H2, 'r-', label='H2', linewidth=3)
    plt.plot(t, H3, 'g-', label='H3', linewidth=3)
    # plt.plot(t, H1e, 'b--', label='H1 (scaled)', linewidth=3)
    # plt.plot(t, H2e, 'r--', label='H2 (scaled)', linewidth=3)
    # plt.plot(t, H3e, 'g--', label='H3 (scaled)', linewidth=3)
    plt.xlabel('Year', fontsize=24)
    plt.ylabel('Mass units', fontsize=24)
    plt.legend(loc='best')
    plt.grid()
    plt.tight_layout()
    plt.savefig('figs/Figure_18.jpeg', dpi=300)

    # Biểu đồ CARNIVORES & HUMANS
    plt.figure(figsize=(14, 8))
    plt.plot(t, C1, 'b-', label='C1', linewidth=3)
    # plt.plot(t, C1e, 'b--', label='C1 (scaled)', linewidth=3)
    plt.plot(t, C2, 'r-', label='C2', linewidth=3)
    # plt.plot(t, C2e, 'r--', label='C2 (scaled)', linewidth=3)
    plt.xlabel('Year', fontsize=24)
    plt.ylabel('Mass units', fontsize=24)
    plt.legend(loc='best')
    plt.grid()

    plt.tight_layout()
    plt.savefig('figs/Figure_19.jpeg', dpi=300)

    # Biểu đồ POOLS
    plt.figure(figsize=(14, 8))
    plt.plot(t, RP, 'b-', label='RP', linewidth=3)
    plt.plot(t, IRP, 'r-', label='IRP', linewidth=3)
    plt.plot(t, ERP, 'g-', label='ERP', linewidth=3)
    # plt.plot(t, RPe, 'b--', label='RP (scaled)', linewidth=3)
    # plt.plot(t, IRPe, 'r--', label='IRP (scaled)', linewidth=3)
    # plt.plot(t, ERPe, 'g--', label='ERP (scaled)', linewidth=3)
    plt.xlabel('Year', fontsize=24)
    plt.ylabel('Mass units', fontsize=24)
    plt.legend(loc='best')
    plt.grid()
    plt.axis([1, 100, -0.2, 1.3])
    plt.tight_layout()
    plt.savefig('figs/Figure_20.jpeg', dpi=300)
