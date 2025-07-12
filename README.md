# Classificador de Segmento de Vendas

Este é um aplicativo web que classifica empresas em diferentes segmentos de vendas (Starter, Bronze, Silver, Gold) com base em suas características, desenvolvido com Streamlit.

## Características

- **Interface moderna e interativa** com Streamlit
- **Classificação em tempo real** usando modelo de machine learning
- **Visualizações avançadas** com Plotly
- **Gráficos de probabilidades** para cada segmento
- **Gráfico de radar** para perfil da empresa
- **Design responsivo** e intuitivo
- **Deploy fácil** no Streamlit Cloud

## Segmentos de Cliente

- **🟡 Starter**: Empresas iniciantes com baixo faturamento
- **🟤 Bronze**: Empresas em crescimento com faturamento moderado
- **⚪ Silver**: Empresas estabelecidas com bom faturamento
- **🟡 Gold**: Empresas premium com alto faturamento

## Variáveis Utilizadas

- **🏢 Atividade Econômica**: Comércio, Indústria, Agronegócio, Serviços
- **💰 Faturamento Mensal**: Valor em reais
- **👥 Número de Funcionários**: Quantidade de colaboradores
- **📍 Localização**: São Paulo, Rio de Janeiro, Belo Horizonte, Vitória
- **📅 Idade da Empresa**: Anos de existência
- **💡 Nível de Inovação**: Escala de 0 a 10

## Deploy no Streamlit Cloud

### Método 1: Deploy via GitHub (Recomendado)

1. **Faça push do código para o GitHub:**
   ```bash
   git add .
   git commit -m "Add Streamlit app"
   git push origin main
   ```

2. **Acesse o Streamlit Cloud:**
   - Vá para [share.streamlit.io](https://share.streamlit.io)
   - Faça login com sua conta GitHub
   - Clique em "New app"

3. **Configure o deploy:**
   - **Repository**: Selecione seu repositório
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
   - Clique em "Deploy!"

### Método 2: Deploy Local

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o app:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Acesse:**
   ```
   http://localhost:8501
   ```

## Desenvolvimento Local

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd modelo_classificacao_arvore_decisao-1
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o app:**
   ```bash
   streamlit run streamlit_app.py
   ```

### Como Usar

1. Preencha todos os campos do formulário com os dados da empresa
2. Clique em "Classificar Segmento"
3. Visualize o resultado da classificação e as probabilidades
4. Explore os gráficos e análises detalhadas

## Estrutura do Projeto

```
modelo_classificacao_arvore_decisao-1/
├── streamlit_app.py              # Aplicativo Streamlit principal
├── .streamlit/
│   └── config.toml              # Configuração do Streamlit
├── app.py                        # Aplicativo Flask (versão alternativa)
├── templates/
│   └── index.html                # Template Flask
├── modelo_classificacao_decision_tree.pkl  # Modelo treinado
├── datasets/                     # Dados de treinamento
├── requirements.txt              # Dependências Python
└── README.md                     # Este arquivo
```

## Tecnologias Utilizadas

- **Frontend**: Streamlit
- **Visualização**: Plotly
- **Machine Learning**: Scikit-learn, Joblib
- **Processamento de Dados**: Pandas
- **Deploy**: Streamlit Cloud

## Modelo de Machine Learning

O modelo utiliza uma **Árvore de Decisão** otimizada com os seguintes hiperparâmetros:
- `max_depth`: 2 (profundidade máxima)
- `min_samples_leaf`: 1 (mínimo de amostras por folha)

O modelo foi treinado com validação cruzada e apresenta uma acurácia de aproximadamente 47% no conjunto de teste.

## Funcionalidades do App

- **📝 Formulário interativo** para entrada de dados
- **🎯 Classificação automática** do segmento
- **📊 Gráficos de probabilidades** por segmento
- **📈 Gráfico de radar** para perfil da empresa
- **📋 Métricas detalhadas** da análise
- **ℹ️ Sidebar informativa** sobre o projeto

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes. 