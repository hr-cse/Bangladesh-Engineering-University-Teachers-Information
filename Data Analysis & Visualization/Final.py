
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
import seaborn as sns


buet_calculation_df = pd.read_csv("buet_calculation_df.csv")
cuet_calculation_df = pd.read_csv("cuet_calculation_df.csv")
duet_calculation_df = pd.read_csv("duet_calculation_df.csv")
ruet_calculation_df = pd.read_csv("ruet_calculation_df.csv")

df = [buet_calculation_df,cuet_calculation_df,duet_calculation_df,ruet_calculation_df]
final_info = pd.concat(df)

#final_info.to_csv("final_info.csv")
'''
print(final_info["Total Professor"],final_info["university_name"])

plt.hist(final_info["Total Professor"],columns=final_info["university_name"])
plt.show()
'''
pro = []
male_pro = []
female_pro = []
u_name = []
asso_p = []
male_asso = []
female_asso = []
assi_p = []
male_assi = []
female_assi = []
m_haed = []
f_head = []
m_lec = []
f_lec = []
s_leave_f = []
s_leave_m = []
for p,mp,fp,na,asso,masso,fasso,assi,massi,fassi,mh,fh,ml,fl,slm,slf in zip(final_info["Total Professor"],final_info["Total Male Pro"],final_info["Total Female Pro"],
            final_info["university_name"],final_info["Total Associate Pro"],final_info["Total Male Asso. Pro"],
            final_info["Total Female Asso. Pro"],final_info["Total Assistant Pro"],final_info["Total Male Assi. Pro"],
            final_info["Total Female Assi. Pro"],final_info["Total Male Head"],final_info["Total Female Head"],
            final_info["Total Male Lec"],final_info["Total Female Lec"],final_info["study_leave_male"],final_info["study_leave_female"]):
    #print(v,n,"\n")
    pro.append(p)
    male_pro.append(mp)
    female_pro.append(fp)
    u_name.append(na)
    asso_p.append(asso)
    male_asso.append(masso)
    female_asso.append(fasso)
    assi_p.append(assi)
    male_assi.append(massi)
    female_assi.append(fassi)
    m_haed.append(mh)
    f_head.append(fh)
    m_lec.append(ml)
    f_lec.append(fl)
    s_leave_m.append(slm)
    s_leave_f.append(slf)













for i in range(0,4):
    x = [1,2,3]
    x1 = [4,5,6]
    x2 = [7,8,9]
    x3 = [10,11]
    x4 = [1,2]
    y = [pro[i],male_pro[i],female_pro[i]]
    y1 = [asso_p[i],male_asso[i],female_asso[i]]
    y2 = [assi_p[i],male_assi[i],female_assi[i]]
    y3 = [m_lec[i],f_lec[i]]
    y4 = [s_leave_m[i],s_leave_f[i]]


    plt.text(3,-20,["T=Total","M= Male","F=Female"])

    plt.bar(x,y,label = "Professor")
    plt.text(0,pro[i]+4,["T",pro[i]])
    plt.text(1,male_pro[i]+2,["M",male_pro[i]])
    plt.text(2,female_pro[i]+1,["F",female_pro[i]])
    plt.legend()







    plt.bar(x1,y1,label = "Associate Pro.")
    plt.text(3,asso_p[i]+4,["T",asso_p[i]])
    plt.text(4,male_asso[i]+2,["M",male_asso[i]])
    plt.text(5,female_asso[i]+1,["F",female_asso[i]])
    plt.legend()

    plt.bar(x2,y2,label = "Assistant Pro.")
    plt.text(6,assi_p[i]+4,["T",assi_p[i]])
    plt.text(7,male_assi[i]+2,["M",male_assi[i]])
    plt.text(8,female_assi[i]+1,["F",female_assi[i]])
    plt.legend()

    plt.bar(x3,y3,label = "Lecturer")
    plt.text(9,m_lec[i]+4,["M",m_lec[i]])
    plt.text(10,f_lec[i]+2,["F",f_lec[i]])
    plt.legend()
    #plt.show()
    plt.title(u_name[i]+" Teachers Information.")

    plt.bar(x4,y4,label = "Study Leave",color = ('b','m'))
    plt.text(1,s_leave_m[i]+1,["M",s_leave_m[i]])
    plt.text(2,s_leave_f[i]+1,["F",s_leave_f[i]])
    plt.legend()
    #plt.show()








f = plt.figure()



