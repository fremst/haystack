import sys
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes.retriever import EmbeddingRetriever
# from 구문 변경되어 수정함

if __name__ == '__main__':

    possible_resources = ['articles', 'papers', 'patents']

    if len(sys.argv) < 2:
        print('provide resource name')
        print(f'ex) python3 update_embedding.py {possible_resources[0]}')
        exit(1)
    resource = sys.argv[1]

    if not (resource in ['articles', 'papers', 'patents']):
        print(f'wrong resource name - possible resource names: {possible_resources}')
        exit(1)

    port = 9200
    if resource == 'papers':
        port = 9201
    elif resource == 'patents':
        port = 9202

    document_store = ElasticsearchDocumentStore(
        host="localhost",
        port=port
    )
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1",
        model_format="sentence_transformers",
        top_k=5
    )
    document_store.update_embeddings(retriever)
    print('All Done')
