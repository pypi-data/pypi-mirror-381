from ....generated.warehousesnapshot.operations import *
from ....generated.warehousesnapshot import operations as _operations
from ....generated.warehousesnapshot import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Warehousesnapshot."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_warehouse_snapshot(self, workspace_id: None, create_warehouse_snapshot_request: None) -> _models.WarehouseSnapshot:
        """Creates a Warehouse snapshot in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         WarehouseSnapshot.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Warehouse snapshot the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_snapshot_request: A create Warehouse snapshot request payload.
         Required.
        :type create_warehouse_snapshot_request:
         ~microsoft.fabric.api.warehousesnapshot.models.CreateWarehouseSnapshotRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns WarehouseSnapshot
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehousesnapshot.models.WarehouseSnapshot]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_warehouse_snapshot(workspace_id=workspace_id, create_warehouse_snapshot_request=create_warehouse_snapshot_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_warehouse_snapshot(self, workspace_id: None, create_warehouse_snapshot_request: None) -> _LROResultExtractor[_models.WarehouseSnapshot]:
        """Creates a Warehouse snapshot in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         WarehouseSnapshot.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Warehouse snapshot the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_snapshot_request: A create Warehouse snapshot request payload.
         Required.
        :type create_warehouse_snapshot_request:
         ~microsoft.fabric.api.warehousesnapshot.models.CreateWarehouseSnapshotRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns WarehouseSnapshot
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehousesnapshot.models.WarehouseSnapshot]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.WarehouseSnapshot]()

        poller = super().begin_create_warehouse_snapshot(
            workspace_id=workspace_id,
            create_warehouse_snapshot_request=create_warehouse_snapshot_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_warehouse_snapshot(self, workspace_id: None, create_warehouse_snapshot_request: None) -> _models.WarehouseSnapshot:
        """Creates a Warehouse snapshot in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         WarehouseSnapshot.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Warehouse snapshot the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_snapshot_request: A create Warehouse snapshot request payload.
         Required.
        :type create_warehouse_snapshot_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns WarehouseSnapshot
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehousesnapshot.models.WarehouseSnapshot]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_warehouse_snapshot(workspace_id=workspace_id, create_warehouse_snapshot_request=create_warehouse_snapshot_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_warehouse_snapshot(self, workspace_id: None, create_warehouse_snapshot_request: None) -> _LROResultExtractor[_models.WarehouseSnapshot]:
        """Creates a Warehouse snapshot in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         WarehouseSnapshot.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Warehouse snapshot the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_snapshot_request: A create Warehouse snapshot request payload.
         Required.
        :type create_warehouse_snapshot_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns WarehouseSnapshot
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehousesnapshot.models.WarehouseSnapshot]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.WarehouseSnapshot]()

        poller = super().begin_create_warehouse_snapshot(
            workspace_id=workspace_id,
            create_warehouse_snapshot_request=create_warehouse_snapshot_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_warehouse_snapshot(self, workspace_id: None, create_warehouse_snapshot_request: None) -> _models.WarehouseSnapshot:
        """Creates a Warehouse snapshot in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         WarehouseSnapshot.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Warehouse snapshot the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_snapshot_request: A create Warehouse snapshot request payload. Is
         either a CreateWarehouseSnapshotRequest type or a IO[bytes] type. Required.
        :type create_warehouse_snapshot_request:
         ~microsoft.fabric.api.warehousesnapshot.models.CreateWarehouseSnapshotRequest or IO[bytes]
        :return: An instance of LROPoller that returns WarehouseSnapshot
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehousesnapshot.models.WarehouseSnapshot]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_warehouse_snapshot(workspace_id=workspace_id, create_warehouse_snapshot_request=create_warehouse_snapshot_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_warehouse_snapshot(self, workspace_id: None, create_warehouse_snapshot_request: None) -> _LROResultExtractor[_models.WarehouseSnapshot]:
        """Creates a Warehouse snapshot in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         WarehouseSnapshot.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a Warehouse snapshot the workspace must be on a supported Fabric capacity. For more
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
        :param create_warehouse_snapshot_request: A create Warehouse snapshot request payload. Is
         either a CreateWarehouseSnapshotRequest type or a IO[bytes] type. Required.
        :type create_warehouse_snapshot_request:
         ~microsoft.fabric.api.warehousesnapshot.models.CreateWarehouseSnapshotRequest or IO[bytes]
        :return: An instance of LROPoller that returns WarehouseSnapshot
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.warehousesnapshot.models.WarehouseSnapshot]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.WarehouseSnapshot]()

        poller = super().begin_create_warehouse_snapshot(
            workspace_id=workspace_id,
            create_warehouse_snapshot_request=create_warehouse_snapshot_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    
