import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace 'your_file.xlsx' with the actual file path
file_path = 'P.xlsx'

# Read data from Excel file
df = pd.read_excel(file_path, engine='openpyxl', index_col=0)

# Determine the appropriate fmt parameter based on the data type
fmt_parameter = 'd' if df.dtypes.all() == 'int64' else '.2f'

# Create a heatmap
sns.heatmap(df, annot=True, cmap="YlGnBu", fmt=fmt_parameter)

# Add labels and title
plt.xlabel("Sales")
plt.ylabel("Date")
plt.title("Heatmap")

# Show the plot
plt.show()
