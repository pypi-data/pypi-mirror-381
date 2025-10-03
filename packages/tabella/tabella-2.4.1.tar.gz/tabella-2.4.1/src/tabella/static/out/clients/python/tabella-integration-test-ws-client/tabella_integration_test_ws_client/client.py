"""Python client template."""

import datetime
from typing import Any, Literal, Union
from uuid import UUID

from jsonrpc2pyclient.decorator import Transportable, rpc_class_method
from jsonrpc2pyclient.wsclient import AsyncRPCWSClient
from jsonrpc2pyclient.rpcclient import AsyncRPCClient, RPCClient
from py_undefined import Undefined
from pydantic import UUID1, UUID3, UUID4, UUID5

from tabella_integration_test_ws_client.models import (
    CollectionsModel,
    Constantly,
    ConstrainedCollections,
    DefaultFactory,
    Defaults,
    Flavor,
    IntEnum,
    KineticBody,
    Numbers,
    PaymentCardBrand,
    Primitives,
    PydanticExtra,
    PydanticNetworkTypes,
    PydanticTypes,
    PythonTypes,
    RecursiveModel,
    RefModel,
    VanillaModel,
    Vector3,
)

ClientType = Union[AsyncRPCClient, RPCClient]
CLIENT_URL = "ws://localhost:8000/api/v1"


