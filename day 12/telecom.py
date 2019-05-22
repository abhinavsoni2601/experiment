import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df = pd.read_csv("Telecom_churn.csv")


df7=df[df['international plan']=='yes']
df7.groupby('state').min()



"""df6=df[df['churn']==True]
count1=df6['customer service calls'].count()
count=df6['customer service calls'][df6['customer service calls']>0].count()
count1=count1-count
plt.bar(['requested','no requested'],[count,count1])"""




"""df['account length'].max()
df5=df[df['account length']==243]"""




"""df4=df[df['churn']==True]
min1=df4['total day charge'].min()
min2=df4['total eve charge'].min()
min3=df4['total night charge'].min()
min4=df4['total intl charge'].min()
plt.bar(['day','evening','night','intl'],[min1,min2,min3,min4])"""




"""df2=df['international plan'][(df['churn']==True)&(df['international plan']=='yes')].count()
df3=df['voice mail plan'][(df['churn']==True)&(df['voice mail plan']=='yes')].count()
plt.bar(['intl plan','voice mail'],[df2,df3])"""




"""df1=df[df['churn']==True]
df1['total night minutes'].max()
state=df[df['total night minutes']==354.9]"""



"""df[(df['international plan']=='yes') & (df['voice mail plan']=='yes')&(df['churn']==True)].count()
churn_true=df['total intl charge'][(df['churn']==True) &(df['international plan']=='yes')].sum()
churn_false=df['total intl charge'][(df['churn']==False)&(df['international plan']=='yes')].sum()
plt.bar(['churn','Nchurn'],[churn_true,churn_false])"""



