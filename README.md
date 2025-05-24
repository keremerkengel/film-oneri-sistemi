# 🎬 CineMatch - Film Öneri Sistemi

CineMatch, seçtiğiniz bir filme benzer içerikleri bulup öneren bir film tavsiye uygulamasıdır.  
Kullanıcı puanlamaları üzerinden benzerlik analizi yapar ve TMDb API üzerinden afiş görüntüleriyle birlikte öneri sunar.

## 🚀 Özellikler

- 🎯 MovieLens 1M veri seti ile içerik temelli öneri sistemi
- 🖼️ TMDb API üzerinden film posterleri
- 🧠 Pearson korelasyon tabanlı benzerlik analizi
- 🎛️ Film seçimi, öneri sayısı ayarı ve etkileşimli arayüz
- 🌐 Streamlit ile sade ve modern kullanıcı deneyimi

## 📸 Uygulama Görseli

![Uygulama Görseli](https://i.hizliresim.com/jdlup5d.png)

## 🌐 Canlı Demo

[🔗 Uygulamayı Aç (Streamlit Cloud)](https://film-oneri-sistemi-buvjrrymsriehytyedh4ih.streamlit.app/)

## 🛠️ Kullanılan Teknolojiler

- **Python** – Veri işleme ve modelleme
- **Streamlit** – Web arayüzü oluşturma
- **Pandas** – Veri manipülasyonu
- **TMDb API** – Film poster bilgileri
- **MovieLens Dataset** – Film derecelendirme verisi

## 📂 Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için:

```bash
# 1. Repoyu klonla
git clone https://github.com/keremerkengel/film-oneri-sistemi.git
cd film-oneri-sistemi

# 2. (İsteğe bağlı) Sanal ortam oluştur
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 3. Gereklilikleri yükle
pip install -r requirements.txt

# 4. API anahtarını secrets.toml dosyasına ekle
mkdir -p app/.streamlit
echo "TMDB_API_KEY = 'senin_api_keyin'" > app/.streamlit/secrets.toml

# 5. Uygulamayı başlat
streamlit run app/streamlit_app.py
```

## 📚 Kaynaklar

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [TMDb API](https://www.themoviedb.org/documentation/api)
- [Streamlit Belgeleri](https://docs.streamlit.io)

## 👤 Geliştirici

**Kerem Erkengel**  
[GitHub](https://github.com/keremerkengel)

---

> 💡 Bu proje eğitim, portfolyo ve kişisel kullanım amaçlıdır.  
> TMDb ve MovieLens lisanslarına tabidir.