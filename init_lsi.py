import jieba
from gensim import corpora, models,similarities
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)

text_list = []

r_file = open('review.txt','r')
count = 0
for line in r_file:
	list = line.split('\t')
	if len(list) < 16 :
		continue

	print(count)
	count += 1
	content = list[14]
	text = jieba.cut_for_search(content)
	text_list.append(text)
r_file.close()

dictionary = corpora.Dictionary(text_list)
dictionary.save('review.dictionary')
corpus = [dictionary.doc2bow(text) for text in text_list]
corpora.MmCorpus('review.mm', corpus)
lsi_model = models.LsiModel(corpus,id2word=dictionary, num_topics = 2)
documents = lsi_model[corpus]
index = similarities.Similarity(documents)
index.save('review.index')