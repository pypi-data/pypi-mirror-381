from ....generated.report.operations import *
from ....generated.report import operations as _operations
from ....generated.report import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class ItemsOperations(_operations.ItemsOperations):
    """ItemsOperations for Report."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def create_report(self, workspace_id: None, create_report_request: None) -> _models.Report:
        """Creates a report in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/report-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a report item, the user must have the appropriate license. For more information
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
        :param create_report_request: Create item request payload. Required.
        :type create_report_request: ~microsoft.fabric.api.report.models.CreateReportRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Report
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.Report]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_report(workspace_id=workspace_id, create_report_request=create_report_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_report(self, workspace_id: None, create_report_request: None) -> _LROResultExtractor[_models.Report]:
        """Creates a report in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/report-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a report item, the user must have the appropriate license. For more information
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
        :param create_report_request: Create item request payload. Required.
        :type create_report_request: ~microsoft.fabric.api.report.models.CreateReportRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Report
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.Report]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Report]()

        poller = super().begin_create_report(
            workspace_id=workspace_id,
            create_report_request=create_report_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_report(self, workspace_id: None, create_report_request: None) -> _models.Report:
        """Creates a report in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/report-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a report item, the user must have the appropriate license. For more information
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
        :param create_report_request: Create item request payload. Required.
        :type create_report_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Report
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.Report]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_report(workspace_id=workspace_id, create_report_request=create_report_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_report(self, workspace_id: None, create_report_request: None) -> _LROResultExtractor[_models.Report]:
        """Creates a report in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/report-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a report item, the user must have the appropriate license. For more information
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
        :param create_report_request: Create item request payload. Required.
        :type create_report_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns Report
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.Report]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Report]()

        poller = super().begin_create_report(
            workspace_id=workspace_id,
            create_report_request=create_report_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def create_report(self, workspace_id: None, create_report_request: None) -> _models.Report:
        """Creates a report in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/report-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a report item, the user must have the appropriate license. For more information
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
        :param create_report_request: Create item request payload. Is either a CreateReportRequest type
         or a IO[bytes] type. Required.
        :type create_report_request: ~microsoft.fabric.api.report.models.CreateReportRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Report
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.Report]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_create_report(workspace_id=workspace_id, create_report_request=create_report_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_create_report(self, workspace_id: None, create_report_request: None) -> _LROResultExtractor[_models.Report]:
        """Creates a report in the specified workspace.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

         This API requires a `definition
        </rest/api/fabric/articles/item-management/definitions/report-definition>`_.

        Permissions
        -----------

         The caller must have a *contributor* workspace role.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------


        * To create a report item, the user must have the appropriate license. For more information
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
        :param create_report_request: Create item request payload. Is either a CreateReportRequest type
         or a IO[bytes] type. Required.
        :type create_report_request: ~microsoft.fabric.api.report.models.CreateReportRequest or
         IO[bytes]
        :return: An instance of LROPoller that returns Report
        :rtype: ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.Report]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.Report]()

        poller = super().begin_create_report(
            workspace_id=workspace_id,
            create_report_request=create_report_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def get_report_definition(self, workspace_id: None, report_id: None) -> _models.ReportDefinitionResponse:
        """Returns the specified report public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a report's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a report with an encrypted sensitivity label.

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :return: An instance of LROPoller that returns ReportDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.ReportDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_get_report_definition(workspace_id=workspace_id, report_id=report_id)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_get_report_definition(self, workspace_id: None, report_id: None) -> _LROResultExtractor[_models.ReportDefinitionResponse]:
        """Returns the specified report public definition.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        When you get a report's public definition, the sensitivity label is not a part of the
        definition.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

        Limitations
        -----------

         This API is blocked for a report with an encrypted sensitivity label.

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :return: An instance of LROPoller that returns ReportDefinitionResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.report.models.ReportDefinitionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.ReportDefinitionResponse]()

        poller = super().begin_get_report_definition(
            workspace_id=workspace_id,
            report_id=report_id,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def update_report_definition(self, workspace_id: None, report_id: None, update_report_definition_request: None) -> None:
        """Overrides the definition for the specified report.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the report's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :param update_report_definition_request: Update report definition request payload. Required.
        :type update_report_definition_request:
         ~microsoft.fabric.api.report.models.UpdateReportDefinitionRequest
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

        
        poller = self.begin_update_report_definition(
            workspace_id=workspace_id,
            report_id=report_id,
            update_report_definition_request=update_report_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_report_definition(self, workspace_id: None, report_id: None, update_report_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified report.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the report's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :param update_report_definition_request: Update report definition request payload. Required.
        :type update_report_definition_request:
         ~microsoft.fabric.api.report.models.UpdateReportDefinitionRequest
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

        

        return super().begin_update_report_definition(
            workspace_id=workspace_id,
            report_id=report_id,
            update_report_definition_request=update_report_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_report_definition(self, workspace_id: None, report_id: None, update_report_definition_request: None) -> None:
        """Overrides the definition for the specified report.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the report's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :param update_report_definition_request: Update report definition request payload. Required.
        :type update_report_definition_request: IO[bytes]
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

        
        poller = self.begin_update_report_definition(
            workspace_id=workspace_id,
            report_id=report_id,
            update_report_definition_request=update_report_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_report_definition(self, workspace_id: None, report_id: None, update_report_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified report.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the report's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :param update_report_definition_request: Update report definition request payload. Required.
        :type update_report_definition_request: IO[bytes]
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

        

        return super().begin_update_report_definition(
            workspace_id=workspace_id,
            report_id=report_id,
            update_report_definition_request=update_report_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def update_report_definition(self, workspace_id: None, report_id: None, update_report_definition_request: None) -> None:
        """Overrides the definition for the specified report.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the report's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :param update_report_definition_request: Update report definition request payload. Is either a
         UpdateReportDefinitionRequest type or a IO[bytes] type. Required.
        :type update_report_definition_request:
         ~microsoft.fabric.api.report.models.UpdateReportDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_update_report_definition(
            workspace_id=workspace_id,
            report_id=report_id,
            update_report_definition_request=update_report_definition_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_update_report_definition(self, workspace_id: None, report_id: None, update_report_definition_request: None) -> LROPoller[None]:
        """Overrides the definition for the specified report.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Updating the report's definition, does not affect its sensitivity label.

        Permissions
        -----------

        The caller must have *read and write* permissions for the report.

        Required Delegated Scopes
        -------------------------

         Report.ReadWrite.All or Item.ReadWrite.All

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
        :param report_id: The report ID. Required.
        :type report_id: str
        :param update_report_definition_request: Update report definition request payload. Is either a
         UpdateReportDefinitionRequest type or a IO[bytes] type. Required.
        :type update_report_definition_request:
         ~microsoft.fabric.api.report.models.UpdateReportDefinitionRequest or IO[bytes]
        :keyword update_metadata: When set to true and the .platform file is provided as part of the
         definition, the item's metadata is updated using the metadata in the .platform file. Default
         value is None.
        :paramtype update_metadata: bool
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_update_report_definition(
            workspace_id=workspace_id,
            report_id=report_id,
            update_report_definition_request=update_report_definition_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    
