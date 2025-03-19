class Extraction:
    def extract_dataset_by_state(df):
        df_state = {estado: df[df['state'] == estado] for estado in df['state'].unique()}
        for estado, df_estado in df_state.items():
            path = f"datasets/datasets_tratadas/logs_{estado}.csv"
            df_estado.to_csv(path, index=False)
            print(f"dataset gerada para o estado de {estado}")