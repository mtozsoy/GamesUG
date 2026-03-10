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






# 🎮 GamesUG - AI-Powered Hybrid Game Recommendation Engine

GamesUG is an AI-powered recommendation engine that analyzes gaming preferences described in natural language to find the perfect matches among tens of thousands of games in the Steam database. 

Unlike standard filtering systems, GamesUG utilizes a **"Hybrid Scoring"** method by combining Large Language Models (LLM), Natural Language Processing (NLP), and Machine Learning algorithms.

## ✨ Features

* 🧠 **Smart Profile Analysis:** Powered by the Groq API (LLaMA 3), it understands text written in everyday language (e.g., *"I love teamwork and I'm looking for a military FPS"*) and converts it into standard Steam tags.
* ⚙️ **Hybrid Scoring Algorithm:** It doesn't just rely on tag similarity (*TF-IDF & Cosine Similarity*). It multiplies this similarity score by the number of *Positive Reviews* on Steam to highlight high-quality and popular AAA titles.
* 🎲 **Controlled Diversity (Serendipity):** To avoid getting stuck in a filter bubble, it randomly selects 5 games from an elite pool of the top 30 highest-scoring games, offering varied but consistently high-quality recommendations every time.
* 🎨 **Modern and Dynamic UI:** A sleek, "Gamer" themed interface built with Streamlit that dynamically fetches Steam cover images and provides direct store links.

## 🛠️ Tech Stack

* **Python 3.x**
* **Streamlit** (Frontend / Web UI)
* **Pandas & Scikit-learn** (Data Analysis, TF-IDF Vectorization, Cosine Similarity)
* **Groq API / LLaMA 3** (User Text Analysis and Tag Extraction)

## 🚀 Installation and Usage

To run this project locally, follow these steps:

**1. Clone the Repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/GamesUG-AI-Recommender.git](https://github.com/YOUR_USERNAME/GamesUG-AI-Recommender.git)
cd GamesUG-AI-Recommender
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set Up API Key:**
Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=gsk_your_api_key_here
```

**4. Run the Application:**
```bash
streamlit run app.py
```

## 📂 Project Architecture

* `app.py`: Main web interface and system orchestration.
* `data_manager.py`: Responsible for loading, cleaning, and preparing the Steam dataset for the AI engine.
* `llm_analyzer.py`: The Prompt Engineering layer that communicates with the Groq API to convert user text into JSON tags.
* `recommender.py`: The hybrid machine learning engine (TF-IDF + Cosine Similarity + Quality Multiplier).

## 👨‍💻 Developer

Developed to showcase AI, NLP, and Data Science capabilities.

* **Developer:** Mete
* Developed with love from Riga 🇱🇻
