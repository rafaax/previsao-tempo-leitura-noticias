import os

class Extraction:
    def extract_dataset_by_state(self, df): # extrai os dados do dataframe original e cria um novo dataframe para cada estado
        df_state = {estado: df[df['state'] == estado] for estado in df['state'].unique()}
        os.makedirs("datasets", exist_ok=True)  # Cria a pasta se não existir
        
        for estado, df_estado in df_state.items():
            path = os.path.join("datasets", f"logs_{estado}.csv")
            df_estado.to_csv(path, index=False)
            