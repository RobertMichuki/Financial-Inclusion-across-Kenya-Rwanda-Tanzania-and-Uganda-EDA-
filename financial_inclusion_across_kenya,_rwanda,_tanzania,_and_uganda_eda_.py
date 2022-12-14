# -*- coding: utf-8 -*-
"""Financial Inclusion across Kenya, Rwanda, Tanzania, and Uganda EDA .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GZHtYqNk4-nujrup90cLsh6FOJtMhvcg

#Exploratory Data Analysis

#Overview 

Financial Inclusion remains one of the main obstacles to economic and human development in Africa. For example, across Kenya, Rwanda, Tanzania, and Uganda only 9.1 million adults (or 13.9% of the adult population) have access to or use a commercial bank account.

Traditionally, access to bank accounts has been regarded as an indicator of financial inclusion. Despite the proliferation of mobile money in Africa and the growth of innovative fintech solutions, banks still play a pivotal role in facilitating access to financial services. Access to bank accounts enables households to save and facilitate payments while also helping businesses build up their credit-worthiness and improve their access to other financial services. Therefore, access to bank accounts is an essential contributor to long-term economic growth.

## 1. Defining the question

### a) Specifying the Question

How we can predict which individuals are most likely to have or use a bank account across Kenya, Rwanda, Tanzania, and Uganda?

### b) Defining the Metric for Success

the objectives of this dataset include:


1.  Identifying which individuals are more likely to use the bank

2.  What are their age groups

### c) Understanding the context 

Financial Inclusion remains one of the main obstacles to economic and human development in Africa. For example, across Kenya, Rwanda, Tanzania, and Uganda only 9.1 million adults (or 13.9% of the adult population) have access to or use a commercial bank account.

Traditionally, access to bank accounts has been regarded as an indicator of financial inclusion. Despite the proliferation of mobile money in Africa and the growth of innovative fintech solutions, banks still play a pivotal role in facilitating access to financial services. Access to bank accounts enables households to save and facilitate payments while also helping businesses build up their credit-worthiness and improve their access to other financial services. Therefore, access to bank accounts is an essential contributor to long-term economic growth.

### d) Recording the Experimental Design

1. Define the question, the metric for success, the context, experimental design taken and the appropriateness of the available data to answer the given question.
2. Find and deal with outliers, anomalies, and missing data within the dataset.
3. Perform univariate, bivariate and multivariate analysis recording your observations.
4. Implement the solution by performing the respective analysis i.e. factor analysis, principal component analysis, and discriminant analysis.
5. Challenge your solution by providing insights on how you can make improvements.

## 2. Reading the Data
"""

# Commented out IPython magic to ensure Python compatibility.
#import libraries to be used 
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib
from matplotlib import pyplot as plt
# %matplotlib inline
##

#load the dataset
df = pd.read_csv('Financial Dataset - 1.csv')
df

#loading the top of the dataset
df.head()

#loading the bottom of the dataset
df.tail()

"""## 3. Checking the Data"""

# Determining the number of records in our dataset
df.count()

# checking the shape of the dataset
df.shape

# checking the data information
df.info()

"""## 4. Tidying the Dataset"""

# checking for missing values / null values
df.dropna(inplace=True)
df.isnull().sum()

"""#univariate analysis

###measuring central tendacy
"""

#mean of household_size
df.household_size.mean()

#mode of household_size
df.household_size.mode()

# median of household_size
df.household_size.median()

#mean of Respondent Age 
df['Respondent Age'].mean()

#mode of Respondent age
df['Respondent Age'].mode()

#median of Respondent age
df['Respondent Age'].median()

"""###Measures of Dispersion"""

# standar deviation for household_size
df.household_size.std()

#variance of household_size
df.household_size.var()

# standar deviation for Respondent age
df['Respondent Age'].std()

# variance for Respondent age
df['Respondent Age'].var()

#skeness for Respondent age
df['Respondent Age'].skew()

#skeness for household_size
df.household_size.skew()

#kurtosis for respondent age
df['Respondent Age'].kurt()

#kurtosis for household_size
df.household_size.kurt()

#quantiles for household_size
df.household_size.quantile([0.25,0.5,0.75])

#quantiles for respondent age
df['Respondent Age'].quantile([0.25,0.5,0.75])

# stat summarries 
df['Respondent Age'].describe()

df.household_size.describe()

#checking for outliers using a boxplot
df.boxplot('Respondent Age')

df.boxplot('household_size')

df.household_size.plot(kind= 'hist', title = 'Univariate: household_size Histogram', color = 'teal');

sn.histplot(df.household_size,kde=True)

sn.histplot(df['Respondent Age'],kde=True)

# checking household_size distribution
plt.figure(figsize=(10,6))
df['Respondent Age'].hist() 
plt.title("Respondent Age Distribution")
plt.xlabel('Respondent Age')
plt.show()

