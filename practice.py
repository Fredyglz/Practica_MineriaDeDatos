# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:58:38 2020

@author: Jose Alfredo Romero Gonzalez
"""

import math as mt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def func_split(l):
    l_aux = []
    d = {}
    for i in l:
        if i is not np.nan:
            if ';' in i: 
                i = i.split(';')
            l_aux.append(i)
        else:
            l_aux.append('NaN')
    for lista in l_aux:
        if lista != 'NaN':
            if isinstance(lista, list): 
                for item in lista:
                    if item not in d:
                        d[item] = 0
            else:
                if lista not in d:
                        d[lista] = 0
    return l_aux, d

def func_yearscodeToNum(yearscode):
    yearscodeNum = []
    for yc in yearscode:
        if yc == "NaN":
            yearscodeNum.append(0.0)
        elif yc == 'Less than 1 year':
            yearscodeNum.append(0.5)
        elif yc == 'More than 50 years':
            yearscodeNum.append(51.0)
        else:
            yearscodeNum.append(float(yc))
    return yearscodeNum
    
def func_salaryToNum(salary):
    salaryNum = []
    for s in salary:
        if mt.isnan(s):
            salaryNum.append(0.0)
        else:
            salaryNum.append(s)
    return salaryNum

def func_ageToNum(age):
    ageNum = []
    for a in age:
        if mt.isnan(a):
            ageNum.append(0.0)
        else:
            ageNum.append(a)
    return ageNum

def func_edlevelToNum(edlevel):
    edlevelNum = []
    for el in edlevel:
        if el == 'I never completed any formal education':
            edlevelNum.append(1.0)
        elif el == 'Primary/elementary school':
            edlevelNum.append(2.0)
        elif el == 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)':
            edlevelNum.append(3.0)
        elif el == 'Some college/university study without earning a degree':
            edlevelNum.append(4.0)
        elif el == 'Bachelor’s degree (BA, BS, B.Eng., etc.)':
            edlevelNum.append(5.0)
        elif el == 'Associate degree':
            edlevelNum.append(6.0)
        elif el == 'Professional degree (JD, MD, etc.)':
            edlevelNum.append(7.0)
        elif el == 'Master’s degree (MA, MS, M.Eng., MBA, etc.)':
            edlevelNum.append(8.0)
        elif el == 'Other doctoral degree (Ph.D, Ed.D., etc.)':
            edlevelNum.append(9.0)
        else:
            edlevelNum.append(0.0)
    return edlevelNum
    
def func_min(l):
    return l[0]

def func_max(l):
    return l[-1]

def percentil(lista, perc):
    med = (len(lista)-1)*perc
    pl = mt.floor(med)
    pu = mt.ceil(med)
    return lista[pl]+(lista[pu] - lista[pl]*perc)

def func_desviacionEstandar(l, media):
    v = 0.0     
    for i in l:
        v += (float(i)-media)**2
    ds = (v/len(l))**(1/2)
    return ds

def func_mediana(l):
    return np.quantile(l, 0.5)

def func_media(l):
    return sum(l)/len(l)

def summary(l):
    l.sort()
    v_min = func_min(l)
    v_max = func_max(l)
    #mediana = percentil(l, 0.5)
    mediana = func_mediana(l)
    media = func_media(l)
    #fq = percentil(l, 0.25)
    fq = np.quantile(l, 0.25)
    #tq = percentil(l, 0.75)
    tq = np.quantile(l, 0.75)
    ds = func_desviacionEstandar(l, media)
    print("Minimo: ", v_min)
    print("Maximo: ", v_max)
    print('Mediana: ', mediana)
    print('Media: ', media)
    print('1q: ', fq)
    print('3q: ', tq)
    print('Desviacion Estandar: ', ds)
    plt.boxplot(l)
    plt.show()

def in1(salary, gender):
    gender, d_g = func_split(gender)
    for i in d_g.keys():
        l_s = []
        for s, g in zip(salary, gender):
            if isinstance(g, list): 
                for item in g:
                    if item == i and not mt.isnan(s) and item != 'NaN':
                        l_s.append(s)
            elif g == i and not mt.isnan(s) and g != 'NaN':
                l_s.append(s)
        d_g[i] = l_s
        print('*************', i, '*************')
        summary(d_g[i])

def in2(salary, ethnicity):
    ethnicity, d_e = func_split(ethnicity)
    for i in d_e.keys():
        l_s = []
        for s, e in zip(salary, ethnicity):
            if isinstance(e, list): 
                for item in e:
                    if item == i and not mt.isnan(s) and item != 'NaN':
                        l_s.append(s)
            elif e == i and not mt.isnan(s) and e != 'NaN':
                l_s.append(s)
        d_e[i] = l_s
        print('*************', i, '*************')
        summary(d_e[i])
        
def in3(salary, devtype):
    devtype, d_dt = func_split(devtype)
    for i in d_dt.keys():
        l_s = []
        for s, dt in zip(salary, devtype):
            if isinstance(dt, list): 
                for item in dt:
                    if item == i and not mt.isnan(s) and item != 'NaN':
                        l_s.append(s)
            elif dt == i and not mt.isnan(s) and dt != 'NaN':
                l_s.append(s)
        d_dt[i] = l_s
        print('*************', i, '*************')
        summary(d_dt[i])

def in4(salary, country):
    country, d_c = func_split(country)
    for i in d_c.keys():
        l_s = []
        for s, c in zip(salary, country):
            if isinstance(c, list): 
                for item in c:
                    if item == i and not mt.isnan(s) and item != 'NaN':
                        l_s.append(s)
            elif c == i and not mt.isnan(s) and c != 'NaN':
                l_s.append(s)
        d_c[i] = l_s
        print('*************', i, '*************')
        if d_c[i] == []:
            print('Dont exists registers')
        else:
            d_c[i].sort()
            print('Mediana: ', func_mediana(d_c[i]))
            print('Media: ', func_media(d_c[i]))
            print('Desviacion Estandar: ', func_desviacionEstandar(d_c[i], func_media(d_c[i])))  

def in5(devtype):
    l_aux = []
    d_fdt = {}
    for i in devtype:
        if i is not np.nan:
            l_aux.append(i.split(';'))
    l_dt = [i for dt in l_aux for i in dt ]
    for i in l_dt:
        if not i in d_fdt:
            d_fdt[i] = 1  
        else:
            d_fdt[i] += 1  
    plt.title("Frequencies of responses for each developer type")
    plt.bar(range(len(d_fdt)), list(d_fdt.values()), edgecolor='black', align='center')
    plt.xticks(range(len(d_fdt)), list(d_fdt.keys()), rotation= 90)
    plt.show()

def in6(yearscode, gender):
    gender, d_g = func_split(gender)
    yearscode, d_yc = func_split(yearscode)
    for i in d_g.keys():
        yearscodefloat = []
        for yc, g in zip(yearscode, gender):
            if isinstance(g, list): 
                for item in g:
                    if item  == i and yc != 'NaN' and item != 'NaN':
                        if yc == 'Less than 1 year':
                            yearscodefloat.append(0.5)
                        elif yc == 'More than 50 years':
                            yearscodefloat.append(51.0)
                        else:
                            yearscodefloat.append(float(yc))
            elif g == i and yc != 'NaN' and g != 'NaN':
                if yc == 'Less than 1 year':
                    yearscodefloat.append(0.5)
                elif yc == 'More than 50 years':
                    yearscodefloat.append(51.0)
                else:
                    yearscodefloat.append(float(yc))  
        print('*************', i, '*************')       
        plt.title("Years of experience with coding per gender")
        plt.hist(yearscodefloat, bins=10, edgecolor='black')
        plt.show()

def in7(workweekhrs, devtype):
    devtype, d_dt = func_split(devtype)
    for i in d_dt.keys():
        l_s = []
        for wwh, dt in zip(workweekhrs, devtype):
            if isinstance(dt, list): 
                for item in dt:
                    if item == i and not mt.isnan(wwh) and item != 'NaN':
                        l_s.append(wwh)
            elif dt == i and not mt.isnan(wwh) and dt != 'NaN':
                l_s.append(wwh) 
        print('*************', i, '*************')  
        plt.title("Average number of working hours per week, per developer type")
        plt.hist(l_s, bins=10, edgecolor='black')
        plt.show()

def in8(age, gender):
    gender, d_g = func_split(gender)
    for i in d_g.keys():
        l_s = []
        for a, g in zip(age, gender):
            if isinstance(g, list): 
                for item in g:
                    if item == i and not mt.isnan(a):
                        l_s.append(a)
            elif g == i and not mt.isnan(a):
                l_s.append(a)
        print('*************', i, '*************')  
        plt.title("Age per gender")
        plt.hist(l_s, bins=10, edgecolor='black')
        plt.show()

def in9(languageworkedwith, age):
    languageworkedwith, d_lw = func_split(languageworkedwith)
    for i in d_lw.keys():
        l_s = []
        for a, lw in zip(age, languageworkedwith):
            if isinstance(lw, list): 
                for item in lw:
                    if item == i and not mt.isnan(a):
                        l_s.append(a)
            elif lw == i and not mt.isnan(a):
                l_s.append(a)
        d_lw[i] = l_s
        print('*************', i, '*************')
        if d_lw[i] == []:
            print('Dont exists registers')
        else:
            d_lw[i].sort()
            print('Mediana: ', func_mediana(d_lw[i]))
            print('Media: ', func_media(d_lw[i]))
            print('Desviacion Estandar: ', func_desviacionEstandar(d_lw[i], func_media(d_lw[i])))

def in10(yearscode, salary):
    num = 0
    r_1 = 0
    r_2 = 0
    yearscode, d_yc = func_split(yearscode)
    yearscodeNum = func_yearscodeToNum(yearscode)
    salaryNum = func_salaryToNum(salary)      
    m_yearscode = np.mean(yearscodeNum)
    m_salary = np.mean(salaryNum)
    for i in range(len(salaryNum)):
        num += (salaryNum[i] - m_salary)*(yearscodeNum[i] - m_yearscode)
        r_1 += (salaryNum[i] - m_salary)**2
        r_2 += (yearscodeNum[i] - m_yearscode)**2 
    p_c = num/mt.sqrt(r_1*r_2)
    print("Correlatin between years of experience and annual salary")
    print(p_c)
    
def in11(age,salary):
    num = 0
    r_1 = 0
    r_2 = 0   
    ageNum = func_ageToNum(age)
    salaryNum = func_salaryToNum(salary) 
    m_age = np.mean(ageNum)
    m_salary = np.mean(salaryNum)
    for i in range(len(salary)):
        num += (salaryNum[i] - m_salary)*(ageNum[i] - m_age)
        r_1 += (salaryNum[i] - m_salary)**2
        r_2 += (ageNum[i] - m_age)**2  
    p_c = num/mt.sqrt(r_1*r_2)
    print("Correlatin between the age and the annual salary")
    print(p_c)
    
def in12(edlevel, salary):
    num = 0
    r_1 = 0
    r_2 = 0 
    edlevel, d_el = func_split(edlevel)
    edlevelNum = func_edlevelToNum(edlevel)
    salaryNum = func_salaryToNum(salary) 
    m_edlevel = np.mean(edlevelNum) 
    m_salary = np.mean(salaryNum)
    for i in range(len(salaryNum)):
        num += (salaryNum[i] - m_salary)*(edlevelNum[i] - m_edlevel)
        r_1 += (salaryNum[i] - m_salary)**2
        r_2 += (edlevelNum[i] - m_edlevel)**2 
    p_c = num/mt.sqrt(r_1*r_2)
    print("Correlatin between years of experience and annual salary")
    print(p_c)
    
def in13(languageworkedwith):
    l_aux = []
    d_fpl = {}
    for i in languageworkedwith:
        if i is not np.nan:
            l_aux.append(i.split(';'))
    l_pl = [i for pl in l_aux for i in pl ]
    for i in l_pl:
        if not i in d_fpl:
            d_fpl[i] = 1  
        else:
            d_fpl[i] += 1  
    plt.title("Frequencies of the different programming languages.")
    plt.bar(range(len(d_fpl)), list(d_fpl.values()), edgecolor='black', align='center')
    plt.xticks(range(len(d_fpl)), list(d_fpl.keys()), rotation= 90)
    plt.show()
    
def main():
    salary = data['ConvertedComp'].tolist()
    gender = data['Gender'].tolist()
    ethnicity = data['Ethnicity'].tolist()
    devtype = data['DevType'].tolist()
    country = data['Country'].tolist()
    yearscode = data['YearsCode'].tolist()
    workweekhrs = data['WorkWeekHrs'].tolist()
    age = data['Age'].tolist()
    edlevel = data['EdLevel'].tolist()
    languageworkedwith = data['LanguageWorkedWith'].tolist()
    '''
    print('*************INCISO 1*********************')
    in1(salary, gender)
    
    print('\n\n*************INCISO 2*********************')
    in2(salary, ethnicity)
    
    print('\n\n*************INCISO 3*********************')
    in3(salary, devtype)
    
    print('\n\n*************INCISO 4*********************')
    in4(salary, country)
    
    print('\n\n*************INCISO 5*********************')
    in5(devtype)
    
    print('\n\n*************INCISO 6*********************')
    in6(yearscode, gender)
    
    print('\n\n*************INCISO 7*********************')
    in7(workweekhrs, devtype)
    
    print('\n\n*************INCISO 8*********************')
    in8(age, gender)
    
    print('\n\n*************INCISO 9*********************')
    in9(languageworkedwith, age)
    '''
    print('\n\n*************INCISO 10*********************')
    in10(yearscode, salary)
    
    print('\n\n*************INCISO 11*********************')
    in11(age, salary)
    
    print('\n\n*************INCISO 12*********************')
    in12(edlevel, salary)
    
    print('\n\n*************INCISO 13*********************')
    in13(languageworkedwith)
    
    
w_d = './'
i_f = w_d+'survey_results_public.csv'
data = pd.read_csv(i_f, encoding = 'utf-8')
main()









