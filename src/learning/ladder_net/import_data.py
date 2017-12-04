# import_data.py
# Imports preprocessed data as data structure
# Authors: Swetha Revanur and Keanu Spies

from __future__ import print_function
import gzip
import os
import urllib
import numpy as np
import glob
import pandas as pd
import math

num_features = 7
num_examples_total = 10
num_labeled = 3

def importFilesAsDF(filename):
	df = pd.read_excel(filename) # remove index?
	return df

def loadDataSet(df):
	return df.values.tolist()

def extract_images(data_list):
	"""Extract the file into a 4D np array [index, y, x, depth]."""
	# totalDataFrame = importFilesAsDF(fileName)
	# print('Extracting Training')
	num_features = len(data_list[0])  # one for each feature
	num_examples = len(data_list)# one for each post
	cols = 1 # column vector
	data = np.zeros(num_examples * num_features)
	data = data_list
	# removes indices 
	data = np.array([np.array(a[0:]) for a in data])
	data = data.reshape(num_examples, num_features, cols, 1)
	return data

def dense_to_one_hot(labels_dense, num_classes=2):
	"""Convert class labels from scalars to one-hot vectors."""
	num_labels = labels_dense.shape[0]
	index_offset = np.arange(num_labels) * num_classes
	labels_one_hot = np.zeros((num_labels, num_classes))
	labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
	return labels_one_hot

def extract_labels(data_list, filename, one_hot=False):

	# labeled_df = importFilesAsDF(filename)
	# labeled_list = labeled_df.values.tolist()
	# label_vector = []
	# unlabeled_vector = []
	# for i in range(len(data_list)):
	# 	labeled = False
	# 	for label in labeled_list:
	# 		if data_list[i][0] in label[0]:
	# 			labeled = True
	# 			label_vector.append(label[1])
	# 			break
	# 	if not labeled:
	# 		unlabeled_vector.append()
	# 		label_vector.append(-1)

	# labels = np.array(label_vector)
	# print(labels)
	# if one_hot:
	# 	return dense_to_one_hot(labels)
	# return labels

	labeled_df = importFilesAsDF(filename)
	labeled_list = labeled_df.values.tolist()

	label_vector = []
	labeled_X = []
	unlabeled_X = []
	unlabeled_vec = []

	for i in range(len(data_list)):
		labeled = False
		for label in labeled_list:
			if data_list[i][0] in label[0]:
				labeled = True
				label_vector.append(label[1])
				labeled_X.append(data_list[i][1:])
				break
		if not labeled:
			unlabeled_X.append(data_list[i][1:])
			unlabeled_vec.append(0)

	labeled_X.extend(unlabeled_X)
	X = labeled_X
	label_vector.extend(unlabeled_vec)
	y = label_vector

	labels = np.array(y)
	# print(labels)
	if one_hot:
		return X, dense_to_one_hot(labels)

	return X, labels
	

class DataSet(object):

	def __init__(self, images, labels, fake_data=False):
		if fake_data:
			self._num_examples = 10000
		else:
			assert images.shape[0] == labels.shape[0], (
					"images.shape: %s labels.shape: %s" % (images.shape, labels.shape))
			self._num_examples = images.shape[0]

			# Convert shape from [num examples, rows, columns, depth]
			# to [num examples, rows*columns] (assuming depth == 1)
			assert images.shape[3] == 1
			images = images.reshape(images.shape[0], images.shape[1] * images.shape[2])
			# Convert from [0, 255] -> [0.0, 1.0].
			images = images.astype(np.float32)
			images = np.multiply(images, 1.0 / 255.0)
		self._images = images
		self._labels = labels
		self._epochs_completed = 0
		self._index_in_epoch = 0

	@property
	def images(self):
		return self._images

	@property
	def labels(self):
		return self._labels

	@property
	def num_examples(self):
		return self._num_examples

	@property
	def epochs_completed(self):
		return self._epochs_completed

	def next_batch(self, batch_size, fake_data=False):
		"""Return the next `batch_size` examples from this data set."""
		if fake_data:
			# fake_image = [1.0 for _ in xrange(num_features)]
			fake_label = 0
			return [fake_image for _ in xrange(batch_size)], [
					fake_label for _ in xrange(batch_size)]
		start = self._index_in_epoch
		self._index_in_epoch += batch_size
		if self._index_in_epoch > self._num_examples:
			# Finished epoch
			self._epochs_completed += 1
			# Shuffle the data
			perm = np.arange(self._num_examples)
			np.random.shuffle(perm)
			self._images = self._images[perm]
			self._labels = self._labels[perm]
			# Start next epoch
			start = 0
			self._index_in_epoch = batch_size
			assert batch_size <= self._num_examples
		end = self._index_in_epoch
		return self._images[start:end], self._labels[start:end]

