import matplotlib.pyplot as plt

# Updated data
updated_sma_values = [26561.7, 26811.7, 27061.7, 27311.7, 27561.7, 27811.7, 28061.7, 28311.7, 28561.7, 28811.7, 29061.7, 29311.7, 29561.7]
updated_acp_values = [0.5366E-07, 0.5268E-07, 0.4674E-07, 0.4677E-07, 0.7013E-07, 0.8382E-07, 0.8303E-07, 0.6103E-07, 0.2711E-07, 0.2431E-07, 0.2865E-07, 0.3512E-07, 0.3945E-07]
updated_flux_values = [0.7630E-03, 0.7319E-03, 0.6515E-03, 0.6758E-03, 0.1081E-02, 0.1302E-02, 0.1248E-02, 0.8935E-03, 0.3700E-03, 0.3248E-03, 0.4319E-03, 0.5677E-03, 0.6547E-03]

# Plotting updated ACP vs SMA
plt.figure(figsize=[10,5])
plt.plot(updated_sma_values, updated_acp_values, marker='o', label='ACP')
plt.title('Catastrophic Annual Collision Probability vs SMA')
plt.xlabel('SMA (km)')
plt.ylabel('ACP')
plt.grid(True)
plt.legend()
plt.show()

# Plotting updated Flux vs SMA
plt.figure(figsize=[10,5])
plt.plot(updated_sma_values, updated_flux_values, marker='o', color='r', label='Flux')
plt.title('Catastrophic Flux vs SMA')
plt.xlabel('SMA (km)')
plt.ylabel('Flux')
plt.grid(True)
plt.legend()
plt.show()
