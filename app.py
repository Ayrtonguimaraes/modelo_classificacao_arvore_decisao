import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Carregar o modelo treinado
modelo = joblib.load('./modelo_classificacao_decision_tree.pkl')

# Valores possíveis para as variáveis categóricas
atividades_economicas = ['Comércio', 'Indústria', 'Agronegócio', 'Serviços']
localizacoes = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Vitória']

@app.route('/')
def index():
    return render_template('index.html', 
                         atividades=atividades_economicas,
                         localizacoes=localizacoes)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obter dados do formulário
        data = request.get_json()
        
        # Criar DataFrame com os dados
        df_input = pd.DataFrame([{
            'atividade_economica': data['atividade_economica'],
            'faturamento_mensal': float(data['faturamento_mensal']),
            'numero_de_funcionarios': int(data['numero_de_funcionarios']),
            'localizacao': data['localizacao'],
            'idade': int(data['idade']),
            'inovacao': int(data['inovacao'])
        }])
        
        # Fazer predição
        predicao = modelo.predict(df_input)[0]
        probabilidades = modelo.predict_proba(df_input)[0]
        
        # Mapear probabilidades para segmentos
        segmentos = ['Starter', 'Bronze', 'Silver', 'Gold']
        prob_dict = dict(zip(segmentos, probabilidades))
        
        return jsonify({
            'success': True,
            'segmento': predicao,
            'probabilidades': prob_dict
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 