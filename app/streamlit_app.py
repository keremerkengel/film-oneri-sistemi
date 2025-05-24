import pandas as pd
import streamlit as st
import requests
import re

# Sayfa ayarları (ilk Streamlit komutu olmak zorunda)
st.set_page_config(page_title="CineMatch", layout="centered")

# Font Awesome CSS (ikon desteği)
st.markdown(
    "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' integrity='sha512-p1CmFqQM1F0X8vKqR87gnX1bECvSeXSOaGp1pDdc6+lAL+j+2+L1nbzoZva12C/Ll+MZ3CkC1af+K8l+0uNfUg==' crossorigin='anonymous' referrerpolicy='no-referrer'/>",
    unsafe_allow_html=True
)

# Başlık
st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='margin-bottom: 0.2rem;'>CineMatch</h1>
        <p style='font-size: 1.1rem; color: gray;'>Bu uygulama, seçtiğiniz filme benzeyen yapımları MovieLens verisi üzerinden analiz ederek önerir.</p>
    </div>
""", unsafe_allow_html=True)

# API Anahtarı
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]

# Veri yükleme
@st.cache_resource
def load_data():
    ratings = pd.read_csv(
        "../data/ratings.dat", sep="::", engine="python",
        names=["user_id", "movie_id", "rating", "timestamp"],
        encoding="latin-1"
    )
    movies = pd.read_csv(
        "../data/movies.dat", sep="::", engine="python",
        names=["movie_id", "title", "genres"],
        encoding="latin-1"
    )
    df = pd.merge(ratings, movies, on="movie_id")
    counts = df["title"].value_counts()
    popular = counts[counts >= 50].index
    return df[df["title"].isin(popular)]

# Benzerlik matrisi oluştur
@st.cache_resource
def build_similarity(df):
    matrix = df.pivot_table(index="user_id", columns="title", values="rating")
    return matrix.corr(method="pearson", min_periods=30)

# Film listesi
@st.cache_resource
def movie_list(df):
    return sorted(df["title"].unique())

# Poster çekme fonksiyonu
def get_poster(title):
    match = re.match(r"^(.*?)(?:\s*\(\d{4}\))?$", title)
    clean = match.group(1).strip() if match else title
    try:
        res = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={"api_key": TMDB_API_KEY, "query": clean, "include_adult": False}
        )
        results = res.json().get("results", [])
        for item in results:
            if item.get("poster_path"):
                return f"https://image.tmdb.org/t/p/w500{item['poster_path']}"
    except:
        pass
    return None

# Öneri fonksiyonu
def recommend(title, sim_matrix, n=5):
    if title not in sim_matrix:
        return pd.Series(dtype=float)
    sims = sim_matrix[title].dropna().sort_values(ascending=False)
    return sims.iloc[1:n+1]

# Veriyi yükle
with st.spinner("Veriler yükleniyor..."):
    df = load_data()

# Benzerlik matrisini oluştur
with st.spinner("Benzerlik hesaplanıyor..."):
    sim = build_similarity(df)

titles = movie_list(df)

# Kullanıcı seçimi
st.markdown("### Film Seçimi")
selected = st.selectbox("", titles)
count = st.slider("Öneri sayısı", min_value=3, max_value=15, value=5)

# Önerileri göster
if st.button("Önerileri Göster", key="rec_button"):
    recs = recommend(selected, sim, count)
    if recs.empty:
        st.warning("Öneri bulunamadı.")
    else:
        st.markdown(f"### '{selected}' için önerilen filmler")
        for idx, (movie, score) in enumerate(recs.items(), start=1):
            c1, c2 = st.columns([1, 4])
            with c1:
                url = get_poster(movie)
                if url:
                    st.image(url, use_container_width=True)
                else:
                    st.write("Poster bulunamadı")
            with c2:
                st.markdown(f"<div style='font-size:1.1rem; font-weight:600;'>{idx}. {movie}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='color:gray;'>Benzerlik: {score * 100:.1f}%</div>", unsafe_allow_html=True)

# Alt bilgi
st.markdown("<hr style='margin-top:2rem; margin-bottom:1rem;'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:0.85rem; color:gray;'>Geliştirici: Kerem Erkengel</p>",
    unsafe_allow_html=True
)
