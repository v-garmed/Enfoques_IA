from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documentos simulados
docs = [
    "La inteligencia artificial puede mejorar la medicina",
    "La visión artificial detecta objetos en imágenes",
    "Los algoritmos genéticos son parte de la IA",
    "La medicina moderna usa datos y tecnología"
]

# Consulta del usuario
consulta = "tecnología en medicina"

# Crear el vectorizador TF-IDF
vectorizador = TfidfVectorizer()

# Ajustar y transformar documentos
tfidf_docs = vectorizador.fit_transform(docs)

# Transformar la consulta
tfidf_query = vectorizador.transform([consulta])

# Calcular similitud coseno entre consulta y documentos
similaridades = cosine_similarity(tfidf_query, tfidf_docs)

# Mostrar documentos más relevantes
for idx in similaridades[0].argsort()[::-1]:
    print(f"Documento {idx + 1} (relevancia: {similaridades[0][idx]:.2f}): {docs[idx]}")
