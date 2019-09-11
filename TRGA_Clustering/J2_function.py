from __future__ import division
import pickle,numpy,xlrd,math,copy,graph_function

def getstatement_rank(statement_matrix,result_list,testcases_number,statements_number):
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
        for l in t_Dstar:
            suspicious_rank.append(l[1])
        remove_count=int(len(suspicious_rank)*0.2)
        suspicious_rank=suspicious_rank[:remove_count]
        rank_result.append([tmp,suspicious_rank])
    return rank_result

def Jaccard_sim(rank1,rank2):
    sim=0
    for i in rank1:
        if i in rank2:
            sim=sim+1
    if sim==0:
        return 0
    else:
        return (sim/(len(rank1)+len(rank2)-sim))

def cluster_result(rank_result,threhold):
    cluster_set=[]
    nodes=[]
    sides=[]
    for i in rank_result:
        nodes.append(i[0])
    for i in range(0,len(rank_result)-1):
        for j in range(i+1,len(rank_result)):

            if(Jaccard_sim(rank_result[i][1],rank_result[j][1])>=threhold):
                sides.append((rank_result[i][0],rank_result[j][0]))
    G = graph_function.Gragh(nodes, sides)
    Node_tmp=copy.deepcopy(nodes)
    while (len(Node_tmp)):
        order=G.DFS(Node_tmp[0])
        cluster_set.append(order)
        for i in order:
            Node_tmp.remove(i)
    return cluster_set


