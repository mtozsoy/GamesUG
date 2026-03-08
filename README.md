# 🎮 GamesUG - Yapay Zeka Destekli Hibrit Oyun Tavsiye Motoru

GamesUG, kullanıcıların doğal dilde anlattığı oyun zevklerini analiz ederek Steam veritabanındaki on binlerce oyun arasından en uygun olanları bulan, yapay zeka destekli bir tavsiye motorudur. 

Sıradan filtreleme sistemlerinin aksine GamesUG; Büyük Dil Modelleri (LLM), Doğal Dil İşleme (NLP) ve Makine Öğrenmesi algoritmalarını birleştirerek **"Hibrit Skorlama"** yöntemiyle çalışır.

## ✨ Özellikler

* 🧠 **Akıllı Profil Analizi:** Groq API (LLaMA 3) entegrasyonu sayesinde kullanıcının günlük dilde yazdığı metinleri (örn: *"Takım çalışmasını severim, askeri FPS arıyorum"*) anlar ve standart Steam etiketlerine dönüştürür.
* ⚙️ **Hibrit Skorlama Algoritması:** Sadece etiket benzerliğine (*TF-IDF & Cosine Similarity*) bakmakla kalmaz; bu benzerlik skorunu oyunun Steam'deki olumlu inceleme sayısıyla (*Positive Reviews*) çarparak yüksek kaliteli ve popüler AAA yapımları öne çıkarır.
* 🎲 **Kontrollü Çeşitlilik (Serendipity):** Tavsiye balonuna (filter bubble) sıkışmamak için, en yüksek puanlı 30 oyunluk elit havuzdan her seferinde rastgele 5 farklı oyun çekerek oyuncuya çeşitlilik sunar.
* 🎨 **Modern ve Dinamik Arayüz:** Streamlit ile tasarlanmış, Steam kapak fotoğraflarını anlık çeken ve doğrudan mağaza linkleri sunan "Gamer" temalı şık arayüz.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **Streamlit** (Frontend / Web Arayüzü)
* **Pandas & Scikit-learn** (Veri Analizi, TF-IDF Vektörizasyonu, Kosinüs Benzerliği)
* **Groq API / LLaMA 3** (Kullanıcı Metni Analizi ve Etiket Çıkarımı)

## 🚀 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

**1. Repoyu Klonlayın:**
```bash
git clone [https://github.com/KULLANICI_ADIN/GamesUG-AI-Recommender.git](https://github.com/KULLANICI_ADIN/GamesUG-AI-Recommender.git)
cd GamesUG-AI-Recommender
```

**2. Gerekli Kütüphaneleri Yükleyin:**
```bash
pip install -r requirements.txt
```

**3. API Anahtarını Ayarlayın:**
Projenin ana dizininde bir `.env` dosyası oluşturun ve Groq API anahtarınızı içine ekleyin:
```env
GROQ_API_KEY=gsk_sizin_api_anahtariniz_buraya
```

**4. Uygulamayı Başlatın:**
```bash
streamlit run app.py
```

## 📂 Proje Mimarisi

* `app.py`: Ana web arayüzü ve sistem orkestrasyonu.
* `data_manager.py`: Steam veri setinin yüklenmesi, temizlenmesi ve yapay zeka motoruna uygun hale getirilmesi.
* `llm_analyzer.py`: Groq API ile haberleşen ve kullanıcı metnini JSON etiketlerine çeviren Prompt Engineering katmanı.
* `recommender.py`: Hibrit makine öğrenmesi motoru (TF-IDF + Cosine Similarity + Kalite Çarpanı).

## 👨‍💻 Geliştirici

Bu proje, yapay zeka ve veri bilimi yeteneklerini sergilemek amacıyla geliştirilmiştir. 

* **Geliştirici:** Mete
* Riga'dan sevgilerle 🇱🇻
