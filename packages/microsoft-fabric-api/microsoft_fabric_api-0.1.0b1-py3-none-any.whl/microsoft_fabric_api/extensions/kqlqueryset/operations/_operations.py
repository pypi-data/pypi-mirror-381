from ....generated.kqlqueryset.operations import *
from ....generated.kqlqueryset import operations as _operations
from ....generated.kqlqueryset import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Kqlqueryset."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_kql_queryset(self, workspace_id: None, create_kql_queryset_request: None) -> _models.KQLQueryset:
        """Creates a KQL queryset in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create a KQL queryset with definition, refer to the `KQL queryset definition article
        </rest/api/fabric/articles/item-management/definitions/kql-queryset-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

        KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param create_kql_queryset_request: Create item request payload. Required.
        :type create_kql_queryset_request:
         ~microsoft.fabric.api.kqlqueryset.models.CreateKQLQuerysetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns KQLQueryset
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQueryset]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_kql_queryset(workspace_id=workspace_id, create_kql_queryset_request=create_kql_queryset_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_kql_queryset(self, workspace_id: None, create_kql_queryset_request: None) -> _LROResultExtractor[_models.KQLQueryset]:
        """Creates a KQL queryset in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create a KQL queryset with definition, refer to the `KQL queryset definition article
        </rest/api/fabric/articles/item-management/definitions/kql-queryset-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

        KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param create_kql_queryset_request: Create item request payload. Required.
        :type create_kql_queryset_request:
         ~microsoft.fabric.api.kqlqueryset.models.CreateKQLQuerysetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns KQLQueryset
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQueryset]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.KQLQueryset]()

        poller = super().begin_create_kql_queryset(
            workspace_id=workspace_id,
            create_kql_queryset_request=create_kql_queryset_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_kql_queryset(self, workspace_id: None, create_kql_queryset_request: None) -> _models.KQLQueryset:
        """Creates a KQL queryset in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create a KQL queryset with definition, refer to the `KQL queryset definition article
        </rest/api/fabric/articles/item-management/definitions/kql-queryset-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

        KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param create_kql_queryset_request: Create item request payload. Required.
        :type create_kql_queryset_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns KQLQueryset
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQueryset]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_kql_queryset(workspace_id=workspace_id, create_kql_queryset_request=create_kql_queryset_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_kql_queryset(self, workspace_id: None, create_kql_queryset_request: None) -> _LROResultExtractor[_models.KQLQueryset]:
        """Creates a KQL queryset in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create a KQL queryset with definition, refer to the `KQL queryset definition article
        </rest/api/fabric/articles/item-management/definitions/kql-queryset-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

        KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param create_kql_queryset_request: Create item request payload. Required.
        :type create_kql_queryset_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns KQLQueryset
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQueryset]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.KQLQueryset]()

        poller = super().begin_create_kql_queryset(
            workspace_id=workspace_id,
            create_kql_queryset_request=create_kql_queryset_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_kql_queryset(self, workspace_id: None, create_kql_queryset_request: None) -> _models.KQLQueryset:
        """Creates a KQL queryset in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create a KQL queryset with definition, refer to the `KQL queryset definition article
        </rest/api/fabric/articles/item-management/definitions/kql-queryset-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

        KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param create_kql_queryset_request: Create item request payload. Is either a
         CreateKQLQuerysetRequest type or a IO[bytes] type. Required.
        :type create_kql_queryset_request:
         ~microsoft.fabric.api.kqlqueryset.models.CreateKQLQuerysetRequest or IO[bytes]
        :return: An instance of LROPoller that returns KQLQueryset
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQueryset]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_kql_queryset(workspace_id=workspace_id, create_kql_queryset_request=create_kql_queryset_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_kql_queryset(self, workspace_id: None, create_kql_queryset_request: None) -> _LROResultExtractor[_models.KQLQueryset]:
        """Creates a KQL queryset in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create a KQL queryset with definition, refer to the `KQL queryset definition article
        </rest/api/fabric/articles/item-management/definitions/kql-queryset-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

        KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param create_kql_queryset_request: Create item request payload. Is either a
         CreateKQLQuerysetRequest type or a IO[bytes] type. Required.
        :type create_kql_queryset_request:
         ~microsoft.fabric.api.kqlqueryset.models.CreateKQLQuerysetRequest or IO[bytes]
        :return: An instance of LROPoller that returns KQLQueryset
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQueryset]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.KQLQueryset]()

        poller = super().begin_create_kql_queryset(
            workspace_id=workspace_id,
            create_kql_queryset_request=create_kql_queryset_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None) -> _models.KQLQuerysetDefinitionResponse:
        """Returns the specified KQL queryset public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :keyword format: The format of the KQL queryset public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns KQLQuerysetDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQuerysetDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_kql_queryset_definition(workspace_id=workspace_id, kql_queryset_id=kql_queryset_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None) -> _LROResultExtractor[_models.KQLQuerysetDefinitionResponse]:
        """Returns the specified KQL queryset public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :keyword format: The format of the KQL queryset public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns KQLQuerysetDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.kqlqueryset.models.KQLQuerysetDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.KQLQuerysetDefinitionResponse]()

        poller = super().begin_get_kql_queryset_definition(
            workspace_id=workspace_id,
            kql_queryset_id=kql_queryset_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None, update_kql_queryset_definition_request: None) -> None:
        """Overrides the definition for the specified KQL queryset.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :param update_kql_queryset_definition_request: Update KQL queryset definition request payload.
         Required.
        :type update_kql_queryset_definition_request:
         ~microsoft.fabric.api.kqlqueryset.models.UpdateKQLQuerysetDefinitionRequest
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

        
        poller = self.begin_update_kql_queryset_definition(
            workspace_id=workspace_id,
            kql_queryset_id=kql_queryset_id,
            update_kql_queryset_definition_request=update_kql_queryset_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None, update_kql_queryset_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified KQL queryset.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :param update_kql_queryset_definition_request: Update KQL queryset definition request payload.
         Required.
        :type update_kql_queryset_definition_request:
         ~microsoft.fabric.api.kqlqueryset.models.UpdateKQLQuerysetDefinitionRequest
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

        

        return super().begin_update_kql_queryset_definition(
            workspace_id=workspace_id,
            kql_queryset_id=kql_queryset_id,
            update_kql_queryset_definition_request=update_kql_queryset_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None, update_kql_queryset_definition_request: None) -> None:
        """Overrides the definition for the specified KQL queryset.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :param update_kql_queryset_definition_request: Update KQL queryset definition request payload.
         Required.
        :type update_kql_queryset_definition_request: IO[bytes]
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

        
        poller = self.begin_update_kql_queryset_definition(
            workspace_id=workspace_id,
            kql_queryset_id=kql_queryset_id,
            update_kql_queryset_definition_request=update_kql_queryset_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None, update_kql_queryset_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified KQL queryset.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :param update_kql_queryset_definition_request: Update KQL queryset definition request payload.
         Required.
        :type update_kql_queryset_definition_request: IO[bytes]
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

        

        return super().begin_update_kql_queryset_definition(
            workspace_id=workspace_id,
            kql_queryset_id=kql_queryset_id,
            update_kql_queryset_definition_request=update_kql_queryset_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None, update_kql_queryset_definition_request: None) -> None:
        """Overrides the definition for the specified KQL queryset.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :param update_kql_queryset_definition_request: Update KQL queryset definition request payload.
         Is either a UpdateKQLQuerysetDefinitionRequest type or a IO[bytes] type. Required.
        :type update_kql_queryset_definition_request:
         ~microsoft.fabric.api.kqlqueryset.models.UpdateKQLQuerysetDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_kql_queryset_definition(
            workspace_id=workspace_id,
            kql_queryset_id=kql_queryset_id,
            update_kql_queryset_definition_request=update_kql_queryset_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_kql_queryset_definition(self, workspace_id: None, kql_queryset_id: None, update_kql_queryset_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified KQL queryset.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the KQL queryset.

        Required Delegated Scopes
        -------------------------

         KQLQueryset.ReadWrite.All or Item.ReadWrite.All

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
        :param kql_queryset_id: The KQL queryset ID. Required.
        :type kql_queryset_id: str
        :param update_kql_queryset_definition_request: Update KQL queryset definition request payload.
         Is either a UpdateKQLQuerysetDefinitionRequest type or a IO[bytes] type. Required.
        :type update_kql_queryset_definition_request:
         ~microsoft.fabric.api.kqlqueryset.models.UpdateKQLQuerysetDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_kql_queryset_definition(
            workspace_id=workspace_id,
            kql_queryset_id=kql_queryset_id,
            update_kql_queryset_definition_request=update_kql_queryset_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
