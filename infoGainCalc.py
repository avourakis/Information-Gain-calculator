'''
Author: Andres Vourakis
Description: Simple script to help compute the information gain of a set of features
Last Date Modified: 2/21/2017
Contributors: Julie Pham 
Known Bugs:
1. 
    
'''

import math

# 1) Collect Number of Features from user
nFeatures = int(input("How many features do you have? "))

# 2) Collect Features from user
features = list();
nData = 0;
for i in range(0,nFeatures):
    feature = str(input("Enter the list of features for x{} (Without Spaces, only 0s and 1s): ".format(i+1)))
    if(i > 0):
        if(len(feature) == nData):
            features.append(feature);
        else:
            print("Number of features mismatch") #Remind: Convert into actual error
    else:
        nData = len(feature)
        features.append(feature);

# 3) Collect Target Values from user
targets = str(input("Enter the list of target values (Without Spaces, only 0s and 1s): "))
if(len(targets) != nData):
    print("Number of target values mismatch") #Remind: Convert into actual error


# 4) Compute Information Gain for Each Feature

print("\n")

# 4.1) Compute Entropy of Y (Target Values)
probY1 = float(targets.count('1'))/nData
probY0 = float(targets.count('0'))/nData

entropyY = (probY1)*(math.log(float(1/probY1), 2)) + (probY0)*(math.log(float(1/probY0),2)) #Remind: Take care of float division by 0


# 4.2) Compute Entropy of features and Information gain
for i in range(0,nFeatures):
    nX0 = features[i].count('0')
    nX1 = features[i].count('1')

    probX0 = float(nX0)/nData
    print("p(X = 0) = {}\n".format(probX0))
    probX1 = float(nX1)/nData
    print("p(X = 1) = {}\n".format(probX1))

    entropyX0 = 0;
    entropyX1 = 0;

    count1 = 0;
    count2 = 0;
    for j in range(0, nData):
        if(features[i][j] == '0' and targets[j] == '0'):
            count1 += 1
        if(features[i][j] == '1' and targets[j] == '0'):
            count2 += 1
    
    try:
        #Entropy of X = 0
        probX0Y0 = float(count1)/nX0
        probX0Y1 = float(nX0-count1)/nX0
        
        if(probX0Y0 == 1): #Takes care of division by zero
            entropyX0 = 0
        else:
            entropyX0 = probX0Y0*(math.log(1/float(probX0Y0),2)) + probX0Y1*(math.log(1/float(probX0Y1), 2))
            
        print("H(X = 0) = {}\n".format(entropyX0))
        
        #Entropy of X = 1
        probX1Y0 = float(count2)/nX1
        probX1Y1 = float(nX1-count2)/nX1
        
        if(probX1Y0 == 1): #Takes care of division by zero
            entropyX1 = 0
        else:
            entropyX1 = probX1Y0*(math.log(1/float(probX1Y0),2)) + probX1Y1*(math.log(1/float(probX1Y1), 2))
            
        print("H(X = 1) = {}\n".format(entropyX1))

        # Compute Information gain
        result = probX0*(entropyY - entropyX0) + probX1*(entropyY - entropyX1)
        print("The Information Gain for X{} = {}\n".format(i+1, result))

    except ZeroDivisionError as e:
        print("Couldnt Compute Information Gain for X{} as one of the probabilities was 0: {}\n".format(i+1, e))


