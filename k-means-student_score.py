import numpy as np
import kmeans_file_write
from sklearn.cluster import KMeans


def loadData(filePath):
    fr = open(filePath,'r+')
    lines = fr.readlines()
    retData = []
    retstudentName = []
    for line in lines:
        items = line.strip().split(",")
        retstudentName.append(items[0])
        retData.append([float(items[i]) for i in range(1,len(items))])
        
    for i in lines:print(i)
    
    return retData,retstudentName,len(lines)


def myKMeans(n_clusters,data,lines,studentName):#lines是点的个数
    mean=[]#聚类
    center=[]#每个点所在的类
    mean_check=[]#检查中心是否移动
    name_mean=[]#
    
  #  for i in range(n_clusters):
   #     mean.append([])
   
    for i in range(lines):#先将所有的点所在集合赋值为-1
        center.append(-1)
    
    for i in range(n_clusters):#初始化mean和mean_check
        name_mean.append([])
        mean.append([0,0,0,0,0,0,])
        mean_check.append([0,0,0,0,0,0,])
        #print(data[i])
        for j in range(len(mean[i])):
            mean[i][j]=data[int(lines/n_clusters*i)][j]
    
    #print(mean)
    print("-----------------------------------")
    
    while mean!=mean_check:#如果中心不变，就跳出
        for i in range(n_clusters):#赋值check
            for j in range(len(mean[i])):
                mean_check[i][j]=mean[i][j]
                
        d=0.0
        for i in range(len(data)):#获得中心
            min_dis=0x3f3f3f
            min_num=0
            for j in range(len(mean)):
                d=getDis(data[i],mean[j])
                #print(d)
                if min_dis>d :
                    min_dis=d
                    min_num=j
                center[i]=min_num
           # print("\n")
        mean=getMean(data,mean,center,n_clusters)#更新中心
        #print(center)
        
    for i in range(len(data)):
        name_mean[center[i]].append(studentName[i])
    
    for i in name_mean:#这个是输出的结果
        print(i)
    
    return center


def getMean(data,mean,center,n_clusters):
    mean_temp=[]
    mean_num=[]
    for i in range(n_clusters):
        mean_temp.append([0.0,0.0,0.0,0.0,0.0,0.0])
        mean_num.append(0.0)
    for i in range(len(data)):
        mean_num[center[i]]+=1
        for j in range(len(data[0])):#data[0]只用作获取一个list的长度，不做特殊用途
            mean_temp[center[i]][j]+=data[i][j]       
    #print(mean_temp)
    #print(mean_num)
    for i in range(n_clusters):
        for j in range(len(mean_temp[i])):
            mean_temp[i][j]/=mean_num[i]
    
    return mean_temp


def getDis(data,mean):
    d=0.0
    for i in range(len(data)):
        if i == 0:
            d+=((data[i]-mean[i])*1.2)**2.0
        if i == 1:
            d+=((data[i]-mean[i])*1.0)**2.0
        if i == 2:
            d+=((data[i]-mean[i])*1.1)**2.0
        if i == 3:
            d+=((data[i]-mean[i])*1.1)**2.0
        if i == 4:
            d+=((data[i]-mean[i])*1.0)**2.0
        if i == 5:
            d+=((data[i]-mean[i])*0.9)**2.0
    return d
     
if __name__ == '__main__':
    center=[]
    name_mean=[]
    kmeans_file_write.write_file()
    data,studentName,lines = loadData('student.txt')
    #clusters_num=input("请输入要分为几类：")
    clusters_num='5'
    clusters_num=int(clusters_num)
    
    
    km = KMeans(n_clusters=clusters_num)
    
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_,axis=1)
    #print(label)
    #print(expenses)
    
    studentCluster=[]
    for i in range(clusters_num):
        studentCluster.append([])
    #print(studentCluster)
    for i in range(len(studentName)):
        studentCluster[label[i]].append(studentName[i])
    for i in range(len(studentCluster)):
        #print("Expenses:%.2f" % expenses[i])
        print(studentCluster[i])
        
    
    center=myKMeans(clusters_num,data,lines,studentName)