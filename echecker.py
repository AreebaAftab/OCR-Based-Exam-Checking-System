# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:34:03 2018

@author: Areeba aftab
"""

# Define if you want to download data from the original database or use the dataset one already provided and preprocessed
# Use:
# 'load': If you want to load the datase from the directory
# 'download': To download data from the database and process the images
dataset_load_method = 'download'

# Define if you want to save the dataset to a file
save_dataset = False nve,

# Define if you want to load the trained classifiers from the directory
#load_classifiers = False
load_classifiers = False


# Define if you want to save the trained classifiers to a file
#save_classifiers = True
save_classifiers = False


# Define if you want to save classification test output to a file
save_results = True
if (save_results):
    result_output_file = open('result_output.txt','w') 

# Define if you want to print errors and warnings
enable_error_output = False


import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import scipy
import sklearn
import pandas as pd
from sklearn import linear_model, datasets, metrics
#from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import binarize
from sklearn.neural_network import BernoulliRBM, MLPClassifier
from sklearn.datasets import fetch_mldata
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from skimage import data, color, exposure, measure
from skimage.transform import resize
from skimage.feature import hog
from sklearn.manifold import TSNE
from sklearn.externals import joblib

from io import StringIO
import cv2
from scipy import ndimage
from difflib import SequenceMatcher
from sys import stdout
from IPython.display import clear_output
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.corpus import wordnet as wn 
import gensim

def print_percentage(prct, msg=None):
    if (prct > 100 or prct < 0):
        return
    clear_output(wait=True)
    if (msg == None):
        stdout.write("Progress: [")
    else:
        stdout.write(msg+" [")
    end = int(int(prct)/10)
    for i in range(0, end):
        stdout.write("=")
    for i in range(end, 10):
        stdout.write(" ")
    stdout.write("] "+str(prct)+"%")
    stdout.flush()

df2=pd.read_csv("../new alphabets.csv", sep=',',header=None)
df3=pd.read_csv("../alphabets test.csv", sep=',',header=None)


def delborders(crop):
    cropf = ndimage.gaussian_filter(crop, 0.5)
    cropbin = (cropf<0.8)
    labeled, nr_objects = ndimage.label(cropbin)
    labels_to_delete = []
    for i in range(0, labeled.shape[1]):
        if (labeled[labeled.shape[0]-1][i] > 0):
            labels_to_delete.append(labeled[labeled.shape[0]-1][i])
    
    label_in_delete = False
    for x in range(0, labeled.shape[1]):
        for y in range(0, labeled.shape[0]):
            label_in_delete = False
            for l in range(0, len(labels_to_delete)):
                if (labeled[y][x] == labels_to_delete[l]):
                    label_in_delete = True
            
            if(label_in_delete):
                crop[y][x] = 1.0
    
    return crop
    
def getcrop(n):
    image = cv2.imread(df2[1][n])
    
    
    #plt.imshow(image) 
    imgh, imgw = image.shape[:-1]
    img_rgb = image.copy()
    template = cv2.imread("../template.png")
    h, w = template.shape[:-1]
    
    template_match_success = False
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .7
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns agetd rows
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        croph1 = pt[1]
        croph2 = pt[1]+h
        cropw = pt[0] + w
        template_match_success = True
        
    
    if (not template_match_success):
        #Template matching has failed so return...
        crop = image.copy()
        crop = color.rgb2gray(crop)
          
        return crop, True
        
    
    if (df2[3][n] == 'first' or df2[3][n] == 'last'):
        crop = image.copy()[max(croph1-6, 0):min(croph2+6, imgh), cropw:imgw]
    else:
        crop = image.copy()[max(min(croph2+4, imgh-1), 0):imgh, :]
        
    crop = color.rgb2gray(crop)
    if (df2[3][n] == 'first_b' or df2[3][n] == 'last_b'):
        crop = delborders(crop)
    crop = cv2.resize(crop, dsize=(315,24), interpolation=cv2.INTER_CUBIC)
    return crop, True

def getcrop1(n):
    image = cv2.imread(df3[1][n])
    
    
    #plt.imshow(image) 
    imgh, imgw = image.shape[:-1]
    img_rgb = image.copy()
    template = cv2.imread("../template.png")
    h, w = template.shape[:-1]
    
    template_match_success = False
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .7
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        croph1 = pt[1]
        croph2 = pt[1]+h
        cropw = pt[0] + w
        template_match_success = True
        
    
    if (not template_match_success):
        #Template matching has failed so return...
        crop = image.copy()
        crop = color.rgb2gray(crop)
          
        return crop, True
        
    
    if (df3[2][n] == 'first' or df3[2][n] == 'last'):
        crop = image.copy()[max(croph1-6, 0):min(croph2+6, imgh), cropw:imgw]
    else:
        crop = image.copy()[max(min(croph2+4, imgh-1), 0):imgh, :]
        
    crop = color.rgb2gray(crop)
    if (df3[2][n] == 'first_b' or df3[2][n] == 'last_b'):
        crop = delborders(crop)
    crop = cv2.resize(crop, dsize=(315,24), interpolation=cv2.INTER_CUBIC)
    return crop, True
def gen_dataset(n=df2.shape[0]):
    data = []
    labels = []
    for i in range(1, n):
        crop, success = getcrop(i)
        if (success):
            data.append(crop)
            labels.append(df2[2][i])
            print(labels)
        else:
            if (enable_error_output):
                print("[WARNING] Template matching has failed for image: "+str(i))
        print_percentage((i*100/(n-1)), "Fetched "+str(i)+" images:")
    
    print_percentage(100, "Fetched "+str(n-1)+" images:")
    print("")
    print("Finished!")
    return data, labels

def gen_dataset1(n=df3.shape[0]):
    data1 = []
    #labels = []
    for i in range(1, n):
        crop1, success1 = getcrop1(i)
        if (success1):
            data1.append(crop1)
            #labels.append(df2[2][i])
            #print(labels)
        else:
            if (enable_error_output):
                print("[WARNING] Template matching has failed for image: "+str(i))
        print_percentage((i*100/(n-1)), "Fetched "+str(i)+" images:")
    
    print_percentage(100, "Fetched "+str(n-1)+" images:")
    print("")
    print("Finished!")
    return data1

 if (dataset_load_method == 'download'):
    dataset, labels = gen_dataset(69)
    dataset1 = gen_dataset1(12)

    
    

# Load dataset from files
if (dataset_load_method == 'load'):
    dataset = np.load("C:/Users/Areeba Aftab/Desktop/checker/github/handwritten/Handwritten-Names-Recognition-master/Notebook/HandwrittenNames_data2.npz")['data']
    labels = np.load("C:/Users/Areeba Aftab/Desktop/checker/github/handwritten/Handwritten-Names-Recognition-master/Notebook/HandwrittenNames_labels.npz")['data']

# If specified, the generated dataset can be saved to .npz files using these functions.

# In[ ]:

# Save dataset to a file if defined
if (save_dataset):
    np.savez("C:/Users/Areeba Aftab/Desktop/checker/github/handwritten/Handwritten-Names-Recognition-master/Notebook/HandwrittenNames_data2.npz", data=dataset)
    np.savez("C:/Users/Areeba Aftab/Desktop/checker/github/handwritten/Handwritten-Names-Recognition-master/Notebook/HandwrittenNames_labels2.npz", data=labels)


# We can plot some images and print their corresponding labels to check that everything is correct: 

# In[ ]:

# Change selection to plot a different image and label
selection = 7
plt.imshow(dataset[selection], cmap='gray')
plt.show()
print(labels[selection])
print(str(type(labels[7])))


# # 3. Defining extra helpful functions
# 
# In this section of the notebook we will define some functions that will be useful later on.

# ### get_labels
# 
# This function labels the connected components in an image by binarizing it and running a clustering method, it returns the labels and the number of labels it detects.

# In[ ]:

def get_labels(crop):
    
    img = crop.copy() # gray-scale image
    
    # You could smooth the image (to remove small objects) but we saw better results without using it...
    # blur_radius = 0.5
    # imgf = ndimage.gaussian_filter(img, blur_radius)
    
    threshold = 0.8
    
    # Find connected components
    labeled, nr_objects = ndimage.label(img<threshold) 
    #print("Number of objects is " +str(nr_objects))

    # Find connected components
    #labeled, nr_objects = ndimage.label(img<threshold) 
                
    return labeled, nr_objects   
                   

# ### get_bboxes
# 
# This function gets the bounding boxes to cut each character correctly given the labels obtained from get_labels. It returns a list of each character's bounding boxes (2 2D points).


# In[ ]:

def get_bboxes(labeled, nr_objects):
    bboxes = np.zeros((nr_objects, 2, 2), dtype='int')

    x1, y1, x2, y2 = 0, labeled.shape[0], 0, 0
    coord = 0
    cont = 0
    ytop, ybot = 0, 0
    nzero, firstb = False, False

    for x in range(0, labeled.shape[1]):
        nzero, firstb = False, False
        ytop, ybot = 0, 0
        for y in range(0, labeled.shape[0]):
            if (labeled[y][x] > 0):
                nzero = True
                if (not firstb):
                    ytop = y
                    firstb = True
                ybot = y

        if (nzero):
            if (ytop < y1):
                y1 = ytop
            if (ybot > y2):
                y2 = ybot
            if (coord == 0):
                x1 = x
                coord = 1
            elif (coord == 1):
                x2 = x
        elif ((not nzero) and (coord == 1)):
            bboxes[cont][0] = [x1, y1]
            bboxes[cont][1] = [x2, y2]
            cont += 1
            coord = 0
            x1, y1, x2, y2 = 0, labeled.shape[0], 0, 0

    bboxes = bboxes[0:cont]
    return bboxes, cont


# ### crop_characters
# 
# Given an image and character bounding boxes this function crops each character in an image and returns each character's corresponding binarized image in a list.

# In[ ]:

def crop_characters(img, bboxes, n):
    characters = []
    for i in range(0, n):
        c = img.copy()[bboxes[i][0][1]:bboxes[i][1][1], bboxes[i][0][0]:bboxes[i][1][0]]
        if (c.shape[0] != 0 and c.shape[1] != 0):
            c = resize(c, (28, 28), mode='constant', cval=1.0, clip=True)
            characters.append((c<0.80).reshape(784))
    return characters, len(characters)


# ### labelsep
# 
# Separates a full name label into a character list. Useful for the training part to have the labels of each character.

# In[ ]:

def labelsep(label):
    if (type(label) is str or type(label) is np.str_):
        decomposed_label = list(label)
        labels = []
        for i in range(0, len(decomposed_label)):
            if (decomposed_label[i] != ' '):
                labels.append(decomposed_label[i])
        return labels
    else:
        return []


# ### get_characters
# 
# Given an image from the dataset and its label this function splits each character into one image and a label. The img_only variant doesn't return the labels (useful when testing with full names to save some memory and time).

# In[ ]:

def get_characters(image, label):
    labeled, nr_objects= get_labels(image)
    
    bboxes, n = get_bboxes(labeled, nr_objects)
    characters, n_chars = crop_characters(image, bboxes, n)
    labels = labelsep(label)
    return characters, labels[0:n_chars]

def get_characters_img_only(image):
    labeled, nr_objects= get_labels(image)
    bboxes, n = get_bboxes(labeled, nr_objects)
    characters, n_chars = crop_characters(image, bboxes, n)
    return characters

#selection=2
#image=dataset[selection]
#def get_characters_img_only(image):
#    labeled, nr_objects = get_labels(image)
#    bboxes, n = get_bboxes(labeled, nr_objects)
#    characters, n_chars = crop_characters(image, bboxes, n)
#    return characters

# ## Checking results
# 
# We can check if it extracts correctly all the data with these plots and prints

# In[ ]:
plt.imshow(dataset[selection], cmap='gray')

selection = 7
plt.imshow(dataset[selection], cmap='gray')
plt.show()
print(labels[selection])


# In[ ]:
selection = 7
characters, charlabels= get_characters(dataset[selection], labels[selection])


# In[ ]:

for i in range(0, len(characters)):
    plt.imshow(characters[i].reshape(28,28), cmap='gray')
    plt.show()
    
print(str(charlabels))


# # 4. Defining our models
# 
# We will define our four classifiers: MLP with RBM features, MLP with HOG features, MLP with PCA features and MLP only.

# In[ ]:

# Define if we want to print status of the training process
verbose_classifiers = True


# ### MLP with RBM features
# We define a RBM with 300 components and a MLP with 3 layers of 300, 400 and 150 neurons respectively. Then whe combine them together into a Scikit-Learn Pipeline to chain the features of the RBM to the input of the MLP.

# In[ ]:

# RBM Definition
rbm = BernoulliRBM(n_components=300, learning_rate=0.01, n_iter=45, random_state=0, verbose=verbose_classifiers)

# MLP Classifier Definition 
mlp = MLPClassifier(hidden_layer_sizes=(300,400,150), activation='relu', max_iter=5000, tol=0.0001, random_state=1, verbose=verbose_classifiers)

# We define the pipeline afterwards: MLP Classifier with RBM features
rbm_mlp_classifier = Pipeline(steps=[('rbm', rbm), ('mlp', mlp)])


# ### MLP with HOG features
# We define a MLP with 3 layers of 300, 400 and 150 neurons respectively to train it with the HOG features later on.

# In[ ]:

# MLP Classifier with HOG (Histogram of Oriented Gradients) features
mlp_classifier_HOG = MLPClassifier(hidden_layer_sizes=(300,400,150), max_iter=5000, tol=0.001, random_state=1, verbose=verbose_classifiers)


# ### MLP with PCA features
# We define a MLP with 3 layers of 300, 400 and 150 neurons respectively to train it with the PCA features later on.

# In[ ]:

# MLP Classifier with PCA (Principal Component Analisis) features
mlp_classifier_PCA = MLPClassifier(hidden_layer_sizes=(300,400,150), max_iter=5000, tol=0.0001, random_state=1, verbose=verbose_classifiers)


# ### MLP
# We define a MLP with 3 layers of 300, 400 and 150 neurons respectively to train it with the data later.

# In[ ]:

# MLP Only classifier
mlp_classifier = MLPClassifier(hidden_layer_sizes=(300,400,150), max_iter=5000, tol=0.0001, random_state=1, verbose=verbose_classifiers)


# # 5. Preparing the train and test batches

# ### Splitting the dataset into train and test batches
# 
# We divide the dataset into 80% train 20% test batches:

# In[ ]:

#X_train, X_test, Y_train, Y_test = train_test_split(dataset, labels, test_size=0.2, random_state=0)
X_train, Y_train = dataset, labels
X_test1= dataset1


# In[ ]:   
 
print("Train batch lenghts:")
print("X_train size: "+str(len(X_train)))
print("Y_train size: "+str(len(Y_train)))
print("")
print("Test batch lenghts:")
print("X_test size: "+str(len(X_test1)))
#print("Y_test size: "+str(len(Y_test)))


# ### Processing the train and test batches for characters
# 
# We process the train and test batches to divide the batches into single character batches instead of full names, this is needed to train and will be useful in case of the test to test per character precision later on.

# In[ ]:

X_train_chars = []
Y_train_chars = []
Train_with_inconsistencies = []
z = 0
for i in range(0, len(X_train)):
    print_percentage(i*100/len(X_train), "Processing train image "+ str(i)+" :")
    characters, charlabels= get_characters(X_train[i], Y_train[i])
    if (len(characters) != len(charlabels) or len(characters) == 0 or len(charlabels) == 0):
        if (enable_error_output):
            print("[Warning] Input number "+str(i)+" inconsistent! Skipping this one...")
        Train_with_inconsistencies.append(i)
        z += 1
    else:
        X_train_chars.extend(characters)
        Y_train_chars.extend(charlabels)

print_percentage(100, "Processing train image "+ str(len(X_train))+" :")
print("")
print(str(100-(z*100/len(X_train)))+"% of the data in train batch correctly extracted.")






# In[ ]:

print("Character splitted train batch lenghts:")
print("X_train_chars size: "+str(len(X_train_chars)))
print("Y_train_chars size: "+str(len(Y_train_chars)))


# In[ ]:

#X_test_chars = []
#Y_test_chars = []
Test_without_inconsistencies = []
z = 0
for i in range(0, len(X_train)):
    print_percentage(i*100/len(X_train), "Processing test image "+ str(i)+" :")
    characters, charlabels= get_characters(X_train[i], Y_train[i])
    if (len(characters) != len(charlabels) or len(characters) == 0 or len(charlabels) == 0):
        if (enable_error_output):
            print("[Warning] Input number "+str(i)+" inconsistent! Skipping this one...")
        z += 1
    else:
#        X_test_chars.extend(characters)
#        Y_test_chars.extend(charlabels)
        Test_without_inconsistencies.append(i)

print_percentage(100, "Processing train image "+ str(len(X_train))+" :")
print("")
print(str(100-(z*100/len(X_train)))+"% of the data in test batch correctly extracted.")

#


# In[ ]:

#print("Character splitted test batch lenghts:")
#print("X_test_chars size: "+str(len(X_test_chars)))
#print("Y_test_chars size: "+str(len(Y_test_chars)))


# ### Calculate the Histogram of Oriented Gradients
# 
# We calculate the Histogram of Oriented Gradients for the MLP_HOG classifier.

# In[ ]:

fd_train = np.zeros((len(X_train_chars),392))
for i in range(0,len(X_train_chars)):
    print_percentage(i*100/len(X_train_chars), "Processing train image "+ str(i)+" :")
    fd_train[i], hog_image = hog(X_train_chars[i].reshape(28,28), orientations=8, pixels_per_cell=(4, 4), cells_per_block=(1, 1), visualise = True) 

print_percentage(100, "Processing train image "+ str(len(X_train_chars))+" :")

print("")
#fd_test = np.zeros((len(X_test_chars),392))
#for i in range(0,len(X_test_chars)):
#    print_percentage(i*100/len(X_test_chars), "Processing test image "+ str(i)+" :")
#    fd_test[i], hog_image = hog(X_test_chars[i].reshape(28,28), orientations=8, pixels_per_cell=(4, 4), cells_per_block=(1, 1), visualise = True) 
#    
#print_percentage(100, "Processing train image "+ str(len(X_test_chars))+" :")
#print("")
#print("Finished!")


# In[ ]:

# We also define a function in case we need to transform something later
def HOG_transform(chars):
    fd_hog = np.zeros((len(chars),392))
    for i in range(0, len(chars)):
        fd_hog[i], hog_image = hog(chars[i].reshape(28,28), orientations=8, pixels_per_cell=(4, 4), cells_per_block=(1, 1), visualise = True)
    return fd_hog

# This function is for visualizing the HOG
def get_HOG_image(char):
    fd_hog = np.zeros((392))
    fd_hog, hog_image = hog(char.reshape(28,28), orientations=8, pixels_per_cell=(4, 4), cells_per_block=(1, 1), visualise = True)
    return hog_image


# We can see how a hog transformed image looks:

# In[ ]:

selection = 2


hog_image = get_HOG_image(X_train_chars[selection])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(X_train_chars[selection].reshape(28,28), cmap=plt.cm.gray)
ax1.set_title('Input image')
ax1.set_adjustable('box-forced')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
ax1.set_adjustable('box-forced')
plt.show()


# ### Transform the data to extract Principal Component Analysis features
# 
# We transform the data to extract Principal Component Analysis features for the MLP_PCA classifier.

# In[ ]:

# Standardising the values
Scaler = StandardScaler().fit(X_train_chars)
X_pca_train = Scaler.transform(X_train_chars)
# Call the PCA method with 100 components. 
pca = PCA(n_components=100)
pca.fit(X_pca_train)
P_train = pca.transform(X_pca_train)

# Standardising the values
X_pca_test = Scaler.transform(X_train_chars)

# Call the PCA method with 100 components. 
P_test = pca.transform(X_pca_test)


# In[ ]:

# We also define a function in case we need to transform something later
def PCA_transform(chars):
    # Standardising the values
    X_pca = Scaler.transform(chars)

    # Call the PCA method with 100 components. 
    P = pca.transform(X_pca)
    return P


# We can see how the PCA looks like (only 2 PCA components):

# In[ ]:

print_limit = 1000
Target = Y_train_chars[:print_limit]
Target_colors = Y_train_chars[:print_limit]
for i in range(0, len(Target_colors)):
    Target_colors[i] = ord(Target_colors[i])
Characters = go.Scatter(
    x = P_train[:print_limit,0],
    y = P_train[:print_limit,1],
    name = Target,
    hoveron = Target,
    mode = 'markers',
    text = Target,
    showlegend = True,
    marker = dict(
        size = 8,
        color = Target_colors,
        colorscale ='Jet',
        showscale = False,
        line = dict(
            width = 2,
            color = 'rgb(255, 255, 255)'
        ),
        opacity = 0.8
    )
)
data = [Characters]

layout = go.Layout(
    title= 'Principal Component Analysis (PCA)',
    hovermode= 'closest',
    xaxis= dict(
         title= 'First Principal Component',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Second Principal Component',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= True
)


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-scatter')


# # 6. Training

# ### Training/loading classifiers
# 
# We feed the train characters and train character labels to each classifier or load the already trained classifiers from files (depending on the selected option):

# In[ ]:

if (not load_classifiers):
    rbm_mlp_classifier.fit(X_train_chars[:], Y_train_chars)
else:
    rbm = joblib.load('RBM.pkl')
    mlp = joblib.load('MLP_withRBMfeatures.pkl')
    rbm_mlp_classifier = joblib.load('RBM_MLP_classifier.pkl')


# In[ ]:

# We can define if we want to plot the components extracted by the RBM
plot_rbm_features = True

if (plot_rbm_features):
    plt.figure(figsize=(28, 28))
    for i, comp in enumerate(rbm.components_):
        plt.subplot(30, 10, i+1)
        plt.imshow(comp.reshape((28, 28)), cmap=plt.cm.gray_r, interpolation='nearest')
        plt.xticks(())
        plt.yticks(())
    plt.suptitle('300 components extracted by the RBM', fontsize=16)
    plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)

    plt.show()


# In[ ]:

if (not load_classifiers):
    mlp_classifier_HOG.fit(fd_train,Y_train_chars)
else:
    mlp_classifier_HOG = joblib.load('MLP_HOG.pkl')


# In[ ]:

if (not load_classifiers):
    mlp_classifier_PCA.fit(P_train,Y_train_chars)
else:
    mlp_classifier_PCA = joblib.load('MLP_PCA.pkl')


# In[ ]:

if (not load_classifiers):
    mlp_classifier.fit(X_train_chars, Y_train_chars)
else:
    mlp_classifier = joblib.load('MLP.pkl')


# ### Saving the classifiers
# 
# If enabled, this will save the trained models to files.

# In[ ]:

# Save the classifiers if enabled:
if (save_classifiers):
    joblib.dump(rbm, 'RBM.pkl')
    joblib.dump(mlp, 'MLP_withRBMfeatures.pkl')
    joblib.dump(rbm_mlp_classifier, 'RBM_MLP_classifier.pkl')
    joblib.dump(mlp_classifier_HOG, 'MLP_HOG.pkl')
    joblib.dump(mlp_classifier_PCA, 'MLP_PCA.pkl')
    joblib.dump(mlp_classifier, 'MLP.pkl')


# # 7. Testing the results

# ### Functions for testing results later
# 
# predict_full_name given a full name image and a classifier divides the image into characters and asks the classifier to predict it, afterwards chains the predictions of each characters into a full string.

# In[ ]:

# transform should be 'hog' for MLP_HOG classifier and 'pca' for MLP_PCA classifier, otherwise None
def predict_full_name(name, classifier, transform=None):
    characters= get_characters_img_only(name)
    if (transform == 'hog'):
        prediction = classifier.predict(HOG_transform(characters))
    elif (transform == 'pca'):
        prediction = classifier.predict(PCA_transform(characters))
    else:
        prediction = classifier.predict(characters)
    strg = ''
    for i in range(0, len(prediction)):
        strg = strg+prediction[i]
    return strg


# predict_full_names gets the prediction for each consistent test data and returns the correct ratio and correlation ratio.

# In[ ]:

# transform should be 'hog' for MLP_HOG classifier and 'pca' for MLP_PCA classifier, otherwise None

