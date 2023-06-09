import sys
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes.retriever import EmbeddingRetriever
# from 구문 변경되어 수정함

if __name__ == '__main__':

    POSSIBLE_RESOURCES = ['article', 'paper', 'patent']

    if len(sys.argv) < 2:
        print('provide resource name')
        print(f'ex) python3 update_embedding.py {POSSIBLE_RESOURCES[0]}')
        exit(1)
    resource = sys.argv[1]

    if not (resource in POSSIBLE_RESOURCES):
        print(f'wrong resource name - possible resource names: {POSSIBLE_RESOURCES}')
        exit(1)

    document_store = ElasticsearchDocumentStore(
        host="localhost",
        port=9200,
        index=resource
    )
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1",
        model_format="sentence_transformers",
        # top_k=25
    )
    document_store.update_embeddings(retriever)
    print('All Done')
