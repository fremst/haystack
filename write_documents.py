import pickle
from haystack.document_stores import ElasticsearchDocumentStore
# from 구문 변경되어 수정함
# PreProcessor import 시 오류 발생하여 아래 파일 임의로 수정함. 자세한 내용은 하단에 따로 작성
# /haystack/nodes/prompt/invocation_layer/handlers.py
# import logging

if __name__ == '__main__':

    # logging.basicConfig(filename='write_documents.log',
    #                     level=logging.DEBUG,
    #                     format='%(asctime)s %(levelname)s: %(message)s')

    with open("ids.pickle","rb") as f:
        ids = pickle.load(f)
        
    with open("docs.pickle","rb") as f:
        docs = pickle.load(f)

    for id_, doc in zip(ids, docs):
        doc.id = id_

    document_store = ElasticsearchDocumentStore()
    document_store.delete_documents()
    document_store.write_documents(docs)  # TODO: _index 수동으로 설정. haystack rest API 설정 필요
    print('All Done')
