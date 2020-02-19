# Toronto-Restaurant-Recommendation

## Introduction
Recommending a restuarant to a foodied based on the cuisine of interest and the price range.The restuarant list is from [Yelp dataset](https://www.yelp.com/dataset). After filtering the data pertaining to Toronto based restuarants, webscraped to find additional information like the website and price information of the restaurant.<br>
[Toronto Restaurant Recommendation page](http://ec2-3-16-154-147.us-east-2.compute.amazonaws.com:8080/)<br><br>
![App_page](https://github.com/A-Aparna/Toronto-Restaurant-Recommendation/blob/master/image/App_page.jpg)<br>
Depending on the selections made by the user the list of 5 restaurants along with the website(if it has one) will be displayed.<br>
The dataset does not have a label/output.Hence the underlying problem is an example of unsupervised learning.


### List of files in the repository
- [restaurant_recommendation.ipynb](https://github.com/A-Aparna/Toronto-Restaurant-Recommendation/blob/master/restaurant_recommendation.ipynb)
- [Data_Preparation](https://github.com/A-Aparna/Toronto-Restaurant-Recommendation/blob/master/Data_Preparation.ipynb)

## About the Data
The data which is used for modeling has 8 feature columns with no output/label.<br>
The number of records in the dataset is 3929 restaurants <br>
![dataset](https://github.com/A-Aparna/Toronto-Restaurant-Recommendation/blob/master/image/dataset.jpg)

## Preprocessing the Data
 Yelp dataset has lot more data then its needed or is relevant for this particular restaurant recommendation project.
 1) Filter data with <i><b>location= Toronto and business= Restaurants</b></i>.
 2) Using the names of the restaurants <i><b>webscrape  their website(If they have one) and the price range</b></i> using Beautifulsoup.
 3) Cuisine is not explicitly mentioned. Each restuarant is <i><b>assigned a Cuisine based on keywords</b></i>.Like Japanese cuisine if keyword is Sushi etc.

## Exploratory Data Analysis



## Modeling
Modeling the dataset has to be using any of the Unsupervised learning algorithms.This data here is fit using K-means clustering algorithm.Only two features i.e. cuisine and price range are used to cluster keeping the clustering neat.
Cluster Sum of Squares is plotted against the no of clusters which is popularly called as elbow method.The plot is as follows-
![elbow_method](https://github.com/A-Aparna/Toronto-Restaurant-Recommendation/blob/master/image/elbow_method.jpg)

After evaluating elbow method as 30, we get the clusters as follows-
![cluster](https://github.com/A-Aparna/Toronto-Restaurant-Recommendation/blob/master/image/data_cluster..jpg) <br>
This plot is very pleasant as the clustering is pretty neat leading to a satisfactory outputs.The reason being both the features we used for clustering are discrete in nature.
This app is then hosted on <b>AWS</b>

## Summary
K means clustering method fairly clusters the two features cuisine and pricing ranges.The output achieved when verified from UI and Google results are consistent.(It can be verified standalone based on the names of the restaurants 80% of the times :) )
