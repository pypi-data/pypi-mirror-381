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
class IdentifyFaces(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        confidenceThreshold (object): Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        customHeaders (object): Map of Custom Header Key-Value Tuples.
        customUrlRoot (str): The custom URL root for the service. This will not append OpenAI specific model path completions (i.e. /chat/completions) to the URL.
        errorCol (str): column to hold http errors
        faceIds (object): Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        handler (object): Which strategy to use when handling requests
        largePersonGroupId (object): largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        maxNumOfCandidatesReturned (object): The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        outputCol (str): The name of the output column
        personGroupId (object): personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        subscriptionKey (object): the API key to use
        telemHeaders (object): Map of Custom Header Key-Value Tuples.
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """

    AADToken = Param(Params._dummy(), "AADToken", "ServiceParam: AAD Token used for authentication")
    
    CustomAuthHeader = Param(Params._dummy(), "CustomAuthHeader", "ServiceParam: A Custom Value for Authorization Header")
    
    concurrency = Param(Params._dummy(), "concurrency", "max number of concurrent calls", typeConverter=TypeConverters.toInt)
    
    concurrentTimeout = Param(Params._dummy(), "concurrentTimeout", "max number seconds to wait on futures if concurrency >= 1", typeConverter=TypeConverters.toFloat)
    
    confidenceThreshold = Param(Params._dummy(), "confidenceThreshold", "ServiceParam: Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.")
    
    customHeaders = Param(Params._dummy(), "customHeaders", "ServiceParam: Map of Custom Header Key-Value Tuples.")
    
    customUrlRoot = Param(Params._dummy(), "customUrlRoot", "The custom URL root for the service. This will not append OpenAI specific model path completions (i.e. /chat/completions) to the URL.", typeConverter=TypeConverters.toString)
    
    errorCol = Param(Params._dummy(), "errorCol", "column to hold http errors", typeConverter=TypeConverters.toString)
    
    faceIds = Param(Params._dummy(), "faceIds", "ServiceParam: Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. ")
    
    handler = Param(Params._dummy(), "handler", "Which strategy to use when handling requests")
    
    largePersonGroupId = Param(Params._dummy(), "largePersonGroupId", "ServiceParam: largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.")
    
    maxNumOfCandidatesReturned = Param(Params._dummy(), "maxNumOfCandidatesReturned", "ServiceParam: The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).")
    
    outputCol = Param(Params._dummy(), "outputCol", "The name of the output column", typeConverter=TypeConverters.toString)
    
    personGroupId = Param(Params._dummy(), "personGroupId", "ServiceParam: personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.")
    
    subscriptionKey = Param(Params._dummy(), "subscriptionKey", "ServiceParam: the API key to use")
    
    telemHeaders = Param(Params._dummy(), "telemHeaders", "ServiceParam: Map of Custom Header Key-Value Tuples.")
    
    timeout = Param(Params._dummy(), "timeout", "number of seconds to wait before closing the connection", typeConverter=TypeConverters.toFloat)
    
    url = Param(Params._dummy(), "url", "Url of the service", typeConverter=TypeConverters.toString)

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        AADToken=None,
        AADTokenCol=None,
        CustomAuthHeader=None,
        CustomAuthHeaderCol=None,
        concurrency=1,
        concurrentTimeout=None,
        confidenceThreshold=None,
        confidenceThresholdCol=None,
        customHeaders=None,
        customHeadersCol=None,
        customUrlRoot=None,
        errorCol="IdentifyFaces_e3314d4d425b_error",
        faceIds=None,
        faceIdsCol=None,
        handler=None,
        largePersonGroupId=None,
        largePersonGroupIdCol=None,
        maxNumOfCandidatesReturned=None,
        maxNumOfCandidatesReturnedCol=None,
        outputCol="IdentifyFaces_e3314d4d425b_output",
        personGroupId=None,
        personGroupIdCol=None,
        subscriptionKey=None,
        subscriptionKeyCol=None,
        telemHeaders=None,
        telemHeadersCol=None,
        timeout=60.0,
        url=None
        ):
        super(IdentifyFaces, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.services.face.IdentifyFaces", self.uid)
        else:
            self._java_obj = java_obj
        self._setDefault(concurrency=1)
        self._setDefault(errorCol="IdentifyFaces_e3314d4d425b_error")
        self._setDefault(outputCol="IdentifyFaces_e3314d4d425b_output")
        self._setDefault(timeout=60.0)
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
        AADToken=None,
        AADTokenCol=None,
        CustomAuthHeader=None,
        CustomAuthHeaderCol=None,
        concurrency=1,
        concurrentTimeout=None,
        confidenceThreshold=None,
        confidenceThresholdCol=None,
        customHeaders=None,
        customHeadersCol=None,
        customUrlRoot=None,
        errorCol="IdentifyFaces_e3314d4d425b_error",
        faceIds=None,
        faceIdsCol=None,
        handler=None,
        largePersonGroupId=None,
        largePersonGroupIdCol=None,
        maxNumOfCandidatesReturned=None,
        maxNumOfCandidatesReturnedCol=None,
        outputCol="IdentifyFaces_e3314d4d425b_output",
        personGroupId=None,
        personGroupIdCol=None,
        subscriptionKey=None,
        subscriptionKeyCol=None,
        telemHeaders=None,
        telemHeadersCol=None,
        timeout=60.0,
        url=None
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
        return "com.microsoft.azure.synapse.ml.services.face.IdentifyFaces"

    @staticmethod
    def _from_java(java_stage):
        module_name=IdentifyFaces.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".IdentifyFaces"
        return from_java(java_stage, module_name)

    def setAADToken(self, value):
        """
        Args:
            AADToken: AAD Token used for authentication
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setAADToken(value)
        return self
    
    def setAADTokenCol(self, value):
        """
        Args:
            AADToken: AAD Token used for authentication
        """
        self._java_obj = self._java_obj.setAADTokenCol(value)
        return self
    
    def setCustomAuthHeader(self, value):
        """
        Args:
            CustomAuthHeader: A Custom Value for Authorization Header
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setCustomAuthHeader(value)
        return self
    
    def setCustomAuthHeaderCol(self, value):
        """
        Args:
            CustomAuthHeader: A Custom Value for Authorization Header
        """
        self._java_obj = self._java_obj.setCustomAuthHeaderCol(value)
        return self
    
    def setConcurrency(self, value):
        """
        Args:
            concurrency: max number of concurrent calls
        """
        self._set(concurrency=value)
        return self
    
    def setConcurrentTimeout(self, value):
        """
        Args:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
        self._set(concurrentTimeout=value)
        return self
    
    def setConfidenceThreshold(self, value):
        """
        Args:
            confidenceThreshold: Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setConfidenceThreshold(value)
        return self
    
    def setConfidenceThresholdCol(self, value):
        """
        Args:
            confidenceThreshold: Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        """
        self._java_obj = self._java_obj.setConfidenceThresholdCol(value)
        return self
    
    def setCustomHeaders(self, value):
        """
        Args:
            customHeaders: Map of Custom Header Key-Value Tuples.
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setCustomHeaders(value)
        return self
    
    def setCustomHeadersCol(self, value):
        """
        Args:
            customHeaders: Map of Custom Header Key-Value Tuples.
        """
        self._java_obj = self._java_obj.setCustomHeadersCol(value)
        return self
    
    def setCustomUrlRoot(self, value):
        """
        Args:
            customUrlRoot: The custom URL root for the service. This will not append OpenAI specific model path completions (i.e. /chat/completions) to the URL.
        """
        self._set(customUrlRoot=value)
        return self
    
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
        self._set(errorCol=value)
        return self
    
    def setFaceIds(self, value):
        """
        Args:
            faceIds: Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setFaceIds(value)
        return self
    
    def setFaceIdsCol(self, value):
        """
        Args:
            faceIds: Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        """
        self._java_obj = self._java_obj.setFaceIdsCol(value)
        return self
    
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
        self._set(handler=value)
        return self
    
    def setLargePersonGroupId(self, value):
        """
        Args:
            largePersonGroupId: largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setLargePersonGroupId(value)
        return self
    
    def setLargePersonGroupIdCol(self, value):
        """
        Args:
            largePersonGroupId: largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
        self._java_obj = self._java_obj.setLargePersonGroupIdCol(value)
        return self
    
    def setMaxNumOfCandidatesReturned(self, value):
        """
        Args:
            maxNumOfCandidatesReturned: The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setMaxNumOfCandidatesReturned(value)
        return self
    
    def setMaxNumOfCandidatesReturnedCol(self, value):
        """
        Args:
            maxNumOfCandidatesReturned: The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        """
        self._java_obj = self._java_obj.setMaxNumOfCandidatesReturnedCol(value)
        return self
    
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
        self._set(outputCol=value)
        return self
    
    def setPersonGroupId(self, value):
        """
        Args:
            personGroupId: personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setPersonGroupId(value)
        return self
    
    def setPersonGroupIdCol(self, value):
        """
        Args:
            personGroupId: personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
        self._java_obj = self._java_obj.setPersonGroupIdCol(value)
        return self
    
    def setSubscriptionKey(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setSubscriptionKey(value)
        return self
    
    def setSubscriptionKeyCol(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
        self._java_obj = self._java_obj.setSubscriptionKeyCol(value)
        return self
    
    def setTelemHeaders(self, value):
        """
        Args:
            telemHeaders: Map of Custom Header Key-Value Tuples.
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.com.microsoft.azure.synapse.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setTelemHeaders(value)
        return self
    
    def setTelemHeadersCol(self, value):
        """
        Args:
            telemHeaders: Map of Custom Header Key-Value Tuples.
        """
        self._java_obj = self._java_obj.setTelemHeadersCol(value)
        return self
    
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
        """
        self._set(timeout=value)
        return self
    
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
        self._set(url=value)
        return self

    
    def getAADToken(self):
        """
        Returns:
            AADToken: AAD Token used for authentication
        """
        return self._java_obj.getAADToken()
    
    
    def getCustomAuthHeader(self):
        """
        Returns:
            CustomAuthHeader: A Custom Value for Authorization Header
        """
        return self._java_obj.getCustomAuthHeader()
    
    
    def getConcurrency(self):
        """
        Returns:
            concurrency: max number of concurrent calls
        """
        return self.getOrDefault(self.concurrency)
    
    
    def getConcurrentTimeout(self):
        """
        Returns:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
        return self.getOrDefault(self.concurrentTimeout)
    
    
    def getConfidenceThreshold(self):
        """
        Returns:
            confidenceThreshold: Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        """
        return self._java_obj.getConfidenceThreshold()
    
    
    def getCustomHeaders(self):
        """
        Returns:
            customHeaders: Map of Custom Header Key-Value Tuples.
        """
        return self._java_obj.getCustomHeaders()
    
    
    def getCustomUrlRoot(self):
        """
        Returns:
            customUrlRoot: The custom URL root for the service. This will not append OpenAI specific model path completions (i.e. /chat/completions) to the URL.
        """
        return self.getOrDefault(self.customUrlRoot)
    
    
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
        return self.getOrDefault(self.errorCol)
    
    
    def getFaceIds(self):
        """
        Returns:
            faceIds: Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        """
        return self._java_obj.getFaceIds()
    
    
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
        return self.getOrDefault(self.handler)
    
    
    def getLargePersonGroupId(self):
        """
        Returns:
            largePersonGroupId: largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
        return self._java_obj.getLargePersonGroupId()
    
    
    def getMaxNumOfCandidatesReturned(self):
        """
        Returns:
            maxNumOfCandidatesReturned: The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        """
        return self._java_obj.getMaxNumOfCandidatesReturned()
    
    
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
        return self.getOrDefault(self.outputCol)
    
    
    def getPersonGroupId(self):
        """
        Returns:
            personGroupId: personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
        return self._java_obj.getPersonGroupId()
    
    
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
        return self._java_obj.getSubscriptionKey()
    
    
    def getTelemHeaders(self):
        """
        Returns:
            telemHeaders: Map of Custom Header Key-Value Tuples.
        """
        return self._java_obj.getTelemHeaders()
    
    
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
        """
        return self.getOrDefault(self.timeout)
    
    
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
        return self.getOrDefault(self.url)

    

    def setCustomServiceName(self, value):
        self._java_obj = self._java_obj.setCustomServiceName(value)
        return self
    
    def setEndpoint(self, value):
        self._java_obj = self._java_obj.setEndpoint(value)
        return self
    
    def setDefaultInternalEndpoint(self, value):
        self._java_obj = self._java_obj.setDefaultInternalEndpoint(value)
        return self
    
    def _transform(self, dataset: DataFrame) -> DataFrame:
        return super()._transform(dataset)
    
    def setLocation(self, value):
        self._java_obj = self._java_obj.setLocation(value)
        return self
    
    def setLinkedService(self, value):
        self._java_obj = self._java_obj.setLinkedService(value)
        return self
        