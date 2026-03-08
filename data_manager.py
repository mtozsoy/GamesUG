import pandas as pd
import streamlit as st
import os

class DataManager:
    def __init__(self):
        # Yeni ve temiz veri setimizin adı
        self.file_path = "games.csv"

    @st.cache_data
    def load_and_clean_data(_self) -> pd.DataFrame:
        if not os.path.exists(_self.file_path):
            st.error(f"Kritik Hata: '{_self.file_path}' dosyası bulunamadı!")
            st.stop()

        # Veriyi okuyoruz
        df = pd.read_csv(_self.file_path, low_memory=False)
        
        # Yeni veri setindeki sütunlara göre seçim yapıyoruz
        gerekli_sutunlar = ['appid','name', 'genres', 'categories', 'developer', 'recommendations']
        
        # Sadece ihtiyacımız olan sütunları alıp boş verileri temizliyoruz
        temiz_df = df[gerekli_sutunlar].copy().dropna()
        
        # Motorumuzun alıştığı standart değişken isimlerine çeviriyoruz
        temiz_df.columns = ['appid', 'name', 'genres', 'popular_tags', 'developer', 'positive_reviews']
        
        # Sıralama yapabilmek için 'recommendations' sütununu gerçek sayılara çevir (Hatalıysa 0 yap)
        temiz_df['positive_reviews'] = pd.to_numeric(temiz_df['positive_reviews'], errors='coerce').fillna(0)
        
        return temiz_df