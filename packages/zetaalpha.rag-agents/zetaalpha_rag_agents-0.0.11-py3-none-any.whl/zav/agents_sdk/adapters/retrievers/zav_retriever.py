import json
import time
from datetime import date, datetime
from functools import wraps
from typing import Dict, List, Literal, Optional

from zav.api.errors import UnknownException
from zav.pydantic_compat import BaseModel
from zav.search_api import ApiClient, Configuration
from zav.search_api.apis import DocumentAssetsApi as DocumentAssetsApiSync
from zav.search_api.apis import DocumentsApi as DocumentsApiSync
from zav.search_api.exceptions import ApiException
from zav.search_api.models import (
    DateRangeSchema,
    DocumentIdString,
    FacetConfiguration,
    FacetsConfiguration,
    FiltersConfiguration,
    ListResponse,
    QueryString,
    RetrievalMethodString,
    RetrievalUnit,
    SearchPostRequest,
    SearchPostResponse,
    SortingConfiguration,
    SortingConfigurationList,
    SortOrderSchema,
    SortSchema,
    UIDString,
    YearRangeSchema,
)

from zav.agents_sdk.adapters.async_wrapper import force_async, is_bound_function
from zav.agents_sdk.domain.agent_dependency import AgentDependencyFactory
from zav.agents_sdk.domain.request_headers import RequestHeaders


class RetrievedHistoryItem(BaseModel):
    search_payload: Dict
    retrieved_hits: List[Dict]


class DocumentsApi(DocumentsApiSync):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattribute__(self, name):
        original = object.__getattribute__(self, name)
        return force_async(original) if is_bound_function(original) else original


class DocumentAssetsApi(DocumentAssetsApiSync):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattribute__(self, name):
        original = object.__getattribute__(self, name)
        return force_async(original) if is_bound_function(original) else original


def _handle_pipeline_service_api_error(e: ApiException):
    error_message = "Server error"
    if e.body:
        body = json.loads(e.body)
        if "message" in body:
            error_message = body["message"]
        elif "detail" in body:
            error_message = body["detail"]
    raise UnknownException(error_message)


def _handle_pipeline_service_errors(f):
    @wraps(f)
    async def decorated(*args, _retries=0, **kwargs):
        try:
            return await f(*args, **kwargs)
        except ApiException as e:
            return _handle_pipeline_service_api_error(e)

    return decorated


def _parse_dates_to_str(obj: Dict) -> Dict:
    def process_value(value):
        if isinstance(value, list):
            return [process_value(v) for v in value]
        if isinstance(value, dict):
            return {k: process_value(v) for k, v in value.items()}
        elif isinstance(value, date) or isinstance(value, datetime):
            return value.isoformat()
        return value

    return {key: process_value(value) for key, value in obj.items()}


def _create_document_hit_url(
    tenant: str,
    retrieval_unit: str,
    property_name: str,
    property_values: str,
    index_cluster: Optional[str],
):
    params = {
        "tenant": tenant,
        **({"index_cluster": index_cluster} if index_cluster else {}),
        "property_name": property_name,
        "property_values": property_values,
    }
    query_params_string = "&".join([f"{key}={value}" for key, value in params.items()])
    return f"/documents/{retrieval_unit}/list?{query_params_string}"


