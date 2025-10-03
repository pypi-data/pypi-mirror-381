from ....generated.notebook.operations import *
from ....generated.notebook import operations as _operations
from ....generated.notebook import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Notebook."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_notebook(self, workspace_id: None, create_notebook_request: None) -> _models.Notebook:
        """Creates a notebook in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Notebook definition
        </rest/api/fabric/articles/item-management/definitions/notebook-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a notebook the workspace must be on a supported Fabric capacity. For more
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
        :param create_notebook_request: Create item request payload. Required.
        :type create_notebook_request: ~microsoft.fabric.api.notebook.models.CreateNotebookRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Notebook
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.Notebook]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_notebook(workspace_id=workspace_id, create_notebook_request=create_notebook_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_notebook(self, workspace_id: None, create_notebook_request: None) -> _LROResultExtractor[_models.Notebook]:
        """Creates a notebook in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Notebook definition
        </rest/api/fabric/articles/item-management/definitions/notebook-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a notebook the workspace must be on a supported Fabric capacity. For more
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
        :param create_notebook_request: Create item request payload. Required.
        :type create_notebook_request: ~microsoft.fabric.api.notebook.models.CreateNotebookRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Notebook
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.Notebook]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Notebook]()

        poller = super().begin_create_notebook(
            workspace_id=workspace_id,
            create_notebook_request=create_notebook_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_notebook(self, workspace_id: None, create_notebook_request: None) -> _models.Notebook:
        """Creates a notebook in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Notebook definition
        </rest/api/fabric/articles/item-management/definitions/notebook-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a notebook the workspace must be on a supported Fabric capacity. For more
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
        :param create_notebook_request: Create item request payload. Required.
        :type create_notebook_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Notebook
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.Notebook]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_notebook(workspace_id=workspace_id, create_notebook_request=create_notebook_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_notebook(self, workspace_id: None, create_notebook_request: None) -> _LROResultExtractor[_models.Notebook]:
        """Creates a notebook in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Notebook definition
        </rest/api/fabric/articles/item-management/definitions/notebook-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a notebook the workspace must be on a supported Fabric capacity. For more
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
        :param create_notebook_request: Create item request payload. Required.
        :type create_notebook_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Notebook
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.Notebook]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Notebook]()

        poller = super().begin_create_notebook(
            workspace_id=workspace_id,
            create_notebook_request=create_notebook_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_notebook(self, workspace_id: None, create_notebook_request: None) -> _models.Notebook:
        """Creates a notebook in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Notebook definition
        </rest/api/fabric/articles/item-management/definitions/notebook-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a notebook the workspace must be on a supported Fabric capacity. For more
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
        :param create_notebook_request: Create item request payload. Is either a CreateNotebookRequest
         type or a IO[bytes] type. Required.
        :type create_notebook_request: ~microsoft.fabric.api.notebook.models.CreateNotebookRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Notebook
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.Notebook]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_notebook(workspace_id=workspace_id, create_notebook_request=create_notebook_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_notebook(self, workspace_id: None, create_notebook_request: None) -> _LROResultExtractor[_models.Notebook]:
        """Creates a notebook in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create notebook with definition, refer to `Notebook definition
        </rest/api/fabric/articles/item-management/definitions/notebook-definition>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a notebook the workspace must be on a supported Fabric capacity. For more
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
        :param create_notebook_request: Create item request payload. Is either a CreateNotebookRequest
         type or a IO[bytes] type. Required.
        :type create_notebook_request: ~microsoft.fabric.api.notebook.models.CreateNotebookRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Notebook
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.Notebook]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Notebook]()

        poller = super().begin_create_notebook(
            workspace_id=workspace_id,
            create_notebook_request=create_notebook_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_notebook_definition(self, workspace_id: None, notebook_id: None) -> _models.NotebookDefinitionResponse:
        """Returns the specified notebook public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a notebook's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a notebook with an encrypted sensitivity label.

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :keyword format: The format of the notebook public definition. Supported format: ``ipynb`` and
         ``fabricGitSource``. If no format is provided, ``fabricGitSource`` is used. Default value is
         None.
        :paramtype format: str
        :return: An instance of LROPoller that returns NotebookDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.NotebookDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_notebook_definition(workspace_id=workspace_id, notebook_id=notebook_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_notebook_definition(self, workspace_id: None, notebook_id: None) -> _LROResultExtractor[_models.NotebookDefinitionResponse]:
        """Returns the specified notebook public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a notebook's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a notebook with an encrypted sensitivity label.

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :keyword format: The format of the notebook public definition. Supported format: ``ipynb`` and
         ``fabricGitSource``. If no format is provided, ``fabricGitSource`` is used. Default value is
         None.
        :paramtype format: str
        :return: An instance of LROPoller that returns NotebookDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.notebook.models.NotebookDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.NotebookDefinitionResponse]()

        poller = super().begin_get_notebook_definition(
            workspace_id=workspace_id,
            notebook_id=notebook_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_notebook_definition(self, workspace_id: None, notebook_id: None, update_notebook_definition_request: None) -> None:
        """Overrides the definition for the specified notebook.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the notebook's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :param update_notebook_definition_request: Update notebook definition request payload.
         Required.
        :type update_notebook_definition_request:
         ~microsoft.fabric.api.notebook.models.UpdateNotebookDefinitionRequest
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

        
        poller = self.begin_update_notebook_definition(
            workspace_id=workspace_id,
            notebook_id=notebook_id,
            update_notebook_definition_request=update_notebook_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_notebook_definition(self, workspace_id: None, notebook_id: None, update_notebook_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified notebook.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the notebook's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :param update_notebook_definition_request: Update notebook definition request payload.
         Required.
        :type update_notebook_definition_request:
         ~microsoft.fabric.api.notebook.models.UpdateNotebookDefinitionRequest
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

        

        return super().begin_update_notebook_definition(
            workspace_id=workspace_id,
            notebook_id=notebook_id,
            update_notebook_definition_request=update_notebook_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_notebook_definition(self, workspace_id: None, notebook_id: None, update_notebook_definition_request: None) -> None:
        """Overrides the definition for the specified notebook.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the notebook's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :param update_notebook_definition_request: Update notebook definition request payload.
         Required.
        :type update_notebook_definition_request: IO[bytes]
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

        
        poller = self.begin_update_notebook_definition(
            workspace_id=workspace_id,
            notebook_id=notebook_id,
            update_notebook_definition_request=update_notebook_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_notebook_definition(self, workspace_id: None, notebook_id: None, update_notebook_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified notebook.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the notebook's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :param update_notebook_definition_request: Update notebook definition request payload.
         Required.
        :type update_notebook_definition_request: IO[bytes]
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

        

        return super().begin_update_notebook_definition(
            workspace_id=workspace_id,
            notebook_id=notebook_id,
            update_notebook_definition_request=update_notebook_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_notebook_definition(self, workspace_id: None, notebook_id: None, update_notebook_definition_request: None) -> None:
        """Overrides the definition for the specified notebook.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the notebook's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :param update_notebook_definition_request: Update notebook definition request payload. Is
         either a UpdateNotebookDefinitionRequest type or a IO[bytes] type. Required.
        :type update_notebook_definition_request:
         ~microsoft.fabric.api.notebook.models.UpdateNotebookDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_notebook_definition(
            workspace_id=workspace_id,
            notebook_id=notebook_id,
            update_notebook_definition_request=update_notebook_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_notebook_definition(self, workspace_id: None, notebook_id: None, update_notebook_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified notebook.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the notebook's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the notebook.

        Required Delegated Scopes
        -------------------------

         Notebook.ReadWrite.All or Item.ReadWrite.All

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
        :param notebook_id: The notebook ID. Required.
        :type notebook_id: str
        :param update_notebook_definition_request: Update notebook definition request payload. Is
         either a UpdateNotebookDefinitionRequest type or a IO[bytes] type. Required.
        :type update_notebook_definition_request:
         ~microsoft.fabric.api.notebook.models.UpdateNotebookDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_notebook_definition(
            workspace_id=workspace_id,
            notebook_id=notebook_id,
            update_notebook_definition_request=update_notebook_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
