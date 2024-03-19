import pickle
import numpy as np
import matplotlib.pyplot as plt
# Set individual font sizes for various elements
plt.rcParams['axes.titlesize'] = 20  # Set the font size for plot titles
plt.rcParams['axes.labelsize'] = 18  # Set the font size for axis labels
plt.rcParams['xtick.labelsize'] = 16  # Set the font size for X tick labels
plt.rcParams['ytick.labelsize'] = 16  # Set the font size for Y tick labels
plt.rcParams['legend.fontsize'] = 14  # Set the font size for legends
plt.rcParams['font.size'] = 12  # Default font size for all text (if not specified otherwise)


with open('output/test.pkl', 'rb') as f:
    data = pickle.load(f)
    
    
# Extracting individual data arrays from the loaded data
kep_array_initial, kep_array_final, reentry_times, kep_array_90, latlon_array_90, latlon_array_initial, latlon_array_final = data


seconds = np.arange(0, 365 * 10) 
percent_remaining = []

# For each day, calculate the percentage of objects that haven't reentered yet
for second in seconds:
    removed_objects = np.sum(reentry_times < second*86400)
    percent_remaining.append(100 * (len(kep_array_initial)-removed_objects) / len(kep_array_initial))

# Plotting the percentage of objects remaining over time
plt.figure(figsize=(10, 6))
plt.plot(seconds, percent_remaining, color='purple')
plt.title('Percentage of Objects Remaining Over 10 Years')
plt.xlabel('Time (days)')
plt.ylabel('Percentage (%)')
plt.grid(True)

# Function to create Angular Distribution plot with fixed axes
def create_angular_distribution_plot_fixed_axes(kep_array, title, raan_range, incl_range):
    inclinations = np.degrees(kep_array[:, 2])  # Convert from radians to degrees
    raan = np.degrees(kep_array[:, 3])  # Convert from radians to degrees
    plt.figure(figsize=(10, 6))
    plt.scatter(raan, inclinations, s=10, c='red', alpha=0.5)
    plt.xlim(raan_range)
    plt.ylim(incl_range)
    plt.title(title)
    plt.xlabel('RAAN (degrees)')
    plt.ylabel('Inclination (degrees)')
    plt.grid(True)
print(len(kep_array_final))
# Determine fixed axes ranges based on all data sets
eccentricities_all = np.concatenate((kep_array_initial[:, 1], kep_array_90[:, 1], kep_array_final[:, 1]))
raan_all = np.degrees(np.concatenate((kep_array_initial[:, 3], kep_array_90[:, 3], kep_array_final[:, 3])))
inclinations_all = np.degrees(np.concatenate((kep_array_initial[:, 2], kep_array_90[:, 2], kep_array_final[:, 2])))

raan_range = (min(raan_all*0.95), max(raan_all*1.05))
incl_range = (min(inclinations_all*0.95), max(inclinations_all*1.05))

create_angular_distribution_plot_fixed_axes(kep_array_initial, 'Angular Distribution: Immediately After Breakup', raan_range, incl_range)
create_angular_distribution_plot_fixed_axes(kep_array_90, 'Angular Distribution: 90 Days After Breakup', raan_range, incl_range)
create_angular_distribution_plot_fixed_axes(kep_array_final, 'Angular Distribution: Final Analysis Point', raan_range, incl_range)



# Function to create Gabbard plot with SMA on x-axis and both Apogee and Perigee altitudes on y-axis
def create_gabbard_plot_sma_apogee_perigee(kep_array, title, sma_range, alt_range):
    semi_major_axis = kep_array[:, 0] / 1000  # Convert from meters to altitude in kilometers
    eccentricities = kep_array[:, 1]
    apogees = (semi_major_axis ) * (1 + eccentricities) - 6378  # Calculate apogee altitude
    perigees = (semi_major_axis ) * (1 - eccentricities) - 6378  # Calculate perigee altitude
    plt.figure(figsize=(10, 6))
    plt.scatter(semi_major_axis, apogees, s=10, c='blue', alpha=0.5, label='Apogee')
    plt.scatter(semi_major_axis, perigees, s=10, c='red', alpha=0.5, label='Perigee')
    plt.xlim(sma_range)
    plt.ylim(alt_range)
    plt.title(title)
    plt.xlabel('Semi-major Axis(km)')
    plt.ylabel('Altitude (km)')
    plt.legend()
    plt.grid(True)

# Determine fixed axes ranges based on all data sets for SMA, Apogee, and Perigee
semi_major_axis_all_km = (np.concatenate([(kep_array_initial[:, 0]), (kep_array_90[:, 0]), (kep_array_final[:, 0])]) / 1000)
apogees_all = (semi_major_axis_all_km) * (1 + eccentricities_all) - 6378
perigees_all = (semi_major_axis_all_km) * (1 - eccentricities_all) - 6378

sma_range = (min(semi_major_axis_all_km) * 0.8, max(semi_major_axis_all_km) * 1.1)
alt_range = (min(perigees_all) * 0.3, max(apogees_all) * 1.1)
print(alt_range[0])

# Generate Gabbard plots with SMA, Apogee, and Perigee for comparison
create_gabbard_plot_sma_apogee_perigee(kep_array_initial, 'Gabbard Plot: Immediately After Breakup', sma_range, alt_range)
create_gabbard_plot_sma_apogee_perigee(kep_array_90, 'Gabbard Plot: 90 Days After Breakup', sma_range, alt_range)
create_gabbard_plot_sma_apogee_perigee(kep_array_final, 'Gabbard Plot: Final Analysis Point', sma_range, alt_range)
print(min(perigees_all))
plt.show()
print('hi')