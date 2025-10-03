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


@inherit_doc
class KNNModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        ballTree (object): the ballTree model used for performing queries
        featuresCol (str): The name of the features column
        k (int): number of matches to return
        leafSize (int): max size of the leaves of the tree
        outputCol (str): The name of the output column
        valuesCol (str): column holding values for each feature (key) that will be returned when queried
    """

    ballTree = Param(Params._dummy(), "ballTree", "the ballTree model used for performing queries")
    
    featuresCol = Param(Params._dummy(), "featuresCol", "The name of the features column", typeConverter=TypeConverters.toString)
    
    k = Param(Params._dummy(), "k", "number of matches to return", typeConverter=TypeConverters.toInt)
    
    leafSize = Param(Params._dummy(), "leafSize", "max size of the leaves of the tree", typeConverter=TypeConverters.toInt)
    
    outputCol = Param(Params._dummy(), "outputCol", "The name of the output column", typeConverter=TypeConverters.toString)
    
    valuesCol = Param(Params._dummy(), "valuesCol", "column holding values for each feature (key) that will be returned when queried", typeConverter=TypeConverters.toString)

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        ballTree=None,
        featuresCol=None,
        k=None,
        leafSize=None,
        outputCol=None,
        valuesCol=None
        ):
        super(KNNModel, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.nn.KNNModel", self.uid)
        else:
            self._java_obj = java_obj
        
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
        ballTree=None,
        featuresCol=None,
        k=None,
        leafSize=None,
        outputCol=None,
        valuesCol=None
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
        return "com.microsoft.azure.synapse.ml.nn.KNNModel"

    @staticmethod
    def _from_java(java_stage):
        module_name=KNNModel.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".KNNModel"
        return from_java(java_stage, module_name)

    def setBallTree(self, value):
        """
        Args:
            ballTree: the ballTree model used for performing queries
        """
        self._set(ballTree=value)
        return self
    
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: The name of the features column
        """
        self._set(featuresCol=value)
        return self
    
    def setK(self, value):
        """
        Args:
            k: number of matches to return
        """
        self._set(k=value)
        return self
    
    def setLeafSize(self, value):
        """
        Args:
            leafSize: max size of the leaves of the tree
        """
        self._set(leafSize=value)
        return self
    
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
        self._set(outputCol=value)
        return self
    
    def setValuesCol(self, value):
        """
        Args:
            valuesCol: column holding values for each feature (key) that will be returned when queried
        """
        self._set(valuesCol=value)
        return self

    
    def getBallTree(self):
        """
        Returns:
            ballTree: the ballTree model used for performing queries
        """
        return self.getOrDefault(self.ballTree)
    
    
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: The name of the features column
        """
        return self.getOrDefault(self.featuresCol)
    
    
    def getK(self):
        """
        Returns:
            k: number of matches to return
        """
        return self.getOrDefault(self.k)
    
    
    def getLeafSize(self):
        """
        Returns:
            leafSize: max size of the leaves of the tree
        """
        return self.getOrDefault(self.leafSize)
    
    
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
        return self.getOrDefault(self.outputCol)
    
    
    def getValuesCol(self):
        """
        Returns:
            valuesCol: column holding values for each feature (key) that will be returned when queried
        """
        return self.getOrDefault(self.valuesCol)

    

    
        