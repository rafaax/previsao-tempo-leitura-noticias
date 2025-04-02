import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer

class RandomForest: 
    def __init__(self):
        self.random_state = 42
        self.test_size = 0.3
        # test_size=0.3 significa que 30% dos dados serão usados para teste
        # random_state garante que a divisão seja a mesma cada vez que o código rodar

    def datasetPreprocessor(self, df):
        label_encoders = {}  # dict para armazenar os encoders e evitar problemas na predição
        for col in ['gender', 'state', 'device', 'periodo', 'best_category', 'time_spent_category']:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

        return df, label_encoders

    def trainModel(self, x, y):

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=self.test_size, random_state=self.random_state)

        model = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=self.random_state)
        
        categorical_cols = x.select_dtypes(include=['object']).columns
        numerical_cols = x.select_dtypes(include=['int64', 'float64']).columns

        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
                ('num', 'passthrough', numerical_cols)
            ])

        X_train_processed = preprocessor.fit_transform(X_train)
        X_test_processed = preprocessor.transform(X_test)

        model.fit(X_train_processed, y_train)

        return model, X_train_processed, X_test_processed, y_train, y_test, preprocessor, X_test

    def predict(self, model, x_test, preprocessor):
        x_test_processed = preprocessor.transform(x_test)
        y_pred = model.predict(x_test_processed)
        return y_pred
    
    def avaliateModel(self, y_pred, y_test):
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"Erro Médio Absoluto (MAE): {mae:.2f}")
        print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
        print(f"Coeficiente de Determinação (R²): {r2:.2f}")
