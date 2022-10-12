import random

from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition
from providedcode.dependencycorpusreader import DependencyCorpusReader

def test_corpus():
    return DependencyCorpusReader('', 'test.conll')

if __name__ == '__main__':
    data = dataset.get_swedish_train_corpus().parsed_sents()
    random.seed(1234)
    subdata = random.sample(data, 200)

    try:
        testdata = test_corpus().parsed_sents()
        tp = TransitionParser.load('badfeatures.model')

        parsed = tp.parse(testdata)

        with open('test.conll', 'w') as f:
            for p in parsed:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')

        ev = DependencyEvaluator(testdata, parsed)
        print "UAS: {} \nLAS: {}".format(*ev.eval())

    except NotImplementedError:
        print "error"