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

def importFilesAsDF():
	pathToFiles =r'../../data/raw' # use your path
	fileNames = glob.glob(pathToFiles + "/secondpostbatch*.xlsx")
	
	postList = []
	for fileName in fileNames:
		df = pd.read_excel(fileName)
		postList.append(df)
	
	totalDataFrame = pd.concat(postList)
	return totalDataFrame

# def _read32(bytestream):
# 	dt = numpy.dtype(numpy.uint32).newbyteorder('>')
# 	return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]

def extract_images(df):
	"""Extract the file into a 4D numpy array [index, y, x, depth]."""
	print('Extracting')
	num_examples = len(df.columns) # one for each post
	rows = len(df) # one for each feature
	cols = 1 # column vector
	data = np.zeros(num_examples * rows)
	data = totalDataFrame.values
	return data

totalDataFrame = importFilesAsDF()
data = extract_images(totalDataFrame)

def dense_to_one_hot(labels_dense, num_classes=10):
	"""Convert class labels from scalars to one-hot vectors."""
	num_labels = labels_dense.shape[0]
	index_offset = numpy.arange(num_labels) * num_classes
	labels_one_hot = numpy.zeros((num_labels, num_classes))
	labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
	return labels_one_hot

def extract_labels(filename, one_hot=False):
	"""Extract the labels into a 1D uint8 numpy array [index]."""
	print('Extracting', filename)
	with gzip.open(filename) as bytestream:
		magic = _read32(bytestream)
		if magic != 2049:
			raise ValueError(
					'Invalid magic number %d in MNIST label file: %s' %
					(magic, filename))
		num_items = _read32(bytestream)
		buf = bytestream.read(num_items)
		labels = numpy.frombuffer(buf, dtype=numpy.uint8)
		if one_hot:
			return dense_to_one_hot(labels)
		return labels

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
			images = images.astype(numpy.float32)
			images = numpy.multiply(images, 1.0 / 255.0)
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
			fake_image = [1.0 for _ in xrange(784)]
			fake_label = 0
			return [fake_image for _ in xrange(batch_size)], [
					fake_label for _ in xrange(batch_size)]
		start = self._index_in_epoch
		self._index_in_epoch += batch_size
		if self._index_in_epoch > self._num_examples:
			# Finished epoch
			self._epochs_completed += 1
			# Shuffle the data
			perm = numpy.arange(self._num_examples)
			numpy.random.shuffle(perm)
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

				# Unlabled DataSet
				self.unlabeled_ds = DataSet(images, labels)

				# Labeled DataSet
				self.num_examples = self.unlabeled_ds.num_examples
				indices = numpy.arange(self.num_examples)
				shuffled_indices = numpy.random.permutation(indices)
				images = images[shuffled_indices]
				labels = labels[shuffled_indices]
				y = numpy.array([numpy.arange(10)[l==1][0] for l in labels])
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
				images = numpy.vstack([labeled_images, unlabeled_images])
				return images, labels

def read_data_sets(train_dir, n_labeled = 100, fake_data=False, one_hot=False):
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

	local_file = maybe_download(TRAIN_IMAGES, train_dir)
	train_images = extract_images(local_file)
	print(train_images)

	local_file = maybe_download(TRAIN_LABELS, train_dir)
	train_labels = extract_labels(local_file, one_hot=one_hot)

	local_file = maybe_download(TEST_IMAGES, train_dir)
	test_images = extract_images(local_file)

	local_file = maybe_download(TEST_LABELS, train_dir)
	test_labels = extract_labels(local_file, one_hot=one_hot)

	validation_images = train_images[:VALIDATION_SIZE]
	validation_labels = train_labels[:VALIDATION_SIZE]
	train_images = train_images[VALIDATION_SIZE:]
	train_labels = train_labels[VALIDATION_SIZE:]

	data_sets.train = SemiDataSet(train_images, train_labels, n_labeled)
	data_sets.validation = DataSet(validation_images, validation_labels)
	data_sets.test = DataSet(test_images, test_labels)

	return data_sets
	