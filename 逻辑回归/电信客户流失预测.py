import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,roc_auc_score,f1_score,classification_report
# 1. 加载原数据集
url = "https://raw.githubusercontent.com/ibm/watson-machine-learning-samples/master/cpd4.5/data/customer_churn/WA_FnUseC_TelcoCustomerChurn.csv"
df = pd.read_csv(url)




# 2. 对 Churn 和 gender 列进行 One-Hot 编码
encoder = OneHotEncoder(sparse_output=False, drop=None)

selected_columns = ['Churn', 'gender']
encoded_data = encoder.fit_transform(df[selected_columns])

encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(selected_columns),
    index=df.index
)

df_encoded = pd.concat([df.drop(columns=selected_columns), encoded_df], axis=1)


df_encoded.drop(['Churn_No', 'gender_Male'], axis=1, inplace=True)
# df_encoded.info()

# 3. 将剩余的字符串类型列转换为浮点型
# object_columns = df_encoded.select_dtypes(include=['object']).columns.tolist()
object_columns = df_encoded.select_dtypes(include=['object', 'string']).columns.tolist()
# print(f"\n需要转换的字符串类型列: {object_columns}")

for col in object_columns:
    if col in df_encoded.columns:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))

# 4. 将所有列转换为浮点型
df_float = df_encoded.astype(float)




df_float.rename(columns={'Churn_Yes': 'flag'}, inplace=True)
# print(df_float.columns)
# ['customerID', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
#        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
#        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
#        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
#        'MonthlyCharges', 'TotalCharges', 'flag', 'gender_Female']
df_float.info()
x=df_float[['Contract','InternetService','PaymentMethod']]
y=df_float['flag']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
estimator=LogisticRegression()
estimator.fit(x_train,y_train)
y_predict=estimator.predict(x_test)

# 4.模型评估
print("准确率:",accuracy_score(y_test,y_predict))
print("AUC:",roc_auc_score(y_test,y_predict))
print(f'精确率：{estimator.score(x_test,y_predict)}')
# print(f'召回率：{estimator.score(x_test,y_predict)}')
# print(f'F1-score：{estimator.score(x_test,y_predict)}')
print(f'分类评估报告：\n{classification_report(y_test,y_predict)}')