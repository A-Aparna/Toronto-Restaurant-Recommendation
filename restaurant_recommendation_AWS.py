#Copy of the fle to be used for AWS deployment
import numpy as np
import pandas as pd
import itertools

df=pd.read_excel('restaurants_toronto3.xlsx')
df=df.dropna()
df=df.reset_index(drop=True)

def condense_cuisine(row):
    if (row=='Sushi' or row=='Korean'):
        return 'Japan'
    if (row=='Vietnamese' ):
        return 'Thai'
    if (row=='French' or row=='Italian'):
        return 'European'
    if (row=='Greek' or row=='Middle'):
        return 'Mediterranean'
    if (row=='Baker' or row=='Juice'):
        return 'Dessert'
    if (row=='Barbeque'):
        return 'Canadian'
    if (row=='Peruvian'):
        return 'Mexican'
    else:
        return row
    return None
df['cuisine']=df['cuisine'].apply(condense_cuisine)


X=df.iloc[:,[5,6]].values
X_train=X.copy()

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X = LabelEncoder()
X_train[:, 0] = labelencoder_X.fit_transform(X_train[:, 0])
onehotencoder = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0])],remainder='passthrough')
X_train = onehotencoder.fit_transform(X_train).toarray()


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib as mpl
wcss = []
for i in range(1, 32):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X_train)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,32), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters = 30, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X_train)

dfd=pd.DataFrame({"Cluster ID":y_kmeans})
dfa=pd.concat([dfd, df],axis=1, sort=False)

def cluster_predict(Xt):
    #Y = vectorizer.transform(list(str_input))
    prediction = kmeans.predict(Xt)
    return prediction

from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recommend',methods=['POST'])
def recommend():
    if request.method == 'POST':
        option = request.form['cuisine']
        print(option)
        cost=request.form['cost']
        print(cost)
        Xt=np.array([[option,cost]])
        Xt[:,0] = labelencoder_X.transform(Xt[:,0])
        print(Xt)
        #onehotencoder = OneHotEncoder(categorical_features = [0])
        Xt = onehotencoder.transform(Xt).toarray()
        print(Xt)
        pred=cluster_predict(Xt)
        pred=int(pred)
        out=dfa.loc[dfa["Cluster ID"]==pred]
        random_subset = out.sample(n=5)
        name=random_subset['name'].values
        print(name)
        address=random_subset['address'].values
        to_pass=[]
        for n in range(0,len(name)):
            lst=[name[n],address[n]]
            to_pass.append(lst)
       # link=random_subset["6"]
        print(to_pass)
    return render_template('recommend.html',name=to_pass)

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=8080)
    app.run()
