# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Basic word2vec example."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import math
import os
import random
from tempfile import gettempdir
import zipfile

import numpy as np
import pandas as pd
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

# # Step 1: Download the data.
# url = 'http://mattmahoney.net/dc/'


# # pylint: disable=redefined-outer-name
# def maybe_download(filename, expected_bytes):
#   """Download a file if not present, and make sure it's the right size."""
#   local_filename = os.path.join(gettempdir(), filename)
#   if not os.path.exists(local_filename):
#     local_filename, _ = urllib.request.urlretrieve(url + filename,
#                                                    local_filename)
#   statinfo = os.stat(local_filename)
#   if statinfo.st_size == expected_bytes:
#     print('Found and verified', filename)
#   else:
#     print(statinfo.st_size)
#     raise Exception('Failed to verify ' + local_filename +
#                     '. Can you get to it with a browser?')
#   return local_filename


# filename = maybe_download('text8.zip', 31344016)


# # Read the data into a list of strings.
# def read_data(filename):
#   """Extract the first file enclosed in a zip file as a list of words."""
#   with zipfile.ZipFile(filename) as f:
#     data = tf.compat.as_str(f.read(f.namelist()[0])).split()
#   return data

filename = "../data/raw/postbatch1.xlsx"

# # Step 1: Read the data into a list of strings.
def read_data(filename):
  df = pd.read_excel(filename)
  text = df['postText'].values # numpy.ndarray type
  data = tf.compat.as_str("".join(text)).split()
  toDelete = []
  for stringIndex in xrange(len(data)):
	string = data[stringIndex]
	if string.isdigit(): 
		toDelete.append(stringIndex)
		continue
	elif not string:
		toDelete.append(stringIndex)
		continue
  data = np.delete(data, toDelete).tolist()
  return data
  # data = "ebddtiayana elites vip athletes fun big booty fun rubs fetish 2egentleman and master his craft can do better than any fem 3pexotic thickness young freaky tight 2ohow many licks takes 2gtomorrow downtown blessing animals pet owners come join usflappers late night no blender bar show open mic wed sat 11 eopmsee craig shoemaker lovemaster live flapperscuban petes latin night club new years eve 2013 brazilian carnaval masquerade ballearth day festival bike ride city hall sat apr zoth lam ipmdowntown culver city third wednesday neighborhood step out spring happy hourdreamgirlsspoken funk not not not has not have not no joke showearthday 2013 inglewood city hall sat apr ieth iiam epmznd annual earth strong festival konshens richie spice warrior king dee lovaboyoperaworks presents arias motionhalloween event sea mountain nude lifestyle couples resort las vegas and palm springszouk masquerade ball 2013 zouk dallas monday 31 december 201zno tricks just treats gorgeous white girl fundeep tissue massage stress relief russian girl waiting you great relaxationmassage latina hottestsexy hot curvy latinas best townu r model availablesea salt and air heavenly massage upscale brunette please call advancebest place latinas 323973609zsexy young pretty asian massage new management 405 fwy exit artesia blvd torranceupscale redbone beauty young fun sweet slim and curvy sensationgrand opening grand opening grand opening 310 679 888bsexy asian bare 626297364psweet fiona petite asain torrance san pedro private incallandrea naughty girl next door private homenuru busty otties latina come babes call now 562 351 2765 we open lateholiday special best touch best time 702 502 874psweet taiwanese girl out your placegood massage shemale available now new new 657 201 075ohands experiencemassage special 80 562 528 490pmy last day new hot asian petitebest back babyhey let dim lights and soft music all you need and than some more 562 565 341lmature lovely petite and skilledhottest college aged latinas blue sky aroma pick your girl 562 968 988gpure bliss massage incall northridge independent tall native american euro mixloving sensual mature lady 4gbare asian hot 626342864enuru massage exotic dominican mixlet me your morning afternoon delight sweet brunette come youauthentic vixan latina highly well reviewedhottest world here isabelmature masseuse sailboat massagereal photos up early hot sexy and ready sheryl best rubdown sfv 2oohrblessed curves thighs thunder hips heavenme latina beauty 100 independent hotel home out call massageindian mix delight bubble ooty ioo realupscale redbone beauty young fun sweet slim and curvy sensationiippp 1992 nissan 3oozx import classic los angeles caaps forks classzi 999 stop call us more information our 2012 bmw series only 58 862 milesii 995 impressive 2016 toyota corolla only 32 875 mileszg 000 2010 toyota tundrapps look just came 2014 nissan maxima 82 239 mileszi 999 2013 bmw 3zbiig 495 impressive 2013 infiniti gel sedan only 49 463 mileszzooo 1958 ford fioo classic truck los angeles calpoo 2006 bmw 750 sedan marina del rey ca"
  # return tf.compat.as_str(data).split()

