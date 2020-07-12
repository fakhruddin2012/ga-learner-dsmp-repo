# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
#print(df.shape)
sum_of_fico=len(df.fico)
print(sum_of_fico)
greater_than_700=len(df[df.fico > 700])
#len(greater_than_700)
print(greater_than_700)
p_a=greater_than_700/sum_of_fico
print(p_a)
conso=len(df[df.purpose=='debt_consolidation'])
#print(conso)
p_b=conso/sum_of_fico
print(p_b)
df1=df.purpose=='debt_consolidation'
p_a_b=conso/greater_than_700
print(p_a_b)
result=p_a_b == p_a
print(result)

# code ends here#


# --------------
# code starts here
total=len(df)
#print(total)
paid_of=len(df[df['paid.back.loan']=='Yes'])
prob_lp=paid_of/total
print(prob_lp)
credit_of=len(df[df['credit.policy']=='Yes'])
prob_cs=credit_of/total
print(prob_cs)
new_df=df[df['paid.back.loan']=='Yes']
#print(new_df)
prob_pd_cs=len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
print(prob_pd_cs)
bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)


# code ends here


# --------------
# code starts he
df.purpose.value_counts(normalize=True).plot(kind='bar')
df1=df[df['paid.back.loan']=='No']
#df1.shape()
df1.plot(kind='bar')



# code ends here


# --------------
# code starts here
inst_median=df.installment.median()
print(inst_median)
inst_mean=df.installment.mean()
print(inst_mean)
df.hist(column='installment')
df.hist(column='log.annual.inc')
 


# code ends here


