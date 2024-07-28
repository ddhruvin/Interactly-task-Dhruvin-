from flask import Flask, request, render_template
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["Indirectly_video"]  # Replace with your database name
collection = db["Condidate_data"]  # Replace with your collection name

def get_texts_from_db():
    # Retrieve all documents from the collection
    cursor = collection.find({})
    texts = []
    for document in cursor:
        texts.append({
            "Name": document.get("Name"),
            "Contact Details": document.get("Contact Details"),
            "Location": document.get("Location"),
            "Job Skills": document.get("Job Skills"),
            "Experience": str(document.get("Experience(in years)", "")),
            "Projects": document.get("Projects"),
            "Comments": document.get("Comments")
        })
    return texts

@app.route('/')
def home():
    return render_template('index.html')  # Corrected

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    texts = get_texts_from_db()
    top_profiles = find_top_profiles(prompt, texts)
    return render_template('index.html', prompt=prompt, top_profiles=top_profiles)

def find_top_profiles(prompt, texts):
    # Create a list of job descriptions
    job_descriptions = [prompt]
    profiles = []
    for text in texts:
        job_description = f"{text['Job Skills']} {text['Projects']} {text['Comments']}"
        profiles.append((text, job_description))

    # Extract the job descriptions and the corresponding profiles
    descriptions = [desc for _, desc in profiles]
    
    # Use TF-IDF Vectorizer to convert text to numerical data
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(job_descriptions + descriptions)

    # Calculate cosine similarity between the job description and profiles
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Get top 10 profiles based on cosine similarity
    top_indices = cosine_sim.argsort()[-10:][::-1]
    top_profiles = [profiles[i][0] for i in top_indices]

    return top_profiles

if __name__ == '__main__':
    app.run(debug=True)
