
from langchain_classic.document_loaders import PyPDFDirectoryLoader
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct , VectorParams , Distance 
import groq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.schema.document import Document
from sentence_transformers import SentenceTransformer
import shutil
import os


def read_document():
    print("- reading documents ...")
    loader = PyPDFDirectoryLoader("./")
    docs = loader.load()
    documnets = ""
    for doc in docs:
        documnets += doc.page_content
    return documnets

def split_text(texts: str):
    print("- ready data for chunking ...")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n", ". ", " ", ""],   
        chunk_size=800,                            
        chunk_overlap=100,                         
        length_function=len,
        is_separator_regex=False
    )
    return text_splitter.split_text(text=texts)


class Embedding_model:
    
    def __init__(self ,chunks:list[str]):
        print("- Embedding chunks ...")
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.vectores = self.embedder.encode(chunks)
        
    def return_vectors_data(self):
        return self.vectores

    def return_vectors_size(self):
        return len(self.vectores)

    


class VectoreDB :
    def __init__(self ,path="./vector_db"):
        print("- Run Vectore Database ...")
        if os.path.exists(path):
            shutil.rmtree(path)
            print("folder is removed")
        self.client = QdrantClient(path=path)
        print("--new folder is created")

    def create_collection(self, name : str  ):
        self.collection_name = name
        print("- Create Collection ...")
        self.client.create_collection(collection_name=name , vectors_config=VectorParams(size=384 , distance=Distance.COSINE ) )
        print("--collection is created")
    
    def insert_data_points(self, embedder_model: Embedding_model, collection_name: str , chunks ):
        print("- Inserting Datas ...")
        vectors = embedder_model.return_vectors_data()
        points = [
            PointStruct(
                id=i,
                vector=vectors[i],
                payload={"content": chunks[i] }   # or better: the actual text
            )
            for i in range(len(vectors))
        ]

        self.client.upsert(
            collection_name=collection_name,
            points=points,          # ← must be a list
            wait=True
        )

    def search_query(self, query: str, embedder_model: Embedding_model):
        # Encode the query using the same model
        query_vector = embedder_model.embedder.encode(query).tolist()

        result = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=1
        )

        for point in result.points:
            print( f"- {point.payload["content"]}")
            print("\n")
        

def main():
    print("Running Rag System ...")
    documents = read_document()
    chunks = split_text(documents)
    embedder_model =  Embedding_model(chunks=chunks)
    vectore_db = VectoreDB()
    vectore_db.create_collection("datas")
    vectore_db.insert_data_points(embedder_model, "datas", chunks)
    print("Succesful \n Hi :)")

    while(True):
        query = input("ask me questiona : ")
        vectore_db.search_query(query , embedder_model)



if __name__=="__main__":
    
    main()


