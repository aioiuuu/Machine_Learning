import pandas
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
y_train =   ['恶性','恶性','恶性','恶性','恶性','恶性'    '良性','良性','良性','良性']
y_pred_A =  ['恶性','恶性','恶性','良性','良性','良性'    '良性','良性','良性','良性']
y_pred_B =  ['恶性','恶性','恶性','恶性','恶性','恶性'    '恶性','恶性','恶性','良性']

label = ['恶性','良性']
df_label = ['恶性(正例)','良性(反例)']

# 5.针对 真实值 和 预测值，生成混淆矩阵
cm_A = confusion_matrix(y_train, y_pred_A, labels=label)
print(f'混淆矩阵A:\n{ cm_A}')

# 6.为了混淆矩阵可视化，将混淆矩阵转为DataFrame
df_cm = pandas.DataFrame(cm_A, index=df_label, columns=df_label)
print(f'混淆矩阵A:\n{ df_cm}')

# 7.针对真实值和模型B的预测值，生成混淆矩阵
cm_B = confusion_matrix(y_train, y_pred_B, labels=label)
print(f'混淆矩阵B:\n{ cm_B}')
# 8.将混淆矩阵转为DataFrame
df_cm = pandas.DataFrame(cm_B, index=df_label, columns=df_label)
print(f'混淆矩阵B:\n{ df_cm}')

print(f'模型A的召回率:{ recall_score(y_train, y_pred_A, average="macro")}')