vocabulary = read_data(filename)
print('Data size', len(vocabulary))

# Step 2: Build the dictionary and replace rare words with UNK token.
vocabulary_size = 5000


def build_dataset(words, n_words):
  """Process raw inputs into a dataset."""
  count = [['UNK', -1]]
  count.extend(collections.Counter(words).most_common(n_words - 1))
  dictionary = dict()
  for word, _ in count:
	dictionary[word] = len(dictionary)
  data = list()
  unk_count = 0
  for word in words:
	index = dictionary.get(word, 0)
	if index == 0:  # dictionary['UNK']
	  unk_count += 1
	data.append(index)
  count[0][1] = unk_count
  reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
  return data, count, dictionary, reversed_dictionary

# Filling 4 global variables:
# data - list of codes (integers from 0 to vocabulary_size-1).
#   This is the original text but words are replaced by their codes
# count - map of words(strings) to count of occurrences
# dictionary - map of words(strings) to their codes(integers)
# reverse_dictionary - maps codes(integers) to words(strings)
data, count, dictionary, reverse_dictionary = build_dataset(vocabulary,
															vocabulary_size)
del vocabulary  # Hint to reduce memory.
print('Most common words (+UNK)', count[:5])
print('Sample data', data[:10], [reverse_dictionary[i] for i in data[:10]])

data_index = 0

# Step 3: Function to generate a training batch for the skip-gram model.
def generate_batch(batch_size, num_skips, skip_window):
  global data_index
  assert batch_size % num_skips == 0
  assert num_skips <= 2 * skip_window
  batch = np.ndarray(shape=(batch_size), dtype=np.int32)
  labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
  span = 2 * skip_window + 1  # [ skip_window target skip_window ]
  buffer = collections.deque(maxlen=span)
  if data_index + span > len(data):
	data_index = 0
  buffer.extend(data[data_index:data_index + span])
  data_index += span
  for i in range(batch_size // num_skips):
	context_words = [w for w in range(span) if w != skip_window]
	words_to_use = random.sample(context_words, num_skips)
	for j, context_word in e numerate(words_to_use):
	  batch[i * num_skips + j] = buffer[skip_window]
	  labels[i * num_skips + j, 0] = buffer[context_word]
	if data_index == len(data):
	  # buffer[:] = data[:span]
	  for word in data[:span]:
   		buffer.append(data)
	  data_index = span
	else:
	  buffer.append(data[data_index])
	  data_index += 1
  # Backtrack a little bit to avoid skipping words in the end of a batch
  data_index = (data_index + len(data) - span) % len(data)
  return batch, labels

batch, labels = generate_batch(batch_size=8, num_skips=2, skip_window=1)
for i in range(8):
  print(batch[i], reverse_dictionary[batch[i]],
		'->', labels[i, 0], reverse_dictionary[labels[i, 0]])

# Step 4: Build and train a skip-gram model.

batch_size = 128
embedding_size = 128  # Dimension of the embedding vector.
skip_window = 1       # How many words to consider left and right.
num_skips = 2         # How many times to reuse an input to generate a label.
num_sampled = 64      # Number of negative examples to sample.

# We pick a random validation set to sample nearest neighbors. Here we limit the
# validation samples to the words that have a low numeric ID, which by
# construction are also the most frequent. These 3 variables are used only for
# displaying model accuracy, they don't affect calculation.
valid_size = 16     # Random set of words to evaluate similarity on.
valid_window = 100  # Only pick dev samples in the head of the distribution.
valid_examples = np.random.choice(valid_window, valid_size, replace=False)


graph = tf.Graph()

with graph.as_default():

  # Input data.
  train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
  train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
  valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

  # Ops and variables pinned to the CPU because of missing GPU implementation
  with tf.device('/cpu:0'):
	# Look up embeddings for inputs.
	embeddings = tf.Variable(
		tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
	embed = tf.nn.embedding_lookup(embeddings, train_inputs)

	# Construct the variables for the NCE loss
	nce_weights = tf.Variable(
		tf.truncated_normal([vocabulary_size, embedding_size],
							stddev=1.0 / math.sqrt(embedding_size)))
	nce_biases = tf.Variable(tf.zeros([vocabulary_size]))

  # Compute the average NCE loss for the batch.
  # tf.nce_loss automatically draws a new sample of the negative labels each
  # time we evaluate the loss.
  # Explanation of the meaning of NCE loss:
  #   http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
  loss = tf.reduce_mean(
	  tf.nn.nce_loss(weights=nce_weights,
					 biases=nce_biases,
					 labels=train_labels,
					 inputs=embed,
					 num_sampled=num_sampled,
					 num_classes=vocabulary_size))

  # Construct the SGD optimizer using a learning rate of 1.0.
  optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

  # Compute the cosine similarity between minibatch examples and all embeddings.
  norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True))
  normalized_embeddings = embeddings / norm
  valid_embeddings = tf.nn.embedding_lookup(
	  normalized_embeddings, valid_dataset)
  similarity = tf.matmul(
	  valid_embeddings, normalized_embeddings, transpose_b=True)

  # Add variable initializer.
  init = tf.global_variables_initializer()

