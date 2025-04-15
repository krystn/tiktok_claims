# TikTok Verified vs. Unverified Accounts: A Hypothesis Test
This project explores whether TikTok verification status influences video view counts using hypothesis testing and statistical analysis in Python.

### 🧪 Hypothesis
**Null Hypothesis (H₀):** There is no difference in the number of views between TikTok videos posted by verified and unverified accounts.
<br>**Alternative Hypothesis (H₁):** There is a difference in the number of views between TikTok videos posted by verified and unverified accounts.
<br>**Significance Level:** 5% (α = 0.05)

### 🧰 Tools & Libraries
`pandas`, `numpy` – data manipulation
<br>`matplotlib`, `seaborn` – data visualization
<br>`scipy.stats` – statistical hypothesis testing

### 📈 Methodology
Loaded and cleaned the data
<br>Checked for and removed missing values
<br>Calculated average video view counts for verified vs. unverified users
<br>Conducted an independent two-sample t-test
<br>Compared the mean video views between the two groups

### 📊 Result
The p-value was less than 0.05, leading us to reject the null hypothesis.
<br>Conclusion: There is a statistically significant difference in the mean view counts between verified and unverified TikTok accounts.

### 💡 Takeaway
Verification status appears to play a meaningful role in video visibility on TikTok.
