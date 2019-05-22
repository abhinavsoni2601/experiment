import pandas as pd
df = pd.read_csv("training_titanic.csv")
df=df[['PassengerId','Survived','Sex','Age']]
df['Age'] = df['Age'].fillna(df['Age'].mean())
df_male=df[(df['Sex'] =='male') ]
df_female=df[(df['Sex'] =='female') ]
df_male['Survived'].value_counts()
df_female['Survived'].value_counts()
df["child"] = df["Age"].map(lambda x: 1 if x <=18 else 0 )
df_child=df[(df['child'] ==1) ]
df_child['Survived'].count()