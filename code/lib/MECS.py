import matplotlib.pyplot as plt

# Set the font to Times New Roman and font size to 14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14

# Data
learning_rates = [0.001, 0.005, 0.01, 0.015, 0.02]
accuracy = [95.3, 96.3, 96.7, 95.9, 95.7]

# Plotting
plt.plot(learning_rates, accuracy, marker='o', color='r', linestyle='-', linewidth=2, markersize=8)

# Adding titles and labels
plt.xlabel('Learning Rate')
plt.ylabel('Accuracy (%)')

# Set y-axis range
plt.ylim(92, max(accuracy) + 1)  # Set y-axis from 92 to max accuracy + 1 to give some space at the top

# Adjust the margins to reduce the white space
plt.subplots_adjust(top=0.95)  # Adjust top margin

# Save the plot as a PNG file with 300 DPI
plt.savefig('learning_rate_sensitivity_analysis.png', dpi=300)

# Show plot
plt.show()
