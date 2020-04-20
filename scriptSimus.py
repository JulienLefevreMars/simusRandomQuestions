import numpy as np
import matplotlib.pyplot as plt

# Fixed Parameters
nbQuestionsPerStudent = 20
nbStudents = 500
nbStudentsPerGroup = 10

nbQuestions = np.arange(nbQuestionsPerStudent+1,nbStudents*nbQuestionsPerStudent,5)

meanPWDistances=np.zeros((len(nbQuestions),))
minmaxPWDistances=np.zeros((len(nbQuestions),2))
meanDistances=np.zeros((len(nbQuestions),))
minmaxDistances=np.zeros((len(nbQuestions),2))
cpt=0
for n in nbQuestions:
    # Generate nbQuestions random partitions of the set {0,n}
    randperm = np.zeros((nbQuestionsPerStudent,nbStudentsPerGroup))
    for i in range(nbStudentsPerGroup):
        randperm[:,i]=np.random.permutation(n)[0:nbQuestionsPerStudent]
    # Compute all pairwise distances between partitions (edit distance)
    distance=[]
    unionOfIntersect=[]
    for i in range(nbStudentsPerGroup):
        for j in range(nbStudentsPerGroup):
            if i<j:
                unionOfIntersect.append(np.intersect1d(randperm[:,i],randperm[:,j]))
                dist=len(np.intersect1d(randperm[:,i],randperm[:,j]))
                distance.append(dist)
    meanPWDistances[cpt]=np.mean(np.array(distance))
    minmaxPWDistances[cpt,0]=np.min(np.array(distance))
    minmaxPWDistances[cpt,1]=np.max(np.array(distance))
    # Union of all questions => diff between individual questions and union
    union=np.unique(randperm.flatten())
    distance=[]
    unionOfIntersect=np.unique(np.concatenate(unionOfIntersect))
    for i in range(nbStudentsPerGroup):
        dist=len(np.setdiff1d(randperm[:,i],unionOfIntersect))
        distance.append(dist)
    meanDistances[cpt]=np.mean(np.array(distance))
    minmaxDistances[cpt,0]=np.min(np.array(distance))
    minmaxDistances[cpt,1]=np.max(np.array(distance))
    cpt=cpt+1
    print(n)


plt.figure(figsize=(12,8))
plt.semilogx(nbQuestions,meanPWDistances,'k-')
plt.fill_between(nbQuestions,minmaxPWDistances[:,0],minmaxPWDistances[:,1])
plt.xlabel('Number of all the questions required for the exam')
plt.ylabel('Questions')
plt.legend(['Average','Min-Max for '+str(nbStudentsPerGroup)+' students per group'])
plt.title('Shared questions between two exam subjects with ' + str(nbQuestionsPerStudent) + ' questions')

plt.savefig("Figure1.png")

plt.figure(figsize=(12,8))
plt.semilogx(nbQuestions,nbQuestionsPerStudent-meanDistances,'k-')
plt.fill_between(nbQuestions,nbQuestionsPerStudent-minmaxDistances[:,0],nbQuestionsPerStudent-minmaxDistances[:,1])
plt.xlabel('Number of all the questions required for the exam')
plt.ylabel('Questions' )
plt.legend(['Average','Min-Max for '+str(nbStudentsPerGroup)+' students per group'])
plt.title('Questions among ' + str(nbQuestionsPerStudent) + ' shared in a group of '+str(nbStudentsPerGroup)+' students')

plt.savefig("Figure2.png")

plt.figure(figsize=(12,8))
plt.semilogx(nbQuestions,meanPWDistances,'r-')
plt.semilogx(nbQuestions,nbQuestionsPerStudent-meanDistances,'b-')
plt.legend(['Shared questions between two exam subjects','Questions shared in a group of '+str(nbStudentsPerGroup)+' students'])

plt.savefig("Figure3.png")