import pickle
import pandas as pd
from haystack.nodes.preprocessor import PreProcessor
# from 구문 변경되어 수정함
# PreProcessor import 시 오류 발생하여 아래 파일 임의로 수정함. 자세한 내용은 하단에 따로 작성
# /haystack/nodes/prompt/invocation_layer/handlers.py
# import logging

if __name__ == '__main__':

    # logging.basicConfig(filename='write_documents.log',
    #                     level=logging.DEBUG,
    #                     format='%(asctime)s %(levelname)s: %(message)s')

    papers = pd.read_json('biomimicry-papers.json', lines=True)

    ids = papers.id.values
    abstract = papers.abstract.values
    title = papers.title.values
    journal_title = papers.journal_title.values
    publication_year = papers.publication_year.values
    doi = papers.doi.values

    dicts = [{'content': abstract,
              'meta': {'title': title,
                       'journal_title': journal_title,
                       'publication_year': publication_year,
                       'doi': doi}}
             for abstract, title, journal_title, publication_year, doi
             in zip(abstract, title, journal_title, publication_year, doi)]

    processor = PreProcessor(split_by='word',
                             split_length=300,
                             split_respect_sentence_boundary=True)

    docs = processor.process(dicts)

    with open("ids.pickle", 'wb') as f:
        pickle.dump(ids, f)

    with open("docs.pickle", 'wb') as f:
        pickle.dump(docs, f)

    print('All Done')
