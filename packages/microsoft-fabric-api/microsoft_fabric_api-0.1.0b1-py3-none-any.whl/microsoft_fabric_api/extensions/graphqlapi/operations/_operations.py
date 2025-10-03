from ....generated.graphqlapi.operations import *
from ....generated.graphqlapi import operations as _operations
from ....generated.graphqlapi import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Graphqlapi."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_graph_ql_api(self, workspace_id: None, create_graph_ql_api_request: None) -> _models.GraphQLApi:
        """Creates a API for GraphQL item in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To create GraphQLApi item with a public definition, refer to `GraphQLApi definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a GraphQLApi the workspace must be on a supported Fabric capacity. For more
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
        :param create_graph_ql_api_request: Create item request payload. Required.
        :type create_graph_ql_api_request:
         ~microsoft.fabric.api.graphqlapi.models.CreateGraphQLApiRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns GraphQLApi
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApi]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_graph_ql_api(workspace_id=workspace_id, create_graph_ql_api_request=create_graph_ql_api_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_graph_ql_api(self, workspace_id: None, create_graph_ql_api_request: None) -> _LROResultExtractor[_models.GraphQLApi]:
        """Creates a API for GraphQL item in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To create GraphQLApi item with a public definition, refer to `GraphQLApi definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a GraphQLApi the workspace must be on a supported Fabric capacity. For more
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
        :param create_graph_ql_api_request: Create item request payload. Required.
        :type create_graph_ql_api_request:
         ~microsoft.fabric.api.graphqlapi.models.CreateGraphQLApiRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns GraphQLApi
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApi]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.GraphQLApi]()

        poller = super().begin_create_graph_ql_api(
            workspace_id=workspace_id,
            create_graph_ql_api_request=create_graph_ql_api_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_graph_ql_api(self, workspace_id: None, create_graph_ql_api_request: None) -> _models.GraphQLApi:
        """Creates a API for GraphQL item in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To create GraphQLApi item with a public definition, refer to `GraphQLApi definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a GraphQLApi the workspace must be on a supported Fabric capacity. For more
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
        :param create_graph_ql_api_request: Create item request payload. Required.
        :type create_graph_ql_api_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns GraphQLApi
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApi]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_graph_ql_api(workspace_id=workspace_id, create_graph_ql_api_request=create_graph_ql_api_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_graph_ql_api(self, workspace_id: None, create_graph_ql_api_request: None) -> _LROResultExtractor[_models.GraphQLApi]:
        """Creates a API for GraphQL item in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To create GraphQLApi item with a public definition, refer to `GraphQLApi definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a GraphQLApi the workspace must be on a supported Fabric capacity. For more
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
        :param create_graph_ql_api_request: Create item request payload. Required.
        :type create_graph_ql_api_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns GraphQLApi
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApi]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.GraphQLApi]()

        poller = super().begin_create_graph_ql_api(
            workspace_id=workspace_id,
            create_graph_ql_api_request=create_graph_ql_api_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_graph_ql_api(self, workspace_id: None, create_graph_ql_api_request: None) -> _models.GraphQLApi:
        """Creates a API for GraphQL item in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To create GraphQLApi item with a public definition, refer to `GraphQLApi definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a GraphQLApi the workspace must be on a supported Fabric capacity. For more
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
        :param create_graph_ql_api_request: Create item request payload. Is either a
         CreateGraphQLApiRequest type or a IO[bytes] type. Required.
        :type create_graph_ql_api_request:
         ~microsoft.fabric.api.graphqlapi.models.CreateGraphQLApiRequest or IO[bytes]
        :return: An instance of LROPoller that returns GraphQLApi
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApi]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_graph_ql_api(workspace_id=workspace_id, create_graph_ql_api_request=create_graph_ql_api_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_graph_ql_api(self, workspace_id: None, create_graph_ql_api_request: None) -> _LROResultExtractor[_models.GraphQLApi]:
        """Creates a API for GraphQL item in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        To create GraphQLApi item with a public definition, refer to `GraphQLApi definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a GraphQLApi the workspace must be on a supported Fabric capacity. For more
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
        :param create_graph_ql_api_request: Create item request payload. Is either a
         CreateGraphQLApiRequest type or a IO[bytes] type. Required.
        :type create_graph_ql_api_request:
         ~microsoft.fabric.api.graphqlapi.models.CreateGraphQLApiRequest or IO[bytes]
        :return: An instance of LROPoller that returns GraphQLApi
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApi]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.GraphQLApi]()

        poller = super().begin_create_graph_ql_api(
            workspace_id=workspace_id,
            create_graph_ql_api_request=create_graph_ql_api_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None) -> _models.GraphQLApiDefinitionResponse:
        """Returns the specified GraphQLApi public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a `GraphQLApi public definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_\ , the
        sensitivity label is not a part of the definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi .

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a  with an encrypted sensitivity label.

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :keyword format: The format of the GraphQLApi public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns GraphQLApiDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApiDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_graph_ql_api_definition(workspace_id=workspace_id, graph_ql_api_id=graph_ql_api_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None) -> _LROResultExtractor[_models.GraphQLApiDefinitionResponse]:
        """Returns the specified GraphQLApi public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a `GraphQLApi public definition
        </rest/api/fabric/articles/item-management/definitions/graphql-api-definition>`_\ , the
        sensitivity label is not a part of the definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi .

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a  with an encrypted sensitivity label.

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :keyword format: The format of the GraphQLApi public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns GraphQLApiDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.graphqlapi.models.GraphQLApiDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.GraphQLApiDefinitionResponse]()

        poller = super().begin_get_graph_ql_api_definition(
            workspace_id=workspace_id,
            graph_ql_api_id=graph_ql_api_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None, update_graph_ql_api_definition_request: None) -> None:
        """Overrides the definition for the specified API for GraphQL.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the GraphQLApi's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :param update_graph_ql_api_definition_request: Update GraphQLApi definition request payload.
         Required.
        :type update_graph_ql_api_definition_request:
         ~microsoft.fabric.api.graphqlapi.models.UpdateGraphQLApiDefinitionRequest
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

        
        poller = self.begin_update_graph_ql_api_definition(
            workspace_id=workspace_id,
            graph_ql_api_id=graph_ql_api_id,
            update_graph_ql_api_definition_request=update_graph_ql_api_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None, update_graph_ql_api_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified API for GraphQL.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the GraphQLApi's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :param update_graph_ql_api_definition_request: Update GraphQLApi definition request payload.
         Required.
        :type update_graph_ql_api_definition_request:
         ~microsoft.fabric.api.graphqlapi.models.UpdateGraphQLApiDefinitionRequest
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

        

        return super().begin_update_graph_ql_api_definition(
            workspace_id=workspace_id,
            graph_ql_api_id=graph_ql_api_id,
            update_graph_ql_api_definition_request=update_graph_ql_api_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None, update_graph_ql_api_definition_request: None) -> None:
        """Overrides the definition for the specified API for GraphQL.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the GraphQLApi's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :param update_graph_ql_api_definition_request: Update GraphQLApi definition request payload.
         Required.
        :type update_graph_ql_api_definition_request: IO[bytes]
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

        
        poller = self.begin_update_graph_ql_api_definition(
            workspace_id=workspace_id,
            graph_ql_api_id=graph_ql_api_id,
            update_graph_ql_api_definition_request=update_graph_ql_api_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None, update_graph_ql_api_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified API for GraphQL.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the GraphQLApi's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :param update_graph_ql_api_definition_request: Update GraphQLApi definition request payload.
         Required.
        :type update_graph_ql_api_definition_request: IO[bytes]
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

        

        return super().begin_update_graph_ql_api_definition(
            workspace_id=workspace_id,
            graph_ql_api_id=graph_ql_api_id,
            update_graph_ql_api_definition_request=update_graph_ql_api_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None, update_graph_ql_api_definition_request: None) -> None:
        """Overrides the definition for the specified API for GraphQL.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the GraphQLApi's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :param update_graph_ql_api_definition_request: Update GraphQLApi definition request payload. Is
         either a UpdateGraphQLApiDefinitionRequest type or a IO[bytes] type. Required.
        :type update_graph_ql_api_definition_request:
         ~microsoft.fabric.api.graphqlapi.models.UpdateGraphQLApiDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_graph_ql_api_definition(
            workspace_id=workspace_id,
            graph_ql_api_id=graph_ql_api_id,
            update_graph_ql_api_definition_request=update_graph_ql_api_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_graph_ql_api_definition(self, workspace_id: None, graph_ql_api_id: None, update_graph_ql_api_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified API for GraphQL.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the GraphQLApi's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the GraphQLApi.

        Required Delegated Scopes
        -------------------------

         GraphQLApi.ReadWrite.All or Item.ReadWrite.All

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
        :param graph_ql_api_id: The GraphQLApi ID. Required.
        :type graph_ql_api_id: str
        :param update_graph_ql_api_definition_request: Update GraphQLApi definition request payload. Is
         either a UpdateGraphQLApiDefinitionRequest type or a IO[bytes] type. Required.
        :type update_graph_ql_api_definition_request:
         ~microsoft.fabric.api.graphqlapi.models.UpdateGraphQLApiDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_graph_ql_api_definition(
            workspace_id=workspace_id,
            graph_ql_api_id=graph_ql_api_id,
            update_graph_ql_api_definition_request=update_graph_ql_api_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
