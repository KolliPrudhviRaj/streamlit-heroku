import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Division App

This app performs division of numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    numerator = st.number_input("NUMERATOR")
    denominator = st.number_input("DENOMINATOR")
    data = {'NUMERATOR': numerator,
            'DENOMINATOR': denominator,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Preprocessing

'''binary_features = ['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','FLAG_WORK_PHONE','FLAG_EMAIL']
continous_features = ['CNT_CHILDREN','AMT_INCOME_TOTAL','DAYS_BIRTH','DAYS_EMPLOYED','CNT_FAM_MEMBERS']
cat_features = ['NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE']

df['FLAG_EMAIL'] = df['FLAG_EMAIL'].replace({1:1,0:0})
df['FLAG_WORK_PHONE'] = df['FLAG_WORK_PHONE'].replace({1:1,0:0})
df['FLAG_PHONE'] = df['FLAG_WORK_PHONE'].replace({1:1,0:0})
df['FLAG_OWN_CAR'] = df['FLAG_OWN_CAR'].replace({'Y':1,'N':0})
df['CODE_GENDER'] = df['CODE_GENDER'].replace({'M':1,'F':0})
df['FLAG_OWN_REALTY'] = df['FLAG_OWN_REALTY'].replace({'Y':1,'N':0})




encoder = pickle.load(open('encoder.sav', 'rb'))
df['NAME_INCOME_TYPE'] = encoder.transform(df.NAME_INCOME_TYPE.values.reshape(-1, 1))

cat_features_req = ['NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE']
for i in cat_features_req:
    encoder_2 = pickle.load(open('encoder2_' + i +'.sav', 'rb'))
    df[i] = encoder_2.transform(df[i].values.reshape(-1, 1))



df = df.rename(columns={'FLAG_EMAIL': 'FLAG_EMAIL_1',
                        'FLAG_WORK_PHONE': 'FLAG_WORK_PHONE_1',
                        'CODE_GENDER': 'CODE_GENDER_M',
                        'FLAG_OWN_CAR': 'FLAG_OWN_CAR_Y',
                        'FLAG_OWN_REALTY': 'FLAG_OWN_REALTY_Y'})


for col in df.columns:
    if df[col].dtype != 'float64':
        df[col] = df[col].values.astype('float64')

st.subheader('Pre-processed Input to the Model')
st.table(df)
mms = pickle.load(open('minmax_scaler.sav', 'rb'))
mms.transform(df)



# Model Loading
clf =  pickle.load(open('finalized_model.sav', 'rb'))

#Model Inferencing

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(pd.DataFrame({'Labels': ['Approved','Declined']}))'''

st.subheader('Division')
if denominator == 0:
    st.write('Invalid Input, Denominator cannot be Zero')
else:
    result=numerator/denominator
    st.write(result)
#st.write(prediction)

'''st.subheader('Prediction Probability')
st.write(prediction_proba)'''
