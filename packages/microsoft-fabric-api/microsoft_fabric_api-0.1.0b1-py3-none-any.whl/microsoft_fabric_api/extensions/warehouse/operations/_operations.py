from ....generated.warehouse.operations import *
from ....generated.warehouse import operations as _operations
from ....generated.warehouse import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Warehouse."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_warehouse(self, workspace_id: None, create_warehouse_request: None) -> _models.Warehouse:
        """Creates a warehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create a warehouse with definition.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a warehouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_request: Create item request payload. Required.
        :type create_warehouse_request: ~microsoft.fabric.api.warehouse.models.CreateWarehouseRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Warehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.Warehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_warehouse(workspace_id=workspace_id, create_warehouse_request=create_warehouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_warehouse(self, workspace_id: None, create_warehouse_request: None) -> _LROResultExtractor[_models.Warehouse]:
        """Creates a warehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create a warehouse with definition.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a warehouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_request: Create item request payload. Required.
        :type create_warehouse_request: ~microsoft.fabric.api.warehouse.models.CreateWarehouseRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Warehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.Warehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Warehouse]()

        poller = super().begin_create_warehouse(
            workspace_id=workspace_id,
            create_warehouse_request=create_warehouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_warehouse(self, workspace_id: None, create_warehouse_request: None) -> _models.Warehouse:
        """Creates a warehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create a warehouse with definition.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a warehouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_request: Create item request payload. Required.
        :type create_warehouse_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Warehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.Warehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_warehouse(workspace_id=workspace_id, create_warehouse_request=create_warehouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_warehouse(self, workspace_id: None, create_warehouse_request: None) -> _LROResultExtractor[_models.Warehouse]:
        """Creates a warehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create a warehouse with definition.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a warehouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_request: Create item request payload. Required.
        :type create_warehouse_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Warehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.Warehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Warehouse]()

        poller = super().begin_create_warehouse(
            workspace_id=workspace_id,
            create_warehouse_request=create_warehouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_warehouse(self, workspace_id: None, create_warehouse_request: None) -> _models.Warehouse:
        """Creates a warehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create a warehouse with definition.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a warehouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_request: Create item request payload. Is either a
         CreateWarehouseRequest type or a IO[bytes] type. Required.
        :type create_warehouse_request: ~microsoft.fabric.api.warehouse.models.CreateWarehouseRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns Warehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.Warehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_warehouse(workspace_id=workspace_id, create_warehouse_request=create_warehouse_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_warehouse(self, workspace_id: None, create_warehouse_request: None) -> _LROResultExtractor[_models.Warehouse]:
        """Creates a warehouse in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create a warehouse with definition.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a warehouse the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_request: Create item request payload. Is either a
         CreateWarehouseRequest type or a IO[bytes] type. Required.
        :type create_warehouse_request: ~microsoft.fabric.api.warehouse.models.CreateWarehouseRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns Warehouse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.Warehouse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Warehouse]()

        poller = super().begin_create_warehouse(
            workspace_id=workspace_id,
            create_warehouse_request=create_warehouse_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    


class RestorePointsOperations(_operations.RestorePointsOperations):
    """RestorePointsOperations for Warehouse."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_restore_point(self, workspace_id: None, warehouse_id: None, create_restore_point_request: None) -> _models.RestorePoint:
        """Creates a restore point for a warehouse at the current timestamp.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *write* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

        Warehouse deletes both the system-created and user-defined restore point at the expiry of the
        30 calendar day retention period.

        A restore point cannot be created if there is already a restore point creation already
        in-progress or during warehouse creation, deletion or rename.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param create_restore_point_request: Create restore point payload. Required.
        :type create_restore_point_request:
         ~microsoft.fabric.api.warehouse.models.CreateRestorePointRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns RestorePoint
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.RestorePoint]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_restore_point(workspace_id=workspace_id, warehouse_id=warehouse_id, create_restore_point_request=create_restore_point_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_restore_point(self, workspace_id: None, warehouse_id: None, create_restore_point_request: None) -> _LROResultExtractor[_models.RestorePoint]:
        """Creates a restore point for a warehouse at the current timestamp.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *write* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

        Warehouse deletes both the system-created and user-defined restore point at the expiry of the
        30 calendar day retention period.

        A restore point cannot be created if there is already a restore point creation already
        in-progress or during warehouse creation, deletion or rename.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param create_restore_point_request: Create restore point payload. Required.
        :type create_restore_point_request:
         ~microsoft.fabric.api.warehouse.models.CreateRestorePointRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns RestorePoint
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.RestorePoint]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.RestorePoint]()

        poller = super().begin_create_restore_point(
            workspace_id=workspace_id,
            warehouse_id=warehouse_id,
            create_restore_point_request=create_restore_point_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_restore_point(self, workspace_id: None, warehouse_id: None, create_restore_point_request: None) -> _models.RestorePoint:
        """Creates a restore point for a warehouse at the current timestamp.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *write* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

        Warehouse deletes both the system-created and user-defined restore point at the expiry of the
        30 calendar day retention period.

        A restore point cannot be created if there is already a restore point creation already
        in-progress or during warehouse creation, deletion or rename.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param create_restore_point_request: Create restore point payload. Required.
        :type create_restore_point_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns RestorePoint
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.RestorePoint]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_restore_point(workspace_id=workspace_id, warehouse_id=warehouse_id, create_restore_point_request=create_restore_point_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_restore_point(self, workspace_id: None, warehouse_id: None, create_restore_point_request: None) -> _LROResultExtractor[_models.RestorePoint]:
        """Creates a restore point for a warehouse at the current timestamp.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *write* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

        Warehouse deletes both the system-created and user-defined restore point at the expiry of the
        30 calendar day retention period.

        A restore point cannot be created if there is already a restore point creation already
        in-progress or during warehouse creation, deletion or rename.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param create_restore_point_request: Create restore point payload. Required.
        :type create_restore_point_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns RestorePoint
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.RestorePoint]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.RestorePoint]()

        poller = super().begin_create_restore_point(
            workspace_id=workspace_id,
            warehouse_id=warehouse_id,
            create_restore_point_request=create_restore_point_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_restore_point(self, workspace_id: None, warehouse_id: None, create_restore_point_request: None) -> _models.RestorePoint:
        """Creates a restore point for a warehouse at the current timestamp.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *write* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

        Warehouse deletes both the system-created and user-defined restore point at the expiry of the
        30 calendar day retention period.

        A restore point cannot be created if there is already a restore point creation already
        in-progress or during warehouse creation, deletion or rename.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param create_restore_point_request: Create restore point payload. Is either a
         CreateRestorePointRequest type or a IO[bytes] type. Required.
        :type create_restore_point_request:
         ~microsoft.fabric.api.warehouse.models.CreateRestorePointRequest or IO[bytes]
        :return: An instance of LROPoller that returns RestorePoint
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.RestorePoint]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_restore_point(workspace_id=workspace_id, warehouse_id=warehouse_id, create_restore_point_request=create_restore_point_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_restore_point(self, workspace_id: None, warehouse_id: None, create_restore_point_request: None) -> _LROResultExtractor[_models.RestorePoint]:
        """Creates a restore point for a warehouse at the current timestamp.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *write* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

        Warehouse deletes both the system-created and user-defined restore point at the expiry of the
        30 calendar day retention period.

        A restore point cannot be created if there is already a restore point creation already
        in-progress or during warehouse creation, deletion or rename.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param create_restore_point_request: Create restore point payload. Is either a
         CreateRestorePointRequest type or a IO[bytes] type. Required.
        :type create_restore_point_request:
         ~microsoft.fabric.api.warehouse.models.CreateRestorePointRequest or IO[bytes]
        :return: An instance of LROPoller that returns RestorePoint
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehouse.models.RestorePoint]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.RestorePoint]()

        poller = super().begin_create_restore_point(
            workspace_id=workspace_id,
            warehouse_id=warehouse_id,
            create_restore_point_request=create_restore_point_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def restore_to_restore_point(self, workspace_id: None, warehouse_id: None, restore_point_id: None) -> None:
        """Restores a warehouse in-place to the restore point specified.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *restore* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.Restore.All

        Limitations
        -----------

        A restore point cannot be restored if there is another restore point restoration already
        in-progress.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param restore_point_id: The restore point ID. Required.
        :type restore_point_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_restore_to_restore_point(
            workspace_id=workspace_id,
            warehouse_id=warehouse_id,
            restore_point_id=restore_point_id)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_restore_to_restore_point(self, workspace_id: None, warehouse_id: None, restore_point_id: None) -> LROPoller[None]:
        """Restores a warehouse in-place to the restore point specified.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *restore* warehouse permission.

        Required Delegated Scopes
        -------------------------

        Warehouse.Restore.All

        Limitations
        -----------

        A restore point cannot be restored if there is another restore point restoration already
        in-progress.

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
        :param warehouse_id: The warehouse ID. Required.
        :type warehouse_id: str
        :param restore_point_id: The restore point ID. Required.
        :type restore_point_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_restore_to_restore_point(
            workspace_id=workspace_id,
            warehouse_id=warehouse_id,
            restore_point_id=restore_point_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
