from ....generated.reflex.operations import *
from ....generated.reflex import operations as _operations
from ....generated.reflex import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Reflex."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_reflex(self, workspace_id: None, create_reflex_request: None) -> _models.Reflex:
        """Creates a Reflex in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Reflex definition
        </rest/api/fabric/articles/item-management/definitions/reflex-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Reflex the workspace must be on a supported Fabric capacity. For more information
        see: `Microsoft Fabric license types
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
        :param create_reflex_request: Create item request payload. Required.
        :type create_reflex_request: ~microsoft.fabric.api.reflex.models.CreateReflexRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Reflex
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.Reflex]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_reflex(workspace_id=workspace_id, create_reflex_request=create_reflex_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_reflex(self, workspace_id: None, create_reflex_request: None) -> _LROResultExtractor[_models.Reflex]:
        """Creates a Reflex in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Reflex definition
        </rest/api/fabric/articles/item-management/definitions/reflex-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Reflex the workspace must be on a supported Fabric capacity. For more information
        see: `Microsoft Fabric license types
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
        :param create_reflex_request: Create item request payload. Required.
        :type create_reflex_request: ~microsoft.fabric.api.reflex.models.CreateReflexRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Reflex
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.Reflex]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Reflex]()

        poller = super().begin_create_reflex(
            workspace_id=workspace_id,
            create_reflex_request=create_reflex_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_reflex(self, workspace_id: None, create_reflex_request: None) -> _models.Reflex:
        """Creates a Reflex in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Reflex definition
        </rest/api/fabric/articles/item-management/definitions/reflex-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Reflex the workspace must be on a supported Fabric capacity. For more information
        see: `Microsoft Fabric license types
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
        :param create_reflex_request: Create item request payload. Required.
        :type create_reflex_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Reflex
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.Reflex]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_reflex(workspace_id=workspace_id, create_reflex_request=create_reflex_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_reflex(self, workspace_id: None, create_reflex_request: None) -> _LROResultExtractor[_models.Reflex]:
        """Creates a Reflex in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Reflex definition
        </rest/api/fabric/articles/item-management/definitions/reflex-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Reflex the workspace must be on a supported Fabric capacity. For more information
        see: `Microsoft Fabric license types
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
        :param create_reflex_request: Create item request payload. Required.
        :type create_reflex_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Reflex
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.Reflex]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Reflex]()

        poller = super().begin_create_reflex(
            workspace_id=workspace_id,
            create_reflex_request=create_reflex_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_reflex(self, workspace_id: None, create_reflex_request: None) -> _models.Reflex:
        """Creates a Reflex in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Reflex definition
        </rest/api/fabric/articles/item-management/definitions/reflex-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Reflex the workspace must be on a supported Fabric capacity. For more information
        see: `Microsoft Fabric license types
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
        :param create_reflex_request: Create item request payload. Is either a CreateReflexRequest type
         or a IO[bytes] type. Required.
        :type create_reflex_request: ~microsoft.fabric.api.reflex.models.CreateReflexRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Reflex
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.Reflex]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_reflex(workspace_id=workspace_id, create_reflex_request=create_reflex_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_reflex(self, workspace_id: None, create_reflex_request: None) -> _LROResultExtractor[_models.Reflex]:
        """Creates a Reflex in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Reflex definition
        </rest/api/fabric/articles/item-management/definitions/reflex-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Reflex the workspace must be on a supported Fabric capacity. For more information
        see: `Microsoft Fabric license types
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
        :param create_reflex_request: Create item request payload. Is either a CreateReflexRequest type
         or a IO[bytes] type. Required.
        :type create_reflex_request: ~microsoft.fabric.api.reflex.models.CreateReflexRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Reflex
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.Reflex]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Reflex]()

        poller = super().begin_create_reflex(
            workspace_id=workspace_id,
            create_reflex_request=create_reflex_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_reflex_definition(self, workspace_id: None, reflex_id: None) -> _models.ReflexDefinitionResponse:
        """Returns the specified Reflex public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a Reflex's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a Reflex with an encrypted sensitivity label.

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :keyword format: The format of the Reflex public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns ReflexDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.ReflexDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_reflex_definition(workspace_id=workspace_id, reflex_id=reflex_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_reflex_definition(self, workspace_id: None, reflex_id: None) -> _LROResultExtractor[_models.ReflexDefinitionResponse]:
        """Returns the specified Reflex public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a Reflex's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a Reflex with an encrypted sensitivity label.

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :keyword format: The format of the Reflex public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns ReflexDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.reflex.models.ReflexDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ReflexDefinitionResponse]()

        poller = super().begin_get_reflex_definition(
            workspace_id=workspace_id,
            reflex_id=reflex_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_reflex_definition(self, workspace_id: None, reflex_id: None, update_reflex_definition_request: None) -> None:
        """Overrides the definition for the specified Reflex.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Reflex's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :param update_reflex_definition_request: Update Reflex definition request payload. Required.
        :type update_reflex_definition_request:
         ~microsoft.fabric.api.reflex.models.UpdateReflexDefinitionRequest
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

        
        poller = self.begin_update_reflex_definition(
            workspace_id=workspace_id,
            reflex_id=reflex_id,
            update_reflex_definition_request=update_reflex_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_reflex_definition(self, workspace_id: None, reflex_id: None, update_reflex_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Reflex.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Reflex's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :param update_reflex_definition_request: Update Reflex definition request payload. Required.
        :type update_reflex_definition_request:
         ~microsoft.fabric.api.reflex.models.UpdateReflexDefinitionRequest
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

        

        return super().begin_update_reflex_definition(
            workspace_id=workspace_id,
            reflex_id=reflex_id,
            update_reflex_definition_request=update_reflex_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_reflex_definition(self, workspace_id: None, reflex_id: None, update_reflex_definition_request: None) -> None:
        """Overrides the definition for the specified Reflex.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Reflex's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :param update_reflex_definition_request: Update Reflex definition request payload. Required.
        :type update_reflex_definition_request: IO[bytes]
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

        
        poller = self.begin_update_reflex_definition(
            workspace_id=workspace_id,
            reflex_id=reflex_id,
            update_reflex_definition_request=update_reflex_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_reflex_definition(self, workspace_id: None, reflex_id: None, update_reflex_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Reflex.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Reflex's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :param update_reflex_definition_request: Update Reflex definition request payload. Required.
        :type update_reflex_definition_request: IO[bytes]
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

        

        return super().begin_update_reflex_definition(
            workspace_id=workspace_id,
            reflex_id=reflex_id,
            update_reflex_definition_request=update_reflex_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_reflex_definition(self, workspace_id: None, reflex_id: None, update_reflex_definition_request: None) -> None:
        """Overrides the definition for the specified Reflex.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Reflex's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :param update_reflex_definition_request: Update Reflex definition request payload. Is either a
         UpdateReflexDefinitionRequest type or a IO[bytes] type. Required.
        :type update_reflex_definition_request:
         ~microsoft.fabric.api.reflex.models.UpdateReflexDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_reflex_definition(
            workspace_id=workspace_id,
            reflex_id=reflex_id,
            update_reflex_definition_request=update_reflex_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_reflex_definition(self, workspace_id: None, reflex_id: None, update_reflex_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Reflex.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the Reflex's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the reflex.

        Required Delegated Scopes
        -------------------------

         Reflex.ReadWrite.All or Item.ReadWrite.All

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
        :param reflex_id: The Reflex ID. Required.
        :type reflex_id: str
        :param update_reflex_definition_request: Update Reflex definition request payload. Is either a
         UpdateReflexDefinitionRequest type or a IO[bytes] type. Required.
        :type update_reflex_definition_request:
         ~microsoft.fabric.api.reflex.models.UpdateReflexDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_reflex_definition(
            workspace_id=workspace_id,
            reflex_id=reflex_id,
            update_reflex_definition_request=update_reflex_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
