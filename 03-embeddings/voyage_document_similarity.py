import voyageai
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# Initialize Voyage client
vo = voyageai.Client()

documents = [
    "Geoffrey Hinton is widely regarded as one of the pioneers of deep learning. His work on neural networks and backpropagation has significantly influenced modern artificial intelligence research.",
    
    "Yann LeCun is the Chief AI Scientist at Meta and is known for developing convolutional neural networks (CNNs). His research has transformed the fields of computer vision and deep learning.",
    
    "Yoshua Bengio is a professor at the University of Montreal and a leading researcher in deep learning. His contributions to representation learning have advanced natural language processing and generative AI.",
    
    "Fei-Fei Li is a computer scientist best known for creating the ImageNet dataset, which accelerated breakthroughs in computer vision. She is also an advocate for human-centered artificial intelligence.",
    
    "Andrew Ng is an AI researcher, educator, and entrepreneur who has helped popularize machine learning through online education. He co-founded Google Brain and has contributed extensively to AI applications and education."
]

query = "Tell me about the scientist who created the ImageNet dataset."

# Embed documents
doc_embeddings = vo.embed(
    documents,
    model="voyage-4-lite",
    input_type="document"
).embeddings

# Embed query
query_embedding = vo.embed(
    [query],
    model="voyage-4-lite",
    input_type="query"
).embeddings[0]

# Calculate cosine similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Sort documents by similarity
ranked_results = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)

print("Top Matches:\n")

for index, score in ranked_results:
    print(f"Score: {score:.4f}")
    print(documents[index])
    print("-" * 80)