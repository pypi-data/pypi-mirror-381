from ....generated.core.operations import *
from ....generated.core import operations as _operations
from ....generated.core import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class WorkspacesOperations(_operations.WorkspacesOperations):
    """WorkspacesOperations for Core."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def provision_identity(self, workspace_id: None) -> _models.WorkspaceIdentity:
        """Provision a workspace identity for a workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have an *admin* role in the workspace.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :return: An instance of LROPoller that returns WorkspaceIdentity
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.WorkspaceIdentity]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_provision_identity(workspace_id=workspace_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_provision_identity(self, workspace_id: None) -> _LROResultExtractor[_models.WorkspaceIdentity]:
        """Provision a workspace identity for a workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have an *admin* role in the workspace.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :return: An instance of LROPoller that returns WorkspaceIdentity
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.WorkspaceIdentity]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.WorkspaceIdentity]()

        poller = super().begin_provision_identity(
            workspace_id=workspace_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def deprovision_identity(self, workspace_id: None) -> None:
        """Deprovision a workspace identity.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have an *admin* role in the workspace.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_deprovision_identity(
            workspace_id=workspace_id)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_deprovision_identity(self, workspace_id: None) -> LROPoller[None]:
        """Deprovision a workspace identity.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have an *admin* role in the workspace.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_deprovision_identity(
            workspace_id=workspace_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    


class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Core."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_item(self, workspace_id: None, create_item_request: None) -> _models.Item:
        """Creates an item in the specified workspace.

        This API is supported for a number of item types, find the supported item types in `Item
        management overview </rest/api/fabric/articles/item-management/item-management-overview>`_. You
        can use `Get item definition API </rest/api/fabric/core/items/get-item-definition>`_ to get an
        item definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------


        * To create a non-PowerBI Fabric item the workspace must be on a supported Fabric capacity. For
        more information see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * To create a PowerBI item, the user must have the appropriate license. For more information
        see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * When creating an item, use either ``creationPayload`` or ``definition``\ , but do not use
        both at the same time.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_item_request: Create item request payload. Required.
        :type create_item_request: ~microsoft.fabric.api.core.models.CreateItemRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Item
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.Item]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_item(workspace_id=workspace_id, create_item_request=create_item_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_item(self, workspace_id: None, create_item_request: None) -> _LROResultExtractor[_models.Item]:
        """Creates an item in the specified workspace.

        This API is supported for a number of item types, find the supported item types in `Item
        management overview </rest/api/fabric/articles/item-management/item-management-overview>`_. You
        can use `Get item definition API </rest/api/fabric/core/items/get-item-definition>`_ to get an
        item definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------


        * To create a non-PowerBI Fabric item the workspace must be on a supported Fabric capacity. For
        more information see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * To create a PowerBI item, the user must have the appropriate license. For more information
        see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * When creating an item, use either ``creationPayload`` or ``definition``\ , but do not use
        both at the same time.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_item_request: Create item request payload. Required.
        :type create_item_request: ~microsoft.fabric.api.core.models.CreateItemRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Item
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.Item]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Item]()

        poller = super().begin_create_item(
            workspace_id=workspace_id,
            create_item_request=create_item_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_item(self, workspace_id: None, create_item_request: None) -> _models.Item:
        """Creates an item in the specified workspace.

        This API is supported for a number of item types, find the supported item types in `Item
        management overview </rest/api/fabric/articles/item-management/item-management-overview>`_. You
        can use `Get item definition API </rest/api/fabric/core/items/get-item-definition>`_ to get an
        item definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------


        * To create a non-PowerBI Fabric item the workspace must be on a supported Fabric capacity. For
        more information see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * To create a PowerBI item, the user must have the appropriate license. For more information
        see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * When creating an item, use either ``creationPayload`` or ``definition``\ , but do not use
        both at the same time.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_item_request: Create item request payload. Required.
        :type create_item_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Item
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.Item]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_item(workspace_id=workspace_id, create_item_request=create_item_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_item(self, workspace_id: None, create_item_request: None) -> _LROResultExtractor[_models.Item]:
        """Creates an item in the specified workspace.

        This API is supported for a number of item types, find the supported item types in `Item
        management overview </rest/api/fabric/articles/item-management/item-management-overview>`_. You
        can use `Get item definition API </rest/api/fabric/core/items/get-item-definition>`_ to get an
        item definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------


        * To create a non-PowerBI Fabric item the workspace must be on a supported Fabric capacity. For
        more information see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * To create a PowerBI item, the user must have the appropriate license. For more information
        see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * When creating an item, use either ``creationPayload`` or ``definition``\ , but do not use
        both at the same time.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_item_request: Create item request payload. Required.
        :type create_item_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Item
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.Item]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Item]()

        poller = super().begin_create_item(
            workspace_id=workspace_id,
            create_item_request=create_item_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_item(self, workspace_id: None, create_item_request: None) -> _models.Item:
        """Creates an item in the specified workspace.

        This API is supported for a number of item types, find the supported item types in `Item
        management overview </rest/api/fabric/articles/item-management/item-management-overview>`_. You
        can use `Get item definition API </rest/api/fabric/core/items/get-item-definition>`_ to get an
        item definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------


        * To create a non-PowerBI Fabric item the workspace must be on a supported Fabric capacity. For
        more information see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * To create a PowerBI item, the user must have the appropriate license. For more information
        see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * When creating an item, use either ``creationPayload`` or ``definition``\ , but do not use
        both at the same time.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_item_request: Create item request payload. Is either a CreateItemRequest type or
         a IO[bytes] type. Required.
        :type create_item_request: ~microsoft.fabric.api.core.models.CreateItemRequest or IO[bytes]
        :return: An instance of LROPoller that returns Item
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.Item]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_item(workspace_id=workspace_id, create_item_request=create_item_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_item(self, workspace_id: None, create_item_request: None) -> _LROResultExtractor[_models.Item]:
        """Creates an item in the specified workspace.

        This API is supported for a number of item types, find the supported item types in `Item
        management overview </rest/api/fabric/articles/item-management/item-management-overview>`_. You
        can use `Get item definition API </rest/api/fabric/core/items/get-item-definition>`_ to get an
        item definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------


        * To create a non-PowerBI Fabric item the workspace must be on a supported Fabric capacity. For
        more information see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * To create a PowerBI item, the user must have the appropriate license. For more information
        see `Microsoft Fabric license types
        </fabric/enterprise/licenses#microsoft-fabric-license-types>`_.
        * When creating an item, use either ``creationPayload`` or ``definition``\ , but do not use
        both at the same time.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_item_request: Create item request payload. Is either a CreateItemRequest type or
         a IO[bytes] type. Required.
        :type create_item_request: ~microsoft.fabric.api.core.models.CreateItemRequest or IO[bytes]
        :return: An instance of LROPoller that returns Item
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.Item]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Item]()

        poller = super().begin_create_item(
            workspace_id=workspace_id,
            create_item_request=create_item_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_item_definition(self, workspace_id: None, item_id: None) -> _models.ItemDefinitionResponse:
        """Returns the specified item definition.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        When you get an item's definition, the sensitivity label is not a part of the definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `Scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------

         This API is blocked for an item with a protected sensitivity label, unless the caller has the
        usage rights to delete the sensitivity label.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :keyword format: The format of the item definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns ItemDefinitionResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.ItemDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_item_definition(workspace_id=workspace_id, item_id=item_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_item_definition(self, workspace_id: None, item_id: None) -> _LROResultExtractor[_models.ItemDefinitionResponse]:
        """Returns the specified item definition.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        When you get an item's definition, the sensitivity label is not a part of the definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `Scopes article </rest/api/fabric/articles/scopes>`_.

        Limitations
        -----------

         This API is blocked for an item with a protected sensitivity label, unless the caller has the
        usage rights to delete the sensitivity label.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :keyword format: The format of the item definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns ItemDefinitionResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.ItemDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ItemDefinitionResponse]()

        poller = super().begin_get_item_definition(
            workspace_id=workspace_id,
            item_id=item_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_item_definition(self, workspace_id: None, item_id: None, update_item_definition_request: None) -> None:
        """Overrides the definition for the specified item.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        Updating the item's definition, does not affect its sensitivity label.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :param update_item_definition_request: Update item definition request payload. Required.
        :type update_item_definition_request:
         ~microsoft.fabric.api.core.models.UpdateItemDefinitionRequest
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

        
        poller = self.begin_update_item_definition(
            workspace_id=workspace_id,
            item_id=item_id,
            update_item_definition_request=update_item_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_item_definition(self, workspace_id: None, item_id: None, update_item_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified item.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        Updating the item's definition, does not affect its sensitivity label.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :param update_item_definition_request: Update item definition request payload. Required.
        :type update_item_definition_request:
         ~microsoft.fabric.api.core.models.UpdateItemDefinitionRequest
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

        

        return super().begin_update_item_definition(
            workspace_id=workspace_id,
            item_id=item_id,
            update_item_definition_request=update_item_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_item_definition(self, workspace_id: None, item_id: None, update_item_definition_request: None) -> None:
        """Overrides the definition for the specified item.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        Updating the item's definition, does not affect its sensitivity label.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :param update_item_definition_request: Update item definition request payload. Required.
        :type update_item_definition_request: IO[bytes]
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

        
        poller = self.begin_update_item_definition(
            workspace_id=workspace_id,
            item_id=item_id,
            update_item_definition_request=update_item_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_item_definition(self, workspace_id: None, item_id: None, update_item_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified item.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        Updating the item's definition, does not affect its sensitivity label.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :param update_item_definition_request: Update item definition request payload. Required.
        :type update_item_definition_request: IO[bytes]
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

        

        return super().begin_update_item_definition(
            workspace_id=workspace_id,
            item_id=item_id,
            update_item_definition_request=update_item_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_item_definition(self, workspace_id: None, item_id: None, update_item_definition_request: None) -> None:
        """Overrides the definition for the specified item.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        Updating the item's definition, does not affect its sensitivity label.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :param update_item_definition_request: Update item definition request payload. Is either a
         UpdateItemDefinitionRequest type or a IO[bytes] type. Required.
        :type update_item_definition_request:
         ~microsoft.fabric.api.core.models.UpdateItemDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_item_definition(
            workspace_id=workspace_id,
            item_id=item_id,
            update_item_definition_request=update_item_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_item_definition(self, workspace_id: None, item_id: None, update_item_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified item.

        This API is supported for a number of item types, find the supported item types and information
        about their definition structure in `Item definition overview
        </rest/api/fabric/articles/item-management/definitions/item-definition-overview>`_.
        Updating the item's definition, does not affect its sensitivity label.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the item.

        Required Delegated Scopes
        -------------------------

         For item APIs use these scope types:


        * Generic scope: Item.ReadWrite.All
        *
          Specific scope: *itemType*.ReadWrite.All (for example: Notebook.ReadWrite.All)

          for more information about scopes, see `scopes article </rest/api/fabric/articles/scopes>`_.

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
             - When the item type in the call is supported. Check the corresponding API for the item
        type you're calling, to see if your call is supported. For example, semantic models are
        supported.


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param item_id: The item ID. Required.
        :type item_id: str
        :param update_item_definition_request: Update item definition request payload. Is either a
         UpdateItemDefinitionRequest type or a IO[bytes] type. Required.
        :type update_item_definition_request:
         ~microsoft.fabric.api.core.models.UpdateItemDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_item_definition(
            workspace_id=workspace_id,
            item_id=item_id,
            update_item_definition_request=update_item_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    


class GitOperations(_operations.GitOperations):
    """GitOperations for Core."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def initialize_connection(self, workspace_id: None, git_initialize_connection_request: None) -> _models.InitializeGitConnectionResponse:
        """Initialize a connection for a workspace that's connected to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        This API should be called after a successful call to the `Connect
        </rest/api/fabric/core/git/connect>`_ API. To complete a full sync of the workspace, use the
        `Required Action <initialize-connection#requiredaction>`_ operation to call the relevant sync
        operation, either `Commit To Git </rest/api/fabric/core/git/commit-to-git>`_ or `Update From
        Git </rest/api/fabric/core/git/update-from-git>`_.

        Permissions
        -----------

        The caller must have an *admin* workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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
        :param git_initialize_connection_request: Initialize the connection request payload. Default
         value is None.
        :type git_initialize_connection_request:
         ~microsoft.fabric.api.core.models.InitializeGitConnectionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns InitializeGitConnectionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.InitializeGitConnectionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_initialize_connection(workspace_id=workspace_id, git_initialize_connection_request=git_initialize_connection_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_initialize_connection(self, workspace_id: None, git_initialize_connection_request: None) -> _LROResultExtractor[_models.InitializeGitConnectionResponse]:
        """Initialize a connection for a workspace that's connected to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        This API should be called after a successful call to the `Connect
        </rest/api/fabric/core/git/connect>`_ API. To complete a full sync of the workspace, use the
        `Required Action <initialize-connection#requiredaction>`_ operation to call the relevant sync
        operation, either `Commit To Git </rest/api/fabric/core/git/commit-to-git>`_ or `Update From
        Git </rest/api/fabric/core/git/update-from-git>`_.

        Permissions
        -----------

        The caller must have an *admin* workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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
        :param git_initialize_connection_request: Initialize the connection request payload. Default
         value is None.
        :type git_initialize_connection_request:
         ~microsoft.fabric.api.core.models.InitializeGitConnectionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns InitializeGitConnectionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.InitializeGitConnectionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.InitializeGitConnectionResponse]()

        poller = super().begin_initialize_connection(
            workspace_id=workspace_id,
            git_initialize_connection_request=git_initialize_connection_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def initialize_connection(self, workspace_id: None, git_initialize_connection_request: None) -> _models.InitializeGitConnectionResponse:
        """Initialize a connection for a workspace that's connected to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        This API should be called after a successful call to the `Connect
        </rest/api/fabric/core/git/connect>`_ API. To complete a full sync of the workspace, use the
        `Required Action <initialize-connection#requiredaction>`_ operation to call the relevant sync
        operation, either `Commit To Git </rest/api/fabric/core/git/commit-to-git>`_ or `Update From
        Git </rest/api/fabric/core/git/update-from-git>`_.

        Permissions
        -----------

        The caller must have an *admin* workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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
        :param git_initialize_connection_request: Initialize the connection request payload. Default
         value is None.
        :type git_initialize_connection_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns InitializeGitConnectionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.InitializeGitConnectionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_initialize_connection(workspace_id=workspace_id, git_initialize_connection_request=git_initialize_connection_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_initialize_connection(self, workspace_id: None, git_initialize_connection_request: None) -> _LROResultExtractor[_models.InitializeGitConnectionResponse]:
        """Initialize a connection for a workspace that's connected to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        This API should be called after a successful call to the `Connect
        </rest/api/fabric/core/git/connect>`_ API. To complete a full sync of the workspace, use the
        `Required Action <initialize-connection#requiredaction>`_ operation to call the relevant sync
        operation, either `Commit To Git </rest/api/fabric/core/git/commit-to-git>`_ or `Update From
        Git </rest/api/fabric/core/git/update-from-git>`_.

        Permissions
        -----------

        The caller must have an *admin* workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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
        :param git_initialize_connection_request: Initialize the connection request payload. Default
         value is None.
        :type git_initialize_connection_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns InitializeGitConnectionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.InitializeGitConnectionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.InitializeGitConnectionResponse]()

        poller = super().begin_initialize_connection(
            workspace_id=workspace_id,
            git_initialize_connection_request=git_initialize_connection_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def initialize_connection(self, workspace_id: None, git_initialize_connection_request: None) -> _models.InitializeGitConnectionResponse:
        """Initialize a connection for a workspace that's connected to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        This API should be called after a successful call to the `Connect
        </rest/api/fabric/core/git/connect>`_ API. To complete a full sync of the workspace, use the
        `Required Action <initialize-connection#requiredaction>`_ operation to call the relevant sync
        operation, either `Commit To Git </rest/api/fabric/core/git/commit-to-git>`_ or `Update From
        Git </rest/api/fabric/core/git/update-from-git>`_.

        Permissions
        -----------

        The caller must have an *admin* workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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
        :param git_initialize_connection_request: Initialize the connection request payload. Is either
         a InitializeGitConnectionRequest type or a IO[bytes] type. Default value is None.
        :type git_initialize_connection_request:
         ~microsoft.fabric.api.core.models.InitializeGitConnectionRequest or IO[bytes]
        :return: An instance of LROPoller that returns InitializeGitConnectionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.InitializeGitConnectionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_initialize_connection(workspace_id=workspace_id, git_initialize_connection_request=git_initialize_connection_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_initialize_connection(self, workspace_id: None, git_initialize_connection_request: None) -> _LROResultExtractor[_models.InitializeGitConnectionResponse]:
        """Initialize a connection for a workspace that's connected to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        This API should be called after a successful call to the `Connect
        </rest/api/fabric/core/git/connect>`_ API. To complete a full sync of the workspace, use the
        `Required Action <initialize-connection#requiredaction>`_ operation to call the relevant sync
        operation, either `Commit To Git </rest/api/fabric/core/git/commit-to-git>`_ or `Update From
        Git </rest/api/fabric/core/git/update-from-git>`_.

        Permissions
        -----------

        The caller must have an *admin* workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.ReadWrite.All

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
        :param git_initialize_connection_request: Initialize the connection request payload. Is either
         a InitializeGitConnectionRequest type or a IO[bytes] type. Default value is None.
        :type git_initialize_connection_request:
         ~microsoft.fabric.api.core.models.InitializeGitConnectionRequest or IO[bytes]
        :return: An instance of LROPoller that returns InitializeGitConnectionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.InitializeGitConnectionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.InitializeGitConnectionResponse]()

        poller = super().begin_initialize_connection(
            workspace_id=workspace_id,
            git_initialize_connection_request=git_initialize_connection_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_from_git(self, workspace_id: None, update_from_git_request: None) -> None:
        """Updates the workspace with commits pushed to the connected branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        The update only affects items in the workspace that were changed in those commits. If called
        after the `Connect </rest/api/fabric/core/git/connect>`_ and `Initialize Connection
        </rest/api/fabric/core/git/initialize-connection>`_ APIs, it will perform a full update of the
        entire workspace.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param update_from_git_request: Update from a Git request payload. Required.
        :type update_from_git_request: ~microsoft.fabric.api.core.models.UpdateFromGitRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_from_git(
            workspace_id=workspace_id,
            update_from_git_request=update_from_git_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_from_git(self, workspace_id: None, update_from_git_request: None) -> LROPoller[None]:
        """Updates the workspace with commits pushed to the connected branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        The update only affects items in the workspace that were changed in those commits. If called
        after the `Connect </rest/api/fabric/core/git/connect>`_ and `Initialize Connection
        </rest/api/fabric/core/git/initialize-connection>`_ APIs, it will perform a full update of the
        entire workspace.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param update_from_git_request: Update from a Git request payload. Required.
        :type update_from_git_request: ~microsoft.fabric.api.core.models.UpdateFromGitRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_from_git(
            workspace_id=workspace_id,
            update_from_git_request=update_from_git_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_from_git(self, workspace_id: None, update_from_git_request: None) -> None:
        """Updates the workspace with commits pushed to the connected branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        The update only affects items in the workspace that were changed in those commits. If called
        after the `Connect </rest/api/fabric/core/git/connect>`_ and `Initialize Connection
        </rest/api/fabric/core/git/initialize-connection>`_ APIs, it will perform a full update of the
        entire workspace.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param update_from_git_request: Update from a Git request payload. Required.
        :type update_from_git_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_from_git(
            workspace_id=workspace_id,
            update_from_git_request=update_from_git_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_from_git(self, workspace_id: None, update_from_git_request: None) -> LROPoller[None]:
        """Updates the workspace with commits pushed to the connected branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        The update only affects items in the workspace that were changed in those commits. If called
        after the `Connect </rest/api/fabric/core/git/connect>`_ and `Initialize Connection
        </rest/api/fabric/core/git/initialize-connection>`_ APIs, it will perform a full update of the
        entire workspace.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param update_from_git_request: Update from a Git request payload. Required.
        :type update_from_git_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_from_git(
            workspace_id=workspace_id,
            update_from_git_request=update_from_git_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_from_git(self, workspace_id: None, update_from_git_request: None) -> None:
        """Updates the workspace with commits pushed to the connected branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        The update only affects items in the workspace that were changed in those commits. If called
        after the `Connect </rest/api/fabric/core/git/connect>`_ and `Initialize Connection
        </rest/api/fabric/core/git/initialize-connection>`_ APIs, it will perform a full update of the
        entire workspace.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param update_from_git_request: Update from a Git request payload. Is either a
         UpdateFromGitRequest type or a IO[bytes] type. Required.
        :type update_from_git_request: ~microsoft.fabric.api.core.models.UpdateFromGitRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_from_git(
            workspace_id=workspace_id,
            update_from_git_request=update_from_git_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_from_git(self, workspace_id: None, update_from_git_request: None) -> LROPoller[None]:
        """Updates the workspace with commits pushed to the connected branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        The update only affects items in the workspace that were changed in those commits. If called
        after the `Connect </rest/api/fabric/core/git/connect>`_ and `Initialize Connection
        </rest/api/fabric/core/git/initialize-connection>`_ APIs, it will perform a full update of the
        entire workspace.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param update_from_git_request: Update from a Git request payload. Is either a
         UpdateFromGitRequest type or a IO[bytes] type. Required.
        :type update_from_git_request: ~microsoft.fabric.api.core.models.UpdateFromGitRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_from_git(
            workspace_id=workspace_id,
            update_from_git_request=update_from_git_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def get_status(self, workspace_id: None) -> _models.GitStatusResponse:
        """Returns the ``Git status`` of items in the workspace, that can be committed to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        The status indicates changes to items since the last workspace and remote branch sync. If the
        remote and workspace items were both modified, the API flags a conflict.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All or Workspace.GitCommit.All

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
        :return: An instance of LROPoller that returns GitStatusResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.GitStatusResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_status(workspace_id=workspace_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_status(self, workspace_id: None) -> _LROResultExtractor[_models.GitStatusResponse]:
        """Returns the ``Git status`` of items in the workspace, that can be committed to Git.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        The status indicates changes to items since the last workspace and remote branch sync. If the
        remote and workspace items were both modified, the API flags a conflict.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitUpdate.All or Workspace.GitCommit.All

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
        :return: An instance of LROPoller that returns GitStatusResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.GitStatusResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.GitStatusResponse]()

        poller = super().begin_get_status(
            workspace_id=workspace_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def commit_to_git(self, workspace_id: None, commit_to_git_request: None) -> None:
        """Commits the changes made in the workspace to the connected remote branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        You can choose to commit all changes or only specific changed items. To sync the workspace for
        the first time, use this API after the `Connect </rest/api/fabric/core/git/connect>`_ and
        `Initialize Connection </rest/api/fabric/core/git/initialize-connection>`_ APIs.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitCommit.All.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param commit_to_git_request: Commit to the Git request payload. Required.
        :type commit_to_git_request: ~microsoft.fabric.api.core.models.CommitToGitRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_commit_to_git(
            workspace_id=workspace_id,
            commit_to_git_request=commit_to_git_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_commit_to_git(self, workspace_id: None, commit_to_git_request: None) -> LROPoller[None]:
        """Commits the changes made in the workspace to the connected remote branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        You can choose to commit all changes or only specific changed items. To sync the workspace for
        the first time, use this API after the `Connect </rest/api/fabric/core/git/connect>`_ and
        `Initialize Connection </rest/api/fabric/core/git/initialize-connection>`_ APIs.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitCommit.All.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param commit_to_git_request: Commit to the Git request payload. Required.
        :type commit_to_git_request: ~microsoft.fabric.api.core.models.CommitToGitRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_commit_to_git(
            workspace_id=workspace_id,
            commit_to_git_request=commit_to_git_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def commit_to_git(self, workspace_id: None, commit_to_git_request: None) -> None:
        """Commits the changes made in the workspace to the connected remote branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        You can choose to commit all changes or only specific changed items. To sync the workspace for
        the first time, use this API after the `Connect </rest/api/fabric/core/git/connect>`_ and
        `Initialize Connection </rest/api/fabric/core/git/initialize-connection>`_ APIs.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitCommit.All.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param commit_to_git_request: Commit to the Git request payload. Required.
        :type commit_to_git_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_commit_to_git(
            workspace_id=workspace_id,
            commit_to_git_request=commit_to_git_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_commit_to_git(self, workspace_id: None, commit_to_git_request: None) -> LROPoller[None]:
        """Commits the changes made in the workspace to the connected remote branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        You can choose to commit all changes or only specific changed items. To sync the workspace for
        the first time, use this API after the `Connect </rest/api/fabric/core/git/connect>`_ and
        `Initialize Connection </rest/api/fabric/core/git/initialize-connection>`_ APIs.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitCommit.All.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param commit_to_git_request: Commit to the Git request payload. Required.
        :type commit_to_git_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_commit_to_git(
            workspace_id=workspace_id,
            commit_to_git_request=commit_to_git_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def commit_to_git(self, workspace_id: None, commit_to_git_request: None) -> None:
        """Commits the changes made in the workspace to the connected remote branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        You can choose to commit all changes or only specific changed items. To sync the workspace for
        the first time, use this API after the `Connect </rest/api/fabric/core/git/connect>`_ and
        `Initialize Connection </rest/api/fabric/core/git/initialize-connection>`_ APIs.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitCommit.All.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param commit_to_git_request: Commit to the Git request payload. Is either a CommitToGitRequest
         type or a IO[bytes] type. Required.
        :type commit_to_git_request: ~microsoft.fabric.api.core.models.CommitToGitRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_commit_to_git(
            workspace_id=workspace_id,
            commit_to_git_request=commit_to_git_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_commit_to_git(self, workspace_id: None, commit_to_git_request: None) -> LROPoller[None]:
        """Commits the changes made in the workspace to the connected remote branch.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To use this API, the caller's Git credentials must be configured using `Update My Git
        Credentials </rest/api/fabric/core/git/update-my-git-credentials>`_ API. You can use the `Get
        My Git Credentials </rest/api/fabric/core/git/get-my-git-credentials>`_ API to check the Git
        credentials configuration.

        You can choose to commit all changes or only specific changed items. To sync the workspace for
        the first time, use this API after the `Connect </rest/api/fabric/core/git/connect>`_ and
        `Initialize Connection </rest/api/fabric/core/git/initialize-connection>`_ APIs.

        Permissions
        -----------

        The caller must have a *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Workspace.GitCommit.All.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param commit_to_git_request: Commit to the Git request payload. Is either a CommitToGitRequest
         type or a IO[bytes] type. Required.
        :type commit_to_git_request: ~microsoft.fabric.api.core.models.CommitToGitRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_commit_to_git(
            workspace_id=workspace_id,
            commit_to_git_request=commit_to_git_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    


class OneLakeShortcutsOperations(_operations.OneLakeShortcutsOperations):
    """OneLakeShortcutsOperations for Core."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def creates_shortcuts_in_bulk(self, workspace_id: None, item_id: None, bulk_create_shortcuts_request: None) -> _models.BulkCreateShortcutResponse:
        """Creates bulk shortcuts.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :param item_id: The ID of the data item. Required.
        :type item_id: str
        :param bulk_create_shortcuts_request: A shortcut bulk create request includes an array of
         shortcut objects, each representing a reference pointing to internal or external storage
         locations within OneLake. Required.
        :type bulk_create_shortcuts_request:
         ~microsoft.fabric.api.core.models.BulkCreateShortcutsRequest
        :keyword shortcut_conflict_policy: When provided, it defines the action to take when a shortcut
         with the same name and path already exists. The default action is 'Abort'. Additional
         ShortcutConflictPolicy types may be added over time. Known values are: "Abort",
         "GenerateUniqueName", "CreateOrOverwrite", and "OverwriteOnly". Default value is None.
        :paramtype shortcut_conflict_policy: str or
         ~microsoft.fabric.api.core.models.ShortcutConflictPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkCreateShortcutResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.BulkCreateShortcutResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_creates_shortcuts_in_bulk(workspace_id=workspace_id, item_id=item_id, bulk_create_shortcuts_request=bulk_create_shortcuts_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_creates_shortcuts_in_bulk(self, workspace_id: None, item_id: None, bulk_create_shortcuts_request: None) -> _LROResultExtractor[_models.BulkCreateShortcutResponse]:
        """Creates bulk shortcuts.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :param item_id: The ID of the data item. Required.
        :type item_id: str
        :param bulk_create_shortcuts_request: A shortcut bulk create request includes an array of
         shortcut objects, each representing a reference pointing to internal or external storage
         locations within OneLake. Required.
        :type bulk_create_shortcuts_request:
         ~microsoft.fabric.api.core.models.BulkCreateShortcutsRequest
        :keyword shortcut_conflict_policy: When provided, it defines the action to take when a shortcut
         with the same name and path already exists. The default action is 'Abort'. Additional
         ShortcutConflictPolicy types may be added over time. Known values are: "Abort",
         "GenerateUniqueName", "CreateOrOverwrite", and "OverwriteOnly". Default value is None.
        :paramtype shortcut_conflict_policy: str or
         ~microsoft.fabric.api.core.models.ShortcutConflictPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkCreateShortcutResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.BulkCreateShortcutResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.BulkCreateShortcutResponse]()

        poller = super().begin_creates_shortcuts_in_bulk(
            workspace_id=workspace_id,
            item_id=item_id,
            bulk_create_shortcuts_request=bulk_create_shortcuts_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def creates_shortcuts_in_bulk(self, workspace_id: None, item_id: None, bulk_create_shortcuts_request: None) -> _models.BulkCreateShortcutResponse:
        """Creates bulk shortcuts.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :param item_id: The ID of the data item. Required.
        :type item_id: str
        :param bulk_create_shortcuts_request: A shortcut bulk create request includes an array of
         shortcut objects, each representing a reference pointing to internal or external storage
         locations within OneLake. Required.
        :type bulk_create_shortcuts_request: IO[bytes]
        :keyword shortcut_conflict_policy: When provided, it defines the action to take when a shortcut
         with the same name and path already exists. The default action is 'Abort'. Additional
         ShortcutConflictPolicy types may be added over time. Known values are: "Abort",
         "GenerateUniqueName", "CreateOrOverwrite", and "OverwriteOnly". Default value is None.
        :paramtype shortcut_conflict_policy: str or
         ~microsoft.fabric.api.core.models.ShortcutConflictPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkCreateShortcutResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.BulkCreateShortcutResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_creates_shortcuts_in_bulk(workspace_id=workspace_id, item_id=item_id, bulk_create_shortcuts_request=bulk_create_shortcuts_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_creates_shortcuts_in_bulk(self, workspace_id: None, item_id: None, bulk_create_shortcuts_request: None) -> _LROResultExtractor[_models.BulkCreateShortcutResponse]:
        """Creates bulk shortcuts.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :param item_id: The ID of the data item. Required.
        :type item_id: str
        :param bulk_create_shortcuts_request: A shortcut bulk create request includes an array of
         shortcut objects, each representing a reference pointing to internal or external storage
         locations within OneLake. Required.
        :type bulk_create_shortcuts_request: IO[bytes]
        :keyword shortcut_conflict_policy: When provided, it defines the action to take when a shortcut
         with the same name and path already exists. The default action is 'Abort'. Additional
         ShortcutConflictPolicy types may be added over time. Known values are: "Abort",
         "GenerateUniqueName", "CreateOrOverwrite", and "OverwriteOnly". Default value is None.
        :paramtype shortcut_conflict_policy: str or
         ~microsoft.fabric.api.core.models.ShortcutConflictPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkCreateShortcutResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.BulkCreateShortcutResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.BulkCreateShortcutResponse]()

        poller = super().begin_creates_shortcuts_in_bulk(
            workspace_id=workspace_id,
            item_id=item_id,
            bulk_create_shortcuts_request=bulk_create_shortcuts_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def creates_shortcuts_in_bulk(self, workspace_id: None, item_id: None, bulk_create_shortcuts_request: None) -> _models.BulkCreateShortcutResponse:
        """Creates bulk shortcuts.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :param item_id: The ID of the data item. Required.
        :type item_id: str
        :param bulk_create_shortcuts_request: A shortcut bulk create request includes an array of
         shortcut objects, each representing a reference pointing to internal or external storage
         locations within OneLake. Is either a BulkCreateShortcutsRequest type or a IO[bytes] type.
         Required.
        :type bulk_create_shortcuts_request:
         ~microsoft.fabric.api.core.models.BulkCreateShortcutsRequest or IO[bytes]
        :keyword shortcut_conflict_policy: When provided, it defines the action to take when a shortcut
         with the same name and path already exists. The default action is 'Abort'. Additional
         ShortcutConflictPolicy types may be added over time. Known values are: "Abort",
         "GenerateUniqueName", "CreateOrOverwrite", and "OverwriteOnly". Default value is None.
        :paramtype shortcut_conflict_policy: str or
         ~microsoft.fabric.api.core.models.ShortcutConflictPolicy
        :return: An instance of LROPoller that returns BulkCreateShortcutResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.BulkCreateShortcutResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_creates_shortcuts_in_bulk(workspace_id=workspace_id, item_id=item_id, bulk_create_shortcuts_request=bulk_create_shortcuts_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_creates_shortcuts_in_bulk(self, workspace_id: None, item_id: None, bulk_create_shortcuts_request: None) -> _LROResultExtractor[_models.BulkCreateShortcutResponse]:
        """Creates bulk shortcuts.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :param item_id: The ID of the data item. Required.
        :type item_id: str
        :param bulk_create_shortcuts_request: A shortcut bulk create request includes an array of
         shortcut objects, each representing a reference pointing to internal or external storage
         locations within OneLake. Is either a BulkCreateShortcutsRequest type or a IO[bytes] type.
         Required.
        :type bulk_create_shortcuts_request:
         ~microsoft.fabric.api.core.models.BulkCreateShortcutsRequest or IO[bytes]
        :keyword shortcut_conflict_policy: When provided, it defines the action to take when a shortcut
         with the same name and path already exists. The default action is 'Abort'. Additional
         ShortcutConflictPolicy types may be added over time. Known values are: "Abort",
         "GenerateUniqueName", "CreateOrOverwrite", and "OverwriteOnly". Default value is None.
        :paramtype shortcut_conflict_policy: str or
         ~microsoft.fabric.api.core.models.ShortcutConflictPolicy
        :return: An instance of LROPoller that returns BulkCreateShortcutResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.BulkCreateShortcutResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.BulkCreateShortcutResponse]()

        poller = super().begin_creates_shortcuts_in_bulk(
            workspace_id=workspace_id,
            item_id=item_id,
            bulk_create_shortcuts_request=bulk_create_shortcuts_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def reset_shortcut_cache(self, workspace_id: None) -> None:
        """Deletes any cached files that were stored while reading from shortcuts.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_reset_shortcut_cache(
            workspace_id=workspace_id)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_reset_shortcut_cache(self, workspace_id: None) -> LROPoller[None]:
        """Deletes any cached files that were stored while reading from shortcuts.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Required Delegated Scopes
        -------------------------

        OneLake.ReadWrite.All

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

        :param workspace_id: The ID of the workspace. Required.
        :type workspace_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_reset_shortcut_cache(
            workspace_id=workspace_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    


class DeploymentPipelinesOperations(_operations.DeploymentPipelinesOperations):
    """DeploymentPipelinesOperations for Core."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def deploy_stage_content(self, deployment_pipeline_id: None, deploy_request: None) -> _models.DeploymentPipelineOperationExtendedInfo:
        """Deploys items from the specified stage of the specified deployment pipeline.

        To learn about items that are supported in deployment pipelines, see: `Supported items
        </fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines#supported-items>`_.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must have an *admin* deployment pipelines role.
        The user must be at least a contributor on both source and target deployment workspaces. For
        more information, see: `Permissions <https://go.microsoft.com/fwlink/?linkid=2235654>`_.

        Required Delegated Scopes
        -------------------------

        Pipeline.Deploy

        Limitations
        -----------

        Maximum 300 deployed items per request.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param deployment_pipeline_id: The deployment pipeline ID. Required.
        :type deployment_pipeline_id: str
        :param deploy_request: The deploy request. Required.
        :type deploy_request: ~microsoft.fabric.api.core.models.DeployRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DeploymentPipelineOperationExtendedInfo
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.DeploymentPipelineOperationExtendedInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_deploy_stage_content(deployment_pipeline_id=deployment_pipeline_id, deploy_request=deploy_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_deploy_stage_content(self, deployment_pipeline_id: None, deploy_request: None) -> _LROResultExtractor[_models.DeploymentPipelineOperationExtendedInfo]:
        """Deploys items from the specified stage of the specified deployment pipeline.

        To learn about items that are supported in deployment pipelines, see: `Supported items
        </fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines#supported-items>`_.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must have an *admin* deployment pipelines role.
        The user must be at least a contributor on both source and target deployment workspaces. For
        more information, see: `Permissions <https://go.microsoft.com/fwlink/?linkid=2235654>`_.

        Required Delegated Scopes
        -------------------------

        Pipeline.Deploy

        Limitations
        -----------

        Maximum 300 deployed items per request.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param deployment_pipeline_id: The deployment pipeline ID. Required.
        :type deployment_pipeline_id: str
        :param deploy_request: The deploy request. Required.
        :type deploy_request: ~microsoft.fabric.api.core.models.DeployRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DeploymentPipelineOperationExtendedInfo
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.DeploymentPipelineOperationExtendedInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DeploymentPipelineOperationExtendedInfo]()

        poller = super().begin_deploy_stage_content(
            deployment_pipeline_id=deployment_pipeline_id,
            deploy_request=deploy_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def deploy_stage_content(self, deployment_pipeline_id: None, deploy_request: None) -> _models.DeploymentPipelineOperationExtendedInfo:
        """Deploys items from the specified stage of the specified deployment pipeline.

        To learn about items that are supported in deployment pipelines, see: `Supported items
        </fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines#supported-items>`_.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must have an *admin* deployment pipelines role.
        The user must be at least a contributor on both source and target deployment workspaces. For
        more information, see: `Permissions <https://go.microsoft.com/fwlink/?linkid=2235654>`_.

        Required Delegated Scopes
        -------------------------

        Pipeline.Deploy

        Limitations
        -----------

        Maximum 300 deployed items per request.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param deployment_pipeline_id: The deployment pipeline ID. Required.
        :type deployment_pipeline_id: str
        :param deploy_request: The deploy request. Required.
        :type deploy_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DeploymentPipelineOperationExtendedInfo
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.DeploymentPipelineOperationExtendedInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_deploy_stage_content(deployment_pipeline_id=deployment_pipeline_id, deploy_request=deploy_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_deploy_stage_content(self, deployment_pipeline_id: None, deploy_request: None) -> _LROResultExtractor[_models.DeploymentPipelineOperationExtendedInfo]:
        """Deploys items from the specified stage of the specified deployment pipeline.

        To learn about items that are supported in deployment pipelines, see: `Supported items
        </fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines#supported-items>`_.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must have an *admin* deployment pipelines role.
        The user must be at least a contributor on both source and target deployment workspaces. For
        more information, see: `Permissions <https://go.microsoft.com/fwlink/?linkid=2235654>`_.

        Required Delegated Scopes
        -------------------------

        Pipeline.Deploy

        Limitations
        -----------

        Maximum 300 deployed items per request.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param deployment_pipeline_id: The deployment pipeline ID. Required.
        :type deployment_pipeline_id: str
        :param deploy_request: The deploy request. Required.
        :type deploy_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns DeploymentPipelineOperationExtendedInfo
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.DeploymentPipelineOperationExtendedInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DeploymentPipelineOperationExtendedInfo]()

        poller = super().begin_deploy_stage_content(
            deployment_pipeline_id=deployment_pipeline_id,
            deploy_request=deploy_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def deploy_stage_content(self, deployment_pipeline_id: None, deploy_request: None) -> _models.DeploymentPipelineOperationExtendedInfo:
        """Deploys items from the specified stage of the specified deployment pipeline.

        To learn about items that are supported in deployment pipelines, see: `Supported items
        </fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines#supported-items>`_.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must have an *admin* deployment pipelines role.
        The user must be at least a contributor on both source and target deployment workspaces. For
        more information, see: `Permissions <https://go.microsoft.com/fwlink/?linkid=2235654>`_.

        Required Delegated Scopes
        -------------------------

        Pipeline.Deploy

        Limitations
        -----------

        Maximum 300 deployed items per request.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param deployment_pipeline_id: The deployment pipeline ID. Required.
        :type deployment_pipeline_id: str
        :param deploy_request: The deploy request. Is either a DeployRequest type or a IO[bytes] type.
         Required.
        :type deploy_request: ~microsoft.fabric.api.core.models.DeployRequest or IO[bytes]
        :return: An instance of LROPoller that returns DeploymentPipelineOperationExtendedInfo
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.DeploymentPipelineOperationExtendedInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_deploy_stage_content(deployment_pipeline_id=deployment_pipeline_id, deploy_request=deploy_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_deploy_stage_content(self, deployment_pipeline_id: None, deploy_request: None) -> _LROResultExtractor[_models.DeploymentPipelineOperationExtendedInfo]:
        """Deploys items from the specified stage of the specified deployment pipeline.

        To learn about items that are supported in deployment pipelines, see: `Supported items
        </fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines#supported-items>`_.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must have an *admin* deployment pipelines role.
        The user must be at least a contributor on both source and target deployment workspaces. For
        more information, see: `Permissions <https://go.microsoft.com/fwlink/?linkid=2235654>`_.

        Required Delegated Scopes
        -------------------------

        Pipeline.Deploy

        Limitations
        -----------

        Maximum 300 deployed items per request.

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
             - Only supported when all the `items
        </rest/api/fabric/articles/item-management/item-management-overview>`_ involved in the
        operation support service principals


        Interface
        ---------.

        :param deployment_pipeline_id: The deployment pipeline ID. Required.
        :type deployment_pipeline_id: str
        :param deploy_request: The deploy request. Is either a DeployRequest type or a IO[bytes] type.
         Required.
        :type deploy_request: ~microsoft.fabric.api.core.models.DeployRequest or IO[bytes]
        :return: An instance of LROPoller that returns DeploymentPipelineOperationExtendedInfo
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.core.models.DeploymentPipelineOperationExtendedInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.DeploymentPipelineOperationExtendedInfo]()

        poller = super().begin_deploy_stage_content(
            deployment_pipeline_id=deployment_pipeline_id,
            deploy_request=deploy_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    
