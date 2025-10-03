from ....generated.mirroreddatabase.operations import *
from ....generated.mirroreddatabase import operations as _operations
from ....generated.mirroreddatabase import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Mirroreddatabase."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def get_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None) -> _models.MirroredDatabaseDefinitionResponse:
        """Returns the specified mirrored database public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :return: An instance of LROPoller that returns MirroredDatabaseDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroreddatabase.models.MirroredDatabaseDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_mirrored_database_definition(workspace_id=workspace_id, mirrored_database_id=mirrored_database_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None) -> _LROResultExtractor[_models.MirroredDatabaseDefinitionResponse]:
        """Returns the specified mirrored database public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :return: An instance of LROPoller that returns MirroredDatabaseDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroreddatabase.models.MirroredDatabaseDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MirroredDatabaseDefinitionResponse]()

        poller = super().begin_get_mirrored_database_definition(
            workspace_id=workspace_id,
            mirrored_database_id=mirrored_database_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None, update_mirrored_database_definition_request: None) -> None:
        """Overrides the definition for the specified mirrored database.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :param update_mirrored_database_definition_request: Update mirrored database definition request
         payload. Required.
        :type update_mirrored_database_definition_request:
         ~microsoft.fabric.api.mirroreddatabase.models.UpdateMirroredDatabaseDefinitionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_mirrored_database_definition(
            workspace_id=workspace_id,
            mirrored_database_id=mirrored_database_id,
            update_mirrored_database_definition_request=update_mirrored_database_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None, update_mirrored_database_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified mirrored database.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :param update_mirrored_database_definition_request: Update mirrored database definition request
         payload. Required.
        :type update_mirrored_database_definition_request:
         ~microsoft.fabric.api.mirroreddatabase.models.UpdateMirroredDatabaseDefinitionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_mirrored_database_definition(
            workspace_id=workspace_id,
            mirrored_database_id=mirrored_database_id,
            update_mirrored_database_definition_request=update_mirrored_database_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None, update_mirrored_database_definition_request: None) -> None:
        """Overrides the definition for the specified mirrored database.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :param update_mirrored_database_definition_request: Update mirrored database definition request
         payload. Required.
        :type update_mirrored_database_definition_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_mirrored_database_definition(
            workspace_id=workspace_id,
            mirrored_database_id=mirrored_database_id,
            update_mirrored_database_definition_request=update_mirrored_database_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None, update_mirrored_database_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified mirrored database.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :param update_mirrored_database_definition_request: Update mirrored database definition request
         payload. Required.
        :type update_mirrored_database_definition_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_mirrored_database_definition(
            workspace_id=workspace_id,
            mirrored_database_id=mirrored_database_id,
            update_mirrored_database_definition_request=update_mirrored_database_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None, update_mirrored_database_definition_request: None) -> None:
        """Overrides the definition for the specified mirrored database.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :param update_mirrored_database_definition_request: Update mirrored database definition request
         payload. Is either a UpdateMirroredDatabaseDefinitionRequest type or a IO[bytes] type.
         Required.
        :type update_mirrored_database_definition_request:
         ~microsoft.fabric.api.mirroreddatabase.models.UpdateMirroredDatabaseDefinitionRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_mirrored_database_definition(
            workspace_id=workspace_id,
            mirrored_database_id=mirrored_database_id,
            update_mirrored_database_definition_request=update_mirrored_database_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_mirrored_database_definition(self, workspace_id: None, mirrored_database_id: None, update_mirrored_database_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified mirrored database.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored database.

        Required Delegated Scopes
        -------------------------

         MirroredDatabase.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_database_id: The mirrored database ID. Required.
        :type mirrored_database_id: str
        :param update_mirrored_database_definition_request: Update mirrored database definition request
         payload. Is either a UpdateMirroredDatabaseDefinitionRequest type or a IO[bytes] type.
         Required.
        :type update_mirrored_database_definition_request:
         ~microsoft.fabric.api.mirroreddatabase.models.UpdateMirroredDatabaseDefinitionRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_mirrored_database_definition(
            workspace_id=workspace_id,
            mirrored_database_id=mirrored_database_id,
            update_mirrored_database_definition_request=update_mirrored_database_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
