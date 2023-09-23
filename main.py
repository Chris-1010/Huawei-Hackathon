#region Imports and Setup


import argparse
# Create a parsing task.
parser = argparse.ArgumentParser(description="train mnist",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# Add parameters.
parser.add_argument('--train_url', type=str, 
                    help='the path model saved')
parser.add_argument('--data_url', type=str, help='the training data')
# Parse the parameters.
args, unkown = parser.parse_known_args()

import os
os.system('pip install transformers')
os.system('pip install nltk')
os.system('pip install tensorflow')

import sqlite3
from transformers import BertTokenizer
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

#endregion

class DatabaseAI(object):
    def __init__(self, database_name:str):
        self._database_name = database_name

    def connect_fun(self, database_name:str):
        """Object that should “establish a connection” to a given SQLite file. 
            That function will be run once before all the questions related to the given database"""
        #Connect to SQLite
        conn = sqlite3.connect(self._database_name)
        cursor = conn.cursor()

        #Execute a query
        rows = cursor.execute(f"SELECT * FROM {database_name};").fetchall()


        #Close connection
        cursor.close()
        conn.close()

        return rows

    def query_fun(self, question:str, tables:list[str]):
        """This function will be run once for each question related to the given database."""

        #Tokenize the question - in order for it to be read by the ai
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")  #create the tokenizer
        stop_words = set(stopwords.words("english"))         #set of english stop words like commas, full stops and question marks
        tokens = tokenizer.tokenize(question)
        for token in tokens:
            if token in stop_words:
                tokens.remove(token)            #removing any stop words so that ai doesn't need to process them and can read more efficiently  

#region Main
# databases = {"covid_vaccinations": "example-data/example-covid-vaccinations.sqlite3", "orders": "example-data/example-simple.sqlite3", "murder_mystery": "example-data/sql-murder-mystery.sqlite3"}
# preferred_database = input("Would you like to use the database of:\n'covid_vaccinations',\t'orders'")
# while preferred_database not in databases:
#         print("Not a valid Database")
#         preferred_database = input("Would you like to use the database of:\n'covid_vaccinations',\t'orders', or\t'murder_mystery'\n\n")
preferred_database = "covid_vaccinations"
db_path = "example-data/example-covid-vaccinations.sqlite3"
the_ai = DatabaseAI(db_path)
rows = the_ai.connect_fun(preferred_database)
print(rows)

#tokenizing
question = input("Enter your question: ")
the_ai.query_fun(question, rows)
#endregion



# tensorflow

'''import os

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import moxing as mox

tf.flags.DEFINE_integer('max_steps', 1000, 'number of training iterations.')
tf.flags.DEFINE_string('data_url', '/home/jnn/nfs/mnist', 'dataset directory.')
tf.flags.DEFINE_string('train_url', '/home/jnn/temp/delete', 'saved model directory.')

FLAGS = tf.flags.FLAGS


def main(*args):
    # Train model
    print('Training model...')
    mnist = input_data.read_data_sets(FLAGS.data_url, one_hot=True)
    sess = tf.InteractiveSession()
    serialized_tf_example = tf.placeholder(tf.string, name='tf_example')
    feature_configs = {'x': tf.FixedLenFeature(shape=[784], dtype=tf.float32),}
    tf_example = tf.parse_example(serialized_tf_example, feature_configs)
    x = tf.identity(tf_example['x'], name='x')
    y_ = tf.placeholder('float', shape=[None, 10])
    w = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    sess.run(tf.global_variables_initializer())
    y = tf.nn.softmax(tf.matmul(x, w) + b, name='y')
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

    tf.summary.scalar('cross_entropy', cross_entropy)

    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
    tf.summary.scalar('accuracy', accuracy)
    merged = tf.summary.merge_all()
    test_writer = tf.summary.FileWriter(FLAGS.train_url, flush_secs=1)

    for step in range(FLAGS.max_steps):
        batch = mnist.train.next_batch(50)
        train_step.run(feed_dict={x: batch[0], y_: batch[1]})
        if step % 10 == 0:
            summary, acc = sess.run([merged, accuracy], feed_dict={x: mnist.test.images, y_: mnist.test.labels})
            test_writer.add_summary(summary, step)
            print('training accuracy is:', acc)
    print('Done training!')

    builder = tf.saved_model.builder.SavedModelBuilder(os.path.join(FLAGS.train_url, 'model'))

    tensor_info_x = tf.saved_model.utils.build_tensor_info(x)
    tensor_info_y = tf.saved_model.utils.build_tensor_info(y)

    prediction_signature = (
        tf.saved_model.signature_def_utils.build_signature_def(
            inputs={'images': tensor_info_x},
            outputs={'scores': tensor_info_y},
            method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME))

    builder.add_meta_graph_and_variables(
        sess, [tf.saved_model.tag_constants.SERVING],
        signature_def_map={
            'predict_images':
                prediction_signature,
        },
        main_op=tf.tables_initializer(),
        strip_default_attrs=True)

    builder.save()

    print('Done exporting!')


if __name__ == '__main__':
    tf.app.run(main=main)
'''