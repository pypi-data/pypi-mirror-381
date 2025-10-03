from ....generated.sqlendpoint.operations import *
from ....generated.sqlendpoint import operations as _operations
from ....generated.sqlendpoint import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Sqlendpoint."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def refresh_sql_endpoint_metadata(self, workspace_id: None, sql_endpoint_id: None, sql_endpoint_refresh_metadata_request: None) -> _models.TableSyncStatuses:
        """Refreshes all tables within a SQL analytics endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All

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
        :param sql_endpoint_id: The SQL analytics endpoint ID. Required.
        :type sql_endpoint_id: str
        :param sql_endpoint_refresh_metadata_request: Refresh SQL analytics endpoint request payload.
         Default value is None.
        :type sql_endpoint_refresh_metadata_request:
         ~microsoft.fabric.api.sqlendpoint.models.SqlEndpointRefreshMetadataRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns TableSyncStatuses
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sqlendpoint.models.TableSyncStatuses]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_refresh_sql_endpoint_metadata(workspace_id=workspace_id, sql_endpoint_id=sql_endpoint_id, sql_endpoint_refresh_metadata_request=sql_endpoint_refresh_metadata_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_refresh_sql_endpoint_metadata(self, workspace_id: None, sql_endpoint_id: None, sql_endpoint_refresh_metadata_request: None) -> _LROResultExtractor[_models.TableSyncStatuses]:
        """Refreshes all tables within a SQL analytics endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All

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
        :param sql_endpoint_id: The SQL analytics endpoint ID. Required.
        :type sql_endpoint_id: str
        :param sql_endpoint_refresh_metadata_request: Refresh SQL analytics endpoint request payload.
         Default value is None.
        :type sql_endpoint_refresh_metadata_request:
         ~microsoft.fabric.api.sqlendpoint.models.SqlEndpointRefreshMetadataRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns TableSyncStatuses
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sqlendpoint.models.TableSyncStatuses]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.TableSyncStatuses]()

        poller = super().begin_refresh_sql_endpoint_metadata(
            workspace_id=workspace_id,
            sql_endpoint_id=sql_endpoint_id,
            sql_endpoint_refresh_metadata_request=sql_endpoint_refresh_metadata_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def refresh_sql_endpoint_metadata(self, workspace_id: None, sql_endpoint_id: None, sql_endpoint_refresh_metadata_request: None) -> _models.TableSyncStatuses:
        """Refreshes all tables within a SQL analytics endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All

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
        :param sql_endpoint_id: The SQL analytics endpoint ID. Required.
        :type sql_endpoint_id: str
        :param sql_endpoint_refresh_metadata_request: Refresh SQL analytics endpoint request payload.
         Default value is None.
        :type sql_endpoint_refresh_metadata_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns TableSyncStatuses
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sqlendpoint.models.TableSyncStatuses]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_refresh_sql_endpoint_metadata(workspace_id=workspace_id, sql_endpoint_id=sql_endpoint_id, sql_endpoint_refresh_metadata_request=sql_endpoint_refresh_metadata_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_refresh_sql_endpoint_metadata(self, workspace_id: None, sql_endpoint_id: None, sql_endpoint_refresh_metadata_request: None) -> _LROResultExtractor[_models.TableSyncStatuses]:
        """Refreshes all tables within a SQL analytics endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All

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
        :param sql_endpoint_id: The SQL analytics endpoint ID. Required.
        :type sql_endpoint_id: str
        :param sql_endpoint_refresh_metadata_request: Refresh SQL analytics endpoint request payload.
         Default value is None.
        :type sql_endpoint_refresh_metadata_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns TableSyncStatuses
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sqlendpoint.models.TableSyncStatuses]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.TableSyncStatuses]()

        poller = super().begin_refresh_sql_endpoint_metadata(
            workspace_id=workspace_id,
            sql_endpoint_id=sql_endpoint_id,
            sql_endpoint_refresh_metadata_request=sql_endpoint_refresh_metadata_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def refresh_sql_endpoint_metadata(self, workspace_id: None, sql_endpoint_id: None, sql_endpoint_refresh_metadata_request: None) -> _models.TableSyncStatuses:
        """Refreshes all tables within a SQL analytics endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All

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
        :param sql_endpoint_id: The SQL analytics endpoint ID. Required.
        :type sql_endpoint_id: str
        :param sql_endpoint_refresh_metadata_request: Refresh SQL analytics endpoint request payload.
         Is either a SqlEndpointRefreshMetadataRequest type or a IO[bytes] type. Default value is None.
        :type sql_endpoint_refresh_metadata_request:
         ~microsoft.fabric.api.sqlendpoint.models.SqlEndpointRefreshMetadataRequest or IO[bytes]
        :return: An instance of LROPoller that returns TableSyncStatuses
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sqlendpoint.models.TableSyncStatuses]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_refresh_sql_endpoint_metadata(workspace_id=workspace_id, sql_endpoint_id=sql_endpoint_id, sql_endpoint_refresh_metadata_request=sql_endpoint_refresh_metadata_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_refresh_sql_endpoint_metadata(self, workspace_id: None, sql_endpoint_id: None, sql_endpoint_refresh_metadata_request: None) -> _LROResultExtractor[_models.TableSyncStatuses]:
        """Refreshes all tables within a SQL analytics endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All

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
        :param sql_endpoint_id: The SQL analytics endpoint ID. Required.
        :type sql_endpoint_id: str
        :param sql_endpoint_refresh_metadata_request: Refresh SQL analytics endpoint request payload.
         Is either a SqlEndpointRefreshMetadataRequest type or a IO[bytes] type. Default value is None.
        :type sql_endpoint_refresh_metadata_request:
         ~microsoft.fabric.api.sqlendpoint.models.SqlEndpointRefreshMetadataRequest or IO[bytes]
        :return: An instance of LROPoller that returns TableSyncStatuses
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.sqlendpoint.models.TableSyncStatuses]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.TableSyncStatuses]()

        poller = super().begin_refresh_sql_endpoint_metadata(
            workspace_id=workspace_id,
            sql_endpoint_id=sql_endpoint_id,
            sql_endpoint_refresh_metadata_request=sql_endpoint_refresh_metadata_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    
