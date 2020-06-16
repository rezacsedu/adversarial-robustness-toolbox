# MIT License
#
# Copyright (C) The Adversarial Robustness Toolbox (ART) Authors 2020
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
This module implements ShapeShifter, a robust physical adversarial attack on Faster R-CNN object detector.

| Paper link: https://arxiv.org/abs/1804.05810
"""
import logging

import numpy as np
import tensorflow as tf

from art.attacks.attack import EvasionAttack
from art.estimators.estimator import BaseEstimator, LossGradientsMixin, NeuralNetworkMixin
from art.estimators.tensorflow import TensorFlowEstimator
from art.estimators.object_detection.tensorflow_faster_rcnn import TensorFlowFasterRCNN
from art.estimators.object_detection.object_detector import ObjectDetectorMixin
from art.utils import Deprecated, deprecated_keyword_arg

logger = logging.getLogger(__name__)


class ShapeShifter(EvasionAttack):
    """
    Implementation of the ShapeShifter attack. This is a robust physical adversarial attack on Faster R-CNN object
    detector and is developed in TensorFlow.

    | Paper link: https://arxiv.org/abs/1804.05810
    """

    attack_params = EvasionAttack.attack_params + [
        "random_transform",
        "learning_rate",
        "batch_size",

        "box_classifier_weight",
    ]

    _estimator_requirements = (
        BaseEstimator,
        LossGradientsMixin,
        NeuralNetworkMixin,
        ObjectDetectorMixin,
        TensorFlowEstimator,
        TensorFlowFasterRCNN
    )

    def __init__(
        self,
        estimator,
        random_transform=tf.identity,
        learning_rate=5.0,
        batch_size=1,
        box_classifier_weight=1.0,
    ):
        """
        Create an instance of the :class:`.ShapeShifter`.

        :param estimator: A trained object detector.
        :type estimator: :class:`.TensorFlowFasterRCNN`
        :param random_transform: A TensorFlow function applies random transformations to images.
        :type random_transform: `tensorflow function`
        :param learning_rate: The learning rate of the optimization.
        :type learning_rate: `float`
        :param batch_size: The size of the training batch.
        :type batch_size: `int`
        """
        super(ShapeShifter, self).__init__(estimator=estimator)

        kwargs = {
            "random_transform": random_transform,
            "learning_rate": learning_rate,
            "batch_size": batch_size,
        }
        self.set_params(**kwargs)

    def generate(self, x, y=None, **kwargs):
        """
        Generate adversarial samples and return them in an array.

        :param x: Sample images.
        :type x: `np.ndarray`
        :param y: Target labels for object detector.
        :type y: `np.ndarray`
        :return: Adversarial patch.
        :rtype: `np.ndarray`
        """
        assert x.ndim == 4, "The adversarial patch can only be applied to images."








        return self._patch

    def set_params(self, **kwargs):
        """
        Take in a dictionary of parameters and applies attack-specific checks before saving them as attributes.

        :param learning_rate: The learning rate of the optimization.
        :type learning_rate: `float`
        :param batch_size: The size of the training batch.
        :type batch_size: `int`
        """
        super(ShapeShifter, self).set_params(**kwargs)

        if not isinstance(self.learning_rate, float):
            raise ValueError("The learning rate must be of type float.")
        if not self.learning_rate > 0.0:
            raise ValueError("The learning rate must be greater than 0.0.")

        if not isinstance(self.batch_size, int):
            raise ValueError("The batch size must be of type int.")
        if not self.batch_size > 0:
            raise ValueError("The batch size must be greater than 0.")