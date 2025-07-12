import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Classificador de Segmento de Vendas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título e descrição
st.title("🎯 Classificador de Segmento de Vendas")
st.markdown("---")
st.markdown("**Análise inteligente para classificação de clientes em diferentes segmentos de mercado**")

# Carregar o modelo
@st.cache_resource
def load_model():
    try:
        modelo = joblib.load('./modelo_classificacao_decision_tree.pkl')
        return modelo
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        return None

modelo = load_model()

# Sidebar com informações
with st.sidebar:
    st.header("ℹ️ Sobre o Projeto")
    st.markdown("""
    Este classificador utiliza um modelo de **Árvore de Decisão** treinado para categorizar empresas em 4 segmentos:
    
    - 🟡 **Starter**: Empresas iniciantes
    - 🟤 **Bronze**: Empresas em crescimento  
    - ⚪ **Silver**: Empresas estabelecidas
    - 🟡 **Gold**: Empresas premium
    
    **Acurácia do modelo**: ~47%
    """)
    
    st.header("📈 Variáveis Analisadas")
    st.markdown("""
    - Atividade Econômica
    - Faturamento Mensal
    - Número de Funcionários
    - Localização
    - Idade da Empresa
    - Nível de Inovação
    """)

# Função para fazer predição
def predict_segment(data):
    if modelo is None:
        return None, None
    
    try:
        # Criar DataFrame
        df_input = pd.DataFrame([data])
        
        # Fazer predição
        predicao = modelo.predict(df_input)[0]
        probabilidades = modelo.predict_proba(df_input)[0]
        
        # Mapear probabilidades para segmentos
        segmentos = ['Starter', 'Bronze', 'Silver', 'Gold']
        prob_dict = dict(zip(segmentos, probabilidades))
        
        return predicao, prob_dict
    except Exception as e:
        st.error(f"Erro na predição: {e}")
        return None, None

# Interface principal
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Dados da Empresa")
    
    # Formulário
    with st.form("prediction_form"):
        col1_1, col1_2 = st.columns(2)
        
        with col1_1:
            atividade_economica = st.selectbox(
                "🏢 Atividade Econômica",
                ["Comércio", "Indústria", "Agronegócio", "Serviços"],
                help="Selecione o setor de atuação da empresa"
            )
            
            faturamento_mensal = st.number_input(
                "💰 Faturamento Mensal (R$)",
                min_value=0.0,
                value=1000000.0,
                step=10000.0,
                help="Faturamento mensal em reais"
            )
            
            numero_funcionarios = st.number_input(
                "👥 Número de Funcionários",
                min_value=1,
                value=15,
                help="Quantidade de colaboradores"
            )
        
        with col1_2:
            localizacao = st.selectbox(
                "📍 Localização",
                ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Vitória"],
                help="Cidade onde a empresa está localizada"
            )
            
            idade = st.number_input(
                "📅 Idade da Empresa (anos)",
                min_value=0,
                value=10,
                help="Anos de existência da empresa"
            )
            
            inovacao = st.slider(
                "💡 Nível de Inovação",
                min_value=0,
                max_value=10,
                value=5,
                help="Nível de inovação da empresa (0-10)"
            )
        
        submitted = st.form_submit_button("🎯 Classificar Segmento", use_container_width=True)

# Processar predição
if submitted:
    st.markdown("---")
    
    # Dados para predição
    data = {
        'atividade_economica': atividade_economica,
        'faturamento_mensal': faturamento_mensal,
        'numero_de_funcionarios': numero_funcionarios,
        'localizacao': localizacao,
        'idade': idade,
        'inovacao': inovacao
    }
    
    # Fazer predição
    with st.spinner("🔍 Analisando dados da empresa..."):
        predicao, probabilidades = predict_segment(data)
    
    if predicao and probabilidades:
        # Resultado principal
        col_result1, col_result2 = st.columns([1, 2])
        
        with col_result1:
            st.subheader("🎯 Segmento Classificado")
            
            # Cores para cada segmento
            cores = {
                'Starter': '#FFD700',
                'Bronze': '#CD7F32', 
                'Silver': '#C0C0C0',
                'Gold': '#FFD700'
            }
            
            # Exibir resultado com estilo
            st.markdown(f"""
            <div style="
                background: {cores.get(predicao, '#007bff')};
                color: {'#000' if predicao in ['Starter', 'Silver', 'Gold'] else '#fff'};
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                margin: 10px 0;
            ">
                {predicao}
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            st.subheader("📊 Probabilidades por Segmento")
            
            # Criar gráfico de barras
            fig = px.bar(
                x=list(probabilidades.keys()),
                y=list(probabilidades.values()),
                color=list(probabilidades.keys()),
                color_discrete_map=cores,
                text=[f"{p*100:.1f}%" for p in probabilidades.values()],
                title="Distribuição de Probabilidades"
            )
            
            fig.update_layout(
                xaxis_title="Segmento",
                yaxis_title="Probabilidade",
                showlegend=False,
                height=400
            )
            
            fig.update_traces(textposition='outside')
            st.plotly_chart(fig, use_container_width=True)
        
        # Detalhes da análise
        st.markdown("---")
        st.subheader("📋 Resumo da Análise")
        
        col_detail1, col_detail2, col_detail3 = st.columns(3)
        
        with col_detail1:
            st.metric("Faturamento Mensal", f"R$ {faturamento_mensal:,.2f}")
            st.metric("Funcionários", numero_funcionarios)
        
        with col_detail2:
            st.metric("Idade da Empresa", f"{idade} anos")
            st.metric("Nível de Inovação", f"{inovacao}/10")
        
        with col_detail3:
            st.metric("Atividade", atividade_economica)
            st.metric("Localização", localizacao)
        
        # Gráfico de radar para visualizar características
        st.markdown("---")
        st.subheader("📈 Perfil da Empresa")
        
        # Normalizar valores para o gráfico de radar
        faturamento_norm = min(faturamento_mensal / 2000000, 1.0)  # Normalizar até 2M
        funcionarios_norm = min(numero_funcionarios / 20, 1.0)     # Normalizar até 20
        idade_norm = min(idade / 20, 1.0)                         # Normalizar até 20 anos
        inovacao_norm = inovacao / 10                              # Já normalizado
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[faturamento_norm, funcionarios_norm, idade_norm, inovacao_norm],
            theta=['Faturamento', 'Funcionários', 'Idade', 'Inovação'],
            fill='toself',
            name='Perfil da Empresa',
            line_color='rgb(102, 126, 234)',
            fillcolor='rgba(102, 126, 234, 0.3)'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>Desenvolvido com ❤️ usando Streamlit | Modelo de Machine Learning: Árvore de Decisão</p>
</div>
""", unsafe_allow_html=True) 