from ...generated import admin
from typing import Any, TYPE_CHECKING

from .operations import DomainsOperations, SharingLinksOperations


if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class FabricAdminClient(admin.FabricAdminClient):
    """FabricAdminClient.

    :ivar items: ItemsOperations operations
    :vartype items: microsoft.fabric.api.admin.operations.ItemsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword endpoint: Service URL. Default value is "https://api.fabric.microsoft.com/v1".
    :paramtype endpoint: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self, credential: "TokenCredential", base_url: str = "https://api.fabric.microsoft.com", **kwargs: Any
    ) -> None:
        super().__init__(credential=credential, endpoint=base_url + "v1/admin", **kwargs)
        
        self.domains = DomainsOperations(self._client, self._config, self._serialize, self._deserialize)  # type: ignore
        
        self.sharinglinks = SharingLinksOperations(self._client, self._config, self._serialize, self._deserialize)  # type: ignore
        