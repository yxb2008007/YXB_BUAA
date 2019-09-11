#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pickle,numpy,xlrd,math,copy


def jaccard(p,q):
    c = []
    for i in p:
        if i in q:
            c.append(i)
    return float(len(c))/(len(p)+len(q)-len(c))

def generate_initial_measure(statement_matrix,result_list,testcases_number,statements_number):
    suspect_tarantula=[]
    for i in range(1, statements_number + 1):
        a00 = 0
        a01 = 0
        a10 = 0
        a11 = 0
        for j in range(1, testcases_number + 1):
            if ((statement_matrix[j - 1, i - 1] == 0) and (result_list[j - 1] == 0)):
                a00 = a00 + 1
            if ((statement_matrix[j - 1, i - 1] == 1) and (result_list[j - 1] == 1)):
                a11 = a11 + 1
            if ((statement_matrix[j - 1, i - 1] == 1) and (result_list[j - 1] == 0)):
                a10 = a10 + 1
            if ((statement_matrix[j - 1, i - 1] == 0) and (result_list[j - 1] == 1)):
                a01 = a01 + 1
        suspect_tarantula.append([a00,a01,a10,a11])
    return suspect_tarantula

def generate_rank(meature_metric,statements_number):
    suspicious_score=[]
    suspicious_rank=[]
    #print meature_metric
    for i in range(1, statements_number + 1):
        if (meature_metric[i-1][2]+meature_metric[i-1][1]==0)and(meature_metric[i-1][3]==0):
            suspect_tarantula=0
        elif (meature_metric[i-1][2]+meature_metric[i-1][1]==0)and(meature_metric[i-1][3] !=0):
            suspect_tarantula = float('inf')
        else:
            suspect_tarantula = (meature_metric[i-1][3] * meature_metric[i-1][3]) / (meature_metric[i-1][2]+meature_metric[i-1][1])
        suspicious_score.append([suspect_tarantula,i])
    t_Tarantula = sorted(suspicious_score, key=lambda x: (-x[0], x[1]))
    for statement in range(1, statements_number + 1):
        position = 0
        for l in t_Tarantula:
            if suspicious_score[statement - 1][0] == l[0]:
                position = t_Tarantula.index(l)
                break
        suspicious_rank.append(position + 1)
    return suspicious_rank

def generate_mesure_conversion_all(statement_matrix,meature_metric_ori,failed_testcase_conversion_set,statements_number):
    metric=copy.deepcopy(meature_metric_ori)
    #failed_testcase_conversion_set从1开始计数
    if (len(failed_testcase_conversion_set)==0):
        return metric
    else:
        for i in range(1, statements_number + 1):
            for j in failed_testcase_conversion_set:
                if (statement_matrix[j - 1][i - 1] == 0):
                    metric[i - 1][1] = metric[i - 1][1] - 1
                    metric[i - 1][0] = metric[i - 1][0] + 1
                elif (statement_matrix[j - 1][i - 1] == 1):
                    metric[i - 1][3] = metric[i - 1][3] - 1
                    metric[i - 1][2] = metric[i - 1][2] + 1
        return metric


def get_expense_score(list_faulty_statement,rank_metric):
    #faulty_statement从1开始计数
    rank=[]
    for tmp in list_faulty_statement:
        rank.append(rank_metric[tmp-1])
    rank_target=min(rank)
    best_score=1-(rank_target/len(rank_metric))
    worst_score=1-((rank_target+rank_metric.count(rank_target)-1)/len(rank_metric))
    return [best_score,worst_score]




def Revised_kendall_tau_distance(rank1,rank2,statements_number):
    K_distance=0
    for i in range(0,statements_number-1):
        for j in range(i+1,statements_number):
            measure=(rank1[i]-rank1[j])*(rank2[i]-rank2[j])
            if (measure<0):
                K_distance_tmp=(1/rank1[i])+(1/rank1[j])+(1/rank2[i])+(1/rank2[j])
            else:
                K_distance_tmp=0
            K_distance=K_distance+K_distance_tmp
    return K_distance




def combination(m,n):
    result=1
    if (n>m):
        print "error"

    else:
        for tmp in range(m-n+1,m+1):
            result=result*tmp
    return result/2


def Revised_kendall_tau_distance_yxb_D(rank1,rank2,statements_number):
    K_distance=0
    for i in range(0,statements_number-1):
        K_distance_tmp=(rank1[i]-rank2[i])*(abs(((1/pow(rank1[i],2))-(1/pow(rank2[i],2)))))
        K_distance=K_distance+K_distance_tmp
    return K_distance