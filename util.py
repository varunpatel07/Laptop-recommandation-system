import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #to create vector using specification
from sklearn.metrics.pairwise import cosine_similarity 
import pickle
recommendation=None
vector_class=None
details=None

def loaddata():
    global recommendation
    global vector_class
    global details
    f=open('recommender_pickle','rb')
    recommendation = pickle.load(f)
    f.close()

    vec=open("vector_class","rb")
    vector_class=pickle.load(vec)
    vec.close()

    details=pd.read_csv("dataset/export_dataframe.csv",index_col="PRODUCT")


    #print(details.head())
def suggest(title):
    print(title)
    print(type(title))
    title=title.lower()
    if(title in details.index.tolist()):
        return suggest_by_spec(details.loc[title,"specification"]) #this will run when you pass full laptop name as argument
    else:
        return suggest_by_spec(title) #this will run when you pass specification



def suggest_by_spec(title):
    title=vector_class.transform([title])
    res=cosine_similarity(recommendation,title)
    similarity = list(enumerate(res))
    similarity_score = sorted(similarity , key=lambda x:x[1] , reverse=True)
    similarity_score = similarity_score[:5]
    lap_indices = [i[0] for i in similarity_score]
    all_data=details.reset_index()
    #print(type(all_data.iloc[lap_indices,0].values.tolist()))
    return(all_data.iloc[lap_indices,0].values.tolist())
    
if __name__ =="util":
    loaddata()  
   
#suggest_by_spec("Lenovo 5gb")