"""From the distribution it is clear that the majority of the respondents are between age 20yrs and 40yrs. The maximum age is 100yrs and the minimum is 16yrs"""

# checking household_size distribution
plt.figure(figsize=(12,6))
df.household_size.hist() 
plt.title("Household Size Distribution")
plt.xlabel('household_size')
plt.show()

"""Household size is not normaly distributed and most households have 2 members"""

# catplot showing bank account distribution 
sn.catplot(x="Has a Bank account", kind="count", data=df)
plt.title("Banck Account Distribution")

"""From the distribution it is clear that most of the respondents have no bank accounts """

# pie chat showing percentage of respondents with bank accounts
colors = ['teal','red']
df['Has a Bank account'].value_counts().plot(kind='pie',figsize=(6,6),fontsize=13,autopct='%1.1f%%',explode=(0, 0.1),colors=colors,startangle=90);



"""From the pie chat we can see that only 14.1% of the respondents have bank accounts """

#catplot showing distribution of country respondents
sn.catplot(x='country', kind='count', data=df)
plt.title('Country of Respondents Distribution')

"""we can see that most of the respondents come from Rwanda and the least come from Uganda"""

# pie chat showing countries of respondents 
colors = ['blue','yellow', 'teal','pink']
df['country'].value_counts().plot(kind='pie',figsize=(6,6),fontsize=13,autopct='%1.1f%%',colors=colors,startangle=90);

"""We can see from the pie chat above that 37.2% of our respondents are Rwandees and lowest respondents are Ugandans at 8.9%

"""

# catplot showing distribution of respondents gender
sn.catplot(x='gender_of_respondent', kind='count', data=df)
plt.title('gender_of_respondent Distribution')

"""Most of the respondents are Female"""

# catplot showing distribution of respondents location 
sn.catplot(x='Type of Location', kind='count', data=df)
plt.title('Type of Location Distribution')

"""Looks like most of  the respondents live in rural setups"""

# catplot showing the distribution of Cell Phone Access	
sn.catplot(x='Cell Phone Access', kind='count', data=df)
plt.title('Cell Phone Access Distribution')

"""We can see that most of our respondents have access to a cellphone"""

# catplot showing the distribution of year of respondents 
sn.catplot(x='year', kind='count', data=df)
plt.title('year Distribution')

"""From the distribution we can see that our data was collected between 2016 and 2018 where high collection was done in 2016 and 2018 and low collection done in 2017"""

# cat plot showing distribution of respondents job type
sn.catplot(x='Type of Job', kind='count', data= df)
plt.title("Job Type Distribution")

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large' ) 
plt.show()

"""From the ditribution we can see that most of the respondents are self  employed followed by informally employed and those who farm and fish. while few of them are government employees on those who refused to answer"""

# cat plot showing distribution of respondents marital_status	
sn.catplot(x='marital_status', kind='count', data= df)
plt.title('marital_status	 Distribution')

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large' ) 
plt.show()

"""Most of the respondents are Married while the least are divorced """

# cat plot showing distribution of respondents Level of Educuation
sn.catplot(x='Level of Educuation', kind='count', data= df)
plt.title('Level of Educuation Distribution')

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large' ) 
plt.show()

"""Most of our respondents from our dataset have primary level eduction while the least have attended specialized training

#Bivariate Analysis
"""

df.plot(x = 'household_size', y = 'Respondent Age', kind='scatter')
plt.title('household_size  vs Respondent Age')

# Labelling our x axis
plt.xlabel('household_size')

# Labelling our y axis
plt.ylabel('Respondent Age')

# We then display our scatterplot as shown below
plt.show()

"""respondent age and houshold size show an inverse relation."""

# bivariate countplot of gender_of _respondents vs bank account 
plt.figure(figsize=(13, 5))
sn.countplot('gender_of_respondent', hue= 'Has a Bank account', data=df)
plt.xticks( 
    fontweight='light', 
    fontsize='x-large')
plt.show()

"""We can see from the above plot that  more  male respondents have bank acounts despite the dataset having more female respondents. we can then make an assumpton that females have less chance of having a bank account """

# bivariate countplot of marital_statust vs bank account 
plt.figure(figsize=(13, 5))
sn.countplot('marital_status', hue= 'Has a Bank account', data=df)
plt.xticks( 
    fontweight='light', 
    fontsize='x-large')
plt.show()

"""From the distribution we can see that the lagest number of respondents who own bank accounts are married """

# bivariate countplot of Type of Location vs bank account 
plt.figure(figsize=(13, 5))
sn.countplot('Type of Location', hue= 'Has a Bank account', data=df)
plt.xticks( 
    fontweight='light', 
    fontsize='x-large')
plt.show()

"""The number of respondents who own bank accounts are similar for both rural and urban location. It is also clear that more respondents from rular location dont own bank account.This confirms the assumption that people with rular location are less likely to have a bank account."""

