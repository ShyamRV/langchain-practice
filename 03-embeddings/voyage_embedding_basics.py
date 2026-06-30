import voyageai
from dotenv import load_dotenv

load_dotenv()

vo = voyageai.Client()

result = vo.embed(
    ["Delhi is the capital of India"],
    model="voyage-4-lite",      # <-- supported
    input_type="query",
)

print(result.embeddings[0])
print(len(result.embeddings[0]))