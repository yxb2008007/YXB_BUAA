from __future__ import division
import pickle,numpy,xlrd,math,copy

def getrank_seq_Dstar(statement_matrix,result_list,testcases_number,statements_number):
    list_success=[]
    list_fail=[]
    rank_result=[]
    suspicious_success=[]
    for tmp in range(0,len(result_list)):
        if result_list[tmp]==0:
            list_success.append(tmp)
        elif result_list[tmp]==1:
            list_fail.append(tmp)
        else:
            print("error")
    success_matrix=copy.deepcopy(statement_matrix[list_success,:])
    for i in range(1,statements_number+1):
        a00_success = 0
        a10_success = 0
        for j in range(1, len(list_success) + 1):
            if (success_matrix[j - 1, i - 1] == 0):
                a00_success = a00_success + 1
            if (success_matrix[j - 1, i - 1] == 1):
                a10_success = a10_success + 1
        suspicious_success.append([a00_success,0,a10_success,0])
        #a00,a11,a10,a01
    for tmp in list_fail:
        suspicious_score=[]
        suspicious_rank=[]
        for i in range(1,statements_number+1):
            suspicious=copy.deepcopy(suspicious_success[i-1])
            a01=0
            a11=0
            if((statement_matrix[tmp][i-1])==0):
                a01=1
            elif ((statement_matrix[tmp][i - 1]) == 1):
                a11=1
            else:
                print("error")
            suspicious[1]=a11
            suspicious[3]=a01
            if(suspicious[1]==0):
                sus_scorefor_that_statement=0
            else:
                sus_scorefor_that_statement=(suspicious[1]/(suspicious[1]+suspicious[3]))/((suspicious[1]/(suspicious[1]+suspicious[3]))+(suspicious[2]/(suspicious[2]+suspicious[0])))

            suspicious_score.append([sus_scorefor_that_statement,i])
        t_Dstar = sorted(suspicious_score, key=lambda x: (-x[0], x[1]))
        for statement in range(1,statements_number+1):
            position=0
            for l in t_Dstar:
                if suspicious_score[statement-1][0]==l[0]:
                    position = t_Dstar.index(l)
                    break
            suspicious_rank.append(position + 1)
        #print tmp,suspicious_rank
        rank_result.append([tmp,suspicious_rank])
    return rank_result


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

#half of the 5% winsorized_score
def winsorized_score(list_distance_input):
    list_distance=copy.deepcopy(list_distance_input)
    list_distance.sort()
    bound=int(0.05*len(list_distance))
    for i in range(0,bound):
        list_distance[i]=list_distance[bound]
        list_distance[len(list_distance)-i-1]=list_distance[bound]
    return (0.5*(sum(list_distance)/len(list_distance)))

def update_potential_value(potential_value_ori,M,R,parameter,rank_set,statements_number):
    for tmp in range(0,len(potential_value_ori)):
        potential_value_ori[tmp]=potential_value_ori[tmp]-M*(math.exp((-(4/numpy.square(1.5*parameter)))*numpy.square(Revised_kendall_tau_distance(rank_set[tmp],rank_set[R],statements_number))))


def choosing_initial_medoid(rank_set,statements_number):
    cluster_number=0
    initial_medoid=[]
    distance_set=[]
    potential_value=[]
    if len(rank_set) == 1:
        cluster_number=1
    else:
        for i in range(0, len(rank_set) - 1):
            for j in range(i + 1, len(rank_set)):
                tmp = Revised_kendall_tau_distance(rank_set[i], rank_set[j], statements_number)
                # print 1
                distance_set.append(tmp)
            # print distance_set
            # print 1
        parameter_main = winsorized_score(distance_set)  # compute the parameter tau
        if parameter_main == 0:
            cluster_number = len(rank_set)
            initial_medoid = range(len(rank_set))
        else:
            alpha = 4 / (parameter_main * parameter_main)  # compute the parameter alpha
            for i in range(1, len(rank_set) + 1):
                potential_value_tmp = 0
                for j in range(1, len(rank_set) + 1):
                    if i == j:
                        l_tmp = 0
                    else:
                        location_tmp = [i, j]
                        location_tmp.sort()
                        location = location_tmp[1] - location_tmp[0] - 1 + (location_tmp[0] - 1) * (
                                2 * len(rank_set) - location_tmp[0]) / 2
                        l_tmp = distance_set[int(location)]
                    potential_value_tmp = potential_value_tmp + math.exp((-alpha) * (l_tmp * l_tmp))
                potential_value.append(potential_value_tmp)  # the initial value for each ranking
                # print 2
            M_initial = max(potential_value)
            R_initial = potential_value.index(M_initial)
            initial_medoid.append(R_initial)
            cluster_number = cluster_number + 1
            M = M_initial
            R = R_initial
            # potential_value_else = copy.deepcopy(potential_value)
            potential_value.sort()
            while True:
                update_potential_value(potential_value, M, R, parameter_main, rank_set, statements_number)
                M = max(potential_value)
                R = potential_value.index(M)
                if M > (0.5 * M_initial):
                    initial_medoid.append(R)
                    cluster_number = cluster_number + 1
                    continue
                elif M < (0.15 * M_initial):
                    break
                else:

                    D_min_list = []
                    for i in range(0, len(initial_medoid)):
                        D_min_list.append(
                            Revised_kendall_tau_distance(rank_set[initial_medoid[i]], rank_set[R], statements_number))
                    D_min = min(D_min_list)
                    if ((D_min / parameter_main) + (M / M_initial) >= 1):
                        initial_medoid.append(R)
                        cluster_number = cluster_number + 1
                        continue
                    else:
                        potential_value.remove(M)
                        M = max(potential_value)
                        R = potential_value.index(M)
                        continue

    result=[cluster_number,initial_medoid]
    return result



