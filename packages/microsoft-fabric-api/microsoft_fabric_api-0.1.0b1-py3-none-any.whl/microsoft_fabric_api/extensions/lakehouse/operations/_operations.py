from ....generated.lakehouse.operations import *
from ....generated.lakehouse import operations as _operations
from ....generated.lakehouse import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Lakehouse."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_lakehouse(self, workspace_id: None, create_lakehouse_request: None) -> _models.Lakehouse:
        """Creates a lakehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        This API does not support create a lakehouse with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Lakehouse.ReadWrite.All or Item.ReadWrite.All

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
        :param create_lakehouse_request: Create item request payload. Required.
        :type create_lakehouse_request: ~microsoft.fabric.api.lakehouse.models.CreateLakehouseRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Lakehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.lakehouse.models.Lakehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_lakehouse(workspace_id=workspace_id, create_lakehouse_request=create_lakehouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_lakehouse(self, workspace_id: None, create_lakehouse_request: None) -> _LROResultExtractor[_models.Lakehouse]:
        """Creates a lakehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        This API does not support create a lakehouse with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Lakehouse.ReadWrite.All or Item.ReadWrite.All

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
        :param create_lakehouse_request: Create item request payload. Required.
        :type create_lakehouse_request: ~microsoft.fabric.api.lakehouse.models.CreateLakehouseRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Lakehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.lakehouse.models.Lakehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Lakehouse]()

        poller = super().begin_create_lakehouse(
            workspace_id=workspace_id,
            create_lakehouse_request=create_lakehouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_lakehouse(self, workspace_id: None, create_lakehouse_request: None) -> _models.Lakehouse:
        """Creates a lakehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        This API does not support create a lakehouse with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Lakehouse.ReadWrite.All or Item.ReadWrite.All

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
        :param create_lakehouse_request: Create item request payload. Required.
        :type create_lakehouse_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Lakehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.lakehouse.models.Lakehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_lakehouse(workspace_id=workspace_id, create_lakehouse_request=create_lakehouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_lakehouse(self, workspace_id: None, create_lakehouse_request: None) -> _LROResultExtractor[_models.Lakehouse]:
        """Creates a lakehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        This API does not support create a lakehouse with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Lakehouse.ReadWrite.All or Item.ReadWrite.All

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
        :param create_lakehouse_request: Create item request payload. Required.
        :type create_lakehouse_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Lakehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.lakehouse.models.Lakehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Lakehouse]()

        poller = super().begin_create_lakehouse(
            workspace_id=workspace_id,
            create_lakehouse_request=create_lakehouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_lakehouse(self, workspace_id: None, create_lakehouse_request: None) -> _models.Lakehouse:
        """Creates a lakehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        This API does not support create a lakehouse with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Lakehouse.ReadWrite.All or Item.ReadWrite.All

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
        :param create_lakehouse_request: Create item request payload. Is either a
         CreateLakehouseRequest type or a IO[bytes] type. Required.
        :type create_lakehouse_request: ~microsoft.fabric.api.lakehouse.models.CreateLakehouseRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns Lakehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.lakehouse.models.Lakehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_lakehouse(workspace_id=workspace_id, create_lakehouse_request=create_lakehouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_lakehouse(self, workspace_id: None, create_lakehouse_request: None) -> _LROResultExtractor[_models.Lakehouse]:
        """Creates a lakehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        This API does not support create a lakehouse with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Lakehouse.ReadWrite.All or Item.ReadWrite.All

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
        :param create_lakehouse_request: Create item request payload. Is either a
         CreateLakehouseRequest type or a IO[bytes] type. Required.
        :type create_lakehouse_request: ~microsoft.fabric.api.lakehouse.models.CreateLakehouseRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns Lakehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.lakehouse.models.Lakehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Lakehouse]()

        poller = super().begin_create_lakehouse(
            workspace_id=workspace_id,
            create_lakehouse_request=create_lakehouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    


class TablesOperations(_operations.TablesOperations):
    """TablesOperations for Lakehouse."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def load_table(self, workspace_id: None, lakehouse_id: None, table_name: None, load_table_request: None) -> None:
        """Starts a load table operation and returns the operation status URL in the response location
        header.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission to the lakehouse item.

        Required Delegated Scopes
        -------------------------

        Lakehouse.ReadWrite.All

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
        :param lakehouse_id: The lakehouse item ID. Required.
        :type lakehouse_id: str
        :param table_name: The table name. Required.
        :type table_name: str
        :param load_table_request: The load table request payload. Required.
        :type load_table_request: ~microsoft.fabric.api.lakehouse.models.LoadTableRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_load_table(
            workspace_id=workspace_id,
            lakehouse_id=lakehouse_id,
            table_name=table_name,
            load_table_request=load_table_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_load_table(self, workspace_id: None, lakehouse_id: None, table_name: None, load_table_request: None) -> LROPoller[None]:
        """Starts a load table operation and returns the operation status URL in the response location
        header.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission to the lakehouse item.

        Required Delegated Scopes
        -------------------------

        Lakehouse.ReadWrite.All

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
        :param lakehouse_id: The lakehouse item ID. Required.
        :type lakehouse_id: str
        :param table_name: The table name. Required.
        :type table_name: str
        :param load_table_request: The load table request payload. Required.
        :type load_table_request: ~microsoft.fabric.api.lakehouse.models.LoadTableRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_load_table(
            workspace_id=workspace_id,
            lakehouse_id=lakehouse_id,
            table_name=table_name,
            load_table_request=load_table_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def load_table(self, workspace_id: None, lakehouse_id: None, table_name: None, load_table_request: None) -> None:
        """Starts a load table operation and returns the operation status URL in the response location
        header.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission to the lakehouse item.

        Required Delegated Scopes
        -------------------------

        Lakehouse.ReadWrite.All

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
        :param lakehouse_id: The lakehouse item ID. Required.
        :type lakehouse_id: str
        :param table_name: The table name. Required.
        :type table_name: str
        :param load_table_request: The load table request payload. Required.
        :type load_table_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_load_table(
            workspace_id=workspace_id,
            lakehouse_id=lakehouse_id,
            table_name=table_name,
            load_table_request=load_table_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_load_table(self, workspace_id: None, lakehouse_id: None, table_name: None, load_table_request: None) -> LROPoller[None]:
        """Starts a load table operation and returns the operation status URL in the response location
        header.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission to the lakehouse item.

        Required Delegated Scopes
        -------------------------

        Lakehouse.ReadWrite.All

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
        :param lakehouse_id: The lakehouse item ID. Required.
        :type lakehouse_id: str
        :param table_name: The table name. Required.
        :type table_name: str
        :param load_table_request: The load table request payload. Required.
        :type load_table_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_load_table(
            workspace_id=workspace_id,
            lakehouse_id=lakehouse_id,
            table_name=table_name,
            load_table_request=load_table_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def load_table(self, workspace_id: None, lakehouse_id: None, table_name: None, load_table_request: None) -> None:
        """Starts a load table operation and returns the operation status URL in the response location
        header.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission to the lakehouse item.

        Required Delegated Scopes
        -------------------------

        Lakehouse.ReadWrite.All

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
        :param lakehouse_id: The lakehouse item ID. Required.
        :type lakehouse_id: str
        :param table_name: The table name. Required.
        :type table_name: str
        :param load_table_request: The load table request payload. Is either a LoadTableRequest type or
         a IO[bytes] type. Required.
        :type load_table_request: ~microsoft.fabric.api.lakehouse.models.LoadTableRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_load_table(
            workspace_id=workspace_id,
            lakehouse_id=lakehouse_id,
            table_name=table_name,
            load_table_request=load_table_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_load_table(self, workspace_id: None, lakehouse_id: None, table_name: None, load_table_request: None) -> LROPoller[None]:
        """Starts a load table operation and returns the operation status URL in the response location
        header.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission to the lakehouse item.

        Required Delegated Scopes
        -------------------------

        Lakehouse.ReadWrite.All

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
        :param lakehouse_id: The lakehouse item ID. Required.
        :type lakehouse_id: str
        :param table_name: The table name. Required.
        :type table_name: str
        :param load_table_request: The load table request payload. Is either a LoadTableRequest type or
         a IO[bytes] type. Required.
        :type load_table_request: ~microsoft.fabric.api.lakehouse.models.LoadTableRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_load_table(
            workspace_id=workspace_id,
            lakehouse_id=lakehouse_id,
            table_name=table_name,
            load_table_request=load_table_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
