import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

class RandomForest: 
    def __init__(self):
        self.random_state = 42
        self.test_size = 0.3
        # test_size=0.3 significa que 30% dos dados serão usados para teste
        # random_state garante que a divisão seja a mesma cada vez que o código rodar

    def datasetPreprocessor():
        return 


    def calculateImportance(self, x,y):
        categorical_cols = x.select_dtypes(include=['object']).columns
        numerical_cols = x.select_dtypes(include=['int64', 'float64']).columns

        preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), categorical_cols),
            ('num', 'passthrough', numerical_cols)
        ])

        X_processed = preprocessor.fit_transform(x)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_processed, y)

        importances = model.feature_importances_

        cat_encoder = preprocessor.named_transformers_['cat']
        cat_features = cat_encoder.get_feature_names_out(categorical_cols)
        all_features = list(cat_features) + list(numerical_cols)

        feature_importance_df = pd.DataFrame({
            'Feature': all_features,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False).head(10) # pegar somente as 10 mais importantes

        return feature_importance_df # timestamp / age / news_id / gender / device / category

    def trainModel(self, x, y):

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=self.test_size, random_state=self.random_state)

        model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=self.random_state)
        
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

        print(model)

        return model, X_train_processed, X_test_processed, y_train, y_test, preprocessor, X_test

    def predict(self, model, x_test, preprocessor):
        x_test_processed = preprocessor.transform(x_test)
        y_pred = model.predict(x_test_processed)
        return y_pred
    
    def avaliateModel(self, y_pred, y_test):
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Acurácia do modelo: {accuracy:.2f}")
        print("\nRelatório de Classificação:")
        print(classification_report(y_test, y_pred))
        return 
