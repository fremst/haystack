from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes.retriever import EmbeddingRetriever
# from 구문 변경되어 수정함
# import logging

if __name__ == '__main__':

    # logging.basicConfig(filename='update_embedding.log',
    #                     level=logging.DEBUG,
    #                     format='%(asctime)s %(levelname)s: %(message)s')

    document_store = ElasticsearchDocumentStore()
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1",
        model_format="sentence_transformers",
        top_k=5
    )
    document_store.update_embeddings(retriever)
    print('All Done')
