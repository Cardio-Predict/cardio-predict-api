from flask import Flask, request, render_template, jsonify
import json
from classifier import prever_doenca_cardiaca

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    """
    Renderiza a página principal com o formulário.
    Se for POST, processa a predição.
    """
    
    if request.method == 'POST':
        try:
            # Receber os dados do formulário
            idade = int(request.form.get("idade"))
            sexo = int(request.form.get("sexo"))
            tipo_dor_peito = int(request.form.get("tipo_dor_peito"))
            pressao_arterial_repouso = int(request.form.get("pressao_arterial_repouso"))
            colesterol = int(request.form.get("colesterol"))
            acucar_jejum = int(request.form.get("acucar_jejum"))
            eletro_repouso = int(request.form.get("eletro_repouso"))
            freq_cardiaca_max = int(request.form.get("freq_cardiaca_max"))
            angina_exercicio = int(request.form.get("angina_exercicio"))
            depressao_st = float(request.form.get("depressao_st"))
            inclinacao_st = int(request.form.get("inclinacao_st"))
            num_vasos_principais = int(request.form.get("num_vasos_principais"))
            thalassemia = int(request.form.get("thalassemia"))
            
            # Fazer a predição
            resultado = prever_doenca_cardiaca(
                idade, sexo, tipo_dor_peito, pressao_arterial_repouso,
                colesterol, acucar_jejum, eletro_repouso, freq_cardiaca_max,
                angina_exercicio, depressao_st, inclinacao_st, num_vasos_principais, thalassemia
            )
            
            # Retornar o resultado para o template
            return render_template(
                'index.html',
                predicao=resultado['predicao'],
                risco=resultado['risco_doenca'],
                mensagem=resultado['mensagem'],
                dados_entrada={
                    'idade': idade,
                    'sexo': sexo,
                    'tipo_dor_peito': tipo_dor_peito,
                    'pressao_arterial_repouso': pressao_arterial_repouso,
                    'colesterol': colesterol,
                    'acucar_jejum': acucar_jejum,
                    'eletro_repouso': eletro_repouso,
                    'freq_cardiaca_max': freq_cardiaca_max,
                    'angina_exercicio': angina_exercicio,
                    'depressao_st': depressao_st,
                    'inclinacao_st': inclinacao_st,
                    'num_vasos_principais': num_vasos_principais,
                    'thalassemia': thalassemia
                }
            )
        except Exception as e:
            return render_template('index.html', erro=f"Erro ao processar: {str(e)}")
    
    return render_template('index.html')

@app.route("/api/prever", methods=['POST'])
def api_prever():
    """
    Endpoint da API para fazer predições via JSON.
    Útil para integração com outras aplicações.
    """
    try:
        dados = request.get_json()
        
        resultado = prever_doenca_cardiaca(
            idade=dados['idade'],
            sexo=dados['sexo'],
            tipo_dor_peito=dados['tipo_dor_peito'],
            pressao_arterial_repouso=dados['pressao_arterial_repouso'],
            colesterol=dados['colesterol'],
            acucar_jejum=dados['acucar_jejum'],
            eletro_repouso=dados['eletro_repouso'],
            freq_cardiaca_max=dados['freq_cardiaca_max'],
            angina_exercicio=dados['angina_exercicio'],
            depressao_st=dados['depressao_st'],
            inclinacao_st=dados['inclinacao_st'],
            num_vasos_principais=dados['num_vasos_principais'],
            thalassemia=dados['thalassemia']
        )
        
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
