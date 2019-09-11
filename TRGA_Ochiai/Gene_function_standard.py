#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pickle,numpy,xlrd,math,copy,basic_function_Barinel,random


def average(seq):
   return float(sum(seq)) / len(seq)

def initial_population(failed_test_cases):
    metric_tmp=numpy.eye(len(failed_test_cases), dtype=int)
    list_zero=[0 for _ in range(len(failed_test_cases))]
    metric=numpy.row_stack((metric_tmp,list_zero))
    return metric.tolist()

def get_mesure(population_list,failed_testcases,rank_ori,statement_matrix,meature_metric_ori,statements_number):

    fitness_value=[]
    for element in population_list:
        tmp_list = []
        if (element.count(1)==0):
            K_distance = 0
            fitness_value.append(K_distance)
        elif(element.count(0)==0):
            K_distance = float('-inf')
            fitness_value.append(K_distance)
        else:
            for tmp in range(0, len(element)):
                if (element[tmp] == 1):
                    tmp_list.append(failed_testcases[tmp])
            mesure = basic_function_Barinel.generate_mesure_conversion_all(statement_matrix, meature_metric_ori, tmp_list, statements_number)
            rank = basic_function_Barinel.generate_rank(mesure, statements_number)
            K_distance = basic_function_Barinel.Revised_kendall_tau_distance_yxb_D(rank, rank_ori, statements_number)
            fitness_value.append(K_distance)
    return fitness_value


def Normalization_function(fitness_value):
    if (fitness_value<-600):
        return (1 / (1 + math.exp(-600)))
    else:
        return (1/(1+math.exp(-fitness_value)))

#fitness_value:a collection of each individual fitness score
def selection_lunpandu(population,fitness_value_ori):
    fitness_value=[]
    for tmp in fitness_value_ori:
        new_fitness_value=Normalization_function(tmp)
        fitness_value.append(new_fitness_value)
    fitness_sum = [] #The probability of roulette for each individual in the sample, as a percentage of the total
    choosing_number=int(len(population))
    for i in range(len(fitness_value)):
        if i==0:
            fitness_sum.append(fitness_value[i])
        else:
            fitness_sum.append(fitness_sum[i - 1] + fitness_value[i])
    if sum(fitness_value)==0:
        return population
    for i in range(len(fitness_sum)):
        fitness_sum[i]/=sum(fitness_value)

    #Selection
    population_new = []
    fitness_new=[]
    for i in range(choosing_number):
        rand = numpy.random.uniform(0, 1)
        for j in range(len(fitness_value)):
            if j == 0:
                if 0 < rand and rand <= fitness_sum[j]:
                    population_new.append(population[j])
                    fitness_new.append(fitness_value[j])

            else:
                if fitness_sum[j - 1] < rand and rand <= fitness_sum[j]:
                    population_new.append(population[j])
                    fitness_new.append(fitness_value[j])
    return population_new,fitness_new

"""
crossover
"""
def crossover(population_new, pcmax,pcmin,fitness_new):
    half=int(len(population_new)/2)
    father=population_new[:half]
    mother=population_new[half:]
    numpy.random.shuffle(father)
    numpy.random.shuffle(mother)
    offspring=[]
    favg=average(fitness_new)
    fmax=max(fitness_new)
    for i in range(half):
        fitness=max(fitness_new[population_new.index(father[i])],fitness_new[population_new.index(mother[i])])
        pc=updatePc(pcmax,pcmin,favg,fitness,fmax)
        if numpy.random.uniform(0,1)<=pc:
            #copint = numpy.random.randint(0,int(len(father[i])/2))
            copint = numpy.random.randint(0, len(father[i]))
            son=father[i][:copint]+(mother[i][copint:])
            daughter=mother[i][:copint]+(father[i][copint:])
        else:
            son=father[i]
            daughter=mother[i]
        offspring.append(son)
        offspring.append(daughter)
    return offspring


"""
mutation
"""
def mutation(offspring,pmmax,pmmin,failed_testcases,rank_ori,statement_matrix,meature_metric_ori,statements_number):
    offspring_tmp=copy.deepcopy(offspring)

    for i in range(len(offspring_tmp)):
        pm=1
        if numpy.random.uniform(0,1)<=pm:
            position = numpy.random.randint(0, len(offspring_tmp[i]))
            if offspring_tmp[i][position]==1:
                offspring_tmp[i][position]=0
            else:
                offspring_tmp[i][position] = 1

    return offspring_tmp

"""
Generating new population
"""
def refresh(fitness_value_old,old_population,new_population,failed_testcases,rank_ori,statement_matrix,meature_metric_ori,statements_number):

    fitness_value_new=get_mesure(new_population,failed_testcases,rank_ori,statement_matrix,meature_metric_ori,statements_number)
    fit_all_set=[]
    result_population=[]
    score_new_population=[]
    for tmp in range(len(fitness_value_old)):
        fit_all_set.append([fitness_value_old[tmp],old_population[tmp]])
    for tmp in range(len(fitness_value_new)):
        fit_all_set.append([fitness_value_new[tmp],new_population[tmp]])
    fit_all_set = sorted(fit_all_set, key=lambda x: (-x[0], x[1].count(1)))
    for tmp in range(0,min(30,len(fitness_value_old))):
        result_population.append(fit_all_set[tmp][1])
        score_new_population.append(fit_all_set[tmp][0])
    return result_population,score_new_population

def updatePc(Pcmax,Pcmin,favg,f,fmax):
    if (f>=favg):
        if(fmax-favg==0):
            Pc=Pcmin
        else:
            Pc = Pcmin + ((Pcmax - Pcmin) * (fmax - f) / (fmax - favg))

    else:
        Pc=Pcmax
    return Pc

def updatePm(Pmmax,Pmmin,favg,f,fmax):
    if (f>=favg):
        if (fmax - favg == 0):
            Pm = Pmmin
        else:
            Pm = Pmmin + ((Pmmax - Pmmin) * (fmax - f) / (fmax - favg))
    else:
        Pm=Pmmax
    return Pm

