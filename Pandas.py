import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1
df = pd.read_csv('train.csv')
colors = ['salmon', 'plum', 'purple', 'cornflowerblue']
plt.hist(df[['A', 'C', 'T', 'G']], color=colors, label=['A', 'C', 'T', 'G'])
plt.legend()
plt.show()

#2
columns = ['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']
df.loc[df['mismatches'] > df['mismatches'].mean(), columns].to_csv('train_part.csv', index=None)

#3
marks_df = pd.read_excel('marks.xlsx', sheet_name='Python')
names = marks_df.columns[7:]
marks_df.loc[:, names].fillna(0, inplace=True)

for name in names:
    plt.hist(marks_df[name], bins=15, range=[0, marks_df[name].max() + 1])
    plt.title(name)
    plt.show()

print(marks_df[names].mean())
print(marks_df[names].median())

plt.figure(figsize=(16, 9))
plt.title('Marks correlation')
sns.heatmap(marks_df[names].corr(), vmin=-1, vmax=1, annot=True)
plt.show()
