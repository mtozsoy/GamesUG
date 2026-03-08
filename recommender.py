import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class GameRecommender:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.reset_index(drop=True)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None

    def _prepare_matrix(self):
        genres = self.df['genres'].fillna('')
        tags = self.df['popular_tags'].fillna('')
        combined_features = genres + " " + tags
        self.tfidf_matrix = self.vectorizer.fit_transform(combined_features)

    def get_recommendations(self, user_tags: str, top_n: int = 5) -> list:
        if self.tfidf_matrix is None:
            self._prepare_matrix()

        # 1. Benzerlik skorlarını hesapla
        user_vector = self.vectorizer.transform([user_tags])
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix)[0]

        # 2. Tüm skorları ana tablomuza matematiksel bir sütun olarak ekliyoruz
        self.df['similarity'] = similarity_scores
        
        # 3. Bizim etiketlerimizle hiç alakası olmayanları (Skoru %1'in altında olanları) ele
        matched_df = self.df[self.df['similarity'] > 0.01].copy()

        if matched_df.empty:
            return []

        # 4. İŞTE SİHRİN OLDUĞU YER: Hibrit Skor!
        matched_df['hybrid_score'] = matched_df['similarity'] * matched_df['positive_reviews']

        # 5. En iyi ilk 30 oyunu (Elitler Kulübü) seçiyoruz
        top_candidates = matched_df.sort_values(by='hybrid_score', ascending=False).head(30)

        # 6. Bu 30 harika oyunun içinden RASTGELE 5 tanesini çekiyoruz (Çeşitlilik için)
        # Eğer listede 5'ten az oyun varsa hata vermesin diye ufak bir kontrol ekliyoruz
        if len(top_candidates) > top_n:
            recommended_df = top_candidates.sample(n=top_n)
        else:
            recommended_df = top_candidates

        # Sonuçları arayüze gönder
        recommendations = recommended_df[['appid', 'name', 'developer', 'positive_reviews']].to_dict('records')

        # Sonuçları arayüze gönder
        
        
        return recommendations