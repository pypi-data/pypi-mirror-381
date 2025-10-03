from ....generated.admin.operations import *
from ....generated.admin import operations as _operations
from ....generated.admin import models as _models
from azure.core.polling.base_polling import LROBasePolling, OperationResourcePolling, StatusCheckPolling
from azure.core.polling import LROPoller
from ....fabric_api_utils import _LROResultExtractor
from typing import IO, Union, overload, Optional
import time



class DomainsOperations(_operations.DomainsOperations):
    """DomainsOperations for Admin."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def assign_domain_workspaces_by_capacities(self, domain_id: None, assign_domain_workspaces_by_capacities_request: None) -> None:
        """Assign all workspaces that reside on the specified capacities to the specified domain.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_capacities_request: The request payload for assigning
         workspaces to the domain by capacity. Required.
        :type assign_domain_workspaces_by_capacities_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByCapacitiesRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_assign_domain_workspaces_by_capacities(
            domain_id=domain_id,
            assign_domain_workspaces_by_capacities_request=assign_domain_workspaces_by_capacities_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_assign_domain_workspaces_by_capacities(self, domain_id: None, assign_domain_workspaces_by_capacities_request: None) -> LROPoller[None]:
        """Assign all workspaces that reside on the specified capacities to the specified domain.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_capacities_request: The request payload for assigning
         workspaces to the domain by capacity. Required.
        :type assign_domain_workspaces_by_capacities_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByCapacitiesRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_assign_domain_workspaces_by_capacities(
            domain_id=domain_id,
            assign_domain_workspaces_by_capacities_request=assign_domain_workspaces_by_capacities_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def assign_domain_workspaces_by_capacities(self, domain_id: None, assign_domain_workspaces_by_capacities_request: None) -> None:
        """Assign all workspaces that reside on the specified capacities to the specified domain.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_capacities_request: The request payload for assigning
         workspaces to the domain by capacity. Required.
        :type assign_domain_workspaces_by_capacities_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_assign_domain_workspaces_by_capacities(
            domain_id=domain_id,
            assign_domain_workspaces_by_capacities_request=assign_domain_workspaces_by_capacities_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_assign_domain_workspaces_by_capacities(self, domain_id: None, assign_domain_workspaces_by_capacities_request: None) -> LROPoller[None]:
        """Assign all workspaces that reside on the specified capacities to the specified domain.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_capacities_request: The request payload for assigning
         workspaces to the domain by capacity. Required.
        :type assign_domain_workspaces_by_capacities_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_assign_domain_workspaces_by_capacities(
            domain_id=domain_id,
            assign_domain_workspaces_by_capacities_request=assign_domain_workspaces_by_capacities_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def assign_domain_workspaces_by_capacities(self, domain_id: None, assign_domain_workspaces_by_capacities_request: None) -> None:
        """Assign all workspaces that reside on the specified capacities to the specified domain.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_capacities_request: The request payload for assigning
         workspaces to the domain by capacity. Is either a AssignDomainWorkspacesByCapacitiesRequest
         type or a IO[bytes] type. Required.
        :type assign_domain_workspaces_by_capacities_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByCapacitiesRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_assign_domain_workspaces_by_capacities(
            domain_id=domain_id,
            assign_domain_workspaces_by_capacities_request=assign_domain_workspaces_by_capacities_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_assign_domain_workspaces_by_capacities(self, domain_id: None, assign_domain_workspaces_by_capacities_request: None) -> LROPoller[None]:
        """Assign all workspaces that reside on the specified capacities to the specified domain.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_capacities_request: The request payload for assigning
         workspaces to the domain by capacity. Is either a AssignDomainWorkspacesByCapacitiesRequest
         type or a IO[bytes] type. Required.
        :type assign_domain_workspaces_by_capacities_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByCapacitiesRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_assign_domain_workspaces_by_capacities(
            domain_id=domain_id,
            assign_domain_workspaces_by_capacities_request=assign_domain_workspaces_by_capacities_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def assign_domain_workspaces_by_principals(self, domain_id: None, assign_domain_workspaces_by_principals_request: None) -> None:
        """Assign workspaces to the specified domain, when one of the specified principals has admin
        permission in the workspace.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_principals_request: The request payload for assigning
         workspaces to the domain by principal. Required.
        :type assign_domain_workspaces_by_principals_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByPrincipalsRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_assign_domain_workspaces_by_principals(
            domain_id=domain_id,
            assign_domain_workspaces_by_principals_request=assign_domain_workspaces_by_principals_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_assign_domain_workspaces_by_principals(self, domain_id: None, assign_domain_workspaces_by_principals_request: None) -> LROPoller[None]:
        """Assign workspaces to the specified domain, when one of the specified principals has admin
        permission in the workspace.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_principals_request: The request payload for assigning
         workspaces to the domain by principal. Required.
        :type assign_domain_workspaces_by_principals_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByPrincipalsRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_assign_domain_workspaces_by_principals(
            domain_id=domain_id,
            assign_domain_workspaces_by_principals_request=assign_domain_workspaces_by_principals_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def assign_domain_workspaces_by_principals(self, domain_id: None, assign_domain_workspaces_by_principals_request: None) -> None:
        """Assign workspaces to the specified domain, when one of the specified principals has admin
        permission in the workspace.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_principals_request: The request payload for assigning
         workspaces to the domain by principal. Required.
        :type assign_domain_workspaces_by_principals_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_assign_domain_workspaces_by_principals(
            domain_id=domain_id,
            assign_domain_workspaces_by_principals_request=assign_domain_workspaces_by_principals_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_assign_domain_workspaces_by_principals(self, domain_id: None, assign_domain_workspaces_by_principals_request: None) -> LROPoller[None]:
        """Assign workspaces to the specified domain, when one of the specified principals has admin
        permission in the workspace.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_principals_request: The request payload for assigning
         workspaces to the domain by principal. Required.
        :type assign_domain_workspaces_by_principals_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_assign_domain_workspaces_by_principals(
            domain_id=domain_id,
            assign_domain_workspaces_by_principals_request=assign_domain_workspaces_by_principals_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def assign_domain_workspaces_by_principals(self, domain_id: None, assign_domain_workspaces_by_principals_request: None) -> None:
        """Assign workspaces to the specified domain, when one of the specified principals has admin
        permission in the workspace.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_principals_request: The request payload for assigning
         workspaces to the domain by principal. Is either a AssignDomainWorkspacesByPrincipalsRequest
         type or a IO[bytes] type. Required.
        :type assign_domain_workspaces_by_principals_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByPrincipalsRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_assign_domain_workspaces_by_principals(
            domain_id=domain_id,
            assign_domain_workspaces_by_principals_request=assign_domain_workspaces_by_principals_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_assign_domain_workspaces_by_principals(self, domain_id: None, assign_domain_workspaces_by_principals_request: None) -> LROPoller[None]:
        """Assign workspaces to the specified domain, when one of the specified principals has admin
        permission in the workspace.

        Preexisting domain assignments will be overridden unless bulk reassignment is blocked by domain
        management tenant settings.

        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All.

        Limitations
        -----------

        Maximum 10 requests per one minute per principal.

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

        :param domain_id: The domain ID. Required.
        :type domain_id: str
        :param assign_domain_workspaces_by_principals_request: The request payload for assigning
         workspaces to the domain by principal. Is either a AssignDomainWorkspacesByPrincipalsRequest
         type or a IO[bytes] type. Required.
        :type assign_domain_workspaces_by_principals_request:
         ~microsoft.fabric.api.admin.models.AssignDomainWorkspacesByPrincipalsRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_assign_domain_workspaces_by_principals(
            domain_id=domain_id,
            assign_domain_workspaces_by_principals_request=assign_domain_workspaces_by_principals_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    


class SharingLinksOperations(_operations.SharingLinksOperations):
    """SharingLinksOperations for Admin."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

    
    def remove_all_sharing_links(self, remove_all_sharing_links_request: None) -> None:
        """Deletes all organization sharing links for all Fabric items in the tenant. This action cannot
        be undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Only Power BI Reports are supported.

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

        :param remove_all_sharing_links_request: Type of sharing links to be removed. Required.
        :type remove_all_sharing_links_request:
         ~microsoft.fabric.api.admin.models.RemoveAllSharingLinksRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_remove_all_sharing_links(
            remove_all_sharing_links_request=remove_all_sharing_links_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_remove_all_sharing_links(self, remove_all_sharing_links_request: None) -> LROPoller[None]:
        """Deletes all organization sharing links for all Fabric items in the tenant. This action cannot
        be undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Only Power BI Reports are supported.

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

        :param remove_all_sharing_links_request: Type of sharing links to be removed. Required.
        :type remove_all_sharing_links_request:
         ~microsoft.fabric.api.admin.models.RemoveAllSharingLinksRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_remove_all_sharing_links(
            remove_all_sharing_links_request=remove_all_sharing_links_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def remove_all_sharing_links(self, remove_all_sharing_links_request: None) -> None:
        """Deletes all organization sharing links for all Fabric items in the tenant. This action cannot
        be undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Only Power BI Reports are supported.

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

        :param remove_all_sharing_links_request: Type of sharing links to be removed. Required.
        :type remove_all_sharing_links_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_remove_all_sharing_links(
            remove_all_sharing_links_request=remove_all_sharing_links_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_remove_all_sharing_links(self, remove_all_sharing_links_request: None) -> LROPoller[None]:
        """Deletes all organization sharing links for all Fabric items in the tenant. This action cannot
        be undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Only Power BI Reports are supported.

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

        :param remove_all_sharing_links_request: Type of sharing links to be removed. Required.
        :type remove_all_sharing_links_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_remove_all_sharing_links(
            remove_all_sharing_links_request=remove_all_sharing_links_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def remove_all_sharing_links(self, remove_all_sharing_links_request: None) -> None:
        """Deletes all organization sharing links for all Fabric items in the tenant. This action cannot
        be undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Only Power BI Reports are supported.

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

        :param remove_all_sharing_links_request: Type of sharing links to be removed. Is either a
         RemoveAllSharingLinksRequest type or a IO[bytes] type. Required.
        :type remove_all_sharing_links_request:
         ~microsoft.fabric.api.admin.models.RemoveAllSharingLinksRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        poller = self.begin_remove_all_sharing_links(
            remove_all_sharing_links_request=remove_all_sharing_links_request)
        
        while not poller.done():
            time.sleep(5)

        
    
    
    def begin_remove_all_sharing_links(self, remove_all_sharing_links_request: None) -> LROPoller[None]:
        """Deletes all organization sharing links for all Fabric items in the tenant. This action cannot
        be undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Only Power BI Reports are supported.

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

        :param remove_all_sharing_links_request: Type of sharing links to be removed. Is either a
         RemoveAllSharingLinksRequest type or a IO[bytes] type. Required.
        :type remove_all_sharing_links_request:
         ~microsoft.fabric.api.admin.models.RemoveAllSharingLinksRequest or IO[bytes]
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        return super().begin_remove_all_sharing_links(
            remove_all_sharing_links_request=remove_all_sharing_links_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )
        
    

    
    def bulk_remove_sharing_links(self, bulk_remove_sharing_links_request: None) -> _models.BulkRemoveSharingLinksResponse:
        """Deletes all organization sharing links for the specified Fabric items. This action cannot be
        undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Each request can delete organization sharing links for up to 500 Fabric items.
        * Only Power BI Reports are supported.

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

        :param bulk_remove_sharing_links_request: A list of items. Required.
        :type bulk_remove_sharing_links_request:
         ~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkRemoveSharingLinksResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_bulk_remove_sharing_links(bulk_remove_sharing_links_request=bulk_remove_sharing_links_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_bulk_remove_sharing_links(self, bulk_remove_sharing_links_request: None) -> _LROResultExtractor[_models.BulkRemoveSharingLinksResponse]:
        """Deletes all organization sharing links for the specified Fabric items. This action cannot be
        undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Each request can delete organization sharing links for up to 500 Fabric items.
        * Only Power BI Reports are supported.

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

        :param bulk_remove_sharing_links_request: A list of items. Required.
        :type bulk_remove_sharing_links_request:
         ~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkRemoveSharingLinksResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.BulkRemoveSharingLinksResponse]()

        poller = super().begin_bulk_remove_sharing_links(
            bulk_remove_sharing_links_request=bulk_remove_sharing_links_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def bulk_remove_sharing_links(self, bulk_remove_sharing_links_request: None) -> _models.BulkRemoveSharingLinksResponse:
        """Deletes all organization sharing links for the specified Fabric items. This action cannot be
        undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Each request can delete organization sharing links for up to 500 Fabric items.
        * Only Power BI Reports are supported.

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

        :param bulk_remove_sharing_links_request: A list of items. Required.
        :type bulk_remove_sharing_links_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkRemoveSharingLinksResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_bulk_remove_sharing_links(bulk_remove_sharing_links_request=bulk_remove_sharing_links_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_bulk_remove_sharing_links(self, bulk_remove_sharing_links_request: None) -> _LROResultExtractor[_models.BulkRemoveSharingLinksResponse]:
        """Deletes all organization sharing links for the specified Fabric items. This action cannot be
        undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Each request can delete organization sharing links for up to 500 Fabric items.
        * Only Power BI Reports are supported.

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

        :param bulk_remove_sharing_links_request: A list of items. Required.
        :type bulk_remove_sharing_links_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns BulkRemoveSharingLinksResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.BulkRemoveSharingLinksResponse]()

        poller = super().begin_bulk_remove_sharing_links(
            bulk_remove_sharing_links_request=bulk_remove_sharing_links_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    

    
    def bulk_remove_sharing_links(self, bulk_remove_sharing_links_request: None) -> _models.BulkRemoveSharingLinksResponse:
        """Deletes all organization sharing links for the specified Fabric items. This action cannot be
        undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Each request can delete organization sharing links for up to 500 Fabric items.
        * Only Power BI Reports are supported.

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

        :param bulk_remove_sharing_links_request: A list of items. Is either a
         BulkRemoveSharingLinksRequest type or a IO[bytes] type. Required.
        :type bulk_remove_sharing_links_request:
         ~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksRequest or IO[bytes]
        :return: An instance of LROPoller that returns BulkRemoveSharingLinksResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        
        extractor = self.begin_bulk_remove_sharing_links(bulk_remove_sharing_links_request=bulk_remove_sharing_links_request)

        while extractor.result is None:
            time.sleep(5)

        return extractor.result
        
    
    
    def begin_bulk_remove_sharing_links(self, bulk_remove_sharing_links_request: None) -> _LROResultExtractor[_models.BulkRemoveSharingLinksResponse]:
        """Deletes all organization sharing links for the specified Fabric items. This action cannot be
        undone.

        ..

           [!NOTE]
           This API is part of a Preview release and is provided for evaluation and development
        purposes only. It may change based on feedback and is not recommended for production use.


        This API supports `long running operations (LRO)
        </rest/api/fabric/articles/long-running-operation>`_.

        Use `LinksSharedToWholeOrganization
        <https://learn.microsoft.com/en-us/rest/api/power-bi/admin>`_ PowerBI Admin REST API to get
        Power BI Reports shared via organizational sharing links.

        Permissions
        -----------

        The caller must be a Fabric administrator.

        Required Delegated Scopes
        -------------------------

        Tenant.ReadWrite.All

        Limitations
        -----------


        * Maximum 10 requests per minute.
        * Each request can delete organization sharing links for up to 500 Fabric items.
        * Only Power BI Reports are supported.

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

        :param bulk_remove_sharing_links_request: A list of items. Is either a
         BulkRemoveSharingLinksRequest type or a IO[bytes] type. Required.
        :type bulk_remove_sharing_links_request:
         ~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksRequest or IO[bytes]
        :return: An instance of LROPoller that returns BulkRemoveSharingLinksResponse
        :rtype:
         ~azure.core.polling.LROPoller[~microsoft.fabric.api.admin.models.BulkRemoveSharingLinksResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
         asynchronously."""

        

        extractor = _LROResultExtractor[_models.BulkRemoveSharingLinksResponse]()

        poller = super().begin_bulk_remove_sharing_links(
            bulk_remove_sharing_links_request=bulk_remove_sharing_links_request,
            polling=LROBasePolling(lro_algorithms=[OperationResourcePolling(operation_location_header="location"), StatusCheckPolling()]),
        )

        poller.add_done_callback(extractor)

        return extractor
        
    