# Step 5: Begin training.
num_steps = 100001

with tf.Session(graph=graph) as session:
  # We must initialize all variables before we use them.
  init.run()
  print('Initialized')

  average_loss = 0
  for step in xrange(num_steps):
	batch_inputs, batch_labels = generate_batch(
		batch_size, num_skips, skip_window)
	feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}

	# We perform one update step by evaluating the optimizer op (including it
	# in the list of returned values for session.run()
	_, loss_val = session.run([optimizer, loss], feed_dict=feed_dict)
	average_loss += loss_val

	if step % 2000 == 0:
	  if step > 0:
		average_loss /= 2000
	  # The average loss is an estimate of the loss over the last 2000 batches.
	  print('Average loss at step ', step, ': ', average_loss)
	  average_loss = 0

	# Note that this is expensive (~20% slowdown if computed every 500 steps)
	if step % 10000 == 0:
	  sim = similarity.eval()
	  for i in xrange(valid_size):
		valid_word = reverse_dictionary[valid_examples[i]]
		top_k = 8  # number of nearest neighbors
		nearest = (-sim[i, :]).argsort()[1:top_k + 1]
		log_str = 'Nearest to %s:' % valid_word
		for k in xrange(top_k):
		  if nearest[k] not in reverse_dictionary: continue
		  close_word = reverse_dictionary[nearest[k]]
		  log_str = '%s %s,' % (log_str, close_word)
		print(log_str)
  final_embeddings = normalized_embeddings.eval()

# Step 6: Visualize the embeddings.


# pylint: disable=missing-docstring
# Function to draw visualization of distance between embeddings.
def plot_with_labels(low_dim_embs, labels, filename):
  assert low_dim_embs.shape[0] >= len(labels), 'More labels than embeddings'
  plt.figure(figsize=(18, 18))  # in inches
  for i, label in enumerate(labels):
	x, y = low_dim_embs[i, :]
	plt.scatter(x, y)
	plt.annotate(label,
				 xy=(x, y),
				 xytext=(5, 2),
				 textcoords='offset points',
				 ha='right',
				 va='bottom')

  plt.savefig(filename)

try:
  # pylint: disable=g-import-not-at-top
  from sklearn.manifold import TSNE
  import matplotlib.pyplot as plt

  tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000, method='exact')
  plot_only = 500
  low_dim_embs = tsne.fit_transform(final_embeddings[:plot_only, :])
  labels = [reverse_dictionary[i] for i in xrange(plot_only)]
  plot_with_labels(low_dim_embs, labels, 'tsne.png')

except ImportError as ex:
  print('Please install sklearn, matplotlib, and scipy to show embeddings.')
  print(ex)
