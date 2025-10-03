from ....generated.digitaltwinbuilderflow.operations import *
from ....generated.digitaltwinbuilderflow import operations as _operations
from ....generated.digitaltwinbuilderflow import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Digitaltwinbuilderflow."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_digital_twin_builder_flow(self, workspace_id: None, create_digital_twin_builder_flow_request: None) -> _models.DigitalTwinBuilderFlow:
        """Creates a Digital Twin Builder Flow in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Digital Twin Builder Flow with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-flow-definition>`_
        article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Digital Twin Builder Flow the workspace must be on a supported Fabric capacity.
        For more information see: `Microsoft Fabric license types
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
        :param create_digital_twin_builder_flow_request: Create item request payload. Required.
        :type create_digital_twin_builder_flow_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.CreateDigitalTwinBuilderFlowRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlow
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlow]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_digital_twin_builder_flow(workspace_id=workspace_id, create_digital_twin_builder_flow_request=create_digital_twin_builder_flow_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_digital_twin_builder_flow(self, workspace_id: None, create_digital_twin_builder_flow_request: None) -> _LROResultExtractor[_models.DigitalTwinBuilderFlow]:
        """Creates a Digital Twin Builder Flow in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Digital Twin Builder Flow with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-flow-definition>`_
        article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Digital Twin Builder Flow the workspace must be on a supported Fabric capacity.
        For more information see: `Microsoft Fabric license types
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
        :param create_digital_twin_builder_flow_request: Create item request payload. Required.
        :type create_digital_twin_builder_flow_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.CreateDigitalTwinBuilderFlowRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlow
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlow]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilderFlow]()

        poller = super().begin_create_digital_twin_builder_flow(
            workspace_id=workspace_id,
            create_digital_twin_builder_flow_request=create_digital_twin_builder_flow_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_digital_twin_builder_flow(self, workspace_id: None, create_digital_twin_builder_flow_request: None) -> _models.DigitalTwinBuilderFlow:
        """Creates a Digital Twin Builder Flow in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Digital Twin Builder Flow with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-flow-definition>`_
        article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Digital Twin Builder Flow the workspace must be on a supported Fabric capacity.
        For more information see: `Microsoft Fabric license types
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
        :param create_digital_twin_builder_flow_request: Create item request payload. Required.
        :type create_digital_twin_builder_flow_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlow
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlow]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_digital_twin_builder_flow(workspace_id=workspace_id, create_digital_twin_builder_flow_request=create_digital_twin_builder_flow_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_digital_twin_builder_flow(self, workspace_id: None, create_digital_twin_builder_flow_request: None) -> _LROResultExtractor[_models.DigitalTwinBuilderFlow]:
        """Creates a Digital Twin Builder Flow in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Digital Twin Builder Flow with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-flow-definition>`_
        article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Digital Twin Builder Flow the workspace must be on a supported Fabric capacity.
        For more information see: `Microsoft Fabric license types
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
        :param create_digital_twin_builder_flow_request: Create item request payload. Required.
        :type create_digital_twin_builder_flow_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlow
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlow]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilderFlow]()

        poller = super().begin_create_digital_twin_builder_flow(
            workspace_id=workspace_id,
            create_digital_twin_builder_flow_request=create_digital_twin_builder_flow_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_digital_twin_builder_flow(self, workspace_id: None, create_digital_twin_builder_flow_request: None) -> _models.DigitalTwinBuilderFlow:
        """Creates a Digital Twin Builder Flow in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Digital Twin Builder Flow with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-flow-definition>`_
        article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Digital Twin Builder Flow the workspace must be on a supported Fabric capacity.
        For more information see: `Microsoft Fabric license types
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
        :param create_digital_twin_builder_flow_request: Create item request payload. Is either a
         CreateDigitalTwinBuilderFlowRequest type or a IO[bytes] type. Required.
        :type create_digital_twin_builder_flow_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.CreateDigitalTwinBuilderFlowRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlow
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlow]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_digital_twin_builder_flow(workspace_id=workspace_id, create_digital_twin_builder_flow_request=create_digital_twin_builder_flow_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_digital_twin_builder_flow(self, workspace_id: None, create_digital_twin_builder_flow_request: None) -> _LROResultExtractor[_models.DigitalTwinBuilderFlow]:
        """Creates a Digital Twin Builder Flow in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Digital Twin Builder Flow with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-flow-definition>`_
        article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Digital Twin Builder Flow the workspace must be on a supported Fabric capacity.
        For more information see: `Microsoft Fabric license types
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
        :param create_digital_twin_builder_flow_request: Create item request payload. Is either a
         CreateDigitalTwinBuilderFlowRequest type or a IO[bytes] type. Required.
        :type create_digital_twin_builder_flow_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.CreateDigitalTwinBuilderFlowRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlow
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlow]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilderFlow]()

        poller = super().begin_create_digital_twin_builder_flow(
            workspace_id=workspace_id,
            create_digital_twin_builder_flow_request=create_digital_twin_builder_flow_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None) -> _models.DigitalTwinBuilderFlowDefinitionResponse:
        """Returns the specified Digital Twin Builder Flow public definition.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a Digital Twin Builder Flow's public definition, the sensitivity label is not a
        part of the definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlowDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlowDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_digital_twin_builder_flow_definition(workspace_id=workspace_id, digital_twin_builder_flow_id=digital_twin_builder_flow_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None) -> _LROResultExtractor[_models.DigitalTwinBuilderFlowDefinitionResponse]:
        """Returns the specified Digital Twin Builder Flow public definition.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a Digital Twin Builder Flow's public definition, the sensitivity label is not a
        part of the definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderFlowDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilderflow.models.DigitalTwinBuilderFlowDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilderFlowDefinitionResponse]()

        poller = super().begin_get_digital_twin_builder_flow_definition(
            workspace_id=workspace_id,
            digital_twin_builder_flow_id=digital_twin_builder_flow_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None, update_digital_twin_builder_flow_definition_request: None) -> None:
        """Overrides the definition for the specified Digital Twin Builder Flow.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Digital Twin Builder Flow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :param update_digital_twin_builder_flow_definition_request: Update Digital Twin Builder Flow
         definition request payload. Required.
        :type update_digital_twin_builder_flow_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.UpdateDigitalTwinBuilderFlowDefinitionRequest
        :keyword update_metadata: When set to true and the Digital Twin Builder Flow.platform file is
         provided as part of the definition, the item's metadata is updated using the metadata in the
         Digital Twin Builder Flow.platform file. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_digital_twin_builder_flow_definition(
            workspace_id=workspace_id,
            digital_twin_builder_flow_id=digital_twin_builder_flow_id,
            update_digital_twin_builder_flow_definition_request=update_digital_twin_builder_flow_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None, update_digital_twin_builder_flow_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Digital Twin Builder Flow.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Digital Twin Builder Flow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :param update_digital_twin_builder_flow_definition_request: Update Digital Twin Builder Flow
         definition request payload. Required.
        :type update_digital_twin_builder_flow_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.UpdateDigitalTwinBuilderFlowDefinitionRequest
        :keyword update_metadata: When set to true and the Digital Twin Builder Flow.platform file is
         provided as part of the definition, the item's metadata is updated using the metadata in the
         Digital Twin Builder Flow.platform file. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_digital_twin_builder_flow_definition(
            workspace_id=workspace_id,
            digital_twin_builder_flow_id=digital_twin_builder_flow_id,
            update_digital_twin_builder_flow_definition_request=update_digital_twin_builder_flow_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None, update_digital_twin_builder_flow_definition_request: None) -> None:
        """Overrides the definition for the specified Digital Twin Builder Flow.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Digital Twin Builder Flow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :param update_digital_twin_builder_flow_definition_request: Update Digital Twin Builder Flow
         definition request payload. Required.
        :type update_digital_twin_builder_flow_definition_request: IO[bytes]
        :keyword update_metadata: When set to true and the Digital Twin Builder Flow.platform file is
         provided as part of the definition, the item's metadata is updated using the metadata in the
         Digital Twin Builder Flow.platform file. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_digital_twin_builder_flow_definition(
            workspace_id=workspace_id,
            digital_twin_builder_flow_id=digital_twin_builder_flow_id,
            update_digital_twin_builder_flow_definition_request=update_digital_twin_builder_flow_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None, update_digital_twin_builder_flow_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Digital Twin Builder Flow.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Digital Twin Builder Flow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :param update_digital_twin_builder_flow_definition_request: Update Digital Twin Builder Flow
         definition request payload. Required.
        :type update_digital_twin_builder_flow_definition_request: IO[bytes]
        :keyword update_metadata: When set to true and the Digital Twin Builder Flow.platform file is
         provided as part of the definition, the item's metadata is updated using the metadata in the
         Digital Twin Builder Flow.platform file. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_digital_twin_builder_flow_definition(
            workspace_id=workspace_id,
            digital_twin_builder_flow_id=digital_twin_builder_flow_id,
            update_digital_twin_builder_flow_definition_request=update_digital_twin_builder_flow_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None, update_digital_twin_builder_flow_definition_request: None) -> None:
        """Overrides the definition for the specified Digital Twin Builder Flow.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Digital Twin Builder Flow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :param update_digital_twin_builder_flow_definition_request: Update Digital Twin Builder Flow
         definition request payload. Is either a UpdateDigitalTwinBuilderFlowDefinitionRequest type or a
         IO[bytes] type. Required.
        :type update_digital_twin_builder_flow_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.UpdateDigitalTwinBuilderFlowDefinitionRequest
         or IO[bytes]
        :keyword update_metadata: When set to true and the Digital Twin Builder Flow.platform file is
         provided as part of the definition, the item's metadata is updated using the metadata in the
         Digital Twin Builder Flow.platform file. Default value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_digital_twin_builder_flow_definition(
            workspace_id=workspace_id,
            digital_twin_builder_flow_id=digital_twin_builder_flow_id,
            update_digital_twin_builder_flow_definition_request=update_digital_twin_builder_flow_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_digital_twin_builder_flow_definition(self, workspace_id: None, digital_twin_builder_flow_id: None, update_digital_twin_builder_flow_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Digital Twin Builder Flow.

        ..

           [!NOTE]
           Digital Twin Builder Flow item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Digital Twin Builder Flow's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder flow.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilderFlow.ReadWrite.All or Item.ReadWrite.All

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
        :param digital_twin_builder_flow_id: The Digital Twin Builder Flow ID. Required.
        :type digital_twin_builder_flow_id: str
        :param update_digital_twin_builder_flow_definition_request: Update Digital Twin Builder Flow
         definition request payload. Is either a UpdateDigitalTwinBuilderFlowDefinitionRequest type or a
         IO[bytes] type. Required.
        :type update_digital_twin_builder_flow_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilderflow.models.UpdateDigitalTwinBuilderFlowDefinitionRequest
         or IO[bytes]
        :keyword update_metadata: When set to true and the Digital Twin Builder Flow.platform file is
         provided as part of the definition, the item's metadata is updated using the metadata in the
         Digital Twin Builder Flow.platform file. Default value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_digital_twin_builder_flow_definition(
            workspace_id=workspace_id,
            digital_twin_builder_flow_id=digital_twin_builder_flow_id,
            update_digital_twin_builder_flow_definition_request=update_digital_twin_builder_flow_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
