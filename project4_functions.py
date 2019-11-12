import re

def regex_nodigits_new(s):
    '''use regex to clean string: 
    get rid of punctuations, capitalized letters and numbers'''
    s = re.sub(r'[\d]','',str(s))#replace digits with empty str
    return s #only returning ingredients of first recipe?

def regex_noads(s):
    #s = re.sub(r'[^\w\s]','',str(df[col])) #replaces anything not alphanumeric or whitespace with empty str
    s = re.sub(r'["ADVERTISEMENT"]','',str(s))#replace the word "ADVERTISEMENT"--also replaced capital letters
    return s
    ##*for re.sub, always change input to strings with str() (wouldn't hurt if it's already a string)

# def find_maxindex(a):
#     '''takes in an array a, returns the index of the maximum value in a
        #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
#     '''
#     import numpy as np
#     for i in len(range(a)):
#         np.argmax(a)  #actually want i of 2nd largest?
        



    #from topic modelling/LSA/NMF lecture
def display_topics(model, feature_names, no_top_words, topic_names=None):
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix)
        else:
            print("\nTopic: '",topic_names[ix],"'")
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))


    #from Kmeans Clustering lecture
# helper function that allows us to display data in 2 dimensions an highlights the clusters
def display_cluster(X,km=[],num_clusters=0):
    import matplotlib.pyplot as plt

    color = 'brgcmyk'
    alpha = 0.3
    s = 20
    if num_clusters == 0:
        plt.scatter(X[:,0],X[:,1],c = color[0],alpha = alpha,s = s)
    else:
        for i in range(num_clusters):
            plt.scatter(X[km.labels_==i,0],X[km.labels_==i,1],c = color[i],alpha = alpha,s=s)
            plt.scatter(km.cluster_centers_[i][0],km.cluster_centers_[i][1],c = color[i], marker = 'x', s = 100)
            #get error: string index out of range? -- took this out of lecture, modify code! also change colours