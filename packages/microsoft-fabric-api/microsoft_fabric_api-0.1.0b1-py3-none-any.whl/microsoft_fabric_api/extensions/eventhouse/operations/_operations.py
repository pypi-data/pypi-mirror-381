from ....generated.eventhouse.operations import *
from ....generated.eventhouse import operations as _operations
from ....generated.eventhouse import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Eventhouse."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_eventhouse(self, workspace_id: None, create_eventhouse_request: None) -> _models.Eventhouse:
        """Creates an eventhouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventhouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventhouse_request: Create eventhouse request payload. Required.
        :type create_eventhouse_request:
         ~microsoft.fabric.api.eventhouse.models.CreateEventhouseRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventhouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.Eventhouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_eventhouse(workspace_id=workspace_id, create_eventhouse_request=create_eventhouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_eventhouse(self, workspace_id: None, create_eventhouse_request: None) -> _LROResultExtractor[_models.Eventhouse]:
        """Creates an eventhouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventhouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventhouse_request: Create eventhouse request payload. Required.
        :type create_eventhouse_request:
         ~microsoft.fabric.api.eventhouse.models.CreateEventhouseRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventhouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.Eventhouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Eventhouse]()

        poller = super().begin_create_eventhouse(
            workspace_id=workspace_id,
            create_eventhouse_request=create_eventhouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_eventhouse(self, workspace_id: None, create_eventhouse_request: None) -> _models.Eventhouse:
        """Creates an eventhouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventhouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventhouse_request: Create eventhouse request payload. Required.
        :type create_eventhouse_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventhouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.Eventhouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_eventhouse(workspace_id=workspace_id, create_eventhouse_request=create_eventhouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_eventhouse(self, workspace_id: None, create_eventhouse_request: None) -> _LROResultExtractor[_models.Eventhouse]:
        """Creates an eventhouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventhouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventhouse_request: Create eventhouse request payload. Required.
        :type create_eventhouse_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Eventhouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.Eventhouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Eventhouse]()

        poller = super().begin_create_eventhouse(
            workspace_id=workspace_id,
            create_eventhouse_request=create_eventhouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_eventhouse(self, workspace_id: None, create_eventhouse_request: None) -> _models.Eventhouse:
        """Creates an eventhouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventhouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventhouse_request: Create eventhouse request payload. Is either a
         CreateEventhouseRequest type or a IO[bytes] type. Required.
        :type create_eventhouse_request:
         ~microsoft.fabric.api.eventhouse.models.CreateEventhouseRequest or IO[bytes]
        :return: An instance of LROPoller that returns Eventhouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.Eventhouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_eventhouse(workspace_id=workspace_id, create_eventhouse_request=create_eventhouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_eventhouse(self, workspace_id: None, create_eventhouse_request: None) -> _LROResultExtractor[_models.Eventhouse]:
        """Creates an eventhouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an eventhouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_eventhouse_request: Create eventhouse request payload. Is either a
         CreateEventhouseRequest type or a IO[bytes] type. Required.
        :type create_eventhouse_request:
         ~microsoft.fabric.api.eventhouse.models.CreateEventhouseRequest or IO[bytes]
        :return: An instance of LROPoller that returns Eventhouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.Eventhouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Eventhouse]()

        poller = super().begin_create_eventhouse(
            workspace_id=workspace_id,
            create_eventhouse_request=create_eventhouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_eventhouse_definition(self, workspace_id: None, eventhouse_id: None) -> _models.EventhouseDefinitionResponse:
        """Returns the specified eventhouse public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :keyword format: The format of the eventhouse public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns EventhouseDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.EventhouseDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_eventhouse_definition(workspace_id=workspace_id, eventhouse_id=eventhouse_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_eventhouse_definition(self, workspace_id: None, eventhouse_id: None) -> _LROResultExtractor[_models.EventhouseDefinitionResponse]:
        """Returns the specified eventhouse public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :keyword format: The format of the eventhouse public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns EventhouseDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.eventhouse.models.EventhouseDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.EventhouseDefinitionResponse]()

        poller = super().begin_get_eventhouse_definition(
            workspace_id=workspace_id,
            eventhouse_id=eventhouse_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_eventhouse_definition(self, workspace_id: None, eventhouse_id: None, update_eventhouse_definition_request: None) -> None:
        """Overrides the definition for the specified eventhouse.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :param update_eventhouse_definition_request: Update eventhouse definition request payload.
         Required.
        :type update_eventhouse_definition_request:
         ~microsoft.fabric.api.eventhouse.models.UpdateEventhouseDefinitionRequest
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

        
        poller = self.begin_update_eventhouse_definition(
            workspace_id=workspace_id,
            eventhouse_id=eventhouse_id,
            update_eventhouse_definition_request=update_eventhouse_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_eventhouse_definition(self, workspace_id: None, eventhouse_id: None, update_eventhouse_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified eventhouse.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :param update_eventhouse_definition_request: Update eventhouse definition request payload.
         Required.
        :type update_eventhouse_definition_request:
         ~microsoft.fabric.api.eventhouse.models.UpdateEventhouseDefinitionRequest
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

        

        return super().begin_update_eventhouse_definition(
            workspace_id=workspace_id,
            eventhouse_id=eventhouse_id,
            update_eventhouse_definition_request=update_eventhouse_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_eventhouse_definition(self, workspace_id: None, eventhouse_id: None, update_eventhouse_definition_request: None) -> None:
        """Overrides the definition for the specified eventhouse.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :param update_eventhouse_definition_request: Update eventhouse definition request payload.
         Required.
        :type update_eventhouse_definition_request: IO[bytes]
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

        
        poller = self.begin_update_eventhouse_definition(
            workspace_id=workspace_id,
            eventhouse_id=eventhouse_id,
            update_eventhouse_definition_request=update_eventhouse_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_eventhouse_definition(self, workspace_id: None, eventhouse_id: None, update_eventhouse_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified eventhouse.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :param update_eventhouse_definition_request: Update eventhouse definition request payload.
         Required.
        :type update_eventhouse_definition_request: IO[bytes]
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

        

        return super().begin_update_eventhouse_definition(
            workspace_id=workspace_id,
            eventhouse_id=eventhouse_id,
            update_eventhouse_definition_request=update_eventhouse_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_eventhouse_definition(self, workspace_id: None, eventhouse_id: None, update_eventhouse_definition_request: None) -> None:
        """Overrides the definition for the specified eventhouse.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :param update_eventhouse_definition_request: Update eventhouse definition request payload. Is
         either a UpdateEventhouseDefinitionRequest type or a IO[bytes] type. Required.
        :type update_eventhouse_definition_request:
         ~microsoft.fabric.api.eventhouse.models.UpdateEventhouseDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_eventhouse_definition(
            workspace_id=workspace_id,
            eventhouse_id=eventhouse_id,
            update_eventhouse_definition_request=update_eventhouse_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_eventhouse_definition(self, workspace_id: None, eventhouse_id: None, update_eventhouse_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified eventhouse.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the eventhouse.

        Required Delegated Scopes
        -------------------------

         Eventhouse.ReadWrite.All or Item.ReadWrite.All

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
        :param eventhouse_id: The eventhouse ID. Required.
        :type eventhouse_id: str
        :param update_eventhouse_definition_request: Update eventhouse definition request payload. Is
         either a UpdateEventhouseDefinitionRequest type or a IO[bytes] type. Required.
        :type update_eventhouse_definition_request:
         ~microsoft.fabric.api.eventhouse.models.UpdateEventhouseDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_eventhouse_definition(
            workspace_id=workspace_id,
            eventhouse_id=eventhouse_id,
            update_eventhouse_definition_request=update_eventhouse_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
