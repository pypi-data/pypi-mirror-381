from ....generated.apacheairflowjob.operations import *
from ....generated.apacheairflowjob import operations as _operations
from ....generated.apacheairflowjob import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Apacheairflowjob."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_apache_airflow_job(self, workspace_id: None, create_apache_airflow_job_request: None) -> _models.ApacheAirflowJob:
        """Creates an Apache Airflow job in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Apache Airflow job with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/public-facing-name>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an Apache Airflow job the workspace must be on a supported Fabric capacity. For
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
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_apache_airflow_job_request: Create item request payload. Required.
        :type create_apache_airflow_job_request:
         ~microsoft.fabric.api.apacheairflowjob.models.CreateApacheAirflowJobRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ApacheAirflowJob
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJob]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_apache_airflow_job(workspace_id=workspace_id, create_apache_airflow_job_request=create_apache_airflow_job_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_apache_airflow_job(self, workspace_id: None, create_apache_airflow_job_request: None) -> _LROResultExtractor[_models.ApacheAirflowJob]:
        """Creates an Apache Airflow job in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Apache Airflow job with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/public-facing-name>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an Apache Airflow job the workspace must be on a supported Fabric capacity. For
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
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_apache_airflow_job_request: Create item request payload. Required.
        :type create_apache_airflow_job_request:
         ~microsoft.fabric.api.apacheairflowjob.models.CreateApacheAirflowJobRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ApacheAirflowJob
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJob]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ApacheAirflowJob]()

        poller = super().begin_create_apache_airflow_job(
            workspace_id=workspace_id,
            create_apache_airflow_job_request=create_apache_airflow_job_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_apache_airflow_job(self, workspace_id: None, create_apache_airflow_job_request: None) -> _models.ApacheAirflowJob:
        """Creates an Apache Airflow job in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Apache Airflow job with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/public-facing-name>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an Apache Airflow job the workspace must be on a supported Fabric capacity. For
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
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_apache_airflow_job_request: Create item request payload. Required.
        :type create_apache_airflow_job_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ApacheAirflowJob
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJob]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_apache_airflow_job(workspace_id=workspace_id, create_apache_airflow_job_request=create_apache_airflow_job_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_apache_airflow_job(self, workspace_id: None, create_apache_airflow_job_request: None) -> _LROResultExtractor[_models.ApacheAirflowJob]:
        """Creates an Apache Airflow job in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Apache Airflow job with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/public-facing-name>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an Apache Airflow job the workspace must be on a supported Fabric capacity. For
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
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_apache_airflow_job_request: Create item request payload. Required.
        :type create_apache_airflow_job_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns ApacheAirflowJob
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJob]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ApacheAirflowJob]()

        poller = super().begin_create_apache_airflow_job(
            workspace_id=workspace_id,
            create_apache_airflow_job_request=create_apache_airflow_job_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_apache_airflow_job(self, workspace_id: None, create_apache_airflow_job_request: None) -> _models.ApacheAirflowJob:
        """Creates an Apache Airflow job in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Apache Airflow job with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/public-facing-name>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an Apache Airflow job the workspace must be on a supported Fabric capacity. For
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
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_apache_airflow_job_request: Create item request payload. Is either a
         CreateApacheAirflowJobRequest type or a IO[bytes] type. Required.
        :type create_apache_airflow_job_request:
         ~microsoft.fabric.api.apacheairflowjob.models.CreateApacheAirflowJobRequest or IO[bytes]
        :return: An instance of LROPoller that returns ApacheAirflowJob
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJob]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_apache_airflow_job(workspace_id=workspace_id, create_apache_airflow_job_request=create_apache_airflow_job_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_apache_airflow_job(self, workspace_id: None, create_apache_airflow_job_request: None) -> _LROResultExtractor[_models.ApacheAirflowJob]:
        """Creates an Apache Airflow job in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         To create Apache Airflow job with a public definition, refer to `
        </rest/api/fabric/articles/item-management/definitions/public-facing-name>`_ article.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create an Apache Airflow job the workspace must be on a supported Fabric capacity. For
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
             - Yes


        Interface
        ---------.

        :param workspace_id: The workspace ID. Required.
        :type workspace_id: str
        :param create_apache_airflow_job_request: Create item request payload. Is either a
         CreateApacheAirflowJobRequest type or a IO[bytes] type. Required.
        :type create_apache_airflow_job_request:
         ~microsoft.fabric.api.apacheairflowjob.models.CreateApacheAirflowJobRequest or IO[bytes]
        :return: An instance of LROPoller that returns ApacheAirflowJob
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJob]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ApacheAirflowJob]()

        poller = super().begin_create_apache_airflow_job(
            workspace_id=workspace_id,
            create_apache_airflow_job_request=create_apache_airflow_job_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None) -> _models.ApacheAirflowJobDefinitionResponse:
        """Returns the specified Apache Airflow job public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a 's public definition, the sensitivity label is not a part of the definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :keyword format: The format of the public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns ApacheAirflowJobDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJobDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_apache_airflow_job_definition(workspace_id=workspace_id, apache_airflow_job_id=apache_airflow_job_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None) -> _LROResultExtractor[_models.ApacheAirflowJobDefinitionResponse]:
        """Returns the specified Apache Airflow job public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a 's public definition, the sensitivity label is not a part of the definition.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :keyword format: The format of the public definition. Default value is None.
        :paramtype format: str
        :return: An instance of LROPoller that returns ApacheAirflowJobDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.apacheairflowjob.models.ApacheAirflowJobDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ApacheAirflowJobDefinitionResponse]()

        poller = super().begin_get_apache_airflow_job_definition(
            workspace_id=workspace_id,
            apache_airflow_job_id=apache_airflow_job_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None, update_apache_airflow_job_definition_request: None) -> None:
        """Overrides the definition for the specified Apache Airflow job.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the 's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :param update_apache_airflow_job_definition_request: Update Apache Airflow job definition
         request payload. Required.
        :type update_apache_airflow_job_definition_request:
         ~microsoft.fabric.api.apacheairflowjob.models.UpdateApacheAirflowJobDefinitionRequest
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

        
        poller = self.begin_update_apache_airflow_job_definition(
            workspace_id=workspace_id,
            apache_airflow_job_id=apache_airflow_job_id,
            update_apache_airflow_job_definition_request=update_apache_airflow_job_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None, update_apache_airflow_job_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Apache Airflow job.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the 's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :param update_apache_airflow_job_definition_request: Update Apache Airflow job definition
         request payload. Required.
        :type update_apache_airflow_job_definition_request:
         ~microsoft.fabric.api.apacheairflowjob.models.UpdateApacheAirflowJobDefinitionRequest
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

        

        return super().begin_update_apache_airflow_job_definition(
            workspace_id=workspace_id,
            apache_airflow_job_id=apache_airflow_job_id,
            update_apache_airflow_job_definition_request=update_apache_airflow_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None, update_apache_airflow_job_definition_request: None) -> None:
        """Overrides the definition for the specified Apache Airflow job.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the 's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :param update_apache_airflow_job_definition_request: Update Apache Airflow job definition
         request payload. Required.
        :type update_apache_airflow_job_definition_request: IO[bytes]
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

        
        poller = self.begin_update_apache_airflow_job_definition(
            workspace_id=workspace_id,
            apache_airflow_job_id=apache_airflow_job_id,
            update_apache_airflow_job_definition_request=update_apache_airflow_job_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None, update_apache_airflow_job_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Apache Airflow job.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the 's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :param update_apache_airflow_job_definition_request: Update Apache Airflow job definition
         request payload. Required.
        :type update_apache_airflow_job_definition_request: IO[bytes]
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

        

        return super().begin_update_apache_airflow_job_definition(
            workspace_id=workspace_id,
            apache_airflow_job_id=apache_airflow_job_id,
            update_apache_airflow_job_definition_request=update_apache_airflow_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None, update_apache_airflow_job_definition_request: None) -> None:
        """Overrides the definition for the specified Apache Airflow job.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the 's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :param update_apache_airflow_job_definition_request: Update Apache Airflow job definition
         request payload. Is either a UpdateApacheAirflowJobDefinitionRequest type or a IO[bytes] type.
         Required.
        :type update_apache_airflow_job_definition_request:
         ~microsoft.fabric.api.apacheairflowjob.models.UpdateApacheAirflowJobDefinitionRequest or
         IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_apache_airflow_job_definition(
            workspace_id=workspace_id,
            apache_airflow_job_id=apache_airflow_job_id,
            update_apache_airflow_job_definition_request=update_apache_airflow_job_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_apache_airflow_job_definition(self, workspace_id: None, apache_airflow_job_id: None, update_apache_airflow_job_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified Apache Airflow job.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the 's definition, does not affect its sensitivity label.

        Permissions
        -----------

         The caller must have *read and write* permissions for the apache airflow job.

        Required Delegated Scopes
        -------------------------

         ApacheAirflowJob.ReadWrite.All or Item.ReadWrite.All

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
        :param apache_airflow_job_id: The Apache Airflow job ID. Required.
        :type apache_airflow_job_id: str
        :param update_apache_airflow_job_definition_request: Update Apache Airflow job definition
         request payload. Is either a UpdateApacheAirflowJobDefinitionRequest type or a IO[bytes] type.
         Required.
        :type update_apache_airflow_job_definition_request:
         ~microsoft.fabric.api.apacheairflowjob.models.UpdateApacheAirflowJobDefinitionRequest or
         IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_apache_airflow_job_definition(
            workspace_id=workspace_id,
            apache_airflow_job_id=apache_airflow_job_id,
            update_apache_airflow_job_definition_request=update_apache_airflow_job_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
