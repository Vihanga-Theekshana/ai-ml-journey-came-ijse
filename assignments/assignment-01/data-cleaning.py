#Q1
import pandas as pd
import numpy as np

df = pd.read_csv('customers_messy_500.csv')
print(df.head()) #print first five raws
print(df.tail()) #print last five raws
print(df.shape) #print shape
print(list(df.columns))#print column name
print(df.dtypes)#print data types
print(df.info())
print(df.describe(include='all'))

#observations

print("""
1)
The score and income columns are stored as object (string) data types instead of numeric types (float/int). 
This suggests there are text characters, currency symbols, or formatting errors mixed with the numbers.
"""
"""
2)
Based on the info() output, there are missing values (nulls) in the dataset. For example, 
the [age] column only has [481] non-null entries out of the total rows.
"""
"""
3)
There are inconsistent labels and invalid values present. The purchased column seems to contain mixed formats (like Yes/No and 1/0),
and there may be out-of-range values in numeric columns like age or score.

""")

#Q2
missing_counts = df.isna().sum() #compute number of missing values
print(missing_counts)
persentage_of_missing_values_per_column = (df.isna().sum()/len(df))*100
print(persentage_of_missing_values_per_column)

print('customer_id column is mostly complete')
print('age column is mostly incomplete')
print("""
Why they don't appear in isna().sum():
Pandas treats empty strings ("") and spaces (" ") as valid text data, not as true missing values (NaN).
Therefore, isna() ignores them.

""")
# we can detect it,
empty_city_count = (df['city'].str.strip() == '').sum()
print(empty_city_count)

#Q3
print(df.loc[0:9,['customer_id','age','city','score']])
print(df.iloc[:10,:4])

#  Select only the score column as a Series
score_series = df['score']
print(type(score_series))

# Select age and score together as a DataFrame
age_score_df = df[['age','score']]
print(type(age_score_df))

print('loc is label-based and includes the final index, whereas iloc is position-based and excludes the final index.')

#Q4
df['age'] = pd.to_numeric(df['age'],errors='coerce')

is_present = df['score'].astype(str).str.contains('%')


df['score'] = df['score'].astype(str).str.replace('%','').str.strip()
df['score'] = pd.to_numeric(df['score'],errors='coerce')
df.loc[is_present,'score'] = df.loc[is_present,'score']/100


df['income'] = df['income'].astype(str).str.replace('LKR', '').str.replace(',','').str.strip()
df['income'] = pd.to_numeric(df['income'],errors='coerce')

print(df.dtypes)


#Q5
df['city'] = df['city'].str.strip()
df['city'] = df['city'].str.strip().str.title()
df['city'] = df['city'].replace({'Colmbo':'Colombo','Gale':'Galle'})
df['city'] = df['city'].replace('',np.nan)

print(df['city'].value_counts())

#Q6
df = df.dropna(subset=['customer_id'])
df = df[df.isna().sum(axis=1) < 3]
df['age'] = df['age'].fillna(df['age'].median())
df['score'] = df['score'].fillna(df['score'].median())
df['income'] = df['income'].fillna(df['income'].median())

print("""
I chose to fill missing city values with the mode 
because it preserves the remaining valid data in those rows that would otherwise be lost.
""")
df['city'] = df['city'].fillna(df['city'].mode()[0])

print(df.isna().sum())

#Q7
initial_rows = df.shape[0]


#Keep only rows where age is between 18 and 80 (inclusive)
df = df[(df['age'] >= 18 ) & (df['age'] <= 80 )]

#Keep only rows where score is between 0 and 1 (inclusive)
df = df[(df['score'] >= 0) & (df['score'] <= 1)]

#Keep only rows where purchases is not missing and is >= 0
df = df[(df['purchases'].notna()) & (df['purchases'] >= 0)]

removed_rows = (initial_rows - df.shape[0])
print(removed_rows)

print(df.shape)


#Q8
def clean_purchased_value(value):
    value_str = str(value).strip().lower()
    
    if value_str in ['yes', 'true', 'y','1']:
        return 1
    elif value_str in ['no','false','n','0']:
        return 0
    else:
        return np.nan
    
df['purchased'] = df['purchased'].apply(clean_purchased_value)

df = df.dropna(subset=['purchased'])

df['purchased'] = df['purchased'].astype(int)

df = df.drop_duplicates()
df = df.drop_duplicates(subset=['customer_id'] , keep='first')

final_number_of_rows = df.shape[0]
print(f"Final number of rows: {final_number_of_rows}")

#Q9
df['score_pct'] = df['score']*100
df['high_value'] = df['income'] > df['income'].median()

df_sorted = df.sort_values(by='score' , ascending=False)
print(df_sorted.head(10))

colombo_filterd = df[(df['city'] == 'Colombo') & (df['score'] >= 0.7) & (df['purchased'] == 1)]

print(f'Count of matching customers in Colombo: {len(colombo_filterd)}')

#Q10
print(df['city'].value_counts())
print(df['purchased'].value_counts())

mean_score = df.groupby('city')['score'].mean()
print(mean_score)

mean_income_and_city = df.groupby('city')[['income','purchases']].mean()                   
print(mean_income_and_city)

summary_table = df.groupby('city').agg(
    row_count = ('age','count'),
    mean_age = ('age','mean'),
    mean_score = ('score','mean'),
    purchase_rate = ('purchased','mean') 
)
print(summary_table)

print(""" 
1) High Conversion in Small Markets: Negombo has the fewest customers (33) but the highest purchase rate (39.3%), making city a strong predictive feature.

2) Age Matters: Negombo also has the highest mean age (44.4). This suggests older customers may have a higher tendency to buy.

3) Volume Doesn't Equal Conversion: Colombo has the most customers (211) but only a moderate 31.7% purchase rate, showing that the largest market isn't necessarily the most efficient.
Score Isn't Everything: Galle has the highest mean score (0.619) but a lower purchase rate than Negombo. The ML model will need to combine score with other variables to predict purchases accurately.

""")

df.info()
