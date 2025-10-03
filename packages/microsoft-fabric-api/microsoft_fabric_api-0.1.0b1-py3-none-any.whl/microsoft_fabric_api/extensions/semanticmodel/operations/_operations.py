from ....generated.semanticmodel.operations import *
from ....generated.semanticmodel import operations as _operations
from ....generated.semanticmodel import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Semanticmodel."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_semantic_model(self, workspace_id: None, create_semantic_model_request: None) -> _models.SemanticModel:
        """Creates a semantic model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/semantic-model-definition>`_.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a semantic model, the user must have the appropriate license. For more information
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
        :param create_semantic_model_request: Create item request payload. Required.
        :type create_semantic_model_request:
         ~microsoft.fabric.api.semanticmodel.models.CreateSemanticModelRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SemanticModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_semantic_model(workspace_id=workspace_id, create_semantic_model_request=create_semantic_model_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_semantic_model(self, workspace_id: None, create_semantic_model_request: None) -> _LROResultExtractor[_models.SemanticModel]:
        """Creates a semantic model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/semantic-model-definition>`_.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a semantic model, the user must have the appropriate license. For more information
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
        :param create_semantic_model_request: Create item request payload. Required.
        :type create_semantic_model_request:
         ~microsoft.fabric.api.semanticmodel.models.CreateSemanticModelRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SemanticModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModel]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SemanticModel]()

        poller = super().begin_create_semantic_model(
            workspace_id=workspace_id,
            create_semantic_model_request=create_semantic_model_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_semantic_model(self, workspace_id: None, create_semantic_model_request: None) -> _models.SemanticModel:
        """Creates a semantic model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/semantic-model-definition>`_.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a semantic model, the user must have the appropriate license. For more information
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
        :param create_semantic_model_request: Create item request payload. Required.
        :type create_semantic_model_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SemanticModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_semantic_model(workspace_id=workspace_id, create_semantic_model_request=create_semantic_model_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_semantic_model(self, workspace_id: None, create_semantic_model_request: None) -> _LROResultExtractor[_models.SemanticModel]:
        """Creates a semantic model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/semantic-model-definition>`_.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a semantic model, the user must have the appropriate license. For more information
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
        :param create_semantic_model_request: Create item request payload. Required.
        :type create_semantic_model_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns SemanticModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModel]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SemanticModel]()

        poller = super().begin_create_semantic_model(
            workspace_id=workspace_id,
            create_semantic_model_request=create_semantic_model_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_semantic_model(self, workspace_id: None, create_semantic_model_request: None) -> _models.SemanticModel:
        """Creates a semantic model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/semantic-model-definition>`_.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a semantic model, the user must have the appropriate license. For more information
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
        :param create_semantic_model_request: Create item request payload. Is either a
         CreateSemanticModelRequest type or a IO[bytes] type. Required.
        :type create_semantic_model_request:
         ~microsoft.fabric.api.semanticmodel.models.CreateSemanticModelRequest or IO[bytes]
        :return: An instance of LROPoller that returns SemanticModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_semantic_model(workspace_id=workspace_id, create_semantic_model_request=create_semantic_model_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_semantic_model(self, workspace_id: None, create_semantic_model_request: None) -> _LROResultExtractor[_models.SemanticModel]:
        """Creates a semantic model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/semantic-model-definition>`_.

        Permissions
        -----------

        The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a semantic model, the user must have the appropriate license. For more information
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
        :param create_semantic_model_request: Create item request payload. Is either a
         CreateSemanticModelRequest type or a IO[bytes] type. Required.
        :type create_semantic_model_request:
         ~microsoft.fabric.api.semanticmodel.models.CreateSemanticModelRequest or IO[bytes]
        :return: An instance of LROPoller that returns SemanticModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModel]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SemanticModel]()

        poller = super().begin_create_semantic_model(
            workspace_id=workspace_id,
            create_semantic_model_request=create_semantic_model_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_semantic_model_definition(self, workspace_id: None, semantic_model_id: None) -> _models.SemanticModelDefinitionResponse:
        """Returns the specified semantic model public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a semantic model's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a semantic model with an encrypted sensitivity label.

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :keyword format: The format of the semantic model definition.

          The following formats are allowed (case sensitive)


         *

           *
             TMDL

           *

             * TMSL

           If not specified, the default is 'TMDL'. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns SemanticModelDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModelDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_semantic_model_definition(workspace_id=workspace_id, semantic_model_id=semantic_model_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_semantic_model_definition(self, workspace_id: None, semantic_model_id: None) -> _LROResultExtractor[_models.SemanticModelDefinitionResponse]:
        """Returns the specified semantic model public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a semantic model's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a semantic model with an encrypted sensitivity label.

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :keyword format: The format of the semantic model definition.

          The following formats are allowed (case sensitive)


         *

           *
             TMDL

           *

             * TMSL

           If not specified, the default is 'TMDL'. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns SemanticModelDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.semanticmodel.models.SemanticModelDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.SemanticModelDefinitionResponse]()

        poller = super().begin_get_semantic_model_definition(
            workspace_id=workspace_id,
            semantic_model_id=semantic_model_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_semantic_model_definition(self, workspace_id: None, semantic_model_id: None, update_semantic_model_definition_request: None) -> None:
        """Overrides the definition for the specified semantic model.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the semantic model's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :param update_semantic_model_definition_request: Update semantic model definition request
         payload. Required.
        :type update_semantic_model_definition_request:
         ~microsoft.fabric.api.semanticmodel.models.UpdateSemanticModelDefinitionRequest
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

        
        poller = self.begin_update_semantic_model_definition(
            workspace_id=workspace_id,
            semantic_model_id=semantic_model_id,
            update_semantic_model_definition_request=update_semantic_model_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_semantic_model_definition(self, workspace_id: None, semantic_model_id: None, update_semantic_model_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified semantic model.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the semantic model's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :param update_semantic_model_definition_request: Update semantic model definition request
         payload. Required.
        :type update_semantic_model_definition_request:
         ~microsoft.fabric.api.semanticmodel.models.UpdateSemanticModelDefinitionRequest
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

        

        return super().begin_update_semantic_model_definition(
            workspace_id=workspace_id,
            semantic_model_id=semantic_model_id,
            update_semantic_model_definition_request=update_semantic_model_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_semantic_model_definition(self, workspace_id: None, semantic_model_id: None, update_semantic_model_definition_request: None) -> None:
        """Overrides the definition for the specified semantic model.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the semantic model's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :param update_semantic_model_definition_request: Update semantic model definition request
         payload. Required.
        :type update_semantic_model_definition_request: IO[bytes]
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

        
        poller = self.begin_update_semantic_model_definition(
            workspace_id=workspace_id,
            semantic_model_id=semantic_model_id,
            update_semantic_model_definition_request=update_semantic_model_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_semantic_model_definition(self, workspace_id: None, semantic_model_id: None, update_semantic_model_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified semantic model.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the semantic model's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :param update_semantic_model_definition_request: Update semantic model definition request
         payload. Required.
        :type update_semantic_model_definition_request: IO[bytes]
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

        

        return super().begin_update_semantic_model_definition(
            workspace_id=workspace_id,
            semantic_model_id=semantic_model_id,
            update_semantic_model_definition_request=update_semantic_model_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_semantic_model_definition(self, workspace_id: None, semantic_model_id: None, update_semantic_model_definition_request: None) -> None:
        """Overrides the definition for the specified semantic model.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the semantic model's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :param update_semantic_model_definition_request: Update semantic model definition request
         payload. Is either a UpdateSemanticModelDefinitionRequest type or a IO[bytes] type. Required.
        :type update_semantic_model_definition_request:
         ~microsoft.fabric.api.semanticmodel.models.UpdateSemanticModelDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_semantic_model_definition(
            workspace_id=workspace_id,
            semantic_model_id=semantic_model_id,
            update_semantic_model_definition_request=update_semantic_model_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_semantic_model_definition(self, workspace_id: None, semantic_model_id: None, update_semantic_model_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified semantic model.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the semantic model's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the semantic model.

        Required Delegated Scopes
        -------------------------

         SemanticModel.ReadWrite.All or Item.ReadWrite.All

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
        :param semantic_model_id: The semantic model ID. Required.
        :type semantic_model_id: str
        :param update_semantic_model_definition_request: Update semantic model definition request
         payload. Is either a UpdateSemanticModelDefinitionRequest type or a IO[bytes] type. Required.
        :type update_semantic_model_definition_request:
         ~microsoft.fabric.api.semanticmodel.models.UpdateSemanticModelDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_semantic_model_definition(
            workspace_id=workspace_id,
            semantic_model_id=semantic_model_id,
            update_semantic_model_definition_request=update_semantic_model_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
