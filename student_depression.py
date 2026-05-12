import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import the data from the csv file and convert it into the dataframe 
data = pd.read_csv(r"C:\Users\ADMIN\OneDrive\Desktop\student depression\student depression.csv")
#print(data)

# cleaning of the data
# it shows the no of rows , name of the columns, data types 
print(data.info())

# generates statistical sumarry of the data
print("describing the data")
print(data.describe())

# with the help of this method we can check the null values in our datasets and find the sum of the null values
print("checking the null values in the data")
print(data.isnull().sum())

#in the given 27000 data only 3 is empty so instead of droping the rows i used bfill to fill as it will not change any outcome
print("filling data using bfill")
data = data.bfill()

#checking for the duplicated data in the datasets
print("duplicated data in the datasets")
print(data.duplicated().sum())

print("column names", data.columns)

#views of the data
print(data.head())

print(data['Age'].describe())

print(data.columns.tolist())
print(data.shape)

#EDA(exploratory data analytics)
# Insights
# Here we are counting the number of people who have suicidal thoughts
print(data['Have you ever had suicidal thoughts ?'].value_counts())

# With a graphical representation we are trying to show that in most of the cases CGPA is not related to suicidal thought 
sns.boxplot(x='Have you ever had suicidal thoughts ?', y='CGPA', data=data)
plt.title('CGPA vs Suicidal Thoughts')
plt.show()

# with this representation we are showing that the students with higher financial stress tend to more suicidal thoughts 
sns.boxplot(x='Have you ever had suicidal thoughts ?', y='Financial Stress', data=data)
plt.title('Financial Stress vs Suicidal Thoughts')
plt.show()

# Here we are counting the number of people who are going through depression
print(data['Depression'].value_counts())

print(pd.crosstab(data['Depression'], data['Have you ever had suicidal thoughts ?']))

#to get the heatmap for corelation to get more insights but had a proble as our Sleep Duration in the data set was in the object form so we changed the datatype of the Sleep duration from object to float
print(data['Sleep Duration'].value_counts())
sleep_map = {
    'Less than 5 hours': 4.5,
    '5-6 hours': 5.5,
    '7-8 hours': 7.5,
    'More than 8 hours': 9,
    'Others': np.nan
}

#as we had the 18 rows with others so we droped the 18 rows
data['Sleep Duration'] = data['Sleep Duration'].map(sleep_map)
data = data.dropna(subset=['Sleep Duration'])
print(data['Sleep Duration'].dtype)

#Differentiating the data based on the gender 
print("depression percentage based on genders")
print(pd.crosstab(data['Gender'], data['Depression'], normalize='index') * 100)

#getting the data to answer the all city and knowing the top 5 city and degree within the dataset
print("all city")
print(data['City'].nunique())
print(data['City'].value_counts().head())
print(data['Degree'].nunique())
print(data['Degree'].value_counts().head())

# Top 5 cities suicidal thoughts rate
top_cities = data['City'].value_counts().head().index
city_data = data[data['City'].isin(top_cities)]
print(pd.crosstab(city_data['City'], city_data['Have you ever had suicidal thoughts ?'], normalize='index') * 100)

# Top 5 Courses suicidal thoughts rate
top_degree = data['Degree'].value_counts().head().index
degree_data = data[data['Degree'].isin(top_degree)]
print(pd.crosstab(degree_data['Degree'], degree_data['Have you ever had suicidal thoughts ?'], normalize='index') * 100)

# Age vs Depression
print(data.groupby('Depression')['Age'].describe())

# Academic Pressure vs Suicidal Thoughts
print(pd.crosstab(data['Academic Pressure'], data['Have you ever had suicidal thoughts ?'], normalize='index') * 100)

#created the heatmap for the corelation
sns.heatmap(data[['CGPA', 'Financial Stress', 'Academic Pressure', 'Work Pressure', 'Sleep Duration', 'Work/Study Hours', 'Depression']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

data.to_csv(r"C:\Users\ADMIN\OneDrive\Desktop\student depression\cleaned_student_depression.csv", index=False)