def cluster_process(rank_set,initial_medoid,cluster_number,statements_number):
    if cluster_number!=len(initial_medoid):
        print("error")
    else:
        distance = [[] for i in range(cluster_number)]
        for j in range(0,len(initial_medoid)):
            for i in range(0,len(rank_set)):
               distance[j].append(Revised_kendall_tau_distance(rank_set[initial_medoid[j]],rank_set[i],statements_number))

        distance_matrix=numpy.array(distance)
        #print distance_matrix

        cluster_result=distance_matrix.argmin(axis=0)
        #print cluster_result
        return cluster_result

def Mseer(statement_matrix,result_list,testcases_number,statements_number):
    rank_set=[]
    rank_set_list=getrank_seq_Dstar(statement_matrix, result_list, testcases_number, statements_number)
    #print rank_set_list
    #print "get rank complete"

    for i in rank_set_list:
        rank_set.append(i[1])
    initial_medoid=choosing_initial_medoid(rank_set, statements_number)
    if initial_medoid[0]==len(rank_set):
        cluster_failedtestcases=[]
        cluster_failedtestcases_tmp=[]
        for i in rank_set_list:
            cluster_failedtestcases_tmp.append(i[0])
        cluster_failedtestcases.append(cluster_failedtestcases_tmp)
        #print cluster_failedtestcases

    else:
        # print initial_medoid
        # print "choosing initial medoid complete"
        cluster_result = cluster_process(rank_set, initial_medoid[1], initial_medoid[0], statements_number)
        # print "clustering complete"
        medoid = initial_medoid[1]
        cluster_failedtestcases_list = [[] for i in range(initial_medoid[0])]
        cluster_failedtestcases = [[] for i in range(initial_medoid[0])]
        for i in range(0, len(rank_set)):
            cluster_failedtestcases_list[cluster_result[i]].append(i)
        for i in range(0, len(medoid)):
            for j in range(0, len(cluster_failedtestcases_list[i])):
                cluster_failedtestcases[i].append(rank_set_list[cluster_failedtestcases_list[i][j]][0])

    return cluster_failedtestcases



def get_the_great_expense_score(cluster_failedtestcases,statement_matrix,result_list,statements_number,list_injected_fault):
    best_score=[]
    worst_score=[]
    list_success = []
    suspicious_success=[]
    for tmp in range(0, len(result_list)):
        if result_list[tmp] == 0:
            list_success.append(tmp)
    success_matrix = copy.deepcopy(statement_matrix[list_success, :])
    for i in range(1, statements_number + 1):
        a00_success = 0
        a10_success = 0
        for j in range(1, len(list_success) + 1):
            if (success_matrix[j - 1, i - 1] == 0):
                a00_success = a00_success + 1
            if (success_matrix[j - 1, i - 1] == 1):
                a10_success = a10_success + 1
        suspicious_success.append([a00_success, 0, a10_success, 0])
        # a00,a11,a10,a01
    for failed_test_set in cluster_failedtestcases:
        suspicious_score=[]
        failed_matrix = copy.deepcopy(statement_matrix[failed_test_set, :])
        for i in range(1, statements_number + 1):
            suspicious = copy.deepcopy(suspicious_success[i - 1])
            a01_fail = 0
            a11_fail = 0
            for j in range(1, len(failed_test_set) + 1):
                if (failed_matrix[j - 1, i - 1] == 0):
                    a01_fail = a01_fail + 1
                if (failed_matrix[j - 1, i - 1] == 1):
                    a11_fail = a11_fail + 1
            suspicious[1] = a11_fail
            suspicious[3] = a01_fail

            if(suspicious[1]==0):
                sus_scorefor_that_statement=0
            else:
                sus_scorefor_that_statement=(suspicious[1]/(suspicious[1]+suspicious[3]))/((suspicious[1]/(suspicious[1]+suspicious[3]))+(suspicious[2]/(suspicious[2]+suspicious[0])))

            suspicious_score.append([sus_scorefor_that_statement, i])
        t_Dstar = sorted(suspicious_score, key=lambda x: (-x[0], x[1]))
        l_position_Dstar=0
        change_position_good_Dstar=0
        change_position_bad_Dstar=0
        for l in t_Dstar:
            if l[1] in list_injected_fault:
                l_position_Dstar = t_Dstar.index(l)
                break
        for l in t_Dstar:
            if l[0] == t_Dstar[l_position_Dstar][0]:
                change_position_good_Dstar = t_Dstar.index(l)
                break
        for l in t_Dstar:
            if l[0] == t_Dstar[l_position_Dstar][0]:
                change_position_bad_Dstar = t_Dstar.index(l)
        good_point_Dstar = 1 - ((change_position_good_Dstar + 1) / statements_number)
        bad_point_Dstar = 1 - ((change_position_bad_Dstar + 1) / statements_number)
        best_score.append(good_point_Dstar)
        worst_score.append(bad_point_Dstar)
    result=[best_score,worst_score]
    return  result

#rank1=(1,2,3,4,5,6,7)
#rank2=(1,2,4,3,7,5,6)
#rank3=(6,7,5,3,4,2,1)
#rank4=(5,7,6,4,3,2,1)
#rank5=(1,3,5,4,7,2,6)
#rank_set=[rank1,rank2,rank3,rank4,rank5]

#print choosing_initial_medoid(rank_set,7)



































