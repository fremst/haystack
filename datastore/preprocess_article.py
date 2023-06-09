import pickle
import json
import os
from haystack.nodes.preprocessor import PreProcessor

# from 구문 변경되어 수정함
# PreProcessor import 시 오류 발생하여 아래 파일 임의로 수정함. 자세한 내용은 하단에 따로 작성
# /haystack/nodes/prompt/invocation_layer/handlers.py

if __name__ == '__main__':

    resource = 'article'
    data_file = f'./data/biomimicry-{resource}.dat'

    if not os.path.exists(data_file):
        print(f"'{data_file}' not exists")
        exit(1)

    ids = []
    doc_dicts = []

    with open(data_file, 'r') as f:
        for row in f:
            item = json.loads(row)

            ids.append(item['id'])
            doc_dicts.append(
                {"content": next((description["contents"]
                                  for description in item["descriptions"] if description["language"] == "en"), None),
                 "meta": {
                     "imageUrl": item['imageUrl'],
                     "uuid": item['uuid'],
                     "creationDate": item['creationDate'],
                     "lastUpdateDate": item['lastUpdateDate'],
                     "count": item['count'],
                     "heroOption": item['heroOption'],
                     "superheroOption": item['superheroOption'],
                     "descriptions": item['descriptions']
                 }
                 }
            )

    # print(ids)
    print(doc_dicts)

    processor = PreProcessor(split_by='word',
                             split_length=2000,
                             split_respect_sentence_boundary=True)

    docs = processor.process(doc_dicts)

    with open(f"{resource}_ids.pickle", 'wb') as f:
        pickle.dump(ids, f)

    with open(f"{resource}_docs.pickle", 'wb') as f:
        pickle.dump(docs, f)

    print(f'All Done: {len(ids)}')
