import torch
from sentence_transformers import SentenceTransformer, util
def dot_score(a, b):
    return util.dot_score(a, b)
def dot_score2(a, b):
    return torch.abs(util.dot_score(a,b))
def cos_sim(a, b):
    return util.cos_sim(a, b)
def cos_sim2(a, b):
    return torch.abs(util.cos_sim(a, b))
def evidance_search(query,corpus,top_n,score_function=cos_sim2,score_limit=0.7):
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
    corpus_embeddings = corpus_embeddings.to("cuda")
    corpus_embeddings = util.normalize_embeddings(corpus_embeddings)
    query_embeddings = embedder.encode(query, convert_to_tensor=True)
    query_embeddings = query_embeddings.to("cuda")
    query_embeddings = util.normalize_embeddings(query_embeddings)
    hits = util.semantic_search(query_embeddings, corpus_embeddings, score_function=dot_score2)
    data = []
    for i, hit in enumerate(hits):
        dat=[]
        for h in hit[0:top_n]:
            h["sentence"]=corpus[h["corpus_id"]]
            if h["score"]>score_limit:
                dat.append(h)
        data.append(dat)
    return data