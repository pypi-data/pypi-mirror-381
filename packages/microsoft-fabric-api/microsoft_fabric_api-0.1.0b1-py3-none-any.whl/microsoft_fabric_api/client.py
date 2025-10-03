import re
from urllib.parse import urlparse
from azure.core.credentials import TokenCredential

from .extensions.admin import FabricAdminClient
from .extensions.apacheairflowjob import FabricApacheAirflowJobClient
from .extensions.copyjob import FabricCopyJobClient
from .extensions.core import FabricCoreClient
from .extensions.dashboard import FabricDashboardClient
from .extensions.dataflow import FabricDataflowClient
from .extensions.datamart import FabricDatamartClient
from .extensions.datapipeline import FabricDataPipelineClient
from .extensions.digitaltwinbuilder import FabricDigitalTwinBuilderClient
from .extensions.digitaltwinbuilderflow import FabricDigitalTwinBuilderFlowClient
from .extensions.environment import FabricEnvironmentClient
from .extensions.eventhouse import FabricEventhouseClient
from .extensions.eventstream import FabricEventstreamClient
from .extensions.graphqlapi import FabricGraphQLApiClient
from .extensions.kqldashboard import FabricKQLDashboardClient
from .extensions.kqldatabase import FabricKQLDatabaseClient
from .extensions.kqlqueryset import FabricKQLQuerysetClient
from .extensions.lakehouse import FabricLakehouseClient
from .extensions.mirroredazuredatabrickscatalog import FabricMirroredAzureDatabricksCatalogClient
from .extensions.mirroreddatabase import FabricMirroredDatabaseClient
from .extensions.mirroredwarehouse import FabricMirroredWarehouseClient
from .extensions.mlexperiment import FabricMLExperimentClient
from .extensions.mlmodel import FabricMLModelClient
from .extensions.mounteddatafactory import FabricMountedDataFactoryClient
from .extensions.notebook import FabricNotebookClient
from .extensions.paginatedreport import FabricPaginatedReportClient
from .extensions.reflex import FabricReflexClient
from .extensions.report import FabricReportClient
from .extensions.semanticmodel import FabricSemanticModelClient
from .extensions.spark import FabricSparkClient
from .extensions.sparkjobdefinition import FabricSparkJobDefinitionClient
from .extensions.sqldatabase import FabricSQLDatabaseClient
from .extensions.sqlendpoint import FabricSQLEndpointClient
from .extensions.variablelibrary import FabricVariableLibraryClient
from .extensions.warehouse import FabricWarehouseClient
from .extensions.warehousesnapshot import FabricWarehouseSnapshotClient


