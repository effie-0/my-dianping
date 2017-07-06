import jieba
from collections import defaultdict
from gensim import corpora, models,similarities
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)

text_list = []

r_file = open('review.txt','r')
for line in r_file:
	list = line.split('\t')
	if len(list) < 16 :
		continue

	content = list[14]
	text = jieba.cut_for_search(content)
	text_list.append(text)
r_file.close()

frequency = defaultdict(int)
for text in text_list:
	for token in text:
         frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in text_list]

#print("/".join(text_list[0]))
dictionary = corpora.Dictionary(text_list)
dictionary.save('review.dictionary')

print('************')
#print(dictionary)
corpus = [dictionary.doc2bow(text) for text in text_list]
#print(corpus)
#print(list(corpus))
corpora.MmCorpus.serialize('review.mm', corpus)
lsi_model = models.LsiModel(corpus,id2word=dictionary, num_topics = 400)
lsi_model.save('review.lsi')
documents = lsi_model[corpus]
print(documents)
index = similarities.Similarity(documents, num_features = 50000)
index.save('review.index')