class SemiDataSet(object):
		def __init__(self, images, labels, n_labeled):
				self.n_labeled = n_labeled

				# Unlabeled DataSet
				self.unlabeled_ds = DataSet(images, labels)

				# Labeled DataSet
				self.num_examples = self.unlabeled_ds.num_examples
				indices = np.arange(self.num_examples)
				shuffled_indices = np.random.permutation(indices)
				images = images[shuffled_indices]
				labels = labels[shuffled_indices]
				# needs to have a one in one of the things in the one hot
				y = np.array([np.arange(2)[l==1][0] for l in labels])
				idx = indices[y==0][:5]
				n_classes = y.max() + 1
				n_from_each_class = n_labeled / n_classes
				i_labeled = []
				for c in range(n_classes):
						i = indices[y==c][:n_from_each_class]
						i_labeled += list(i)
				l_images = images[i_labeled]
				l_labels = labels[i_labeled]
				self.labeled_ds = DataSet(l_images, l_labels)

		def next_batch(self, batch_size):
				unlabeled_images, _ = self.unlabeled_ds.next_batch(batch_size)
				if batch_size > self.n_labeled:
						labeled_images, labels = self.labeled_ds.next_batch(self.n_labeled)
				else:
						labeled_images, labels = self.labeled_ds.next_batch(batch_size)
				images = np.vstack([labeled_images, unlabeled_images])
				return images, labels

def read_data_sets(train_dir, n_labeled=10, fake_data=False, one_hot=False):
	class DataSets(object):
		pass
	data_sets = DataSets()

	if fake_data:
		data_sets.train = DataSet([], [], fake_data=True)
		data_sets.validation = DataSet([], [], fake_data=True)
		data_sets.test = DataSet([], [], fake_data=True)
		return data_sets

	TRAIN_IMAGES = 'train-images-idx3-ubyte.gz'
	TRAIN_LABELS = 'train-labels-idx1-ubyte.gz'
	TEST_IMAGES = 't10k-images-idx3-ubyte.gz'
	TEST_LABELS = 't10k-labels-idx1-ubyte.gz'
	VALIDATION_SIZE = 0
	# TEST_SIZE = int(math.floor(num_labeled/5))
	TEST_SIZE = 2

	# local_file = maybe_download(TRAIN_LABELS, train_dir)
	image_file = 'dummy_lda_output.xlsx'
	data_set = loadDataSet(importFilesAsDF(image_file))
	local_file = 'dummy_labeled_lda_output.xlsx'

	X, train_labels = extract_labels(data_set,local_file, one_hot=one_hot)
	train_images = extract_images(X)

	# local_file = maybe_download(TEST_IMAGES, train_dir)
	# test_images = extract_images(local_file)
	test_images = train_images[:TEST_SIZE]
	train_images = train_images[TEST_SIZE:]

	# local_file = maybe_download(TEST_LABELS, train_dir)
	# test_labels = extract_labels(local_file, one_hot=one_hot)
	test_labels = train_labels[:TEST_SIZE]
	train_labels = train_labels[TEST_SIZE:]

	validation_images = train_images[:VALIDATION_SIZE]
	validation_labels = train_labels[:VALIDATION_SIZE]
	train_images = train_images[VALIDATION_SIZE:]
	train_labels = train_labels[VALIDATION_SIZE:]

	data_sets.train = SemiDataSet(train_images, train_labels, n_labeled)
	data_sets.validation = DataSet(validation_images, validation_labels)
	data_sets.test = DataSet(test_images, test_labels)

	return data_sets
