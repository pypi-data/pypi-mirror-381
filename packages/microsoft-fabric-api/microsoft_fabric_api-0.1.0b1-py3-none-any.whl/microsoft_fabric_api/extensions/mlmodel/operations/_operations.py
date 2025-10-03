from ....generated.mlmodel.operations import *
from ....generated.mlmodel import operations as _operations
from ....generated.mlmodel import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Mlmodel."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_ml_model(self, workspace_id: None, create_ml_model_request: None) -> _models.MLModel:
        """Creates a machine learning model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create an machine learning model with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a machine learning model the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_ml_model_request: Create item request payload. Required.
        :type create_ml_model_request: ~microsoft.fabric.api.mlmodel.models.CreateMLModelRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MLModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.MLModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_ml_model(workspace_id=workspace_id, create_ml_model_request=create_ml_model_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_ml_model(self, workspace_id: None, create_ml_model_request: None) -> _LROResultExtractor[_models.MLModel]:
        """Creates a machine learning model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create an machine learning model with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a machine learning model the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_ml_model_request: Create item request payload. Required.
        :type create_ml_model_request: ~microsoft.fabric.api.mlmodel.models.CreateMLModelRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MLModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.MLModel]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MLModel]()

        poller = super().begin_create_ml_model(
            workspace_id=workspace_id,
            create_ml_model_request=create_ml_model_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_ml_model(self, workspace_id: None, create_ml_model_request: None) -> _models.MLModel:
        """Creates a machine learning model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create an machine learning model with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a machine learning model the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_ml_model_request: Create item request payload. Required.
        :type create_ml_model_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MLModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.MLModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_ml_model(workspace_id=workspace_id, create_ml_model_request=create_ml_model_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_ml_model(self, workspace_id: None, create_ml_model_request: None) -> _LROResultExtractor[_models.MLModel]:
        """Creates a machine learning model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create an machine learning model with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a machine learning model the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_ml_model_request: Create item request payload. Required.
        :type create_ml_model_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns MLModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.MLModel]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MLModel]()

        poller = super().begin_create_ml_model(
            workspace_id=workspace_id,
            create_ml_model_request=create_ml_model_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_ml_model(self, workspace_id: None, create_ml_model_request: None) -> _models.MLModel:
        """Creates a machine learning model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create an machine learning model with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a machine learning model the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_ml_model_request: Create item request payload. Is either a CreateMLModelRequest
         type or a IO[bytes] type. Required.
        :type create_ml_model_request: ~microsoft.fabric.api.mlmodel.models.CreateMLModelRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns MLModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.MLModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_ml_model(workspace_id=workspace_id, create_ml_model_request=create_ml_model_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_ml_model(self, workspace_id: None, create_ml_model_request: None) -> _LROResultExtractor[_models.MLModel]:
        """Creates a machine learning model in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API does not support create an machine learning model with definition.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a machine learning model the workspace must be on a supported Fabric capacity. For
        more information see: `Microsoft Fabric license types
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
             - No


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_ml_model_request: Create item request payload. Is either a CreateMLModelRequest
         type or a IO[bytes] type. Required.
        :type create_ml_model_request: ~microsoft.fabric.api.mlmodel.models.CreateMLModelRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns MLModel
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.MLModel]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.MLModel]()

        poller = super().begin_create_ml_model(
            workspace_id=workspace_id,
            create_ml_model_request=create_ml_model_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    


class EndpointOperations(_operations.EndpointOperations):
    """EndpointOperations for Mlmodel."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def deactivate_all_ml_model_endpoint_versions(self, workspace_id: None, model_id: None) -> None:
        """Deactivates the specified machine learning model and its version's endpoints.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_deactivate_all_ml_model_endpoint_versions(
            workspace_id=workspace_id,
            model_id=model_id)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_deactivate_all_ml_model_endpoint_versions(self, workspace_id: None, model_id: None) -> LROPoller[None]:
        """Deactivates the specified machine learning model and its version's endpoints.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_deactivate_all_ml_model_endpoint_versions(
            workspace_id=workspace_id,
            model_id=model_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def activate_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None) -> None:
        """Activates the specified model version endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_activate_ml_model_endpoint_version(
            workspace_id=workspace_id,
            model_id=model_id,
            name=name)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_activate_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None) -> LROPoller[None]:
        """Activates the specified model version endpoint.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_activate_ml_model_endpoint_version(
            workspace_id=workspace_id,
            model_id=model_id,
            name=name,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def deactivate_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None) -> None:
        """Deactivates the specified model version version.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_deactivate_ml_model_endpoint_version(
            workspace_id=workspace_id,
            model_id=model_id,
            name=name)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_deactivate_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None) -> LROPoller[None]:
        """Deactivates the specified model version version.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_deactivate_ml_model_endpoint_version(
            workspace_id=workspace_id,
            model_id=model_id,
            name=name,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def score_ml_model_endpoint(self, workspace_id: None, model_id: None, score_data_request: None) -> _models.ScoreDataResponse:
        """Scores input data using the default version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_score_ml_model_endpoint(workspace_id=workspace_id, model_id=model_id, score_data_request=score_data_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_score_ml_model_endpoint(self, workspace_id: None, model_id: None, score_data_request: None) -> _LROResultExtractor[_models.ScoreDataResponse]:
        """Scores input data using the default version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ScoreDataResponse]()

        poller = super().begin_score_ml_model_endpoint(
            workspace_id=workspace_id,
            model_id=model_id,
            score_data_request=score_data_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def score_ml_model_endpoint(self, workspace_id: None, model_id: None, score_data_request: None) -> _models.ScoreDataResponse:
        """Scores input data using the default version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_score_ml_model_endpoint(workspace_id=workspace_id, model_id=model_id, score_data_request=score_data_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_score_ml_model_endpoint(self, workspace_id: None, model_id: None, score_data_request: None) -> _LROResultExtractor[_models.ScoreDataResponse]:
        """Scores input data using the default version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ScoreDataResponse]()

        poller = super().begin_score_ml_model_endpoint(
            workspace_id=workspace_id,
            model_id=model_id,
            score_data_request=score_data_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def score_ml_model_endpoint(self, workspace_id: None, model_id: None, score_data_request: None) -> _models.ScoreDataResponse:
        """Scores input data using the default version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param score_data_request: The data to score with the model. Is either a ScoreDataRequest type
         or a IO[bytes] type. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest or IO[bytes]
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_score_ml_model_endpoint(workspace_id=workspace_id, model_id=model_id, score_data_request=score_data_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_score_ml_model_endpoint(self, workspace_id: None, model_id: None, score_data_request: None) -> _LROResultExtractor[_models.ScoreDataResponse]:
        """Scores input data using the default version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param score_data_request: The data to score with the model. Is either a ScoreDataRequest type
         or a IO[bytes] type. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest or IO[bytes]
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ScoreDataResponse]()

        poller = super().begin_score_ml_model_endpoint(
            workspace_id=workspace_id,
            model_id=model_id,
            score_data_request=score_data_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def score_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None, score_data_request: None) -> _models.ScoreDataResponse:
        """Scores input data for the specific version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_score_ml_model_endpoint_version(workspace_id=workspace_id, model_id=model_id, name=name, score_data_request=score_data_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_score_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None, score_data_request: None) -> _LROResultExtractor[_models.ScoreDataResponse]:
        """Scores input data for the specific version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ScoreDataResponse]()

        poller = super().begin_score_ml_model_endpoint_version(
            workspace_id=workspace_id,
            model_id=model_id,
            name=name,
            score_data_request=score_data_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def score_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None, score_data_request: None) -> _models.ScoreDataResponse:
        """Scores input data for the specific version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_score_ml_model_endpoint_version(workspace_id=workspace_id, model_id=model_id, name=name, score_data_request=score_data_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_score_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None, score_data_request: None) -> _LROResultExtractor[_models.ScoreDataResponse]:
        """Scores input data for the specific version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :param score_data_request: The data to score with the model. Required.
        :type score_data_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ScoreDataResponse]()

        poller = super().begin_score_ml_model_endpoint_version(
            workspace_id=workspace_id,
            model_id=model_id,
            name=name,
            score_data_request=score_data_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def score_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None, score_data_request: None) -> _models.ScoreDataResponse:
        """Scores input data for the specific version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :param score_data_request: The data to score with the model. Is either a ScoreDataRequest type
         or a IO[bytes] type. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest or IO[bytes]
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_score_ml_model_endpoint_version(workspace_id=workspace_id, model_id=model_id, name=name, score_data_request=score_data_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_score_ml_model_endpoint_version(self, workspace_id: None, model_id: None, name: None, score_data_request: None) -> _LROResultExtractor[_models.ScoreDataResponse]:
        """Scores input data for the specific version of the endpoint and returns results.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

         The caller must have write permission on the MLModel.

        Required Delegated Scopes
        -------------------------

         MLModel.ReadWrite.All or Item.ReadWrite.All

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
        :param model_id: The machine learning model ID. Required.
        :type model_id: str
        :param name: The MLModel version name. Required.
        :type name: str
        :param score_data_request: The data to score with the model. Is either a ScoreDataRequest type
         or a IO[bytes] type. Required.
        :type score_data_request: ~microsoft.fabric.api.mlmodel.models.ScoreDataRequest or IO[bytes]
        :return: An instance of LROPoller that returns ScoreDataResponse
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.mlmodel.models.ScoreDataResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ScoreDataResponse]()

        poller = super().begin_score_ml_model_endpoint_version(
            workspace_id=workspace_id,
            model_id=model_id,
            name=name,
            score_data_request=score_data_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    
