#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:53:34 2018

@author: madhurendratripathy
"""
#Truth_Tables


def evaluate(final_list,slicedexp,dct):
    new_list=[]
    p1=slicedexp[0]#proposition 1
    p2=slicedexp[2]#proposition 2
    op=slicedexp[1]#operation between p1, p2
    location1,location2=-1,-1#location of propositions in the dictionry
    count=0
    for i in range(len(dct)):
        if(count==2):
            break
        if(dct[i]==p1):
            location1=i
            count+=1
        elif(dct[i]==p2):
            location2=i
            count+=1
    print("len(final_list)=",len(final_list))
    if(op=='^'):
        for i in range(len(final_list[0])):
            new_list.append(final_list[location1][i] and final_list[location2][i])
        return new_list
    if(op==':'):
        for i in range(len(final_list[0])):
            new_list.append(final_list[location1][i] or final_list[location2][i])
        return new_list
    if(op=='>'):
        for i in range(len(final_list[0])):
            if(final_list[location1][i]==True and final_list[location2][i]==False):
                new_list.append(False)
            else:
                new_list.append(True)
        return new_list
    if(op=='='):
        for i in range(len(final_list[0])):
            if(final_list[location1][i]==final_list[location2][i]):
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
            
    
        

def partition(exp,substitution_list,l,final_list,dct):
    sol=[]
    #print(final_list)
    for ele in exp:
        if(((ele>='a' and ele<='z')or(ele>='A' and ele<='Z')) and (ele not in l)):
            l.append(ele)
    for i in range(len(l)):
        dct[i]=l[i]
        #print(dct)
    slicedexp=""
    exp1=""
    #print("exp recieved in partion:- ",exp)
    i=-1
    if(len(exp)!=1):
        while((exp[i]==')' or 'a'<=exp[i]<='z' or 'A'<=exp[i]<='Z' or exp[i]=='^' or exp[i]==':' or exp[i]=='=' or exp[i]=='>' or exp[i]=='~') and exp[i-4]!='('):
            if((exp[i]==')' and exp[i-4]=='(')):
                break
            i=i-1
        
        #print("i=",i)  
        slicedexp=(exp[i-3]+exp[i-2]+exp[i-1])
        #print("sliced exp=",slicedexp)
        l.append(slicedexp)
        sol=evaluate(final_list,slicedexp,dct)
        final_list.append(sol)
        minimized_exp=list(exp)
        #print(minimized_exp)
        for j in range(5):
            minimized_exp.pop(i)
        #print("minimized_exp=",minimized_exp)
        minimized_exp.insert((i+1),substitution_list[0])
        substitution_list.remove(substitution_list[0])
        #print(final_list)
        for ele in minimized_exp:
            exp1=exp1+ele
        #print("newly obtained exp=",exp1)
        if(len(exp1)!=0):
            partition(exp1,substitution_list,l,final_list,dct)
    else:
        for i in range(len(final_list)):
            print(l[i]," :-",final_list[i],"\n")
        #print("Expressions are:- ",l)
        #print("Solns Are:- ",final_list)

            
            
def generator(exp):#generates truth values for each proposition
    l=[]#list of propositions given
    l2=[]
    for ele in exp:
        if(((ele>='a' and ele<='z')or(ele>='A' and ele<='Z')) and (ele not in l)):
            l.append(ele)
        
    #print("Number of Propositions entered=",len(l))
    length=2**len(l)
    #print("length=",length)
    divider=1
    while(len(l2)!=len(l)):
        divider=divider*2
        count=0
        l1=[]
        #l3=[]
        while(count!=length):
            #print("count=",count)
            #print("divider=",divider)
            for i in range(length//divider):
                #print("appending",i+1,"True")
                l1.append(True)
                count=count+1
                #print("count=",count)
                #print("l1=",l1)
            for i in range(length//divider):
                #print("appending",i+1,"False")
                l1.append(False)
                count=count+1
                #print("count=",count)
                #print('l1=',l1)
            if(count==length):
                #print("appending l1 in l2")
                l2.append(l1)
    
    return l2
                
    
def scan():#read the input and verify if it is correct
    openbr=0
    closebr=0
    propositions=0
    connectives=0
    dct={}
    l=[]
    substitution_list=['!','@','#','$','%','&','*','-','_','+','|']
    print("\n\nUse The Following Special Chrecters Only, use proper brackets '(' and ')':-\n1)'^' for 'AND' operation\n2)':' for 'OR' operation\n3)'>' for 'IMPLICATION'\n4)'=' for 'BI-CONDITIONAL'")
    exp=input("Enter the Expression:- ")#reading the expression to be evaluated
    
    
    for i in range(len(exp)):
        #print("exp[i]=",exp[i])
        if((exp[i]>='a' and exp[i]<='z') or (exp[i]>='A' and exp[i]<='Z') or(exp[i]=='(')or(exp[i]=='~')or(exp[i]==')')or(exp[i]=='^')or(exp[i]=='>')or(exp[i]=='=')or(exp[i]==':')):
            if((exp[i]>='a' and exp[i]<='z') or (exp[i]>='A' and exp[i]<='Z')):
                propositions=propositions+1
            if((exp[i]=='~')or(exp[i]=='^')or(exp[i]=='>')or(exp[i]=='=')or(exp[i]==':')):
                connectives=connectives+1
            if(exp[i]=='('):
                openbr=openbr+1
            if(exp[i]==')'):
                closebr=closebr+1
            if(len(exp)<5):
                valid=False
    if(closebr==openbr and closebr>0 and openbr>0 and (propositions-1==connectives)):#checking for correctness in braces and the number of terms entered
        valid=True
    else:
        valid=False
    if(valid==True):
        final_list=generator(exp)
        for ele in exp:
            if(((ele>='a' and ele<='z')or(ele>='A' and ele<='Z')) and (ele not in l)):
                l.append(ele)

        partition(exp,substitution_list,l,final_list,dct)
    else:
        print("Inappropriate Expression Entered!! Try Again")
        scan()

scan()