class TabellaIntegrationTestClient(Transportable):
    def __init__(
        self, headers: dict[str, Any], client_url: str = CLIENT_URL, **kwargs: Any
    ) -> None:
        transport = AsyncRPCWSClient(client_url, headers, **kwargs)
        self.math = TabellaIntegrationTestClient._MathClient(transport)
        self.auth = TabellaIntegrationTestClient._AuthClient(transport)
        self.extra = TabellaIntegrationTestClient._ExtraClient(transport)
        super().__init__(transport)

    @rpc_class_method(method_name="http_only_method")
    async def http_only_method(self) -> None: ...
    @rpc_class_method(method_name="ws_only_method")
    async def ws_only_method(self) -> None: ...
    @rpc_class_method(method_name="wait")
    async def wait(self, seconds: float = Undefined) -> float: ...
    @rpc_class_method(method_name="wait_5")
    async def wait_5(self) -> None: ...
    @rpc_class_method(method_name="wait_sum")
    async def wait_sum(self, a: int, b: int) -> int: ...
    @rpc_class_method(method_name="untyped")
    async def untyped(self, a: Any, b: Any) -> Any: ...
    @rpc_class_method(method_name="undocumented")
    async def undocumented(self, a: int, b: int) -> int: ...
    @rpc_class_method(method_name="arrays_of_models")
    async def arrays_of_models(
        self, model: list[Primitives], models: list[PythonTypes], nested_model: RefModel
    ) -> None: ...
    @rpc_class_method(method_name="dicts_of_models")
    async def dicts_of_models(self) -> None: ...
    @rpc_class_method(method_name="int_enum_method")
    async def int_enum_method(self, kale: IntEnum) -> IntEnum: ...
    @rpc_class_method(method_name="nested_models")
    async def nested_models(self, a: KineticBody) -> KineticBody: ...
    @rpc_class_method(method_name="list_union_model")
    async def list_union_model(
        self, a: list[VanillaModel | RecursiveModel]
    ) -> list[VanillaModel | RecursiveModel]: ...
    @rpc_class_method(method_name="constant")
    async def constant(
        self,
        const_str_field: Literal["Cat."],
        const_num_field: Literal[3],
        const_none_field: Literal[None],
        const_true_field: Literal[True],
        const_false_field: Literal[False],
    ) -> Constantly: ...
    @rpc_class_method(method_name="primitives")
    async def primitives(
        self, a: int, b: float, c: str, d: bool, e: bytes, f: None
    ) -> Primitives: ...
    @rpc_class_method(method_name="models")
    async def models(
        self, a: VanillaModel, b: RecursiveModel
    ) -> tuple[VanillaModel, RecursiveModel]: ...
    @rpc_class_method(method_name="python_types")
    async def python_types(
        self,
        str_enum: Flavor,
        num_enum: Numbers,
        date: datetime.date,
        time: datetime.time,
        datetime_field: datetime.datetime,
        timedelta: datetime.timedelta,
        uuid_field: UUID,
        decimal: float | str,
        path: str,
    ) -> PythonTypes: ...
    @rpc_class_method(method_name="default")
    async def default(
        self,
        a: str = Undefined,
        b: int = Undefined,
        c: float = Undefined,
        d: bool = Undefined,
        e: bool = Undefined,
        f: list[str] | None = Undefined,
        g: DefaultFactory | None = Undefined,
    ) -> Defaults: ...
    @rpc_class_method(method_name="default_untyped")
    async def default_untyped(
        self,
        g: Any = Undefined,
        h: Any = Undefined,
        i: Any = Undefined,
        j: Any = Undefined,
        k: Any = Undefined,
        m: Any = Undefined,
    ) -> tuple[Any, Any, Any, Any, Any, Any]: ...
    @rpc_class_method(method_name="default_enum")
    async def default_enum(
        self, a: Flavor = Undefined, b: Any = Undefined
    ) -> tuple[Flavor, Any]: ...
    @rpc_class_method(method_name="enum_method")
    async def enum_method(self, flavor: Flavor) -> Flavor: ...
    @rpc_class_method(method_name="collections_function")
    async def collections_function(
        self,
        list_field: list[Any],
        list_str: list[str],
        list_list: list[list[Any]],
        list_list_int: list[list[int]],
        list_model: list[VanillaModel],
        list_model_or_model: list[VanillaModel | RecursiveModel],
        list_union: list[str | int],
        list_dict: list[dict[str, Any]],
        list_dict_str: list[dict[str, str]],
        list_dict_int_keys: list[dict[str, str]],
        tuple_field: list[Any],
        tuple_str: tuple[str],
        tuple_tuple: tuple[list[Any]],
        tuple_tuple_int: tuple[tuple[int]],
        tuple_model: tuple[VanillaModel],
        tuple_union: tuple[str | int],
        tuple_int_str_none: tuple[int, str, None],
        set_str: set[str],
        set_union: set[str | int],
        dict_field: dict[str, Any],
        dict_str: dict[str, str],
        dict_dict: dict[str, dict[str, Any]],
        dict_int_keys: dict[str, str],
        dict_model: dict[str, VanillaModel],
        dict_model_or_model: dict[str, VanillaModel | RecursiveModel],
        dict_union: dict[str, str | int],
        dict_list: dict[str, list[int]],
    ) -> CollectionsModel: ...
    @rpc_class_method(method_name="constrained_collection")
    async def constrained_collection(
        self, list_min: list[Any], list_max: list[str], list_min_max: list[str]
    ) -> ConstrainedCollections: ...
    @rpc_class_method(method_name="unions")
    async def unions(self, union_param: int | bool | None) -> int | bool | None: ...
    @rpc_class_method(method_name="tuple_method")
    async def tuple_method(
        self, a: tuple[int | None, str, str]
    ) -> tuple[int | None, str, str]: ...
    @rpc_class_method(method_name="any_array")
    async def any_array(self, a: list[Any]) -> list[Any]: ...
    @rpc_class_method(method_name="array")
    async def array(self, a: list[int | None]) -> list[int | None]: ...
    @rpc_class_method(method_name="array_array")
    async def array_array(
        self, a: list[list[int | None]]
    ) -> list[list[int | None]]: ...
    @rpc_class_method(method_name="array_object")
    async def array_object(self, a: list[dict[str, Any]]) -> list[dict[str, Any]]: ...
    @rpc_class_method(method_name="array_union_array")
    async def array_union_array(
        self, a: list[list[list[Any] | int]]
    ) -> list[list[list[Any] | int]]: ...
    @rpc_class_method(method_name="objects")
    async def objects(self, a: dict[str, Any]) -> dict[str, Any]: ...
    @rpc_class_method(method_name="typed_object")
    async def typed_object(
        self, a: dict[str, int | Flavor | None]
    ) -> dict[str, int | Flavor | None]: ...
    @rpc_class_method(method_name="object_object")
    async def object_object(
        self, a: dict[str, dict[str, str]]
    ) -> dict[str, dict[str, str]]: ...
    @rpc_class_method(method_name="object_model")
    async def object_model(
        self, a: dict[str, RecursiveModel]
    ) -> dict[str, RecursiveModel]: ...
    @rpc_class_method(method_name="object_array")
    async def object_array(self, a: dict[str, list[int]]) -> dict[str, list[int]]: ...
    @rpc_class_method(method_name="array_model")
    async def array_model(self, a: list[VanillaModel]) -> list[VanillaModel]: ...
    @rpc_class_method(method_name="array_recursive_model")
    async def array_recursive_model(
        self, a: list[RecursiveModel]
    ) -> list[RecursiveModel]: ...
    @rpc_class_method(method_name="top_level_union_array")
    async def top_level_union_array(
        self, a: list[bool] | None
    ) -> list[bool] | None: ...
    @rpc_class_method(method_name="union_arrays")
    async def union_arrays(
        self, a: list[bool] | list[int] | list[str]
    ) -> list[bool] | list[int] | list[str]: ...

    class _MathClient(Transportable):
        @rpc_class_method(method_name="math.add")
        async def add(self, a: int, b: int) -> int: ...
        @rpc_class_method(method_name="math.divide")
        async def divide(self, a: int, b: int) -> float: ...
        @rpc_class_method(method_name="math.subtract")
        async def subtract(self, a: int, b: int) -> int: ...
        @rpc_class_method(method_name="math.get_distance")
        async def get_distance(self, a: Vector3, b: Vector3) -> Vector3: ...
        @rpc_class_method(method_name="math.get_origin")
        async def get_origin(self) -> Vector3: ...

    class _AuthClient(Transportable):
        @rpc_class_method(method_name="auth.needs_api_key")
        async def needs_api_key(self) -> str: ...
        @rpc_class_method(method_name="auth.needs_bearer_token")
        async def needs_bearer_token(self) -> str: ...
        @rpc_class_method(method_name="auth.needs_oauth_read")
        async def needs_oauth_read(self) -> int: ...
        @rpc_class_method(method_name="auth.needs_oauth_write")
        async def needs_oauth_write(self) -> bool: ...
        @rpc_class_method(method_name="auth.needs_oauth_read_write")
        async def needs_oauth_read_write(self) -> int: ...
        @rpc_class_method(method_name="auth.needs_apikey_or_bearer")
        async def needs_apikey_or_bearer(self) -> bool: ...

    class _ExtraClient(Transportable):
        @rpc_class_method(method_name="extra.pydantic_types")
        async def pydantic_types(
            self,
            strict_bool: bool,
            positive_int: int,
            negative_int: int,
            non_positive_int: int,
            non_negative_int: int,
            strict_int: int,
            positive_float: float,
            negative_float: float,
            non_positive_float: float,
            non_negative_float: float,
            strict_float: float,
            finite_float: float,
            strict_bytes: bytes,
            strict_str: str,
            uuid1: UUID1,
            uuid3: UUID3,
            uuid4: UUID4,
            uuid5: UUID5,
            base64_bytes: str,
            base64_str: str,
            str_constraints_strip_whitespace: str,
            str_constraints_to_upper: str,
            str_constraints_to_lower: str,
            str_constraints_strict: str,
            str_constraints_min_length: str,
            str_constraints_max_length: str,
            json_field: str,
            past_date: datetime.date,
            future_date: datetime.date,
            aware_datetime: datetime.datetime,
            naive_datetime: datetime.datetime,
            past_datetime: datetime.datetime,
            future_datetime: datetime.datetime,
            constrained_float: float,
        ) -> PydanticTypes: ...
        @rpc_class_method(method_name="extra.pydantic_network_types")
        async def pydantic_network_types(
            self,
            any_url: str,
            any_http_url: str,
            http_url: str,
            postgres_dsn: str,
            cockroach_dsn: str,
            amqp_dsn: str,
            redis_dsn: str,
            mongo_dsn: str,
            kafka_dsn: str,
            mysql_dsn: str,
            mariadb_dsn: str,
            email_str: str,
            name_email: str,
            ipv_any_address: str,
            ipv_any_interface: str,
            ipv_any_network: str,
        ) -> PydanticNetworkTypes: ...
        @rpc_class_method(method_name="extra.pydantic_extra")
        async def pydantic_extra(
            self,
            color: str,
            payment_card_brand: PaymentCardBrand,
            payment_card_number: str,
            aba_routing_number: str,
        ) -> PydanticExtra: ...
    async def connect(self) -> None:
        """Connect to WebSocket server."""
        await self.transport.connect()

    async def close(self) -> None:
        """Close connection to WebSocket server."""
        await self.transport.close()
