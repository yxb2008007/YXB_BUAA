#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pickle,numpy,xlrd,math,copy,time
import xlrd,xlwt,basic_function_Ochiai,random,Gene_function_standard


#pc:交叉概率
#pm:变异概率
Pcmax=1
Pcmin=0.1
Pmmax=1
Pmmin=1


def get_matrix_result(matrix_path):
    result = []
    matrix = []
    f = open(matrix_path)
    for data in f.readlines():

        data = data.strip('\n')
        nums = data.split(" ")

        if nums[len(nums) - 1] == '+':
            result.append(0)
        elif nums[len(nums) - 1] == '-':
            result.append(1)
        else:
            exit()
        del nums[len(nums) - 1]
        nums = [int(x) for x in nums]
        matrix.append(nums)
    matrix=numpy.array(matrix)
    return matrix, result


version_list=range(12,39)
version_list.remove(18)
version_list.remove(19)
version_list.remove(20)
version_list.remove(21)
version_list.remove(26)

for version in version_list:
    print "version "+str(version)

    matrix_path="The matrix file path of corresponding faulty version"
    spectrum_path="The spectra file path of corresponding faulty version"
    faulty_statements_list=get_faultystatements_mokito("mockito",version,spectrum_path) #This function "get_faultystatements_mokito" returns the exact position of faulty statements in the spectra file
    matrix_sample, execution_result_sample = get_matrix_result(matrix_path)
    num_testcases=len(execution_result_sample)
    num_statements=matrix_sample.shape[1]
    list_success=[]
    list_fail=[]
    for tmp in range(0, len(execution_result_sample)):
        if execution_result_sample[tmp] == 0:
            list_success.append(tmp + 1)
        elif execution_result_sample[tmp] == 1:
            list_fail.append(tmp + 1)
        else:
            print("error")

    measure_ori = basic_function_Ochiai.generate_initial_measure(matrix_sample, execution_result_sample,num_testcases, num_statements)
    rank_ori = basic_function_Ochiai.generate_rank(measure_ori, num_statements)
    expense_ori = basic_function_Ochiai.get_expense_score(faulty_statements_list, rank_ori)

    if(len(list_fail)==1):
        continue
    else:
        ########################################################################
        #TRGA Starts
        ########################################################################
        start_TRGA = time.clock()
        list_set = []
        ########################################################################
        #Stage 1
        ########################################################################
        Initial_population = Gene_function_standard.initial_population(list_fail)  # Initialize
        fitness_value = Gene_function_standard.get_mesure(Initial_population, list_fail, rank_ori, matrix_sample,
                                                          measure_ori, num_statements)
        population_new, fitness_value_new = Gene_function_standard.selection_lunpandu(Initial_population,
                                                                                      fitness_value)  # Selection
        offspring = Gene_function_standard.crossover(population_new, Pcmax, Pcmin, fitness_value_new)
        offspring_aftermutation = Gene_function_standard.mutation(offspring, Pmmax, Pmmin, list_fail, rank_ori,
                                                                  matrix_sample, measure_ori, num_statements)
        population_nextgeneration, fitness_next_generation = Gene_function_standard.refresh(fitness_value,
                                                                                            Initial_population,
                                                                                            offspring_aftermutation,
                                                                                            list_fail, rank_ori,
                                                                                            matrix_sample,
                                                                                            measure_ori, num_statements)

        k = 1
        zuiyoujie = population_nextgeneration[0]
        iterations = 1

        while ((k <= 50) and (iterations <= 200)):
            population_new_loop, fitness_value_new_loop = Gene_function_standard.selection_lunpandu(
                population_nextgeneration, fitness_next_generation)  # Selection
            offspring = Gene_function_standard.crossover(population_new_loop, Pcmax, Pcmin, fitness_value_new_loop)
            offspring_aftermutation = Gene_function_standard.mutation(offspring, Pmmax, Pmmin, list_fail, rank_ori,
                                                                      matrix_sample, measure_ori, num_statements)
            population_nextgeneration, fitness_next_generation = Gene_function_standard.refresh(
                fitness_next_generation, population_nextgeneration, offspring_aftermutation, list_fail, rank_ori,
                matrix_sample, measure_ori, num_statements)
            if zuiyoujie == population_nextgeneration[0]:
                k = k + 1
            else:
                zuiyoujie = population_nextgeneration[0]
                k = 1
            print iterations
            iterations = iterations + 1
        ########################################################################
        # Stage 2
        ########################################################################
        for tmp in range(len(population_nextgeneration[0])):
            if population_nextgeneration[0][tmp] == 1:
                list_set.append(list_fail[tmp])
        measure_conversion = basic_function_Ochiai.generate_mesure_conversion_all(matrix_sample, measure_ori,
                                                                                   list_set, num_statements)
        rank_conversion = basic_function_Ochiai.generate_rank(measure_conversion, num_statements)
        expense_conversion = basic_function_Ochiai.get_expense_score(faulty_statements_list, rank_conversion)
        #expense_conversion: the expense score of the most localizable fault after TRGA






















