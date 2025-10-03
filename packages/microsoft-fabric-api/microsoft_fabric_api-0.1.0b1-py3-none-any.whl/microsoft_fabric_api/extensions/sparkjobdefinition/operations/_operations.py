from ....generated.sparkjobdefinition.operations import *
from ....generated.sparkjobdefinition import operations as _operations
from ....generated.sparkjobdefinition import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Sparkjobdefinition."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_spark_job_definition(self, workspace_id: None, create_spark_job_definition_request: None) -> _models.SparkJobDefinition:
        """Creates a spark job definition in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create spark job definition with a public definition, refer to `Spark job definition
        </rest/api/fabric/articles/item-management/definitions/spark-job-definition>`_ article.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a spark job definition the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_spark_job_definition_request: Create item request payload. Required.
        :type create_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.CreateSparkJobDefinitionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SparkJobDefinition
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_spark_job_definition(workspace_id=workspace_id, create_spark_job_definition_request=create_spark_job_definition_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_spark_job_definition(self, workspace_id: None, create_spark_job_definition_request: None) -> _LROResultExtractor[_models.SparkJobDefinition]:
        """Creates a spark job definition in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create spark job definition with a public definition, refer to `Spark job definition
        </rest/api/fabric/articles/item-management/definitions/spark-job-definition>`_ article.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a spark job definition the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_spark_job_definition_request: Create item request payload. Required.
        :type create_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.CreateSparkJobDefinitionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SparkJobDefinition
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SparkJobDefinition]()

        poller = super().begin_create_spark_job_definition(
            workspace_id=workspace_id,
            create_spark_job_definition_request=create_spark_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_spark_job_definition(self, workspace_id: None, create_spark_job_definition_request: None) -> _models.SparkJobDefinition:
        """Creates a spark job definition in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create spark job definition with a public definition, refer to `Spark job definition
        </rest/api/fabric/articles/item-management/definitions/spark-job-definition>`_ article.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a spark job definition the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_spark_job_definition_request: Create item request payload. Required.
        :type create_spark_job_definition_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SparkJobDefinition
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_spark_job_definition(workspace_id=workspace_id, create_spark_job_definition_request=create_spark_job_definition_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_spark_job_definition(self, workspace_id: None, create_spark_job_definition_request: None) -> _LROResultExtractor[_models.SparkJobDefinition]:
        """Creates a spark job definition in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create spark job definition with a public definition, refer to `Spark job definition
        </rest/api/fabric/articles/item-management/definitions/spark-job-definition>`_ article.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a spark job definition the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_spark_job_definition_request: Create item request payload. Required.
        :type create_spark_job_definition_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SparkJobDefinition
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SparkJobDefinition]()

        poller = super().begin_create_spark_job_definition(
            workspace_id=workspace_id,
            create_spark_job_definition_request=create_spark_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_spark_job_definition(self, workspace_id: None, create_spark_job_definition_request: None) -> _models.SparkJobDefinition:
        """Creates a spark job definition in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create spark job definition with a public definition, refer to `Spark job definition
        </rest/api/fabric/articles/item-management/definitions/spark-job-definition>`_ article.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a spark job definition the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_spark_job_definition_request: Create item request payload. Is either a
         CreateSparkJobDefinitionRequest type or a IO[bytes] type. Required.
        :type create_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.CreateSparkJobDefinitionRequest or IO[bytes]
        :return: An instance of LROPoller that returns SparkJobDefinition
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_spark_job_definition(workspace_id=workspace_id, create_spark_job_definition_request=create_spark_job_definition_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_spark_job_definition(self, workspace_id: None, create_spark_job_definition_request: None) -> _LROResultExtractor[_models.SparkJobDefinition]:
        """Creates a spark job definition in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create spark job definition with a public definition, refer to `Spark job definition
        </rest/api/fabric/articles/item-management/definitions/spark-job-definition>`_ article.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a spark job definition the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_spark_job_definition_request: Create item request payload. Is either a
         CreateSparkJobDefinitionRequest type or a IO[bytes] type. Required.
        :type create_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.CreateSparkJobDefinitionRequest or IO[bytes]
        :return: An instance of LROPoller that returns SparkJobDefinition
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SparkJobDefinition]()

        poller = super().begin_create_spark_job_definition(
            workspace_id=workspace_id,
            create_spark_job_definition_request=create_spark_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None) -> _models.SparkJobDefinitionResponse:
        """Returns the specified spark job definition public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a spark job definition's public definition, the sensitivity label is not a part of
        the definition.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a spark job definition with an encrypted sensitivity label.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :keyword format: The format of the spark job definition public definition. Default value is
         None.
        :paramtype format: str
        :return: An instance of LROPoller that returns SparkJobDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_spark_job_definition_definition(workspace_id=workspace_id, spark_job_definition_id=spark_job_definition_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None) -> _LROResultExtractor[_models.SparkJobDefinitionResponse]:
        """Returns the specified spark job definition public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a spark job definition's public definition, the sensitivity label is not a part of
        the definition.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a spark job definition with an encrypted sensitivity label.

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :keyword format: The format of the spark job definition public definition. Default value is
         None.
        :paramtype format: str
        :return: An instance of LROPoller that returns SparkJobDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sparkjobdefinition.models.SparkJobDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SparkJobDefinitionResponse]()

        poller = super().begin_get_spark_job_definition_definition(
            workspace_id=workspace_id,
            spark_job_definition_id=spark_job_definition_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None, update_spark_job_definition_request: None) -> None:
        """Overrides the definition for the specified spark job definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the spark job definition's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :param update_spark_job_definition_request: Update spark job definition definition request
         payload. Required.
        :type update_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.UpdateSparkJobDefinitionDefinitionRequest
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_spark_job_definition_definition(
            workspace_id=workspace_id,
            spark_job_definition_id=spark_job_definition_id,
            update_spark_job_definition_request=update_spark_job_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None, update_spark_job_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified spark job definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the spark job definition's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :param update_spark_job_definition_request: Update spark job definition definition request
         payload. Required.
        :type update_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.UpdateSparkJobDefinitionDefinitionRequest
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_spark_job_definition_definition(
            workspace_id=workspace_id,
            spark_job_definition_id=spark_job_definition_id,
            update_spark_job_definition_request=update_spark_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None, update_spark_job_definition_request: None) -> None:
        """Overrides the definition for the specified spark job definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the spark job definition's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :param update_spark_job_definition_request: Update spark job definition definition request
         payload. Required.
        :type update_spark_job_definition_request: IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_spark_job_definition_definition(
            workspace_id=workspace_id,
            spark_job_definition_id=spark_job_definition_id,
            update_spark_job_definition_request=update_spark_job_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None, update_spark_job_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified spark job definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the spark job definition's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :param update_spark_job_definition_request: Update spark job definition definition request
         payload. Required.
        :type update_spark_job_definition_request: IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_spark_job_definition_definition(
            workspace_id=workspace_id,
            spark_job_definition_id=spark_job_definition_id,
            update_spark_job_definition_request=update_spark_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None, update_spark_job_definition_request: None) -> None:
        """Overrides the definition for the specified spark job definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the spark job definition's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :param update_spark_job_definition_request: Update spark job definition definition request
         payload. Is either a UpdateSparkJobDefinitionDefinitionRequest type or a IO[bytes] type.
         Required.
        :type update_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.UpdateSparkJobDefinitionDefinitionRequest or
         IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_spark_job_definition_definition(
            workspace_id=workspace_id,
            spark_job_definition_id=spark_job_definition_id,
            update_spark_job_definition_request=update_spark_job_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_spark_job_definition_definition(self, workspace_id: None, spark_job_definition_id: None, update_spark_job_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified spark job definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the spark job definition's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the spark job definition.

        Required Delegated Scopes
        -------------------------

         SparkJobDefinition.ReadWrite.All or Item.ReadWrite.All

        Microsoft Entra supported identities
        ------------------------------------

        This API supports the Microsoft `identities </rest/api/fabric/articles/identity-support>`_
        listed in this section.

        .. list-table::
           :header-rows: 1

           * - Identity
             - Support
           * - User
             - Yes
           * - `Service principal
        </entra/identity-platform/app-objects-and-service-principals#service-principal-object>`_ and
        `Managed identities </entra/identity/managed-identities-azure-resources/overview>`_
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param spark_job_definition_id: The spark job definition ID. Required.
        :type spark_job_definition_id: str
        :param update_spark_job_definition_request: Update spark job definition definition request
         payload. Is either a UpdateSparkJobDefinitionDefinitionRequest type or a IO[bytes] type.
         Required.
        :type update_spark_job_definition_request:
         ~microsoft.fabric.api.sparkjobdefinition.models.UpdateSparkJobDefinitionDefinitionRequest or
         IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_spark_job_definition_definition(
            workspace_id=workspace_id,
            spark_job_definition_id=spark_job_definition_id,
            update_spark_job_definition_request=update_spark_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