colors1 = ['c','m']
plt.title("Total Professor. vs female_pro")
plt_o = f.add_subplot(311)
labels = "Male","Female"
plt_o.pie([pro[0],female_pro[0]],labels = labels,colors=colors1,startangle=90,shadow=True,explode=(0.1,0.1),autopct="%1.1f%%")
plt.title("                                                                               "+u_name[0])
plt.legend()

plt_t = f.add_subplot(312)
plt_t.pie([pro[1],female_pro[1]],colors=colors1,startangle=90,shadow=True,explode=(0.1,0.1),autopct="%1.1f%%")
plt.title(u_name[1])

plt_tr = f.add_subplot(325)
plt_tr.pie([pro[2],female_pro[2]],colors=colors1,startangle=90,shadow=True,explode=(0.1,0.1),autopct="%1.1f%%")
plt.title(u_name[2])

plt_f = f.add_subplot(326)
plt_f.pie([pro[3],female_pro[3]],colors=colors1,startangle=90,shadow=True,explode=(0.1,0.1),autopct="%1.1f%%")
plt.title(u_name[3])
#plt.show()





fig = plt.figure()

plt_one = fig.add_subplot(311)
plt.bar(1,pro[0],label = u_name[0])
plt.text(.8,pro[0]+2,pro[0])
plt.bar(2,pro[1],label = u_name[1])
plt.text(1.8,pro[1]+2,pro[1])
plt.bar(3,pro[2],label = u_name[2])
plt.text(2.8,pro[2]+2,pro[2])
plt.bar(4,pro[3],label = u_name[3])
plt.text(3.8,pro[3]+2,pro[3])
plt.title("Professor")
plt.legend()


plt_two = fig.add_subplot(312)
plt.bar(1,asso_p[0],label = u_name[0])
plt.text(.8,asso_p[0]+2,asso_p[0])
plt.bar(2,asso_p[1],label = u_name[1])
plt.text(1.8,asso_p[1]+2,asso_p[1])
plt.bar(3,asso_p[2],label = u_name[2])
plt.text(2.8,asso_p[2]+2,asso_p[2])
plt.bar(4,asso_p[3],label = u_name[3])
plt.text(3.8,asso_p[3]+2,asso_p[3])
plt.title("Associate Professor")


plt_three = fig.add_subplot(325)
plt.bar(1,assi_p[0],label = u_name[0])
plt.text(.8,assi_p[0]+2,assi_p[0])
plt.bar(2,assi_p[1],label = u_name[1])
plt.text(1.8,assi_p[1]+2,assi_p[1])
plt.bar(3,assi_p[2],label = u_name[2])
plt.text(2.8,assi_p[2]+2,assi_p[2])
plt.bar(4,assi_p[3],label = u_name[3])
plt.text(3.8,assi_p[3]+2,assi_p[3])
plt.title("Assistant Professor")

#plt.show()


ll = []
m_hh = 0
f_hh = 0
for i,j,mh,fh in zip(m_lec,f_lec,m_haed,f_head):
    ll.append(i+j)
    m_hh += mh
    f_hh += fh

plt_four = fig.add_subplot(326)
plt.bar(1,ll[0],label = u_name[0])
plt.text(.8,ll[0]+2,ll[0])
plt.bar(2,ll[1],label = u_name[1])
plt.text(1.8,ll[1]+2,ll[1])
plt.bar(3,ll[2],label = u_name[2])
plt.text(2.8,ll[2]+2,ll[2])
plt.bar(4,ll[3],label = u_name[3])
plt.text(3.8,ll[3]+2,ll[3])
plt.title("Lecturer")

#plt.show()



f= plt.figure()
plt1 = plt.subplot(211)
plt1.bar(1,m_hh,label = "Male Head")
plt1.text(.8,m_hh+1,m_hh)
plt1.bar(2,f_hh,label = "Female Head")
plt1.text(1.8,f_hh+1,f_hh)
plt.title("Male VS Female Head.")
plt1.legend()



colors1 = ['b','m']
plt2 = plt.subplot(212)
labels = "Male","Female"
plt2.pie([m_hh,f_hh],labels = labels,colors=colors1,startangle=90,shadow=True,explode=(0.1,0.1),autopct="%1.1f%%")
plt.legend()
plt.title("Male VS Female Head Percentage")
plt.show()




'''
colors2 = ['y','m','r','b']
plt_three = fig.add_subplot(212)
plt_three.pie(female_pro,labels = u_name,colors=colors2,startangle=9i,shadow=True,explode=(i.1,i.1,i.1,i),autopct="%1.1f%%")
plt.title("Total Female Professor.")
plt.show()

#plt.xlabel ("H")
#plt.ylabel ("A")
'''
