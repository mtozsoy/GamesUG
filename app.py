import streamlit as st
import os
from dotenv import load_dotenv
from data_manager import DataManager
from recommender import GameRecommender
from llm_analyzer import LLMAnalyzer

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="GamesUG | AI Oyun Öneri Motoru",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ÖZEL CSS (Header'ı gizleme kodunu sildik ki yan menü butonu kaybolmasın!)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #00ffcc;
        background-color: transparent;
        color: #00ffcc;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #00ffcc;
        color: #000000;
        box-shadow: 0 0 10px #00ffcc;
    }
    </style>
""", unsafe_allow_html=True)

# 3. YAN MENÜ (SIDEBAR)
with st.sidebar:
    st.title("🎮 GamesUG")
    st.caption("Yapay Zeka Destekli Tavsiye Motoru")
    st.divider()
    
    st.markdown("### 👨‍💻 Geliştirici")
    st.info("**Yapay Zeka & Python Geliştiricisi**\n\n*Securencryptor ve GamesUG'nin Yaratıcısı*")
    st.markdown("[💼 LinkedIn Profilim](https://www.linkedin.com/in/meteozsoy)")
    st.markdown("[🐙 GitHub](https://github.com/mtozsoy)")
    
    st.divider()
    st.caption("Riga'dan sevgilerle geliştirildi 🇱🇻")

# 4. MOTORLARI BAŞLATMA VE API AYARLARI
@st.cache_resource(show_spinner=False)
def load_system():
    dm = DataManager()
    df = dm.load_and_clean_data()
    recommender = GameRecommender(df)
    recommender._prepare_matrix()
    return recommender

game_recommender = load_system()

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Kritik Hata: .env dosyası okunamadı veya GROQ_API_KEY bulunamadı!")
    st.stop()

profile_analyzer = LLMAnalyzer(api_key=api_key)

# 5. ANA EKRAN TASARIMI VE İŞLEYİŞ
st.title("Sana Özel Oyun Bulucu")
st.markdown("Nasıl bir oyuncusun? Ne tarz oyunlar arıyorsun? Bana biraz kendinden bahset, yapay zeka senin için devasa Steam kütüphanesini tarayıp nokta atışı oyunları bulsun.")

user_input = st.text_area("✍️ Oyun Zevkini Anlat:", height=120, placeholder="Örn: Lider ruhluyum, takım çalışmasına önem veririm, hype şarkılar eşliğinde aksiyona girmeyi severim...")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit_button = st.button("🚀 Yapay Zeka ile Oyun Öner!", use_container_width=True)

if submit_button and user_input:
    with st.spinner("🧠 Profilin analiz ediliyor ve Steam veritabanı taranıyor..."):
        
        # LLM'den etiketleri alıyoruz (Senin dosyandaki extract_tags fonksiyonu)
        user_tags = profile_analyzer.extract_tags(user_input)
        st.success(f"**🏷️ Çıkarılan Oyun Profilin:** {', '.join(user_tags)}")
        
        # Etiketleri string yapıp motorumuza veriyoruz (küçük harfle başlayan game_recommender)
        tags_str = " ".join(user_tags)
        recommendations = game_recommender.get_recommendations(tags_str, top_n=5)
        
        if recommendations:
            st.markdown("---")
            st.subheader("🎯 GamesUG'nin Senin İçin Seçtikleri:")
            st.write("") 
            
            for idx, game in enumerate(recommendations, 1):
                with st.container():
                    img_col, info_col = st.columns([1, 3]) 
                    
                    with img_col:
                        image_url = f"https://cdn.akamai.steamstatic.com/steam/apps/{game['appid']}/header.jpg"
                        st.image(image_url, width='stretch')
                    
                    with info_col:
                        st.markdown(f"#### {idx}. {game['name']}")
                        st.write(f"🏢 **Geliştirici:** {game['developer']}")
                        st.write(f"⭐️ **{int(game['positive_reviews']):,}** Olumlu İnceleme")
                        
                        steam_link = f"https://store.steampowered.com/app/{game['appid']}/"
                        st.markdown(f"[**🛒 Steam Mağazasına Git**]({steam_link})")
                        
                st.markdown("<br>", unsafe_allow_html=True)