# bivariate countplot of Level of Educuation vs bank account 
plt.figure(figsize=(13, 5))
sn.countplot('Level of Educuation', hue= 'Has a Bank account', data=df)
plt.xticks( 
     rotation=45, 
    horizontalalignment='right',fontweight='light', 
    fontsize='x-large')
plt.show()

"""From the plot we can see that a high number of respondents have primary level education and don't own bank accounts.This confirms the assumption that people with lower level of education  are less likely to have a bank account."""

# bivariate countplot of Type of Job vs bank account 
plt.figure(figsize=(13, 5))
sn.countplot('Type of Job', hue= 'Has a Bank account', data=df)
plt.xticks( 
     rotation=45, 
    horizontalalignment='right',fontweight='light', 
    fontsize='x-large')
plt.show()

"""From the plot above we can see that most of our respondents are self employed and don't own bank accounts """

# bivariate countplot of Cell Phone Accessvs bank account 
plt.figure(figsize=(13, 5))
sn.countplot('Cell Phone Access', hue= 'Has a Bank account', data=df)
plt.xticks( 
    fontweight='light', 
    fontsize='x-large')
plt.show()

"""From the plot above we can see that most of the respondents have access to  cellphones but done have bank accounts. This maybe as a result of increased convinience of mobile money platforms and digital lending platforms."""

# Calculating the pearson coefficient
pearson_coeff = df["Respondent Age"].corr(df["household_size"], method="pearson") 
print(pearson_coeff)
# Checking whether you have to define the pearson
coeff = df["Respondent Age"].corr(df["household_size"]) 
print(coeff)

"""Resondent Age and Household size are weakly correlated

##Recommendation.
There is need for education improvement as most of our respondents are up to primary level. our dependants should also be educated on different financial facilities  banks offers that will bennefit their businesses since most of them are self employed.

#Multivariate Analysis
##7. Implementing the Solution
###PCA
"""

# previewing   our data
df.head()

#droping null values
df.dropna(inplace=True)
df.isnull().sum()

df.info()

df.describe()

df.columns

#ENCODING THE DATA
df['country'] = df['country'].astype('category').cat.codes
df['Has a Bank account'] = df['Has a Bank account'].astype('category').cat.codes
df['Type of Location'] = df['Type of Location'].astype('category').cat.codes
df['Cell Phone Access'] = df['Cell Phone Access'].astype('category').cat.codes
df['gender_of_respondent'] = df['gender_of_respondent'].astype('category').cat.codes
df['Type of Job'] = df['Type of Job'].astype('category').cat.codes
df['Respondent Age'] = df['Respondent Age'].astype('category').cat.codes
df['uniqueid'] = df['uniqueid'].astype('category').cat.codes
df['Level of Educuation'] = df['Level of Educuation'].astype('category').cat.codes
df.head()

df.dtypes

# dropping unnecessary columns
to_drop = ['marital_status', 'The relathip with head']
df.drop(to_drop, axis=1, inplace=True)

X = df.drop(['uniqueid', 'Has a Bank account', 'household_size', 'Respondent Age', ], axis=1)
y = df['Has a Bank account']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#scalling our data
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
X_train

# Applying PCA
from sklearn.decomposition import PCA

pca = PCA()
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

#Explained Variance Ratio
explained_variance = pca.explained_variance_ratio_
explained_variance

from sklearn.decomposition import PCA

pca = PCA(n_components=1)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#  Performance Evaluation

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy' , accuracy_score(y_test, y_pred))

"""The accuracy level is 85%"""



"""##Factor Analysis

"""

df.head()

!pip install factor_analyzer==0.2.3

from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

chi_square_value,p_value=calculate_bartlett_sphericity(df)
chi_square_value, p_value

from factor_analyzer.factor_analyzer import calculate_kmo

kmo_all,kmo_model=calculate_kmo(df)
kmo_model

from factor_analyzer.factor_analyzer import FactorAnalyzer

# Creating factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(df, 11, rotation=None)

# Checking the Eigenvalues
ev, v = fa.get_eigenvalues()
ev

#Creating a scree plot using matplotlib
plt.scatter(range(1,df.shape[1]+1),ev)
plt.plot(range(1,df.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

# Performing Factor Analysis
# Creating factor analysis object and perform factor analysis
#
fa = FactorAnalyzer()
fa.analyze(df, 6, rotation="varimax")
fa.loadings

"""##Discriminant Analysys"""

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from tqdm import tqdm_notebook

import warnings
warnings.filterwarnings('ignore')

df.head()

X = df.iloc[:, 3:6].values
y = df.iloc[:, 3].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
X_train.shape

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=1)
X_train = lda.fit_transform(X_train, y)
X_test = lda.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy' + str(accuracy_score(y_test, y_pred)))

"""the accuracy score is 100%

## Challenging the solution
Is the data sufficient to make the right conclusions? financial inclusion should not be based on bank accout alone as there are other mobile banking platforms that offer simillar services but with convinience.

## Follow up questions
1. Did we have the right data?
2. Did we have the right question?
"""

