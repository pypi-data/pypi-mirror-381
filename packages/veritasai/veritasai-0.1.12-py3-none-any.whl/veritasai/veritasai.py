import json
from .claim_extractor import claim_extractor
from .claim_verifier import claim_verifier
from .evidence_retriever import evidence_retriever
class veritasai:
    def __init__(self):
        self.ce = claim_extractor()
        self.cv = claim_verifier()
        self.er = evidence_retriever()
    def extract_claims(self,reports,knowledgebase,top_n=5,score_function=evidence_retriever.cos_sim2,score_limit=0.7):
        for report in reports:
            text_out, claims = self.ce.extract_claims(report)
            hits = self.er.evidence_search(claims, knowledgebase, top_n,score_function,score_limit)
            fact_check=[]
            for i in range(len(claims)):
                sentences=[]
                for hit in hits[i]:
                    sentences.append(hit["sentence"])
                raw, parsed = self.cv.verify_claim(claims[i],sentences)
                fact_check.append({"claim":claims[i], "evidence":sentences, "labels":parsed})
        return fact_check
