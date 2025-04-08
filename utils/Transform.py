class Transform:
    def dataframeToJson(self, df): # converte o dataframe em um arquivo json
        return df.to_json()