#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pickle,numpy,xlrd,math,copy,random


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
            mesure = generate_mesure_conversion_all(statement_matrix, meature_metric_ori, tmp_list, statements_number)
            rank = generate_rank(mesure, statements_number)

            K_distance = Revised_kendall_tau_distance_yxb_D(rank, rank_ori, statements_number)
            fitness_value.append(K_distance)
    return fitness_value


def Normalization_function(fitness_value):
    if (fitness_value<-600):
        return (1 / (1 + math.exp(-600)))
    else:
        return (1/(1+math.exp(-fitness_value)))


def selection_lunpandu(population,fitness_value_ori):
    fitness_value=[]
    for tmp in fitness_value_ori:
        new_fitness_value=Normalization_function(tmp)
        fitness_value.append(new_fitness_value)
    fitness_sum = []
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


def selection_Tournament(population,fitness_value):
    choosing_number = int(len(population))
    population_new=[]
    for tmp in range(0,choosing_number):
        sample=random.sample(population,2)
        if(fitness_value[population.index(sample[0])]>fitness_value[population.index(sample[1])]):
            population_new.append(sample[0])
        else:
            population_new.append(sample[1])
    return population_new

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

def Revised_kendall_tau_distance_yxb_D(rank1,rank2,statements_number):
    K_distance=0
    for i in range(0,statements_number-1):
        K_distance_tmp=(rank1[i]-rank2[i])*(abs(((1/pow(rank1[i],2))-(1/pow(rank2[i],2)))))
        K_distance=K_distance+K_distance_tmp
    return K_distance

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

def generate_rank(meature_metric,statements_number):
    suspicious_score=[]
    suspicious_rank=[]
    #print meature_metric
    for i in range(1, statements_number + 1):
        if (meature_metric[i-1][3]==0):
            suspect_tarantula = 0
        else:
            suspect_tarantula = (meature_metric[i-1][3] / (meature_metric[i-1][3] + meature_metric[i-1][1])) / ((meature_metric[i-1][3] / (meature_metric[i-1][3] + meature_metric[i-1][1])) + (meature_metric[i-1][2] / (meature_metric[i-1][2] + meature_metric[i-1][0])))

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

def get_expense_score(list_faulty_statement,rank_metric):
    #faulty_statement从1开始计数
    rank=[]
    for tmp in list_faulty_statement:
        rank.append(rank_metric[tmp-1])
    rank_target=min(rank)
    best_score=1-(rank_target/len(rank_metric))
    worst_score=1-((rank_target+rank_metric.count(rank_target)-1)/len(rank_metric))
    return [best_score,worst_score]

def TRGA(matrix_ori,result_list_ori,list_faulty_statements,testcases_number,statements_number):
    list_success = []
    list_fail = []
    for tmp in range(0, len(result_list_ori)):
        if result_list_ori[tmp] == 0:
            list_success.append(tmp + 1)
        elif result_list_ori[tmp] == 1:
            list_fail.append(tmp + 1)  # list_fail此段代码中从1开始计数
        else:
            print("error")
    #print len(list_success)
    #print len(list_fail)
    measure_ori = generate_initial_measure(matrix_ori, result_list_ori, testcases_number, statements_number)
    rank_ori = generate_rank(measure_ori, statements_number)
    Flag = 0
    rank1_list = []
    rank_tmp = copy.deepcopy(rank_ori)
    for tmp in range(0, rank_ori.count(1)):
        rank1_list.append(rank_tmp.index(1) + 1)
        rank_tmp[rank_tmp.index(1)] = -1
    # print rank1_list
    for tmp in rank1_list:
        # print measure_ori[tmp-1]
        if ((measure_ori[tmp - 1][2] == 0) and (measure_ori[tmp - 1][3] - measure_ori[tmp - 1][1] > 0)):
            Flag = 1
            break
    if (len(list_fail) == 0) or (Flag == 1):
        expense_ori = get_expense_score(list_faulty_statements, rank_ori)
        origin_population=[0 for _ in range(len(list_fail))]
        return expense_ori,origin_population
    else:
        list_set = []
        Initial_population = initial_population(list_fail)  # 初始化种群矩阵
        fitness_value = get_mesure(Initial_population, list_fail, rank_ori, matrix_ori,measure_ori, statements_number)
        population_new, fitness_value_new = selection_lunpandu(Initial_population,fitness_value)  # 选择算子
        offspring = crossover(population_new, 1, 0.1, fitness_value_new)
        offspring_aftermutation = mutation(offspring, 1, 1, list_fail, rank_ori,matrix_ori, measure_ori, statements_number)
        population_nextgeneration, fitness_next_generation = refresh(fitness_value,Initial_population,offspring_aftermutation,list_fail, rank_ori,matrix_ori, measure_ori,statements_number)
        xunhuancishu = 1
        zuiyoujie = population_nextgeneration[0]
        iterations = 1

        while ((xunhuancishu <= 50) and (iterations <= 200)):
            population_new_loop, fitness_value_new_loop = selection_lunpandu(population_nextgeneration, fitness_next_generation)  # 选择算子
            offspring = crossover(population_new_loop, 1, 0.1, fitness_value_new_loop)
            offspring_aftermutation = mutation(offspring, 1, 1, list_fail, rank_ori,matrix_ori, measure_ori, statements_number)
            population_nextgeneration, fitness_next_generation = refresh(fitness_next_generation,population_nextgeneration,offspring_aftermutation,list_fail,rank_ori,matrix_ori,measure_ori,statements_number)
            if zuiyoujie == population_nextgeneration[0]:
                xunhuancishu = xunhuancishu + 1
            else:
                zuiyoujie = population_nextgeneration[0]
                xunhuancishu = 1
            #print iterations
            iterations = iterations + 1
        for tmp in range(len(population_nextgeneration[0])):
            if population_nextgeneration[0][tmp] == 1:
                list_set.append(list_fail[tmp])
        measure_conversion = generate_mesure_conversion_all(matrix_ori,measure_ori,list_set, statements_number)
        rank_conversion = generate_rank(measure_conversion, statements_number)
        expense_conversion = get_expense_score(list_faulty_statements,rank_conversion)
        return expense_conversion,population_nextgeneration[0]

def matrix_result_list_conversion_get_success(matrix_ori,result_list_ori):
    list_success = []
    list_fail = []
    success_result_list=[]
    for tmp in range(0, len(result_list_ori)):
        if result_list_ori[tmp] == 0:
            list_success.append(tmp)
        elif result_list_ori[tmp] == 1:
            list_fail.append(tmp)
        else:
            print("error")
    success_matrix = copy.deepcopy(matrix_ori[list_success, :])
    for tmp in range(0,len(list_success)):
        success_result_list.append(0)
    return success_matrix,success_result_list

def matrix_result_list_conversion_generate_sub(matrix_ori,success_matrix,success_result_list,list_fail_sub):
    fail_matrix=copy.deepcopy(matrix_ori[list_fail_sub, :])
    sub_matrix=numpy.row_stack((success_matrix,fail_matrix))
    sub_result_list=copy.deepcopy(success_result_list)
    for tmp in range(0,len(list_fail_sub)):
        sub_result_list.append(1)
    return sub_matrix,sub_result_list
