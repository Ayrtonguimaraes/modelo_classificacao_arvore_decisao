import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Classificador de Segmento de Vendas",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para design moderno
st.markdown("""
<style>
    /* Reset e configurações gerais */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Header personalizado */
    .header-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .header-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .header-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 1rem;
    }
    
    /* Cards modernos */
    .card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    /* Botões modernos */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 1.1rem;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Sidebar moderno */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Segmento badges */
    .segment-badge {
        padding: 1rem 2rem;
        border-radius: 50px;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .segment-starter {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
        color: #000;
    }
    
    .segment-bronze {
        background: linear-gradient(135deg, #cd7f32 0%, #daa520 100%);
        color: #fff;
    }
    
    .segment-silver {
        background: linear-gradient(135deg, #c0c0c0 0%, #e5e4e2 100%);
        color: #000;
    }
    
    .segment-gold {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
        color: #000;
    }
    

    
    /* Métricas modernas */
    .metric-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Formulário moderno */
    .stSelectbox, .stNumberInput, .stSlider {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: 2px solid rgba(102, 126, 234, 0.2);
    }
    
    .stSelectbox:focus, .stNumberInput:focus, .stSlider:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
    

    
    /* Footer moderno */
    .footer {
        text-align: center;
        padding: 2rem;
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .header-title {
            font-size: 2rem;
        }
        
        .card {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header moderno
st.markdown("""
<div class="header-container">
    <div class="header-title">🎯 Classificador de Segmento de Vendas</div>
    <div class="header-subtitle">Análise inteligente para classificação de clientes em diferentes segmentos de mercado</div>
</div>
""", unsafe_allow_html=True)

# Carregar o modelo
@st.cache_resource
def load_model():
    try:
        modelo = joblib.load('./models/modelo_classificacao_decision_tree.pkl')
        return modelo
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        st.info("Verifique se o arquivo do modelo existe na pasta 'models/'")
        return None

modelo = load_model()

# Verificar se o modelo foi carregado
if modelo is None:
    st.error("❌ Não foi possível carregar o modelo. Verifique se o arquivo 'modelo_classificacao_decision_tree.pkl' existe na pasta 'models/'")
    st.stop()

# Sidebar moderno com informações
with st.sidebar:
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.95); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
        <h3 style="color: #667eea; margin-bottom: 1rem;">ℹ️ Sobre o Projeto</h3>
        <p style="font-size: 0.9rem; line-height: 1.6;">
        Este classificador utiliza um modelo de <strong>Árvore de Decisão</strong> treinado para categorizar empresas em 4 segmentos:
        </p>
        <ul style="font-size: 0.9rem; line-height: 1.8;">
            <li>🟡 <strong>Starter</strong>: Empresas iniciantes</li>
            <li>🟤 <strong>Bronze</strong>: Empresas em crescimento</li>
            <li>⚪ <strong>Silver</strong>: Empresas estabelecidas</li>
            <li>🟡 <strong>Gold</strong>: Empresas premium</li>
        </ul>
        <p style="font-size: 0.9rem; margin-top: 1rem;">
        <strong>Acurácia do modelo</strong>: ~47%
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.95); padding: 1.5rem; border-radius: 15px;">
        <h3 style="color: #667eea; margin-bottom: 1rem;">📈 Variáveis Analisadas</h3>
        <ul style="font-size: 0.9rem; line-height: 1.8;">
            <li>🏢 Atividade Econômica</li>
            <li>💰 Faturamento Mensal</li>
            <li>👥 Número de Funcionários</li>
            <li>📍 Localização</li>
            <li>📅 Idade da Empresa</li>
            <li>💡 Nível de Inovação</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

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
    st.markdown("""
    <div class="card">
        <h2 style="color: #667eea; margin-bottom: 1.5rem;">📝 Dados da Empresa</h2>
    """, unsafe_allow_html=True)
    
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
    
    st.markdown("</div>", unsafe_allow_html=True)

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
            st.markdown("""
            <div class="card">
                <h3 style="color: #667eea; text-align: center; margin-bottom: 1.5rem;">🎯 Segmento Classificado</h3>
            """, unsafe_allow_html=True)
            
            # Cores para cada segmento
            cores = {
                'Starter': '#FFD700',
                'Bronze': '#CD7F32', 
                'Silver': '#C0C0C0',
                'Gold': '#FFD700'
            }
            
            # Exibir resultado com estilo moderno
            st.markdown(f"""
            <div class="segment-badge segment-{predicao.lower()}">
                {predicao}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col_result2:
            st.markdown("""
            <div class="card">
                <h3 style="color: #667eea; margin-bottom: 1.5rem;">📊 Probabilidades por Segmento</h3>
            """, unsafe_allow_html=True)
            
            # Criar gráfico de barras moderno
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
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(size=14),
                title_font_size=18
            )
            
            fig.update_traces(
                textposition='outside',
                marker_line_color='rgba(255,255,255,0.8)',
                marker_line_width=2
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Detalhes da análise
        st.markdown("---")
        st.markdown("""
        <div class="card">
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">📋 Resumo da Análise</h3>
        """, unsafe_allow_html=True)
        
        col_detail1, col_detail2, col_detail3 = st.columns(3)
        
        with col_detail1:
            st.markdown(f"""
            <div class="metric-container">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">💰 Faturamento Mensal</h4>
                <p style="font-size: 1.5rem; font-weight: bold; color: #333;">R$ {faturamento_mensal:,.2f}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-container">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">👥 Funcionários</h4>
                <p style="font-size: 1.5rem; font-weight: bold; color: #333;">{numero_funcionarios}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_detail2:
            st.markdown(f"""
            <div class="metric-container">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">📅 Idade da Empresa</h4>
                <p style="font-size: 1.5rem; font-weight: bold; color: #333;">{idade} anos</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-container">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">💡 Nível de Inovação</h4>
                <p style="font-size: 1.5rem; font-weight: bold; color: #333;">{inovacao}/10</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_detail3:
            st.markdown(f"""
            <div class="metric-container">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">🏢 Atividade</h4>
                <p style="font-size: 1.5rem; font-weight: bold; color: #333;">{atividade_economica}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-container">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">📍 Localização</h4>
                <p style="font-size: 1.5rem; font-weight: bold; color: #333;">{localizacao}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Gráfico de radar para visualizar características
        st.markdown("---")
        st.markdown("""
        <div class="card">
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">📈 Perfil da Empresa</h3>
        """, unsafe_allow_html=True)
        
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
                    range=[0, 1],
                    tickfont=dict(size=12),
                    gridcolor='rgba(102, 126, 234, 0.2)'
                ),
                angularaxis=dict(
                    tickfont=dict(size=14, color='#333')
                ),
                bgcolor='rgba(255, 255, 255, 0.8)'
            ),
            showlegend=False,
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# Footer moderno
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>🚀 Desenvolvido com ❤️ usando Streamlit | 🤖 Modelo de Machine Learning: Árvore de Decisão</p>
    <p style="font-size: 0.8rem; margin-top: 0.5rem;">© 2024 Classificador de Segmento de Vendas</p>
</div>
""", unsafe_allow_html=True) 