from ....generated.eventstream.operations import *
from ....generated.eventstream import operations as _operations
from ....generated.eventstream import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Eventstream."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_eventstream(self, workspace_id: None, create_eventstream_request: None) -> _models.Eventstream:
        """Creates an eventstream in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create eventstream with definition, refer to `Eventstream definition
        </rest/api/fabric/articles/item-management/definitions/eventstream-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventstream the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventstream_request: Create item request payload. Required.
        :type create_eventstream_request:
         ~microsoft.fabric.api.eventstream.models.CreateEventstreamRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventstream
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.Eventstream]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_eventstream(workspace_id=workspace_id, create_eventstream_request=create_eventstream_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_eventstream(self, workspace_id: None, create_eventstream_request: None) -> _LROResultExtractor[_models.Eventstream]:
        """Creates an eventstream in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create eventstream with definition, refer to `Eventstream definition
        </rest/api/fabric/articles/item-management/definitions/eventstream-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventstream the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventstream_request: Create item request payload. Required.
        :type create_eventstream_request:
         ~microsoft.fabric.api.eventstream.models.CreateEventstreamRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventstream
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.Eventstream]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Eventstream]()

        poller = super().begin_create_eventstream(
            workspace_id=workspace_id,
            create_eventstream_request=create_eventstream_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_eventstream(self, workspace_id: None, create_eventstream_request: None) -> _models.Eventstream:
        """Creates an eventstream in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create eventstream with definition, refer to `Eventstream definition
        </rest/api/fabric/articles/item-management/definitions/eventstream-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventstream the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventstream_request: Create item request payload. Required.
        :type create_eventstream_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventstream
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.Eventstream]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_eventstream(workspace_id=workspace_id, create_eventstream_request=create_eventstream_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_eventstream(self, workspace_id: None, create_eventstream_request: None) -> _LROResultExtractor[_models.Eventstream]:
        """Creates an eventstream in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create eventstream with definition, refer to `Eventstream definition
        </rest/api/fabric/articles/item-management/definitions/eventstream-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventstream the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventstream_request: Create item request payload. Required.
        :type create_eventstream_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventstream
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.Eventstream]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Eventstream]()

        poller = super().begin_create_eventstream(
            workspace_id=workspace_id,
            create_eventstream_request=create_eventstream_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_eventstream(self, workspace_id: None, create_eventstream_request: None) -> _models.Eventstream:
        """Creates an eventstream in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create eventstream with definition, refer to `Eventstream definition
        </rest/api/fabric/articles/item-management/definitions/eventstream-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventstream the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventstream_request: Create item request payload. Is either a
         CreateEventstreamRequest type or a IO[bytes] type. Required.
        :type create_eventstream_request:
         ~microsoft.fabric.api.eventstream.models.CreateEventstreamRequest or IO[bytes]
        :return: An instance of LROPoller that returns Eventstream
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.Eventstream]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_eventstream(workspace_id=workspace_id, create_eventstream_request=create_eventstream_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_eventstream(self, workspace_id: None, create_eventstream_request: None) -> _LROResultExtractor[_models.Eventstream]:
        """Creates an eventstream in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create eventstream with definition, refer to `Eventstream definition
        </rest/api/fabric/articles/item-management/definitions/eventstream-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventstream the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventstream_request: Create item request payload. Is either a
         CreateEventstreamRequest type or a IO[bytes] type. Required.
        :type create_eventstream_request:
         ~microsoft.fabric.api.eventstream.models.CreateEventstreamRequest or IO[bytes]
        :return: An instance of LROPoller that returns Eventstream
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.Eventstream]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Eventstream]()

        poller = super().begin_create_eventstream(
            workspace_id=workspace_id,
            create_eventstream_request=create_eventstream_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_eventstream_definition(self, workspace_id: None, eventstream_id: None) -> _models.EventstreamDefinitionResponse:
        """Returns the specified eventstream public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get an eventstream public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for an eventstream with an encrypted sensitivity label.

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :keyword format: The format of the eventstream public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns EventstreamDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.EventstreamDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_eventstream_definition(workspace_id=workspace_id, eventstream_id=eventstream_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_eventstream_definition(self, workspace_id: None, eventstream_id: None) -> _LROResultExtractor[_models.EventstreamDefinitionResponse]:
        """Returns the specified eventstream public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get an eventstream public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for an eventstream with an encrypted sensitivity label.

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :keyword format: The format of the eventstream public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns EventstreamDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventstream.models.EventstreamDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.EventstreamDefinitionResponse]()

        poller = super().begin_get_eventstream_definition(
            workspace_id=workspace_id,
            eventstream_id=eventstream_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_eventstream_definition(self, workspace_id: None, eventstream_id: None, update_eventstream_definition_request: None) -> None:
        """Updates the definition of a specified eventstream. The update overrides the current definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the eventstream definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :param update_eventstream_definition_request: Update eventstream definition request payload.
         Required.
        :type update_eventstream_definition_request:
         ~microsoft.fabric.api.eventstream.models.UpdateEventstreamDefinitionRequest
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

        
        poller = self.begin_update_eventstream_definition(
            workspace_id=workspace_id,
            eventstream_id=eventstream_id,
            update_eventstream_definition_request=update_eventstream_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_eventstream_definition(self, workspace_id: None, eventstream_id: None, update_eventstream_definition_request: None) -> LROPoller[None]:
        """Updates the definition of a specified eventstream. The update overrides the current definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the eventstream definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :param update_eventstream_definition_request: Update eventstream definition request payload.
         Required.
        :type update_eventstream_definition_request:
         ~microsoft.fabric.api.eventstream.models.UpdateEventstreamDefinitionRequest
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

        

        return super().begin_update_eventstream_definition(
            workspace_id=workspace_id,
            eventstream_id=eventstream_id,
            update_eventstream_definition_request=update_eventstream_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_eventstream_definition(self, workspace_id: None, eventstream_id: None, update_eventstream_definition_request: None) -> None:
        """Updates the definition of a specified eventstream. The update overrides the current definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the eventstream definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :param update_eventstream_definition_request: Update eventstream definition request payload.
         Required.
        :type update_eventstream_definition_request: IO[bytes]
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

        
        poller = self.begin_update_eventstream_definition(
            workspace_id=workspace_id,
            eventstream_id=eventstream_id,
            update_eventstream_definition_request=update_eventstream_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_eventstream_definition(self, workspace_id: None, eventstream_id: None, update_eventstream_definition_request: None) -> LROPoller[None]:
        """Updates the definition of a specified eventstream. The update overrides the current definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the eventstream definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :param update_eventstream_definition_request: Update eventstream definition request payload.
         Required.
        :type update_eventstream_definition_request: IO[bytes]
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

        

        return super().begin_update_eventstream_definition(
            workspace_id=workspace_id,
            eventstream_id=eventstream_id,
            update_eventstream_definition_request=update_eventstream_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_eventstream_definition(self, workspace_id: None, eventstream_id: None, update_eventstream_definition_request: None) -> None:
        """Updates the definition of a specified eventstream. The update overrides the current definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the eventstream definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :param update_eventstream_definition_request: Update eventstream definition request payload. Is
         either a UpdateEventstreamDefinitionRequest type or a IO[bytes] type. Required.
        :type update_eventstream_definition_request:
         ~microsoft.fabric.api.eventstream.models.UpdateEventstreamDefinitionRequest or IO[bytes]
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_eventstream_definition(
            workspace_id=workspace_id,
            eventstream_id=eventstream_id,
            update_eventstream_definition_request=update_eventstream_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_eventstream_definition(self, workspace_id: None, eventstream_id: None, update_eventstream_definition_request: None) -> LROPoller[None]:
        """Updates the definition of a specified eventstream. The update overrides the current definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the eventstream definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventstream.

        Required Delegated Scopes
        -------------------------

         Eventstream.ReadWrite.All or Item.ReadWrite.All

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
        :param eventstream_id: The eventstream ID. Required.
        :type eventstream_id: str
        :param update_eventstream_definition_request: Update eventstream definition request payload. Is
         either a UpdateEventstreamDefinitionRequest type or a IO[bytes] type. Required.
        :type update_eventstream_definition_request:
         ~microsoft.fabric.api.eventstream.models.UpdateEventstreamDefinitionRequest or IO[bytes]
        :keyword update_metadata: Whether to update the item's metadata if it is provided in the
         ``.platform`` file. True - Update the metadata if it is provided in the ``.platform`` file as
         part of the definition, False - Do not update the metadata. Default value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_eventstream_definition(
            workspace_id=workspace_id,
            eventstream_id=eventstream_id,
            update_eventstream_definition_request=update_eventstream_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
