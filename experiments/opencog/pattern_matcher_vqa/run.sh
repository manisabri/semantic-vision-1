#!/usr/bin/env bash

python3 pattern_matcher_vqa.py \
    --questions test_question.txt \
    --model-kind SPLITMULTIDNN \
    --atomspace atomspace.scm \
    --multidnn-model /home/noskill/projects/models/multi/visual_genome \
    --features-extractor-kind PRECALCULATED \
    --precalculated-features /home/noskill/projects/models/features/val2014_parsed_features.zip \
    --precalculated-features-prefix val2014_parsed_features/COCO_val2014_ \
    --python-log-level DEBUG \
    --opencog-log-level NONE

