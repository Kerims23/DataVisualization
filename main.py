import matplotlib.pyplot as plt

# Filter the DataFrame for the top 10 procedures
top10 = delta['ProcCd'].value_counts().nlargest(10).index
filtered_data = delta[delta['ProcCd'].isin(top10)]

# Group and plot the filtered data
grouped_counts = filtered_data.groupby(['ProcCd', 'NetworkStatus']).size().unstack()
grouped_counts.plot(kind='bar', stacked=True)

# Customize the plot as needed
plt.xlabel('Procedure Code')
plt.ylabel('Count')
plt.title('Top 10 Procedure Codes by NetworkStatus')
plt.legend(title='NetworkStatus')
plt.show()