class FabricClient:

    def __init__(self, token_credential: TokenCredential, base_url: str = "https://api.fabric.microsoft.com/", **kwargs):
        """
        Initialize FabricClient with custom configurations.
        
        Args:
            token_credential: Azure credential for authentication
            base_url: Base URL for Fabric API (default: "https://api.fabric.microsoft.com/")
            **kwargs: Additional keyword arguments passed to underlying clients
                     (e.g., http_logging_policy, etc.)
        """
        assert token_credential is not None, "token_credential should not be None"
        self.ensure_valid_uri(base_url)

        self._admin_client = FabricAdminClient(credential=token_credential, base_url=base_url, **kwargs)
        self._apacheairflowjob_client = FabricApacheAirflowJobClient(credential=token_credential, base_url=base_url, **kwargs)
        self._copyjob_client = FabricCopyJobClient(credential=token_credential, base_url=base_url, **kwargs)
        self._core_client = FabricCoreClient(credential=token_credential, base_url=base_url, **kwargs)
        self._dashboard_client = FabricDashboardClient(credential=token_credential, base_url=base_url, **kwargs)
        self._dataflow_client = FabricDataflowClient(credential=token_credential, base_url=base_url, **kwargs)
        self._datamart_client = FabricDatamartClient(credential=token_credential, base_url=base_url, **kwargs)
        self._datapipeline_client = FabricDataPipelineClient(credential=token_credential, base_url=base_url, **kwargs)
        self._digitaltwinbuilder_client = FabricDigitalTwinBuilderClient(credential=token_credential, base_url=base_url, **kwargs)
        self._digitaltwinbuilderflow_client = FabricDigitalTwinBuilderFlowClient(credential=token_credential, base_url=base_url, **kwargs)
        self._environment_client = FabricEnvironmentClient(credential=token_credential, base_url=base_url, **kwargs)
        self._eventhouse_client = FabricEventhouseClient(credential=token_credential, base_url=base_url, **kwargs)
        self._eventstream_client = FabricEventstreamClient(credential=token_credential, base_url=base_url, **kwargs)
        self._graphqlapi_client = FabricGraphQLApiClient(credential=token_credential, base_url=base_url, **kwargs)
        self._kqldashboard_client = FabricKQLDashboardClient(credential=token_credential, base_url=base_url, **kwargs)
        self._kqldatabase_client = FabricKQLDatabaseClient(credential=token_credential, base_url=base_url, **kwargs)
        self._kqlqueryset_client = FabricKQLQuerysetClient(credential=token_credential, base_url=base_url, **kwargs)
        self._lakehouse_client = FabricLakehouseClient(credential=token_credential, base_url=base_url, **kwargs)
        self._mirroredazuredatabrickscatalog_client = FabricMirroredAzureDatabricksCatalogClient(credential=token_credential, base_url=base_url, **kwargs)
        self._mirroreddatabase_client = FabricMirroredDatabaseClient(credential=token_credential, base_url=base_url, **kwargs)
        self._mirroredwarehouse_client = FabricMirroredWarehouseClient(credential=token_credential, base_url=base_url, **kwargs)
        self._mlexperiment_client = FabricMLExperimentClient(credential=token_credential, base_url=base_url, **kwargs)
        self._mlmodel_client = FabricMLModelClient(credential=token_credential, base_url=base_url, **kwargs)
        self._mounteddatafactory_client = FabricMountedDataFactoryClient(credential=token_credential, base_url=base_url, **kwargs)
        self._notebook_client = FabricNotebookClient(credential=token_credential, base_url=base_url, **kwargs)
        self._paginatedreport_client = FabricPaginatedReportClient(credential=token_credential, base_url=base_url, **kwargs)
        self._reflex_client = FabricReflexClient(credential=token_credential, base_url=base_url, **kwargs)
        self._report_client = FabricReportClient(credential=token_credential, base_url=base_url, **kwargs)
        self._semanticmodel_client = FabricSemanticModelClient(credential=token_credential, base_url=base_url, **kwargs)
        self._spark_client = FabricSparkClient(credential=token_credential, base_url=base_url, **kwargs)
        self._sparkjobdefinition_client = FabricSparkJobDefinitionClient(credential=token_credential, base_url=base_url, **kwargs)
        self._sqldatabase_client = FabricSQLDatabaseClient(credential=token_credential, base_url=base_url, **kwargs)
        self._sqlendpoint_client = FabricSQLEndpointClient(credential=token_credential, base_url=base_url, **kwargs)
        self._variablelibrary_client = FabricVariableLibraryClient(credential=token_credential, base_url=base_url, **kwargs)
        self._warehouse_client = FabricWarehouseClient(credential=token_credential, base_url=base_url, **kwargs)
        self._warehousesnapshot_client = FabricWarehouseSnapshotClient(credential=token_credential, base_url=base_url, **kwargs)
        

    def ensure_valid_uri(self, uri: str) -> None:
        assert uri is not None, "uri should not be None"

        parsed_uri = urlparse(uri)
        assert parsed_uri.scheme == "https", "Invalid URL: URL should start with 'https://'"

        assert parsed_uri.path == "" or parsed_uri.path == "/" or parsed_uri.path == "/v1", "Invalid URL: URL should not contain any path except for /v1"
        assert parsed_uri.hostname.endswith("api.fabric.microsoft.com"), "Invalid URL: Host is not a valid Fabric host."

        assert parsed_uri.port is None, "Invalid URL: URL should not contain any port number"
        assert parsed_uri.query == "", "Invalid URL: URL should not contain any query parameters"
        assert parsed_uri.fragment == "", "Invalid URL: URL should not contain any fragment"

    @property
    def admin(self):
        return self._admin_client

    @property
    def apacheairflowjob(self):
        return self._apacheairflowjob_client

    @property
    def copyjob(self):
        return self._copyjob_client

    @property
    def core(self):
        return self._core_client

    @property
    def dashboard(self):
        return self._dashboard_client

    @property
    def dataflow(self):
        return self._dataflow_client

    @property
    def datamart(self):
        return self._datamart_client

    @property
    def datapipeline(self):
        return self._datapipeline_client

    @property
    def digitaltwinbuilder(self):
        return self._digitaltwinbuilder_client

    @property
    def digitaltwinbuilderflow(self):
        return self._digitaltwinbuilderflow_client

    @property
    def environment(self):
        return self._environment_client

    @property
    def eventhouse(self):
        return self._eventhouse_client

    @property
    def eventstream(self):
        return self._eventstream_client

    @property
    def graphqlapi(self):
        return self._graphqlapi_client

    @property
    def kqldashboard(self):
        return self._kqldashboard_client

    @property
    def kqldatabase(self):
        return self._kqldatabase_client

    @property
    def kqlqueryset(self):
        return self._kqlqueryset_client

    @property
    def lakehouse(self):
        return self._lakehouse_client

    @property
    def mirroredazuredatabrickscatalog(self):
        return self._mirroredazuredatabrickscatalog_client

    @property
    def mirroreddatabase(self):
        return self._mirroreddatabase_client

    @property
    def mirroredwarehouse(self):
        return self._mirroredwarehouse_client

    @property
    def mlexperiment(self):
        return self._mlexperiment_client

    @property
    def mlmodel(self):
        return self._mlmodel_client

    @property
    def mounteddatafactory(self):
        return self._mounteddatafactory_client

    @property
    def notebook(self):
        return self._notebook_client

    @property
    def paginatedreport(self):
        return self._paginatedreport_client

    @property
    def reflex(self):
        return self._reflex_client

    @property
    def report(self):
        return self._report_client

    @property
    def semanticmodel(self):
        return self._semanticmodel_client

    @property
    def spark(self):
        return self._spark_client

    @property
    def sparkjobdefinition(self):
        return self._sparkjobdefinition_client

    @property
    def sqldatabase(self):
        return self._sqldatabase_client

    @property
    def sqlendpoint(self):
        return self._sqlendpoint_client

    @property
    def variablelibrary(self):
        return self._variablelibrary_client

    @property
    def warehouse(self):
        return self._warehouse_client

    @property
    def warehousesnapshot(self):
        return self._warehousesnapshot_client

    