class ZAVRetriever:
    def __init__(
        self,
        api_client: ApiClient,
        configuration: Configuration,
        request_headers: RequestHeaders,
        tenant: str,
        index_id: Optional[str] = None,
    ) -> None:
        if request_headers.authorization:
            api_client.set_default_header(
                "Authorization", request_headers.authorization
            )
        if request_headers.x_auth:
            api_client.set_default_header("X-Auth", request_headers.x_auth)
        self.__retrieved_history: List[RetrievedHistoryItem] = []
        self.__documents = DocumentsApi(api_client)
        self.__document_assets = DocumentAssetsApi(api_client)
        self.__internal_headers = request_headers.dict(
            exclude_none=True, exclude={"authorization", "x_auth"}
        )
        self.__configuration = configuration
        self.__tenant = tenant
        self.__index_id = index_id
        super().__init__()

    def get_retrieved_history(self) -> List[RetrievedHistoryItem]:
        return self.__retrieved_history

    def update_retrieved_history(self, retrieved_history_item: RetrievedHistoryItem):
        self.__retrieved_history.append(retrieved_history_item)

    @_handle_pipeline_service_errors
    async def search(
        self,
        retrieval_unit: Literal["document", "chunk"] = "document",
        retrieval_method: Optional[Literal["knn", "keyword", "mixed"]] = None,
        filters: Optional[Dict] = None,
        facets: Optional[List[Dict]] = None,
        sorting: Optional[List[Dict]] = None,
        sort: Optional[Dict] = None,
        sort_order: Optional[List[str]] = None,
        search_engine: Optional[str] = None,
        query_string: Optional[str] = None,
        include_default_filters: Optional[bool] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        rerank: Optional[bool] = None,
        rerank_top_n: Optional[int] = None,
        index_id: Optional[str] = None,
        index_type: Literal["internal", "federated"] = "internal",
        collapse: Optional[str] = "__NOT_SET",
        doc_ids: Optional[List[str]] = None,
        visibility: Optional[List[str]] = None,
        document_types: Optional[List[str]] = None,
        date: Optional[Dict] = None,
        sources: Optional[List[str]] = None,
        requested_field_paths: Optional[List[str]] = None,
        tag_ids: Optional[List[str]] = None,
        similar_to: Optional[List[str]] = None,
        include_doc_in_similar_to: Optional[bool] = None,
        year: Optional[Dict] = None,
    ) -> Dict:
        start_time = time.perf_counter_ns()
        date = _parse_dates_to_str(date) if date else None

        sel_index_id = index_id or self.__index_id
        search_payload = dict(
            tenant=self.__tenant,
            retrieval_unit=retrieval_unit,
            retrieval_method=retrieval_method,
            filters=filters,
            facets=facets,
            search_engine=search_engine,
            query_string=query_string,
            include_default_filters=include_default_filters,
            page=page,
            page_size=page_size,
            rerank=rerank,
            rerank_top_n=rerank_top_n,
            index_id=sel_index_id,
            index_type=index_type,
            visibility=visibility,
            document_types=document_types,
            sources=sources,
            tag_ids=tag_ids,
            similar_to=similar_to,
            include_doc_in_similar_to=include_doc_in_similar_to,
            year=year,
        )
        search_post_request = SearchPostRequest(
            tenant=self.__tenant,
            retrieval_unit=RetrievalUnit(retrieval_unit),
            **(
                {"retrieval_method": RetrievalMethodString(retrieval_method)}
                if retrieval_method
                else {}
            ),
            **(
                {
                    "filters": FiltersConfiguration(
                        **filters, _configuration=self.__configuration
                    )
                }
                if filters
                else {}
            ),
            **(
                {
                    "facets": FacetsConfiguration(
                        value=[
                            FacetConfiguration(
                                **facet, _configuration=self.__configuration
                            )
                            for facet in facets
                        ]
                    )
                }
                if facets
                else {}
            ),
            **(
                {
                    "sorting": SortingConfigurationList(
                        [
                            SortingConfiguration(
                                **s, _configuration=self.__configuration
                            )
                            for s in sorting
                        ]
                    )
                }
                if sorting
                else {}
            ),
            **(
                {"sort": SortSchema(**sort, _configuration=self.__configuration)}
                if sort
                else {}
            ),
            **(
                {
                    "sort_order": SortOrderSchema(
                        sort_order, _configuration=self.__configuration
                    )
                }
                if sort_order
                else {}
            ),
            **(
                {"date": DateRangeSchema(**date, _configuration=self.__configuration)}
                if date
                else {}
            ),
            **({"search_engine": search_engine} if search_engine else {}),
            **({"query_string": QueryString(query_string)} if query_string else {}),
            **(
                {"include_default_filters": include_default_filters}
                if include_default_filters
                else {}
            ),
            **({"page": page} if page else {}),
            **({"page_size": page_size} if page_size else {}),
            **({"rerank": rerank} if rerank else {}),
            **({"rerank_top_n": rerank_top_n} if rerank_top_n else {}),
            **({"index_id": sel_index_id} if sel_index_id else {}),
            **({"index_type": index_type} if index_type else {}),
            **({"collapse": collapse} if collapse != "__NOT_SET" else {}),
            **(
                {"doc_ids": [DocumentIdString(doc_id) for doc_id in doc_ids]}
                if doc_ids
                else {}
            ),
            **({"visibility": visibility} if visibility else {}),
            **({"document_types": document_types} if document_types else {}),
            **({"sources": sources} if sources else {}),
            **(
                {"requested_field_paths": requested_field_paths}
                if requested_field_paths
                else {}
            ),
            **({"tag_ids": tag_ids} if tag_ids else {}),
            **(
                {
                    "similar_to": [
                        UIDString(uid, _configuration=self.__configuration)
                        for uid in similar_to
                    ]
                }
                if similar_to
                else {}
            ),
            **(
                {"include_doc_in_similar_to": include_doc_in_similar_to}
                if include_doc_in_similar_to
                else {}
            ),
            **(
                {"year": YearRangeSchema(**year, _configuration=self.__configuration)}
                if year
                else {}
            ),
        )
        search_response: SearchPostResponse = (
            await self.__documents.document_search_post(
                search_post_request=search_post_request, **self.__internal_headers
            )
        )
        response_dict = search_response.to_dict()

        if "hits" in response_dict:
            for hit in response_dict["hits"]:
                hit["document_hit_url"] = _create_document_hit_url(
                    tenant=self.__tenant,
                    retrieval_unit=retrieval_unit,
                    property_name="id",
                    property_values=hit["id"],
                    index_cluster=(
                        f"default:{self.__index_id}" if self.__index_id else None
                    ),
                )
                chunk_id = hit["id"]
                doc_id = chunk_id.split("_")[0] + "_0"
                uri_hash = hit["uri_hash"]
                if any(
                    resource.get("resource_type") == "pdf_url"
                    for resource in hit.get("custom_metadata", {}).get("resources", [])
                ):
                    hit["document_url"] = f"/pdf/{doc_id}?chunkId={chunk_id}"
                else:
                    hit["document_url"] = f"/documents/{uri_hash}"

                if "document_content" in hit:
                    hit["document_content"] = [
                        document_content.to_dict()
                        for document_content in hit["document_content"]
                    ]
        if "facet_results" in response_dict:
            response_dict["facet_results"] = [
                facet_result.to_dict()
                for facet_result in response_dict["facet_results"]
            ]
        self.update_retrieved_history(
            RetrievedHistoryItem(
                search_payload=search_payload,
                retrieved_hits=response_dict.get("hits", []),
            )
        )
        end_time = time.perf_counter_ns()
        response_dict["latency_ms"] = round((end_time - start_time) / 1_000_000, 2)
        return response_dict

    @_handle_pipeline_service_errors
    async def retrieve(self, document_hit_url: str) -> Optional[Dict]:
        document_hit_url_parts = document_hit_url.split("?")
        if len(document_hit_url_parts) != 2:
            return None
        retrieval_unit = document_hit_url_parts[0].split("/")[-2]
        query_params = document_hit_url_parts[1].split("&")
        query_params_dict = {
            param_parts[0]: param_parts[1]
            for param in query_params
            if (param_parts := param.split("=")) and len(param_parts) == 2
        }
        tenant = query_params_dict.get("tenant")
        property_name = query_params_dict.get("property_name")
        property_values = query_params_dict.get("property_values")
        index_cluster = query_params_dict.get("index_cluster")
        index_id = index_cluster.split(":")[1] if index_cluster else None
        if tenant is None or property_name is None or property_values is None:
            return None

        return await self.list(
            retrieval_unit=retrieval_unit,  # type: ignore
            property_name=property_name,
            property_values=[property_values],
            **({"index_id": index_id} if index_id else {}),  # type: ignore
        )

    @_handle_pipeline_service_errors
    async def list(
        self,
        retrieval_unit: Literal["document", "chunk"] = "document",
        property_name: str = "id",
        property_values: List[str] = [],
        index_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Dict:
        if index_id:
            index_cluster = f"default:{index_id}"
        elif self.__index_id:
            index_cluster = f"default:{self.__index_id}"
        else:
            index_cluster = None
        list_response: ListResponse = await self.__documents.document_list(
            retrieval_unit=retrieval_unit,
            property_name=property_name,
            property_values=property_values,
            tenant=self.__tenant,
            **({"page": page} if page else {}),
            **({"page_size": page_size} if page_size else {}),
            **({"index_cluster": index_cluster} if index_cluster else {}),
            **self.__internal_headers,
        )
        response_dict = list_response.to_dict()
        if "hits" in response_dict:
            for hit in response_dict["hits"]:
                hit["document_hit_url"] = _create_document_hit_url(
                    tenant=self.__tenant,
                    retrieval_unit=retrieval_unit,
                    property_name=property_name,
                    property_values=hit[
                        "document_id" if property_name == "guid" else property_name
                    ],
                    index_cluster=index_cluster,
                )
        return response_dict

    @_handle_pipeline_service_errors
    async def get_full_text(self, document_id: Optional[str]) -> Optional[str]:
        if not document_id:
            return None
        index_cluster = f"default:{self.__index_id}" if self.__index_id else None
        document_assets_response = await self.__document_assets.retrieve_content(
            document_id=document_id,
            asset_type="text_url",
            tenant=self.__tenant,
            **({"index_cluster": index_cluster} if index_cluster else {}),
            **self.__internal_headers,
        )
        doc_content = document_assets_response.read().decode("utf-8")
        return doc_content

    @_handle_pipeline_service_errors
    async def get_image_asset(self, document_id: Optional[str]) -> Optional[bytes]:
        if not document_id:
            return None
        index_cluster = f"default:{self.__index_id}" if self.__index_id else None
        document_assets_response = await self.__document_assets.retrieve_content(
            document_id=document_id,
            asset_type="image_url",
            tenant=self.__tenant,
            **({"index_cluster": index_cluster} if index_cluster else {}),
            **self.__internal_headers,
        )
        return document_assets_response.read()

    @_handle_pipeline_service_errors
    async def get_pdf_asset(self, document_id: Optional[str]) -> Optional[bytes]:
        if not document_id:
            return None
        index_cluster = f"default:{self.__index_id}" if self.__index_id else None
        document_assets_response = await self.__document_assets.retrieve_content(
            document_id=document_id,
            asset_type="pdf_url",
            tenant=self.__tenant,
            **({"index_cluster": index_cluster} if index_cluster else {}),
            **self.__internal_headers,
        )
        return document_assets_response.read()

    @_handle_pipeline_service_errors
    async def get_content_asset(self, document_id: Optional[str]) -> Optional[bytes]:
        if not document_id:
            return None
        index_cluster = f"default:{self.__index_id}" if self.__index_id else None
        document_assets_response = await self.__document_assets.retrieve_content(
            document_id=document_id,
            asset_type="content_url",
            tenant=self.__tenant,
            **({"index_cluster": index_cluster} if index_cluster else {}),
            **self.__internal_headers,
        )
        return document_assets_response.read()


def _api_config(host: str, retries: Optional[int] = None) -> Configuration:
    config = Configuration(host=host, discard_unknown_keys=True)
    # `None` value in retries means that the default value of `urllib3`
    # will be used, which is 3 retries.
    config.retries = retries  # type: ignore
    return config


class ZAVRetrieverFactory(AgentDependencyFactory):
    @classmethod
    def create(
        cls,
        request_headers: RequestHeaders,
        zav_retriever_host: str = "https://api.zeta-alpha.com/v0/service",
        tenant: str = "zetaalpha",
        index_id: Optional[str] = None,
        authorization: Optional[str] = None,
        x_auth: Optional[str] = None,
        retries: Optional[int] = None,
    ) -> ZAVRetriever:
        configuration = _api_config(zav_retriever_host, retries)
        api_client = ApiClient(configuration)
        if authorization:
            api_client.set_default_header("Authorization", authorization)
        if x_auth:
            api_client.set_default_header("X-Auth", x_auth)

        return ZAVRetriever(
            api_client=api_client,
            configuration=configuration,
            request_headers=request_headers,
            tenant=tenant,
            index_id=index_id,
        )
