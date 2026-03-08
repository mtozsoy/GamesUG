import os 
import json
from groq import Groq

class LLMAnalyzer:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

        self.model = "llama-3.1-8b-instant"

    def extract_tags(self, user_profile_text: str) -> list:
        """Kullanıcı metnini analiz edip Steam oyun etiketlerini döndürür."""
        
        # LLM'e tam olarak ne yapması gerektiğini anlattığımız Prompt
        prompt = f"""
        Sen bir oyuncu psikolojisi ve oyun eşleştirme uzmanısın. 
        Aşağıdaki kullanıcı profilini analiz et ve bu kişiye en uygun olabilecek 5 standart Steam oyun etiketini (İngilizce olarak) belirle.
        Sadece etiketlerin olduğu bir JSON dizisi (array) döndür. Başka hiçbir açıklama yapma, sohbet etme.
        Örnek çıktı: ["FPS", "Multiplayer", "Tactical", "Action", "Co-op"]

        Kullanıcı Profili: {user_profile_text}
        """

        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Sadece JSON formatında bir liste döndüren bir asistansın."},
                    {"role": "user", "content": prompt}
                ],
                model=self.model,
                temperature=0.3, # Daha tutarlı ve net cevaplar için yaratıcılığı biraz kısıyoruz
            )

            # API'den gelen string formatındaki listeyi gerçek bir Python listesine çeviriyoruz
            result_text = response.choices[0].message.content
            tags = json.loads(result_text)
            return tags
            
        except Exception as e:
            print(f"Groq API Hatası veya Format Uymazlığı: {e}")
            # Eğer API çökerse veya LLM saçmalarsa, sistemin patlamaması için varsayılan etiketler dönüyoruz
            return ["Action", "Adventure", "Singleplayer"]
