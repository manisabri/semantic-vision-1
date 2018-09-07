#!/usr/bin/env bash

python3 pattern_matcher_vqa.py \
    --questions /home/noskill/projects/semantic-vision-1/experiments/opencog/pattern_matcher_vqa/test_question.txt \
    --model-kind MULTIDNN \
    --atomspace atomspace.scm \
    --multidnn-model /home/noskill/projects/models/multi/model_01_max_score_val.pth.tar \
    --features-extractor-kind PRECALCULATED \
    --precalculated-features /home/noskill/projects/models/features/val2014_parsed_features.zip \
    --precalculated-features-prefix val2014_parsed_features/COCO_val2014_ \
    --python-log-level INFO \
    --opencog-log-level NONE

