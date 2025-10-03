from ....generated.datapipeline.operations import *
from ....generated.datapipeline import operations as _operations
from ....generated.datapipeline import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Datapipeline."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_data_pipeline(self, workspace_id: None, create_data_pipeline_request: None) -> _models.DataPipeline:
        """Creates a data pipeline in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a data pipeline, the workspace must be on a supported Fabric capacity.

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
        :param create_data_pipeline_request: Create item request payload. Required.
        :type create_data_pipeline_request:
         ~microsoft.fabric.api.datapipeline.models.CreateDataPipelineRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DataPipeline
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipeline]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_data_pipeline(workspace_id=workspace_id, create_data_pipeline_request=create_data_pipeline_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_data_pipeline(self, workspace_id: None, create_data_pipeline_request: None) -> _LROResultExtractor[_models.DataPipeline]:
        """Creates a data pipeline in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a data pipeline, the workspace must be on a supported Fabric capacity.

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
        :param create_data_pipeline_request: Create item request payload. Required.
        :type create_data_pipeline_request:
         ~microsoft.fabric.api.datapipeline.models.CreateDataPipelineRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DataPipeline
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipeline]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DataPipeline]()

        poller = super().begin_create_data_pipeline(
            workspace_id=workspace_id,
            create_data_pipeline_request=create_data_pipeline_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_data_pipeline(self, workspace_id: None, create_data_pipeline_request: None) -> _models.DataPipeline:
        """Creates a data pipeline in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a data pipeline, the workspace must be on a supported Fabric capacity.

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
        :param create_data_pipeline_request: Create item request payload. Required.
        :type create_data_pipeline_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DataPipeline
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipeline]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_data_pipeline(workspace_id=workspace_id, create_data_pipeline_request=create_data_pipeline_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_data_pipeline(self, workspace_id: None, create_data_pipeline_request: None) -> _LROResultExtractor[_models.DataPipeline]:
        """Creates a data pipeline in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a data pipeline, the workspace must be on a supported Fabric capacity.

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
        :param create_data_pipeline_request: Create item request payload. Required.
        :type create_data_pipeline_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DataPipeline
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipeline]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DataPipeline]()

        poller = super().begin_create_data_pipeline(
            workspace_id=workspace_id,
            create_data_pipeline_request=create_data_pipeline_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_data_pipeline(self, workspace_id: None, create_data_pipeline_request: None) -> _models.DataPipeline:
        """Creates a data pipeline in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a data pipeline, the workspace must be on a supported Fabric capacity.

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
        :param create_data_pipeline_request: Create item request payload. Is either a
         CreateDataPipelineRequest type or a IO[bytes] type. Required.
        :type create_data_pipeline_request:
         ~microsoft.fabric.api.datapipeline.models.CreateDataPipelineRequest or IO[bytes]
        :return: An instance of LROPoller that returns DataPipeline
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipeline]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_data_pipeline(workspace_id=workspace_id, create_data_pipeline_request=create_data_pipeline_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_data_pipeline(self, workspace_id: None, create_data_pipeline_request: None) -> _LROResultExtractor[_models.DataPipeline]:
        """Creates a data pipeline in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a data pipeline, the workspace must be on a supported Fabric capacity.

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
        :param create_data_pipeline_request: Create item request payload. Is either a
         CreateDataPipelineRequest type or a IO[bytes] type. Required.
        :type create_data_pipeline_request:
         ~microsoft.fabric.api.datapipeline.models.CreateDataPipelineRequest or IO[bytes]
        :return: An instance of LROPoller that returns DataPipeline
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipeline]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DataPipeline]()

        poller = super().begin_create_data_pipeline(
            workspace_id=workspace_id,
            create_data_pipeline_request=create_data_pipeline_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None) -> _models.DataPipelineDefinitionResponse:
        """Returns the specified data pipeline public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a DataPipeline's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :keyword format: The format of the data pipeline public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns DataPipelineDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipelineDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_data_pipeline_definition(workspace_id=workspace_id, data_pipeline_id=data_pipeline_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None) -> _LROResultExtractor[_models.DataPipelineDefinitionResponse]:
        """Returns the specified data pipeline public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a DataPipeline's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :keyword format: The format of the data pipeline public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns DataPipelineDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.datapipeline.models.DataPipelineDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DataPipelineDefinitionResponse]()

        poller = super().begin_get_data_pipeline_definition(
            workspace_id=workspace_id,
            data_pipeline_id=data_pipeline_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None, update_pipeline_definition_request: None) -> None:
        """Overrides the definition for the specified data pipeline.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the DataPipeline's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :param update_pipeline_definition_request: Update data pipeline definition request payload.
         Required.
        :type update_pipeline_definition_request:
         ~microsoft.fabric.api.datapipeline.models.UpdateDataPipelineDefinitionRequest
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

        
        poller = self.begin_update_data_pipeline_definition(
            workspace_id=workspace_id,
            data_pipeline_id=data_pipeline_id,
            update_pipeline_definition_request=update_pipeline_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None, update_pipeline_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified data pipeline.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the DataPipeline's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :param update_pipeline_definition_request: Update data pipeline definition request payload.
         Required.
        :type update_pipeline_definition_request:
         ~microsoft.fabric.api.datapipeline.models.UpdateDataPipelineDefinitionRequest
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

        

        return super().begin_update_data_pipeline_definition(
            workspace_id=workspace_id,
            data_pipeline_id=data_pipeline_id,
            update_pipeline_definition_request=update_pipeline_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None, update_pipeline_definition_request: None) -> None:
        """Overrides the definition for the specified data pipeline.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the DataPipeline's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :param update_pipeline_definition_request: Update data pipeline definition request payload.
         Required.
        :type update_pipeline_definition_request: IO[bytes]
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

        
        poller = self.begin_update_data_pipeline_definition(
            workspace_id=workspace_id,
            data_pipeline_id=data_pipeline_id,
            update_pipeline_definition_request=update_pipeline_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None, update_pipeline_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified data pipeline.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the DataPipeline's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :param update_pipeline_definition_request: Update data pipeline definition request payload.
         Required.
        :type update_pipeline_definition_request: IO[bytes]
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

        

        return super().begin_update_data_pipeline_definition(
            workspace_id=workspace_id,
            data_pipeline_id=data_pipeline_id,
            update_pipeline_definition_request=update_pipeline_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None, update_pipeline_definition_request: None) -> None:
        """Overrides the definition for the specified data pipeline.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the DataPipeline's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :param update_pipeline_definition_request: Update data pipeline definition request payload. Is
         either a UpdateDataPipelineDefinitionRequest type or a IO[bytes] type. Required.
        :type update_pipeline_definition_request:
         ~microsoft.fabric.api.datapipeline.models.UpdateDataPipelineDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_data_pipeline_definition(
            workspace_id=workspace_id,
            data_pipeline_id=data_pipeline_id,
            update_pipeline_definition_request=update_pipeline_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_data_pipeline_definition(self, workspace_id: None, data_pipeline_id: None, update_pipeline_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified data pipeline.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the DataPipeline's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the data pipeline.

        Required Delegated Scopes
        -------------------------

         DataPipeline.ReadWrite.All or Item.ReadWrite.All

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
        :param data_pipeline_id: The data pipeline ID. Required.
        :type data_pipeline_id: str
        :param update_pipeline_definition_request: Update data pipeline definition request payload. Is
         either a UpdateDataPipelineDefinitionRequest type or a IO[bytes] type. Required.
        :type update_pipeline_definition_request:
         ~microsoft.fabric.api.datapipeline.models.UpdateDataPipelineDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_data_pipeline_definition(
            workspace_id=workspace_id,
            data_pipeline_id=data_pipeline_id,
            update_pipeline_definition_request=update_pipeline_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
