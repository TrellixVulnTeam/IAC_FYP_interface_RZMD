# Copyright (c) 2019-present, HuggingFace Inc.
# All rights reserved. This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
from datetime import datetime
import json
import logging
import os
import tarfile
import tempfile
import socket

import torch

from transformers import cached_path


#PERSONACHAT_URL = "https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json"
PERSONACHAT_URL = "./celebs_dialog_dataset.json"

#HF_FINETUNED_MODEL = "https://s3.amazonaws.com/models.huggingface.co/transfer-learning-chatbot/gpt_personachat_cache.tar.gz"
#CACHED_BOT = "./model_/model.75f2a4fe69178ff43138117a977e107a5fc7d402603a0825a296b531f246b3f2"
FINE_TUNED_BOT = "./tempdir/model_/model.75f2a4fe69178ff43138117a977e107a5fc7d402603a0825a296b531f246b3f2"

tempfile.tempdir = "./tempdir"

def download_pretrained_model():
    """ Download and extract finetuned model from S3 """
    tempdir = tempfile.mkdtemp()
    with tarfile.open(FINE_TUNED_BOT, 'r:gz') as archive:
        archive.extractall(tempdir)
    return tempdir


def get_dataset(tokenizer, dataset_path, dataset_cache):
    """ Get tokenized PERSONACHAT dataset from S3 or cache."""
    dataset_cache = dataset_cache + '_' + type(tokenizer).__name__  # To avoid using GPT cache for GPT-2 and vice-versa
    dataset = torch.load(dataset_cache)
    return dataset


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def make_logdir(model_name: str):
    """Create unique path to save results and checkpoints, e.g. runs/Sep22_19-45-59_gpu-7_gpt2"""
    # Code copied from ignite repo
    current_time = datetime.now().strftime('%b%d_%H-%M-%S')
    logdir = os.path.join(
        'runs', current_time + '_' + socket.gethostname() + '_' + model_name)
    return logdir
