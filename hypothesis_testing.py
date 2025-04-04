# Null hypothesis: there is no difference in the number of views between TikTok videos posted by verified and unverified accounts
# Alternative hypothesis: there is a difference in the number of views between TikTok videos posted by verified and unverified accounts
# significance level: 5%

# Import packages for data manipulation
import pandas as pd
import numpy as np

# Import packages for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Import packages for statistical analysis
from scipy import stats

# Load dataset
data = pd.read_csv("tiktok_dataset.csv")

# Display data
data.head()
data.describe()

# Check for missing values
data.isna().sum()

# Remove rows with missing values
data = data.dropna(axis=0)
data.head()

# Calculate the mean view count for each group in 'verified_status'
data.groupby("verified_status")["video_view_count"].mean()

# Conduct a two-sample t-test to compare means
not_verified = data[data["verified_status"] == "not verified"]["video_view_count"]
verified = data[data["verified_status"] == "verified"]["video_view_count"]

stats.ttest_ind(a=not_verified, b=verified, equal_var=False)

# The P-value is less than the significant level of 5%, therefore, reject the null hypothesis.
# There is a statistically significant difference in the mean view counts between verified and unverified accounts.
