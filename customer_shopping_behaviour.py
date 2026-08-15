import pandas as pd
df=pd.read_csv("customer_shopping_behavior.csv")

print(df)
#print(df.describe(include="all"))

df['Review Rating']= df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
#print(df.isnull().sum())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

labels=['Young Adult','Adult','Middle-aged','Senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']].head(10))
frequency_mapping={'Fortnightly':14, 'weekly':7, 'Monthly':30,'Quarterly':90,'Bi-weekly':14,
    'Annualy':365,
    'Every 3 months':90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
md=df[['purchase_frequency_days','frequency_of_purchases']].head(10)
#print(md)
df=df.drop('promo_code_used',axis=1)
#print(df)
#print(df.columns)
