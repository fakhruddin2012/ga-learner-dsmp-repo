# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here

#Loading the data
data=pd.read_csv(path)

#Plotting histogram of Rating
data['Rating'].plot(kind='hist')

plt.show()


#Subsetting the dataframe based on `Rating` column
data=data[data['Rating']<=5]

#Plotting histogram of Rating
data['Rating'].plot(kind='hist')   

#Code ends here


# --------------
# code starts here
total_null=data.isnull().sum()
#print(total_null)
percent_null=(total_null/data.isnull().count())*100
print(percent_null)
missing_data=pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)
#missing_data=total_null+percent_null
print(missing_data)
#print(total_null.dtypes)
#print(percent_null.dtypes)
data=data.dropna()
total_null_1=data.isnull().sum()
percent_null_1=(total_null/data.isnull().count())
missing_data_1=pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here
import seaborn as sns
import matplotlib.pyplot as plt
pl=sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)
pl.set_xticklabels(rotation=90)
plt.title("Rating vs Category [BoxPlot]")
plt.show()
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt 
#Code starts here
data['Installs'].value_counts()
data['Installs']=data['Installs'].str.replace(',','')
data['Installs']=data['Installs'].str.replace('+','')
data['Installs']=data['Installs'].astype(int)
le=LabelEncoder()
#print(data['Installs'])
data['Installs']=le.fit_transform(data['Installs'])
#print(data['Installs'])
sns.regplot(x="Installs", y="Rating",data=data)
plt.title('Rating vs Installs [RegPlot]')
#Code ends here



# --------------
#Code starts here
import seaborn as sns
import matplotlib.pyplot as plt
print(data['Price'].value_counts(normalize=True).astype(str))
data['Price']=data['Price'].str.replace('$','').astype(float)
sns.regplot(x="Price", y="Rating",data=data)
plt.title('Rating vs Price [RegPlot]')
#Code ends here


# --------------

#Code starts here

#Finding the length of unique genres
print( len(data['Genres'].unique()) , "genres")

#Splitting the column to include only the first genre of each app
data['Genres'] = data['Genres'].str.split(';').str[0]

#Grouping Genres and Rating
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())

#Sorting the grouped dataframe by Rating
gr_mean=gr_mean.sort_values('Rating')

print(gr_mean.head(1))

print(gr_mean.tail(1))

#Code ends here



# --------------
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#print(data['Last Updated'])
data['Last Updated']=pd.to_datetime(data['Last Updated'])
max_date=data['Last Updated'].max()
print(max_date)
data['Last Updated Days']=(max_date-data['Last Updated'])
data['Last Updated Days']=(data['Last Updated Days'].dt.days)
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')


