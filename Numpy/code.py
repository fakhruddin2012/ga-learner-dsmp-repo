# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census=np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
import numpy as np 
age=census[:,0]
print(age)
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)


# --------------
#Code starts here
import numpy as np 
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)
race_list=[len_0,len_1,len_2,len_3,len_4]
minority_race=race_list.index(min(race_list))
print(minority_race)


# --------------
#Code starts here
import numpy as np
citizens=census[:,0]
#print(citizens)
senior=citizens>60
senior_citizens=census[senior]
print(senior_citizens)
working_hours=np.array(census[:,6])
working_hours_sum=sum(working_hours[senior])
print(working_hours_sum)
senior_citizens_len=len(list(senior_citizens))
print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np 
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=census[census[:,1]>10][:,7].mean()
avg_pay_low=census[census[:,1]<=10][:,7].mean()
print(avg_pay_high>avg_pay_low)


