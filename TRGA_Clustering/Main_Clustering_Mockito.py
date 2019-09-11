#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import pickle,numpy,xlrd,math,copy,Mseer_function,xlwt,J2_function,random,sys,TRGA_function,time

sys.setrecursionlimit(1000000)
def average(a):
    return (sum(a)/len(a))


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
    ####################
    # 获取特定版本的用例集执行结果
    matrix_path="The matrix file path of corresponding faulty version"
    spectrum_path="The spectra file path of corresponding faulty version"
    faulty_statements_list=get_faultystatements_mokito("mockito",version,spectrum_path) #This function "get_faultystatements_mokito" returns the exact position of faulty statements in the spectra file
    matrix_sample, execution_result_sample = get_matrix_result(matrix_path)
    num_testcases = len(execution_result_sample)
    num_statements = matrix_sample.shape[1]
    success_matrix, success_result_list = TRGA_function.matrix_result_list_conversion_get_success(matrix_sample,
                                                                                                  execution_result_sample)
    ####################################################
    #################################################
    ##########Mseer##################################
    # 对失效用例集进行Mseer聚类，返回聚类结果：[[failed_testcases for cluster1],[failed_testcases for cluster2]...](failed test case从0开始计数)
    a_Mseer = Mseer_function.Mseer(matrix_sample, execution_result_sample, num_testcases, num_statements)
    # print a_Mseer
    print "Mseer clustering done!"
    # 对Mseer聚类结果进行定位效率计算，计算expense score
    b_Mseer = Mseer_function.get_the_great_expense_score(a_Mseer, matrix_sample, execution_result_sample, num_statements,
                                                         faulty_statements_list)
    print "Mseer done!"

    ####################################################
    ##################Mseer_TRGA################################
    TRGA_result_best_list = []
    TRGA_result_worst_list = []
    TRGA_Clustering_result = []
    for testsuite in a_Mseer:
        tmp_TRGA = []
        matrix_tmp, result_list_tmp = TRGA_function.matrix_result_list_conversion_generate_sub(matrix_sample,
                                                                                               success_matrix,
                                                                                               success_result_list,
                                                                                               testsuite)
        TRGA_result, Specific_Vector = TRGA_function.TRGA(matrix_tmp, result_list_tmp, faulty_statements_list,
                                                          len(result_list_tmp),
                                                          num_statements)
        TRGA_result_best_list.append(TRGA_result[0])
        TRGA_result_worst_list.append(TRGA_result[1])
        for tmp in range(0, len(Specific_Vector)):
            if (Specific_Vector[tmp] == 1):
                tmp_TRGA.append(testsuite[tmp])
        TRGA_Clustering_result.append(tmp_TRGA)

    print "TRGA TRGA done!"

    ####################################################
    ##################J2################################
    a_J2 = J2_function.getstatement_rank(matrix_sample, execution_result_sample, num_testcases, num_statements)
    cluster_result = J2_function.cluster_result(a_J2, 0.7)
    b_J2 = Mseer_function.get_the_great_expense_score(cluster_result, matrix_sample, execution_result_sample, num_statements,
                                                      faulty_statements_list)

    print "J2 done!"
    ####################################################
    ##################J2_TRGA################################
    TRGA_result_best_list_J = []
    TRGA_result_worst_list_J = []
    TRGA_Clustering_result_J = []
    for testsuite_J in cluster_result:
        tmp_TRGA_J = []
        matrix_tmp_J, result_list_tmp_J = TRGA_function.matrix_result_list_conversion_generate_sub(matrix_sample,
                                                                                                   success_matrix,
                                                                                                   success_result_list,
                                                                                                   testsuite_J)
        TRGA_result_J, Specific_Vector_J = TRGA_function.TRGA(matrix_tmp_J, result_list_tmp_J, faulty_statements_list,
                                                              len(result_list_tmp_J), num_statements)
        TRGA_result_best_list_J.append(TRGA_result_J[0])
        TRGA_result_worst_list_J.append(TRGA_result_J[1])
        for tmp in range(0, len(Specific_Vector_J)):
            if (Specific_Vector_J[tmp] == 1):
                tmp_TRGA_J.append(testsuite_J[tmp])
        TRGA_Clustering_result_J.append(tmp_TRGA_J)






