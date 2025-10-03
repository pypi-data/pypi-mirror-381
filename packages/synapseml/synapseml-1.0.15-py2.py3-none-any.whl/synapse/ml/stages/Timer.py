# Copyright (C) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.


import sys
if sys.version >= '3':
    basestring = str

from pyspark import SparkContext, SQLContext
from pyspark.sql import DataFrame
from pyspark.ml.param.shared import *
from pyspark import keyword_only
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from synapse.ml.core.platform import running_on_synapse_internal
from synapse.ml.core.serialize.java_params_patch import *
from pyspark.ml.wrapper import JavaTransformer, JavaEstimator, JavaModel
from pyspark.ml.evaluation import JavaEvaluator
from pyspark.ml.common import inherit_doc
from synapse.ml.core.schema.Utils import *
from pyspark.ml.param import TypeConverters
from synapse.ml.core.schema.TypeConversionUtils import generateTypeConverter, complexTypeConverter
from synapse.ml.stages.TimerModel import TimerModel

@inherit_doc
class Timer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        disableMaterialization (bool): Whether to disable timing (so that one can turn it off for evaluation)
        logToScala (bool): Whether to output the time to the scala console
        stage (object): The stage to time
    """

    disableMaterialization = Param(Params._dummy(), "disableMaterialization", "Whether to disable timing (so that one can turn it off for evaluation)", typeConverter=TypeConverters.toBoolean)
    
    logToScala = Param(Params._dummy(), "logToScala", "Whether to output the time to the scala console", typeConverter=TypeConverters.toBoolean)
    
    stage = Param(Params._dummy(), "stage", "The stage to time")

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        disableMaterialization=True,
        logToScala=True,
        stage=None
        ):
        super(Timer, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.stages.Timer", self.uid)
        else:
            self._java_obj = java_obj
        self._setDefault(disableMaterialization=True)
        self._setDefault(logToScala=True)
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
    
        if java_obj is None:
            for k,v in kwargs.items():
                if v is not None:
                    getattr(self, "set" + k[0].upper() + k[1:])(v)

    @keyword_only
    def setParams(
        self,
        disableMaterialization=True,
        logToScala=True,
        stage=None
        ):
        """
        Set the (keyword only) parameters
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.azure.synapse.ml.stages.Timer"

    @staticmethod
    def _from_java(java_stage):
        module_name=Timer.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".Timer"
        return from_java(java_stage, module_name)

    def setDisableMaterialization(self, value):
        """
        Args:
            disableMaterialization: Whether to disable timing (so that one can turn it off for evaluation)
        """
        self._set(disableMaterialization=value)
        return self
    
    def setLogToScala(self, value):
        """
        Args:
            logToScala: Whether to output the time to the scala console
        """
        self._set(logToScala=value)
        return self
    
    def setStage(self, value):
        """
        Args:
            stage: The stage to time
        """
        self._set(stage=value)
        return self

    
    def getDisableMaterialization(self):
        """
        Returns:
            disableMaterialization: Whether to disable timing (so that one can turn it off for evaluation)
        """
        return self.getOrDefault(self.disableMaterialization)
    
    
    def getLogToScala(self):
        """
        Returns:
            logToScala: Whether to output the time to the scala console
        """
        return self.getOrDefault(self.logToScala)
    
    
    def getStage(self):
        """
        Returns:
            stage: The stage to time
        """
        return JavaParams._from_java(self._java_obj.getStage())

    def _create_model(self, java_model):
        try:
            model = TimerModel(java_obj=java_model)
            model._transfer_params_from_java()
        except TypeError:
            model = TimerModel._from_java(java_model)
        return model
    
    def _fit(self, dataset):
        java_model = self._fit_java(dataset)
        return self._create_model(java_model)

    
        