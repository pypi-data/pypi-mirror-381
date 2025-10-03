from ....generated.environment.operations import *
from ....generated.environment import operations as _operations
from ....generated.environment import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Environment."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_environment(self, workspace_id: None, create_environment_request: None) -> _models.Environment:
        """Creates an environment in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an environment, the workspace must be on a supported Fabric capacity.

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
        :param create_environment_request: Create item request payload. Required.
        :type create_environment_request:
         ~microsoft.fabric.api.environment.models.CreateEnvironmentRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Environment
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.Environment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_environment(workspace_id=workspace_id, create_environment_request=create_environment_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_environment(self, workspace_id: None, create_environment_request: None) -> _LROResultExtractor[_models.Environment]:
        """Creates an environment in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an environment, the workspace must be on a supported Fabric capacity.

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
        :param create_environment_request: Create item request payload. Required.
        :type create_environment_request:
         ~microsoft.fabric.api.environment.models.CreateEnvironmentRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Environment
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.Environment]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Environment]()

        poller = super().begin_create_environment(
            workspace_id=workspace_id,
            create_environment_request=create_environment_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_environment(self, workspace_id: None, create_environment_request: None) -> _models.Environment:
        """Creates an environment in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an environment, the workspace must be on a supported Fabric capacity.

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
        :param create_environment_request: Create item request payload. Required.
        :type create_environment_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Environment
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.Environment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_environment(workspace_id=workspace_id, create_environment_request=create_environment_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_environment(self, workspace_id: None, create_environment_request: None) -> _LROResultExtractor[_models.Environment]:
        """Creates an environment in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an environment, the workspace must be on a supported Fabric capacity.

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
        :param create_environment_request: Create item request payload. Required.
        :type create_environment_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Environment
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.Environment]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Environment]()

        poller = super().begin_create_environment(
            workspace_id=workspace_id,
            create_environment_request=create_environment_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_environment(self, workspace_id: None, create_environment_request: None) -> _models.Environment:
        """Creates an environment in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an environment, the workspace must be on a supported Fabric capacity.

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
        :param create_environment_request: Create item request payload. Is either a
         CreateEnvironmentRequest type or a IO[bytes] type. Required.
        :type create_environment_request:
         ~microsoft.fabric.api.environment.models.CreateEnvironmentRequest or IO[bytes]
        :return: An instance of LROPoller that returns Environment
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.Environment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_environment(workspace_id=workspace_id, create_environment_request=create_environment_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_environment(self, workspace_id: None, create_environment_request: None) -> _LROResultExtractor[_models.Environment]:
        """Creates an environment in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an environment, the workspace must be on a supported Fabric capacity.

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
        :param create_environment_request: Create item request payload. Is either a
         CreateEnvironmentRequest type or a IO[bytes] type. Required.
        :type create_environment_request:
         ~microsoft.fabric.api.environment.models.CreateEnvironmentRequest or IO[bytes]
        :return: An instance of LROPoller that returns Environment
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.Environment]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Environment]()

        poller = super().begin_create_environment(
            workspace_id=workspace_id,
            create_environment_request=create_environment_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_environment_definition(self, workspace_id: None, environment_id: None) -> _models.EnvironmentDefinitionResponse:
        """Returns the specified environment public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a environment's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a environment with an encrypted sensitivity label.

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :keyword format: The format of the environment public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns EnvironmentDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.EnvironmentDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_environment_definition(workspace_id=workspace_id, environment_id=environment_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_environment_definition(self, workspace_id: None, environment_id: None) -> _LROResultExtractor[_models.EnvironmentDefinitionResponse]:
        """Returns the specified environment public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a environment's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a environment with an encrypted sensitivity label.

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :keyword format: The format of the environment public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns EnvironmentDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.EnvironmentDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.EnvironmentDefinitionResponse]()

        poller = super().begin_get_environment_definition(
            workspace_id=workspace_id,
            environment_id=environment_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_environment_definition(self, workspace_id: None, environment_id: None, update_environment_definition_request: None) -> None:
        """Overrides the definition for the specified environment.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the environment's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :param update_environment_definition_request: Update environment definition request payload.
         Required.
        :type update_environment_definition_request:
         ~microsoft.fabric.api.environment.models.UpdateEnvironmentDefinitionRequest
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

        
        poller = self.begin_update_environment_definition(
            workspace_id=workspace_id,
            environment_id=environment_id,
            update_environment_definition_request=update_environment_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_environment_definition(self, workspace_id: None, environment_id: None, update_environment_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified environment.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the environment's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :param update_environment_definition_request: Update environment definition request payload.
         Required.
        :type update_environment_definition_request:
         ~microsoft.fabric.api.environment.models.UpdateEnvironmentDefinitionRequest
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

        

        return super().begin_update_environment_definition(
            workspace_id=workspace_id,
            environment_id=environment_id,
            update_environment_definition_request=update_environment_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_environment_definition(self, workspace_id: None, environment_id: None, update_environment_definition_request: None) -> None:
        """Overrides the definition for the specified environment.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the environment's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :param update_environment_definition_request: Update environment definition request payload.
         Required.
        :type update_environment_definition_request: IO[bytes]
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

        
        poller = self.begin_update_environment_definition(
            workspace_id=workspace_id,
            environment_id=environment_id,
            update_environment_definition_request=update_environment_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_environment_definition(self, workspace_id: None, environment_id: None, update_environment_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified environment.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the environment's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :param update_environment_definition_request: Update environment definition request payload.
         Required.
        :type update_environment_definition_request: IO[bytes]
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

        

        return super().begin_update_environment_definition(
            workspace_id=workspace_id,
            environment_id=environment_id,
            update_environment_definition_request=update_environment_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_environment_definition(self, workspace_id: None, environment_id: None, update_environment_definition_request: None) -> None:
        """Overrides the definition for the specified environment.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the environment's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :param update_environment_definition_request: Update environment definition request payload. Is
         either a UpdateEnvironmentDefinitionRequest type or a IO[bytes] type. Required.
        :type update_environment_definition_request:
         ~microsoft.fabric.api.environment.models.UpdateEnvironmentDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_environment_definition(
            workspace_id=workspace_id,
            environment_id=environment_id,
            update_environment_definition_request=update_environment_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_environment_definition(self, workspace_id: None, environment_id: None, update_environment_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified environment.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the environment's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the environment.

        Required Delegated Scopes
        -------------------------

         Environment.ReadWrite.All or Item.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :param update_environment_definition_request: Update environment definition request payload. Is
         either a UpdateEnvironmentDefinitionRequest type or a IO[bytes] type. Required.
        :type update_environment_definition_request:
         ~microsoft.fabric.api.environment.models.UpdateEnvironmentDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_environment_definition(
            workspace_id=workspace_id,
            environment_id=environment_id,
            update_environment_definition_request=update_environment_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def publish_environment(self, workspace_id: None, environment_id: None) -> _models.EnvironmentProperties:
        """Trigger an environment publish operation.

        ..

           [!NOTE]
           This API is a release version of a preview version due to be deprecated on March 1, 2026.
           **When calling this API - callers must set the query parameter ``preview`` to the value
        ``false``\ **


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission for the environment item.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All or Environment.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :keyword preview: This parameter specifies which version of the API to use. Set to ``false`` to
         use the release version. Required.
        :paramtype preview: bool
        :return: An instance of LROPoller that returns EnvironmentProperties
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.EnvironmentProperties]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_publish_environment(workspace_id=workspace_id, environment_id=environment_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_publish_environment(self, workspace_id: None, environment_id: None) -> _LROResultExtractor[_models.EnvironmentProperties]:
        """Trigger an environment publish operation.

        ..

           [!NOTE]
           This API is a release version of a preview version due to be deprecated on March 1, 2026.
           **When calling this API - callers must set the query parameter ``preview`` to the value
        ``false``\ **


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        Write permission for the environment item.

        Required Delegated Scopes
        -------------------------

        Item.ReadWrite.All or Environment.ReadWrite.All

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
        :param environment_id: The environment ID. Required.
        :type environment_id: str
        :keyword preview: This parameter specifies which version of the API to use. Set to ``false`` to
         use the release version. Required.
        :paramtype preview: bool
        :return: An instance of LROPoller that returns EnvironmentProperties
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.environment.models.EnvironmentProperties]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.EnvironmentProperties]()

        poller = super().begin_publish_environment(
            workspace_id=workspace_id,
            environment_id=environment_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    
