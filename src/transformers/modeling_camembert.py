# coding=utf-8
# Copyright 2019 Inria, Facebook AI Research and the HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
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
"""PyTorch CamemBERT model. """


import logging

from .configuration_camembert import CamembertConfig
from .file_utils import add_start_docstrings
from .modeling_roberta import (
    RobertaForMaskedLM,
    RobertaForMultipleChoice,
    RobertaForSequenceClassification,
    RobertaForTokenClassification,
    RobertaModel,
)


logger = logging.getLogger(__name__)

CAMEMBERT_PRETRAINED_MODEL_ARCHIVE_MAP = {
    "camembert-base": "https://s3.amazonaws.com/models.huggingface.co/bert/camembert-base-pytorch_model.bin",
    "umberto-commoncrawl-cased-v1": "https://s3.amazonaws.com/models.huggingface.co/bert/Musixmatch/umberto-commoncrawl-cased-v1/pytorch_model.bin",
    "umberto-wikipedia-uncased-v1": "https://s3.amazonaws.com/models.huggingface.co/bert/Musixmatch/umberto-wikipedia-uncased-v1/pytorch_model.bin",
}


CAMEMBERT_START_DOCSTRING = r"""

    This model is a PyTorch `torch.nn.Module <https://pytorch.org/docs/stable/nn.html#torch.nn.Module>`_ sub-class.
    Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general
    usage and behavior.

    Parameters:
        config (:class:`~transformers.CamembertConfig`): Model configuration class with all the parameters of the
            model. Initializing with a config file does not load the weights associated with the model, only the configuration.
            Check out the :meth:`~transformers.PreTrainedModel.from_pretrained` method to load the model weights.
"""


@add_start_docstrings(
    "The bare CamemBERT Model transformer outputting raw hidden-states without any specific head on top.",
    CAMEMBERT_START_DOCSTRING,
)
class CamembertModel(RobertaModel):
    """
    This class overrides :class:`~transformers.RobertaModel`. Please check the
    superclass for the appropriate documentation alongside usage examples.
    """

    config_class = CamembertConfig
    pretrained_model_archive_map = CAMEMBERT_PRETRAINED_MODEL_ARCHIVE_MAP


@add_start_docstrings(
    """CamemBERT Model with a `language modeling` head on top. """, CAMEMBERT_START_DOCSTRING,
)
class CamembertForMaskedLM(RobertaForMaskedLM):
    """
    This class overrides :class:`~transformers.RobertaForMaskedLM`. Please check the
    superclass for the appropriate documentation alongside usage examples.
    """

    config_class = CamembertConfig
    pretrained_model_archive_map = CAMEMBERT_PRETRAINED_MODEL_ARCHIVE_MAP


@add_start_docstrings(
    """CamemBERT Model transformer with a sequence classification/regression head on top (a linear layer
    on top of the pooled output) e.g. for GLUE tasks. """,
    CAMEMBERT_START_DOCSTRING,
)
class CamembertForSequenceClassification(RobertaForSequenceClassification):
    """
    This class overrides :class:`~transformers.RobertaForSequenceClassification`. Please check the
    superclass for the appropriate documentation alongside usage examples.
    """

    config_class = CamembertConfig
    pretrained_model_archive_map = CAMEMBERT_PRETRAINED_MODEL_ARCHIVE_MAP


@add_start_docstrings(
    """CamemBERT Model with a multiple choice classification head on top (a linear layer on top of
    the pooled output and a softmax) e.g. for RocStories/SWAG tasks. """,
    CAMEMBERT_START_DOCSTRING,
)
class CamembertForMultipleChoice(RobertaForMultipleChoice):
    """
    This class overrides :class:`~transformers.RobertaForMultipleChoice`. Please check the
    superclass for the appropriate documentation alongside usage examples.
    """

    config_class = CamembertConfig
    pretrained_model_archive_map = CAMEMBERT_PRETRAINED_MODEL_ARCHIVE_MAP


@add_start_docstrings(
    """CamemBERT Model with a token classification head on top (a linear layer on top of
    the hidden-states output) e.g. for Named-Entity-Recognition (NER) tasks. """,
    CAMEMBERT_START_DOCSTRING,
)
class CamembertForTokenClassification(RobertaForTokenClassification):
    """
    This class overrides :class:`~transformers.RobertaForTokenClassification`. Please check the
    superclass for the appropriate documentation alongside usage examples.
    """

    config_class = CamembertConfig
    pretrained_model_archive_map = CAMEMBERT_PRETRAINED_MODEL_ARCHIVE_MAP
