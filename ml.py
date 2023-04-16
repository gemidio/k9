import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = [
    {"ip": "192.168.0.1", "hits": 1, "suspect": False},
    {"ip": "192.168.0.2", "hits": 10, "suspect": True},
    {"ip": "192.168.0.3", "hits": 20, "suspect": True},
    {"ip": "192.168.0.4", "hits": 30, "suspect": True},
    {"ip": "192.168.0.5", "hits": 2, "suspect": False},
]

df = pd.DataFrame(data)

df = pd.get_dummies(df)


X = df.drop("suspect", axis=1)  # variáveis preditoras (exceto a coluna alvo)
y = df["suspect"]  # coluna alvo

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=1
)

modelo = DecisionTreeClassifier(criterion="entropy", max_depth=3)

modelo.fit(X_treino, y_treino)

# criar nova observação em forma de lista
nova_observacao = ["192.168.0.4", 27]

# transformar lista em DataFrame
nova_observacao_df = pd.DataFrame([nova_observacao], columns=["ip", "hits"])

print(nova_observacao_df)

# realizar a codificação one-hot na nova observação

nova_observacao_df = pd.get_dummies(nova_observacao_df)

print(X_teste)

# fazer a predição do modelo para a nova observação
predicao = modelo.predict(X_teste)

print(predicao)
