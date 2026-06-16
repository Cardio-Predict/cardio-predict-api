import joblib
import numpy as np

# Carrega o modelo uma única vez (para não recarregar a cada requisição)
modelo = joblib.load('models/modelo_cardiaco.pkl')

def prever_doenca_cardiaca(idade, sexo, tipo_dor_peito, pressao_arterial_repouso, 
                           colesterol, acucar_jejum, eletro_repouso, freq_cardiaca_max, 
                           angina_exercicio, depressao_st, inclinacao_st, num_vasos_principais, thalassemia):
    """
    Recebe os dados do paciente e retorna a predição.
    
    Retorna:
    - 0: Sem doença cardíaca
    - 1: Com doença cardíaca
    """
    
    # Organizar os dados na mesma ordem que o modelo foi treinado
    caracteristicas = np.array([[
        idade, sexo, tipo_dor_peito, pressao_arterial_repouso, 
        colesterol, acucar_jejum, eletro_repouso, freq_cardiaca_max, 
        angina_exercicio, depressao_st, inclinacao_st, num_vasos_principais, thalassemia
    ]])
    
    # Fazer a predição
    predicao = modelo.predict(caracteristicas)
    probabilidade = modelo.predict_proba(caracteristicas)
    
    # Mapear o resultado
    resultado = {
        'predicao': int(predicao[0]),
        'risco_doenca': float(probabilidade[0][1]) * 100,  # Probabilidade de ter doença
        'mensagem': 'Risco alto de doença cardíaca' if predicao[0] == 1 else 'Baixo risco de doença cardíaca'
    }
    
    return resultado
