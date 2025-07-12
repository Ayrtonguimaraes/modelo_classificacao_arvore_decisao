# Classificador de Segmento de Vendas

Este é um aplicativo web simples que utiliza um modelo de árvore de decisão treinado para classificar empresas em diferentes segmentos de vendas (Starter, Bronze, Silver, Gold) com base em suas características.

## Características

- **Interface moderna e responsiva** com design gradiente
- **Classificação em tempo real** usando modelo de machine learning
- **Visualização de probabilidades** para cada segmento
- **Validação de dados** no frontend e backend
- **Design responsivo** para desktop e mobile

## Segmentos de Cliente

- **Starter**: Empresas iniciantes com baixo faturamento
- **Bronze**: Empresas em crescimento com faturamento moderado
- **Silver**: Empresas estabelecidas com bom faturamento
- **Gold**: Empresas premium com alto faturamento

## Variáveis Utilizadas

- **Atividade Econômica**: Comércio, Indústria, Agronegócio, Serviços
- **Faturamento Mensal**: Valor em reais
- **Número de Funcionários**: Quantidade de colaboradores
- **Localização**: São Paulo, Rio de Janeiro, Belo Horizonte, Vitória
- **Idade da Empresa**: Anos de existência
- **Nível de Inovação**: Escala de 0 a 10

## Instalação e Uso

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Execução

1. Execute o aplicativo:
   ```bash
   python app.py
   ```

2. Abra seu navegador e acesse:
   ```
   http://localhost:5000
   ```

### Como Usar

1. Preencha todos os campos do formulário com os dados da empresa
2. Clique em "Classificar Segmento"
3. Visualize o resultado da classificação e as probabilidades

## Estrutura do Projeto

```
modelo_classificacao_arvore_decisao-1/
├── app.py                          # Aplicativo Flask principal
├── templates/
│   └── index.html                  # Interface do usuário
├── modelo_classificacao_decision_tree.pkl  # Modelo treinado
├── datasets/                       # Dados de treinamento
├── requirements.txt                # Dependências Python
└── README.md                       # Este arquivo
```

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Machine Learning**: Scikit-learn, Joblib
- **Processamento de Dados**: Pandas

## Modelo de Machine Learning

O modelo utiliza uma **Árvore de Decisão** otimizada com os seguintes hiperparâmetros:
- `max_depth`: 2 (profundidade máxima)
- `min_samples_leaf`: 1 (mínimo de amostras por folha)

O modelo foi treinado com validação cruzada e apresenta uma acurácia de aproximadamente 47% no conjunto de teste.

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes. 