import sys
import pickle
from haystack.document_stores import ElasticsearchDocumentStore
# from 구문 변경되어 수정함
# PreProcessor import 시 오류 발생하여 아래 파일 임의로 수정함. 자세한 내용은 하단에 따로 작성
# /haystack/nodes/prompt/invocation_layer/handlers.py
import logging

if __name__ == '__main__':

    logging.basicConfig(filename='write_documents.py.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')

    possible_resources = ['articles', 'papers', 'patents']

    if len(sys.argv) < 2:
        print('provide resource name')
        print(f'ex) python3 write_documents.py {possible_resources[0]}')
        exit(1)
    resource = sys.argv[1]

    if not (resource in ['articles', 'papers', 'patents']):
        print(f'wrong resource name - possible resource names: {possible_resources}')
        exit(1)

    with open(f"{resource}_ids.pickle", "rb") as f:
        ids = pickle.load(f)
        
    with open(f"{resource}_docs.pickle", "rb") as f:
        docs = pickle.load(f)

    for id_, doc in zip(ids, docs):
        doc.id = id_

    port = 9200
    if resource == 'papers':
        port = 9201
    elif resource == 'patents':
        port = 9202

    document_store = ElasticsearchDocumentStore(
        host="localhost",
        port=port
    )
    document_store.delete_documents()
    document_store.write_documents(docs)  # TODO: _index 수동으로 설정. haystack rest API 설정 필요
    print('All Done')
