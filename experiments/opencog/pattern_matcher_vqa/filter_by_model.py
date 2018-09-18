#!/usr/bin/env python

from splitnet.splitmultidnnmodel import SplitMultidnnRunner, SplitNetsVocab
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + '../question2atomese')
from record import Record

def load_records(questionsFileName):
    questionFile = open(questionsFileName, 'r')
    for line in questionFile:
        record = Record.fromString(line)
        yield record


def filter_words(input_file, output_file):
    genome_path = '/home/noskill/projects/models/multi/visual_genome'
    vocab = SplitNetsVocab(genome_path)
    allowed_words = vocab.get_words()
    target = open(output_file, 'wt')

    filter_out = set(['_$qVar', 'be', 'is'])
    for record in load_records(input_file):
        ok = False
        if 'yes/no' == record.questionType and record.formula == '_predadj(A, B)':
            ok = True
        if 'other' == record.questionType and record.formula == '_det(A, B);_obj(C, D);_subj(C, A)':
            ok = True
        if not ok:
            continue

        target.write(record.toString())

    target.close()



parser = argparse.ArgumentParser(description='filter questions.')
parser.add_argument('input', type=str, action='store',
                    help='parsed questions')
parser.add_argument('output', type=str, action='store',
                    help='filtered quesions')


if __name__ == '__main__':
    args = parser.parse_args()
    filter_words(args.input, args.output)
