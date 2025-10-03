from typing import Optional, TypeVar, Generic
from azure.core.polling.base_polling import PollingMethod

ResultType = TypeVar('ResultType', covariant=True)

class _LROResultExtractor(Generic[ResultType]):
    """Helper class to extract the result from a long running operation."""
    
    def __init__(self):
        self._result: Optional[ResultType] = None

    def __call__(self, method: PollingMethod) -> None:
        """Extract the result from the long running operation."""
        if (method.resource().additional_properties and method.resource().additional_properties["status"] == "Succeeded"):
            self._result : ResultType = method._parse_resource(method.request_status(method._pipeline_response.http_response.url + '/result'))
        else:
            self._result = method.resource()

    @property
    def result(self) -> ResultType:
        """Get the result of the long running operation."""
        return self._result