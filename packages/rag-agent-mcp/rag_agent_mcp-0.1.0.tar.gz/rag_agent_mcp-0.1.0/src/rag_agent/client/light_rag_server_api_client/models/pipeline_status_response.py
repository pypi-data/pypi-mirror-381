from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_status_response_update_status_type_0 import PipelineStatusResponseUpdateStatusType0


T = TypeVar("T", bound="PipelineStatusResponse")


@_attrs_define
class PipelineStatusResponse:
    """Response model for pipeline status

    Attributes:
        autoscanned: Whether auto-scan has started
        busy: Whether the pipeline is currently busy
        job_name: Current job name (e.g., indexing files/indexing texts)
        job_start: Job start time as ISO format string (optional)
        docs: Total number of documents to be indexed
        batchs: Number of batches for processing documents
        cur_batch: Current processing batch
        request_pending: Flag for pending request for processing
        latest_message: Latest message from pipeline processing
        history_messages: List of history messages
        update_status: Status of update flags for all namespaces

        Attributes:
            autoscanned (Union[Unset, bool]):  Default: False.
            busy (Union[Unset, bool]):  Default: False.
            job_name (Union[Unset, str]):  Default: 'Default Job'.
            job_start (Union[None, Unset, str]):
            docs (Union[Unset, int]):  Default: 0.
            batchs (Union[Unset, int]):  Default: 0.
            cur_batch (Union[Unset, int]):  Default: 0.
            request_pending (Union[Unset, bool]):  Default: False.
            latest_message (Union[Unset, str]):  Default: ''.
            history_messages (Union[None, Unset, list[str]]):
            update_status (Union['PipelineStatusResponseUpdateStatusType0', None, Unset]):
    """

    autoscanned: Union[Unset, bool] = False
    busy: Union[Unset, bool] = False
    job_name: Union[Unset, str] = "Default Job"
    job_start: Union[None, Unset, str] = UNSET
    docs: Union[Unset, int] = 0
    batchs: Union[Unset, int] = 0
    cur_batch: Union[Unset, int] = 0
    request_pending: Union[Unset, bool] = False
    latest_message: Union[Unset, str] = ""
    history_messages: Union[None, Unset, list[str]] = UNSET
    update_status: Union["PipelineStatusResponseUpdateStatusType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pipeline_status_response_update_status_type_0 import PipelineStatusResponseUpdateStatusType0

        autoscanned = self.autoscanned

        busy = self.busy

        job_name = self.job_name

        job_start: Union[None, Unset, str]
        if isinstance(self.job_start, Unset):
            job_start = UNSET
        else:
            job_start = self.job_start

        docs = self.docs

        batchs = self.batchs

        cur_batch = self.cur_batch

        request_pending = self.request_pending

        latest_message = self.latest_message

        history_messages: Union[None, Unset, list[str]]
        if isinstance(self.history_messages, Unset):
            history_messages = UNSET
        elif isinstance(self.history_messages, list):
            history_messages = self.history_messages

        else:
            history_messages = self.history_messages

        update_status: Union[None, Unset, dict[str, Any]]
        if isinstance(self.update_status, Unset):
            update_status = UNSET
        elif isinstance(self.update_status, PipelineStatusResponseUpdateStatusType0):
            update_status = self.update_status.to_dict()
        else:
            update_status = self.update_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if autoscanned is not UNSET:
            field_dict["autoscanned"] = autoscanned
        if busy is not UNSET:
            field_dict["busy"] = busy
        if job_name is not UNSET:
            field_dict["job_name"] = job_name
        if job_start is not UNSET:
            field_dict["job_start"] = job_start
        if docs is not UNSET:
            field_dict["docs"] = docs
        if batchs is not UNSET:
            field_dict["batchs"] = batchs
        if cur_batch is not UNSET:
            field_dict["cur_batch"] = cur_batch
        if request_pending is not UNSET:
            field_dict["request_pending"] = request_pending
        if latest_message is not UNSET:
            field_dict["latest_message"] = latest_message
        if history_messages is not UNSET:
            field_dict["history_messages"] = history_messages
        if update_status is not UNSET:
            field_dict["update_status"] = update_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_status_response_update_status_type_0 import PipelineStatusResponseUpdateStatusType0

        d = dict(src_dict)
        autoscanned = d.pop("autoscanned", UNSET)

        busy = d.pop("busy", UNSET)

        job_name = d.pop("job_name", UNSET)

        def _parse_job_start(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_start = _parse_job_start(d.pop("job_start", UNSET))

        docs = d.pop("docs", UNSET)

        batchs = d.pop("batchs", UNSET)

        cur_batch = d.pop("cur_batch", UNSET)

        request_pending = d.pop("request_pending", UNSET)

        latest_message = d.pop("latest_message", UNSET)

        def _parse_history_messages(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_messages_type_0 = cast(list[str], data)

                return history_messages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        history_messages = _parse_history_messages(d.pop("history_messages", UNSET))

        def _parse_update_status(data: object) -> Union["PipelineStatusResponseUpdateStatusType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_status_type_0 = PipelineStatusResponseUpdateStatusType0.from_dict(data)

                return update_status_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PipelineStatusResponseUpdateStatusType0", None, Unset], data)

        update_status = _parse_update_status(d.pop("update_status", UNSET))

        pipeline_status_response = cls(
            autoscanned=autoscanned,
            busy=busy,
            job_name=job_name,
            job_start=job_start,
            docs=docs,
            batchs=batchs,
            cur_batch=cur_batch,
            request_pending=request_pending,
            latest_message=latest_message,
            history_messages=history_messages,
            update_status=update_status,
        )

        pipeline_status_response.additional_properties = d
        return pipeline_status_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
