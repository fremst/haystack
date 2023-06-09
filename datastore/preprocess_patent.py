import pickle
import json
import os
from haystack.nodes.preprocessor import PreProcessor

# from 구문 변경되어 수정함
# PreProcessor import 시 오류 발생하여 아래 파일 임의로 수정함. 자세한 내용은 하단에 따로 작성
# /haystack/nodes/prompt/invocation_layer/handlers.py

if __name__ == '__main__':

    resource = 'patent'
    data_file = f'./data/biomimicry-{resource}.dat'

    if not os.path.exists(data_file):
        print(f"'{data_file}' not exists")
        exit(1)

    ids = []
    doc_dicts = []

    with open(data_file, 'r') as f:
        for row in f:
            item = json.loads(row)

            if item['abstract'] is None:
                continue

            ids.append(item['id'])
            doc_dicts.append(
                {"content": item['abstract'],
                 "meta": {
                     "publicationNumber": item['publicationNumber'],
                     "submitDate": item['submitDate'],
                     "grantDate": item['grantDate'],
                     "url": item['url'],
                     "title": item['title'],
                     "author": item['author'],
                     "count": item['count'],
                     "heroOption": item['heroOption'],
                     "superheroOption": item['superheroOption'],
                     "imageUrl": item['imageUrl'],
                     "patentSubclasses": item['patentSubclasses'],
                     "taxa": item['taxa']
                 }
                 }
            )

    # print(ids)
    print(doc_dicts[0])

    processor = PreProcessor(split_by='word',
                             split_length=2000,
                             split_respect_sentence_boundary=True)

    docs = processor.process(doc_dicts)

    with open(f"{resource}_ids.pickle", 'wb') as f:
        pickle.dump(ids, f)

    with open(f"{resource}_docs.pickle", 'wb') as f:
        pickle.dump(docs, f)

    print(f'All Done: {len(ids)}')
