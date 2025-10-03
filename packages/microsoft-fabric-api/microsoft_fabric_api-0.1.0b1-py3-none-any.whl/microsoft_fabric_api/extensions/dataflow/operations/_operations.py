from ....generated.dataflow.operations import *
from ....generated.dataflow import operations as _operations
from ....generated.dataflow import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Dataflow."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_dataflow(self, workspace_id: None, create_dataflow_request: None) -> _models.Dataflow:
        """Creates a Dataflow in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Dataflow with a public definition, refer to `Dataflow
        </rest/api/fabric/articles/item-management/definitions/dataflow-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Dataflow the workspace must be on a supported Fabric capacity. For more
        information see: `Microsoft Fabric license types
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
        :param create_dataflow_request: Create item request payload. Required.
        :type create_dataflow_request: ~microsoft.fabric.api.dataflow.models.CreateDataflowRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Dataflow
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.Dataflow]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_dataflow(workspace_id=workspace_id, create_dataflow_request=create_dataflow_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_dataflow(self, workspace_id: None, create_dataflow_request: None) -> _LROResultExtractor[_models.Dataflow]:
        """Creates a Dataflow in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Dataflow with a public definition, refer to `Dataflow
        </rest/api/fabric/articles/item-management/definitions/dataflow-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Dataflow the workspace must be on a supported Fabric capacity. For more
        information see: `Microsoft Fabric license types
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
        :param create_dataflow_request: Create item request payload. Required.
        :type create_dataflow_request: ~microsoft.fabric.api.dataflow.models.CreateDataflowRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Dataflow
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.Dataflow]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Dataflow]()

        poller = super().begin_create_dataflow(
            workspace_id=workspace_id,
            create_dataflow_request=create_dataflow_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_dataflow(self, workspace_id: None, create_dataflow_request: None) -> _models.Dataflow:
        """Creates a Dataflow in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Dataflow with a public definition, refer to `Dataflow
        </rest/api/fabric/articles/item-management/definitions/dataflow-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Dataflow the workspace must be on a supported Fabric capacity. For more
        information see: `Microsoft Fabric license types
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
        :param create_dataflow_request: Create item request payload. Required.
        :type create_dataflow_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Dataflow
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.Dataflow]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_dataflow(workspace_id=workspace_id, create_dataflow_request=create_dataflow_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_dataflow(self, workspace_id: None, create_dataflow_request: None) -> _LROResultExtractor[_models.Dataflow]:
        """Creates a Dataflow in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Dataflow with a public definition, refer to `Dataflow
        </rest/api/fabric/articles/item-management/definitions/dataflow-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Dataflow the workspace must be on a supported Fabric capacity. For more
        information see: `Microsoft Fabric license types
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
        :param create_dataflow_request: Create item request payload. Required.
        :type create_dataflow_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Dataflow
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.Dataflow]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Dataflow]()

        poller = super().begin_create_dataflow(
            workspace_id=workspace_id,
            create_dataflow_request=create_dataflow_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_dataflow(self, workspace_id: None, create_dataflow_request: None) -> _models.Dataflow:
        """Creates a Dataflow in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Dataflow with a public definition, refer to `Dataflow
        </rest/api/fabric/articles/item-management/definitions/dataflow-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Dataflow the workspace must be on a supported Fabric capacity. For more
        information see: `Microsoft Fabric license types
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
        :param create_dataflow_request: Create item request payload. Is either a CreateDataflowRequest
         type or a IO[bytes] type. Required.
        :type create_dataflow_request: ~microsoft.fabric.api.dataflow.models.CreateDataflowRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Dataflow
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.Dataflow]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_dataflow(workspace_id=workspace_id, create_dataflow_request=create_dataflow_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_dataflow(self, workspace_id: None, create_dataflow_request: None) -> _LROResultExtractor[_models.Dataflow]:
        """Creates a Dataflow in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Dataflow with a public definition, refer to `Dataflow
        </rest/api/fabric/articles/item-management/definitions/dataflow-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Dataflow the workspace must be on a supported Fabric capacity. For more
        information see: `Microsoft Fabric license types
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
        :param create_dataflow_request: Create item request payload. Is either a CreateDataflowRequest
         type or a IO[bytes] type. Required.
        :type create_dataflow_request: ~microsoft.fabric.api.dataflow.models.CreateDataflowRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Dataflow
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.Dataflow]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Dataflow]()

        poller = super().begin_create_dataflow(
            workspace_id=workspace_id,
            create_dataflow_request=create_dataflow_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_dataflow_definition(self, workspace_id: None, dataflow_id: None) -> _models.DataflowDefinitionResponse:
        """Returns the specified Dataflow public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a Dataflow's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :return: An instance of LROPoller that returns DataflowDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.DataflowDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_dataflow_definition(workspace_id=workspace_id, dataflow_id=dataflow_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_dataflow_definition(self, workspace_id: None, dataflow_id: None) -> _LROResultExtractor[_models.DataflowDefinitionResponse]:
        """Returns the specified Dataflow public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a Dataflow's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :return: An instance of LROPoller that returns DataflowDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.dataflow.models.DataflowDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DataflowDefinitionResponse]()

        poller = super().begin_get_dataflow_definition(
            workspace_id=workspace_id,
            dataflow_id=dataflow_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_dataflow_definition(self, workspace_id: None, dataflow_id: None, update_dataflow_definition_request: None) -> None:
        """Overrides the definition for the specified Dataflow.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Dataflow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :param update_dataflow_definition_request: Update Dataflow definition request payload.
         Required.
        :type update_dataflow_definition_request:
         ~microsoft.fabric.api.dataflow.models.UpdateDataflowDefinitionRequest
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

        
        poller = self.begin_update_dataflow_definition(
            workspace_id=workspace_id,
            dataflow_id=dataflow_id,
            update_dataflow_definition_request=update_dataflow_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_dataflow_definition(self, workspace_id: None, dataflow_id: None, update_dataflow_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Dataflow.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Dataflow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :param update_dataflow_definition_request: Update Dataflow definition request payload.
         Required.
        :type update_dataflow_definition_request:
         ~microsoft.fabric.api.dataflow.models.UpdateDataflowDefinitionRequest
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

        

        return super().begin_update_dataflow_definition(
            workspace_id=workspace_id,
            dataflow_id=dataflow_id,
            update_dataflow_definition_request=update_dataflow_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_dataflow_definition(self, workspace_id: None, dataflow_id: None, update_dataflow_definition_request: None) -> None:
        """Overrides the definition for the specified Dataflow.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Dataflow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :param update_dataflow_definition_request: Update Dataflow definition request payload.
         Required.
        :type update_dataflow_definition_request: IO[bytes]
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

        
        poller = self.begin_update_dataflow_definition(
            workspace_id=workspace_id,
            dataflow_id=dataflow_id,
            update_dataflow_definition_request=update_dataflow_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_dataflow_definition(self, workspace_id: None, dataflow_id: None, update_dataflow_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Dataflow.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Dataflow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :param update_dataflow_definition_request: Update Dataflow definition request payload.
         Required.
        :type update_dataflow_definition_request: IO[bytes]
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

        

        return super().begin_update_dataflow_definition(
            workspace_id=workspace_id,
            dataflow_id=dataflow_id,
            update_dataflow_definition_request=update_dataflow_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_dataflow_definition(self, workspace_id: None, dataflow_id: None, update_dataflow_definition_request: None) -> None:
        """Overrides the definition for the specified Dataflow.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Dataflow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :param update_dataflow_definition_request: Update Dataflow definition request payload. Is
         either a UpdateDataflowDefinitionRequest type or a IO[bytes] type. Required.
        :type update_dataflow_definition_request:
         ~microsoft.fabric.api.dataflow.models.UpdateDataflowDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_dataflow_definition(
            workspace_id=workspace_id,
            dataflow_id=dataflow_id,
            update_dataflow_definition_request=update_dataflow_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_dataflow_definition(self, workspace_id: None, dataflow_id: None, update_dataflow_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Dataflow.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Dataflow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the dataflow.

        Required Delegated Scopes
        -------------------------

         Dataflow.ReadWrite.All or Item.ReadWrite.All

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
        :param dataflow_id: The Dataflow ID. Required.
        :type dataflow_id: str
        :param update_dataflow_definition_request: Update Dataflow definition request payload. Is
         either a UpdateDataflowDefinitionRequest type or a IO[bytes] type. Required.
        :type update_dataflow_definition_request:
         ~microsoft.fabric.api.dataflow.models.UpdateDataflowDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_dataflow_definition(
            workspace_id=workspace_id,
            dataflow_id=dataflow_id,
            update_dataflow_definition_request=update_dataflow_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
