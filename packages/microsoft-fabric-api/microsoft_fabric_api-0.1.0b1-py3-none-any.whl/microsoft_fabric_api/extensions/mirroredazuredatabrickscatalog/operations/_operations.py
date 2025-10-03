from ....generated.mirroredazuredatabrickscatalog.operations import *
from ....generated.mirroredazuredatabrickscatalog import operations as _operations
from ....generated.mirroredazuredatabrickscatalog import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Mirroredazuredatabrickscatalog."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_mirrored_azure_databricks_catalog(self, workspace_id: None, create_mirrored_azure_databricks_catalog_request: None) -> _models.MirroredAzureDatabricksCatalog:
        """Creates a mirroredAzureDatabricksCatalog in the specified workspace.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param create_mirrored_azure_databricks_catalog_request: Create item request payload. Required.
        :type create_mirrored_azure_databricks_catalog_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.CreateMirroredAzureDatabricksCatalogRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalog
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalog]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_mirrored_azure_databricks_catalog(workspace_id=workspace_id, create_mirrored_azure_databricks_catalog_request=create_mirrored_azure_databricks_catalog_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_mirrored_azure_databricks_catalog(self, workspace_id: None, create_mirrored_azure_databricks_catalog_request: None) -> _LROResultExtractor[_models.MirroredAzureDatabricksCatalog]:
        """Creates a mirroredAzureDatabricksCatalog in the specified workspace.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param create_mirrored_azure_databricks_catalog_request: Create item request payload. Required.
        :type create_mirrored_azure_databricks_catalog_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.CreateMirroredAzureDatabricksCatalogRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalog
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalog]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MirroredAzureDatabricksCatalog]()

        poller = super().begin_create_mirrored_azure_databricks_catalog(
            workspace_id=workspace_id,
            create_mirrored_azure_databricks_catalog_request=create_mirrored_azure_databricks_catalog_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_mirrored_azure_databricks_catalog(self, workspace_id: None, create_mirrored_azure_databricks_catalog_request: None) -> _models.MirroredAzureDatabricksCatalog:
        """Creates a mirroredAzureDatabricksCatalog in the specified workspace.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param create_mirrored_azure_databricks_catalog_request: Create item request payload. Required.
        :type create_mirrored_azure_databricks_catalog_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalog
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalog]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_mirrored_azure_databricks_catalog(workspace_id=workspace_id, create_mirrored_azure_databricks_catalog_request=create_mirrored_azure_databricks_catalog_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_mirrored_azure_databricks_catalog(self, workspace_id: None, create_mirrored_azure_databricks_catalog_request: None) -> _LROResultExtractor[_models.MirroredAzureDatabricksCatalog]:
        """Creates a mirroredAzureDatabricksCatalog in the specified workspace.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param create_mirrored_azure_databricks_catalog_request: Create item request payload. Required.
        :type create_mirrored_azure_databricks_catalog_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalog
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalog]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MirroredAzureDatabricksCatalog]()

        poller = super().begin_create_mirrored_azure_databricks_catalog(
            workspace_id=workspace_id,
            create_mirrored_azure_databricks_catalog_request=create_mirrored_azure_databricks_catalog_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_mirrored_azure_databricks_catalog(self, workspace_id: None, create_mirrored_azure_databricks_catalog_request: None) -> _models.MirroredAzureDatabricksCatalog:
        """Creates a mirroredAzureDatabricksCatalog in the specified workspace.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param create_mirrored_azure_databricks_catalog_request: Create item request payload. Is either
         a CreateMirroredAzureDatabricksCatalogRequest type or a IO[bytes] type. Required.
        :type create_mirrored_azure_databricks_catalog_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.CreateMirroredAzureDatabricksCatalogRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalog
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalog]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_mirrored_azure_databricks_catalog(workspace_id=workspace_id, create_mirrored_azure_databricks_catalog_request=create_mirrored_azure_databricks_catalog_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_mirrored_azure_databricks_catalog(self, workspace_id: None, create_mirrored_azure_databricks_catalog_request: None) -> _LROResultExtractor[_models.MirroredAzureDatabricksCatalog]:
        """Creates a mirroredAzureDatabricksCatalog in the specified workspace.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param create_mirrored_azure_databricks_catalog_request: Create item request payload. Is either
         a CreateMirroredAzureDatabricksCatalogRequest type or a IO[bytes] type. Required.
        :type create_mirrored_azure_databricks_catalog_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.CreateMirroredAzureDatabricksCatalogRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalog
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalog]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MirroredAzureDatabricksCatalog]()

        poller = super().begin_create_mirrored_azure_databricks_catalog(
            workspace_id=workspace_id,
            create_mirrored_azure_databricks_catalog_request=create_mirrored_azure_databricks_catalog_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None) -> _models.MirroredAzureDatabricksCatalogDefinitionResponse:
        """Returns the specified mirroredAzureDatabricksCatalog public definition.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalogDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalogDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_mirrored_azure_databricks_catalog_definition(workspace_id=workspace_id, mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None) -> _LROResultExtractor[_models.MirroredAzureDatabricksCatalogDefinitionResponse]:
        """Returns the specified mirroredAzureDatabricksCatalog public definition.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :return: An instance of LROPoller that returns MirroredAzureDatabricksCatalogDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.MirroredAzureDatabricksCatalogDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MirroredAzureDatabricksCatalogDefinitionResponse]()

        poller = super().begin_get_mirrored_azure_databricks_catalog_definition(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None, update_mirrored_azure_databricks_catalog_definition_request: None) -> None:
        """Overrides the definition for the specified mirroredAzureDatabricksCatalog.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

         [!NOTE]

        ..

           Item.Execute.All is required if you are updating AutoSync property.


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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :param update_mirrored_azure_databricks_catalog_definition_request: Update
         mirroredAzureDatabricksCatalog definition request payload. Required.
        :type update_mirrored_azure_databricks_catalog_definition_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.UpdatemirroredAzureDatabricksCatalogDefinitionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_mirrored_azure_databricks_catalog_definition(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            update_mirrored_azure_databricks_catalog_definition_request=update_mirrored_azure_databricks_catalog_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None, update_mirrored_azure_databricks_catalog_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified mirroredAzureDatabricksCatalog.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

         [!NOTE]

        ..

           Item.Execute.All is required if you are updating AutoSync property.


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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :param update_mirrored_azure_databricks_catalog_definition_request: Update
         mirroredAzureDatabricksCatalog definition request payload. Required.
        :type update_mirrored_azure_databricks_catalog_definition_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.UpdatemirroredAzureDatabricksCatalogDefinitionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_mirrored_azure_databricks_catalog_definition(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            update_mirrored_azure_databricks_catalog_definition_request=update_mirrored_azure_databricks_catalog_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None, update_mirrored_azure_databricks_catalog_definition_request: None) -> None:
        """Overrides the definition for the specified mirroredAzureDatabricksCatalog.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

         [!NOTE]

        ..

           Item.Execute.All is required if you are updating AutoSync property.


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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :param update_mirrored_azure_databricks_catalog_definition_request: Update
         mirroredAzureDatabricksCatalog definition request payload. Required.
        :type update_mirrored_azure_databricks_catalog_definition_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_mirrored_azure_databricks_catalog_definition(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            update_mirrored_azure_databricks_catalog_definition_request=update_mirrored_azure_databricks_catalog_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None, update_mirrored_azure_databricks_catalog_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified mirroredAzureDatabricksCatalog.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

         [!NOTE]

        ..

           Item.Execute.All is required if you are updating AutoSync property.


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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :param update_mirrored_azure_databricks_catalog_definition_request: Update
         mirroredAzureDatabricksCatalog definition request payload. Required.
        :type update_mirrored_azure_databricks_catalog_definition_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_mirrored_azure_databricks_catalog_definition(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            update_mirrored_azure_databricks_catalog_definition_request=update_mirrored_azure_databricks_catalog_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None, update_mirrored_azure_databricks_catalog_definition_request: None) -> None:
        """Overrides the definition for the specified mirroredAzureDatabricksCatalog.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

         [!NOTE]

        ..

           Item.Execute.All is required if you are updating AutoSync property.


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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :param update_mirrored_azure_databricks_catalog_definition_request: Update
         mirroredAzureDatabricksCatalog definition request payload. Is either a
         UpdatemirroredAzureDatabricksCatalogDefinitionRequest type or a IO[bytes] type. Required.
        :type update_mirrored_azure_databricks_catalog_definition_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.UpdatemirroredAzureDatabricksCatalogDefinitionRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_mirrored_azure_databricks_catalog_definition(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            update_mirrored_azure_databricks_catalog_definition_request=update_mirrored_azure_databricks_catalog_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_mirrored_azure_databricks_catalog_definition(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None, update_mirrored_azure_databricks_catalog_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified mirroredAzureDatabricksCatalog.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have *read and write* permissions for the mirrored azure databricks catalog.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

         [!NOTE]

        ..

           Item.Execute.All is required if you are updating AutoSync property.


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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :param update_mirrored_azure_databricks_catalog_definition_request: Update
         mirroredAzureDatabricksCatalog definition request payload. Is either a
         UpdatemirroredAzureDatabricksCatalogDefinitionRequest type or a IO[bytes] type. Required.
        :type update_mirrored_azure_databricks_catalog_definition_request:
         ~microsoft.fabric.api.mirroredazuredatabrickscatalog.models.UpdatemirroredAzureDatabricksCatalogDefinitionRequest
         or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_mirrored_azure_databricks_catalog_definition(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            update_mirrored_azure_databricks_catalog_definition_request=update_mirrored_azure_databricks_catalog_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    


class RefreshOperations(_operations.RefreshOperations):
    """RefreshOperations for Mirroredazuredatabrickscatalog."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def refresh_catalog_metadata(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None) -> None:
        """Refresh Databricks catalog metadata in mirroredAzureDatabricksCatalogs Item.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The API caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_refresh_catalog_metadata(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_refresh_catalog_metadata(self, workspace_id: None, mirrored_azure_databricks_catalog_id: None) -> LROPoller[None]:
        """Refresh Databricks catalog metadata in mirroredAzureDatabricksCatalogs Item.

        ..

           [!NOTE]
           Mirrored Azure Databricks Catalog item is currently in Preview (\ `learn more
        </fabric/fundamentals/preview>`_\ ).


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The API caller must have *contributor* or higher workspace role.

        Required Delegated Scopes
        -------------------------

         MirroredAzureDatabricksCatalog.ReadWrite.All or Item.ReadWrite.All

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
        :param mirrored_azure_databricks_catalog_id: The mirroredAzureDatabricksCatalog ID. Required.
        :type mirrored_azure_databricks_catalog_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_refresh_catalog_metadata(
            workspace_id=workspace_id,
            mirrored_azure_databricks_catalog_id=mirrored_azure_databricks_catalog_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
