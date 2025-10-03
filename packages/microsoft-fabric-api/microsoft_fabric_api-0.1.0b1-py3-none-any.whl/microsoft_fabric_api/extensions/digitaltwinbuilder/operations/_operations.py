from ....generated.digitaltwinbuilder.operations import *
from ....generated.digitaltwinbuilder import operations as _operations
from ....generated.digitaltwinbuilder import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Digitaltwinbuilder."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_digital_twin_builder(self, workspace_id: None, create_digital_twin_builder_request: None) -> _models.DigitalTwinBuilder:
        """Creates a DigitalTwinBuilder in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create digitaltwinbuilder with definition, refer to `DigitalTwinBuilder definition
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a digitaltwinbuilder the workspace must be on a supported Fabric capacity. For more
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_digital_twin_builder_request: Create item request payload. Required.
        :type create_digital_twin_builder_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.CreateDigitalTwinBuilderRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilder
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilder]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_digital_twin_builder(workspace_id=workspace_id, create_digital_twin_builder_request=create_digital_twin_builder_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_digital_twin_builder(self, workspace_id: None, create_digital_twin_builder_request: None) -> _LROResultExtractor[_models.DigitalTwinBuilder]:
        """Creates a DigitalTwinBuilder in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create digitaltwinbuilder with definition, refer to `DigitalTwinBuilder definition
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a digitaltwinbuilder the workspace must be on a supported Fabric capacity. For more
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_digital_twin_builder_request: Create item request payload. Required.
        :type create_digital_twin_builder_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.CreateDigitalTwinBuilderRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilder
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilder]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilder]()

        poller = super().begin_create_digital_twin_builder(
            workspace_id=workspace_id,
            create_digital_twin_builder_request=create_digital_twin_builder_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_digital_twin_builder(self, workspace_id: None, create_digital_twin_builder_request: None) -> _models.DigitalTwinBuilder:
        """Creates a DigitalTwinBuilder in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create digitaltwinbuilder with definition, refer to `DigitalTwinBuilder definition
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a digitaltwinbuilder the workspace must be on a supported Fabric capacity. For more
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_digital_twin_builder_request: Create item request payload. Required.
        :type create_digital_twin_builder_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilder
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilder]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_digital_twin_builder(workspace_id=workspace_id, create_digital_twin_builder_request=create_digital_twin_builder_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_digital_twin_builder(self, workspace_id: None, create_digital_twin_builder_request: None) -> _LROResultExtractor[_models.DigitalTwinBuilder]:
        """Creates a DigitalTwinBuilder in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create digitaltwinbuilder with definition, refer to `DigitalTwinBuilder definition
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a digitaltwinbuilder the workspace must be on a supported Fabric capacity. For more
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_digital_twin_builder_request: Create item request payload. Required.
        :type create_digital_twin_builder_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DigitalTwinBuilder
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilder]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilder]()

        poller = super().begin_create_digital_twin_builder(
            workspace_id=workspace_id,
            create_digital_twin_builder_request=create_digital_twin_builder_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_digital_twin_builder(self, workspace_id: None, create_digital_twin_builder_request: None) -> _models.DigitalTwinBuilder:
        """Creates a DigitalTwinBuilder in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create digitaltwinbuilder with definition, refer to `DigitalTwinBuilder definition
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a digitaltwinbuilder the workspace must be on a supported Fabric capacity. For more
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_digital_twin_builder_request: Create item request payload. Is either a
         CreateDigitalTwinBuilderRequest type or a IO[bytes] type. Required.
        :type create_digital_twin_builder_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.CreateDigitalTwinBuilderRequest or IO[bytes]
        :return: An instance of LROPoller that returns DigitalTwinBuilder
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilder]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_digital_twin_builder(workspace_id=workspace_id, create_digital_twin_builder_request=create_digital_twin_builder_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_digital_twin_builder(self, workspace_id: None, create_digital_twin_builder_request: None) -> _LROResultExtractor[_models.DigitalTwinBuilder]:
        """Creates a DigitalTwinBuilder in the specified workspace.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create digitaltwinbuilder with definition, refer to `DigitalTwinBuilder definition
        </rest/api/fabric/articles/item-management/definitions/digital-twin-builder-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a digitaltwinbuilder the workspace must be on a supported Fabric capacity. For more
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_digital_twin_builder_request: Create item request payload. Is either a
         CreateDigitalTwinBuilderRequest type or a IO[bytes] type. Required.
        :type create_digital_twin_builder_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.CreateDigitalTwinBuilderRequest or IO[bytes]
        :return: An instance of LROPoller that returns DigitalTwinBuilder
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilder]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilder]()

        poller = super().begin_create_digital_twin_builder(
            workspace_id=workspace_id,
            create_digital_twin_builder_request=create_digital_twin_builder_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None) -> _models.DigitalTwinBuilderDefinitionResponse:
        """Returns the specified DigitalTwinBuilder public definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a digitaltwinbuilder public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a digitaltwinbuilder with an encrypted sensitivity label.

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :keyword format: The format of the DigitalTwinBuilder public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilderDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_digital_twin_builder_definition(workspace_id=workspace_id, digitaltwinbuilder_id=digitaltwinbuilder_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None) -> _LROResultExtractor[_models.DigitalTwinBuilderDefinitionResponse]:
        """Returns the specified DigitalTwinBuilder public definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a digitaltwinbuilder public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a digitaltwinbuilder with an encrypted sensitivity label.

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :keyword format: The format of the DigitalTwinBuilder public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns DigitalTwinBuilderDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.digitaltwinbuilder.models.DigitalTwinBuilderDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DigitalTwinBuilderDefinitionResponse]()

        poller = super().begin_get_digital_twin_builder_definition(
            workspace_id=workspace_id,
            digitaltwinbuilder_id=digitaltwinbuilder_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None, update_digital_twin_builder_definition_request: None) -> None:
        """Updates the definition of a specified DigitalTwinBuilder. The update overrides the current
        definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the digitaltwinbuilder definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :param update_digital_twin_builder_definition_request: Update digitaltwinbuilder definition
         request payload. Required.
        :type update_digital_twin_builder_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.UpdateDigitalTwinBuilderDefinitionRequest
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_digital_twin_builder_definition(
            workspace_id=workspace_id,
            digitaltwinbuilder_id=digitaltwinbuilder_id,
            update_digital_twin_builder_definition_request=update_digital_twin_builder_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None, update_digital_twin_builder_definition_request: None) -> LROPoller[None]:
        """Updates the definition of a specified DigitalTwinBuilder. The update overrides the current
        definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the digitaltwinbuilder definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :param update_digital_twin_builder_definition_request: Update digitaltwinbuilder definition
         request payload. Required.
        :type update_digital_twin_builder_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.UpdateDigitalTwinBuilderDefinitionRequest
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_digital_twin_builder_definition(
            workspace_id=workspace_id,
            digitaltwinbuilder_id=digitaltwinbuilder_id,
            update_digital_twin_builder_definition_request=update_digital_twin_builder_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None, update_digital_twin_builder_definition_request: None) -> None:
        """Updates the definition of a specified DigitalTwinBuilder. The update overrides the current
        definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the digitaltwinbuilder definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :param update_digital_twin_builder_definition_request: Update digitaltwinbuilder definition
         request payload. Required.
        :type update_digital_twin_builder_definition_request: IO[bytes]
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_digital_twin_builder_definition(
            workspace_id=workspace_id,
            digitaltwinbuilder_id=digitaltwinbuilder_id,
            update_digital_twin_builder_definition_request=update_digital_twin_builder_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None, update_digital_twin_builder_definition_request: None) -> LROPoller[None]:
        """Updates the definition of a specified DigitalTwinBuilder. The update overrides the current
        definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the digitaltwinbuilder definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :param update_digital_twin_builder_definition_request: Update digitaltwinbuilder definition
         request payload. Required.
        :type update_digital_twin_builder_definition_request: IO[bytes]
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_digital_twin_builder_definition(
            workspace_id=workspace_id,
            digitaltwinbuilder_id=digitaltwinbuilder_id,
            update_digital_twin_builder_definition_request=update_digital_twin_builder_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None, update_digital_twin_builder_definition_request: None) -> None:
        """Updates the definition of a specified DigitalTwinBuilder. The update overrides the current
        definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the digitaltwinbuilder definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :param update_digital_twin_builder_definition_request: Update digitaltwinbuilder definition
         request payload. Is either a UpdateDigitalTwinBuilderDefinitionRequest type or a IO[bytes]
         type. Required.
        :type update_digital_twin_builder_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.UpdateDigitalTwinBuilderDefinitionRequest or
         IO[bytes]
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_digital_twin_builder_definition(
            workspace_id=workspace_id,
            digitaltwinbuilder_id=digitaltwinbuilder_id,
            update_digital_twin_builder_definition_request=update_digital_twin_builder_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_digital_twin_builder_definition(self, workspace_id: None, digitaltwinbuilder_id: None, update_digital_twin_builder_definition_request: None) -> LROPoller[None]:
        """Updates the definition of a specified DigitalTwinBuilder. The update overrides the current
        definition.

        ..

           [!NOTE]
           Digital Twin Builder item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the digitaltwinbuilder definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the digital twin builder.

        Required Delegated Scopes
        -------------------------

         DigitalTwinBuilder.ReadWrite.All or Item.ReadWrite.All

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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param digitaltwinbuilder_id: The digitaltwinbuilder ID. Required.
        :type digitaltwinbuilder_id: str
        :param update_digital_twin_builder_definition_request: Update digitaltwinbuilder definition
         request payload. Is either a UpdateDigitalTwinBuilderDefinitionRequest type or a IO[bytes]
         type. Required.
        :type update_digital_twin_builder_definition_request:
         ~microsoft.fabric.api.digitaltwinbuilder.models.UpdateDigitalTwinBuilderDefinitionRequest or
         IO[bytes]
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_digital_twin_builder_definition(
            workspace_id=workspace_id,
            digitaltwinbuilder_id=digitaltwinbuilder_id,
            update_digital_twin_builder_definition_request=update_digital_twin_builder_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
