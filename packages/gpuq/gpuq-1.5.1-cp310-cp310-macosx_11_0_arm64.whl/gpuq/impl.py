import os
import site
import itertools
from abc import ABC, abstractmethod
from types import TracebackType
from typing import Any, ContextManager, Generator, Literal
from contextlib import contextmanager

from . import C
from .datatypes import Provider, MockCObj, Properties
from .cuda import CudaRuntimeInfo, get_cuda_info, CudaRuntimeInfoMock
from .hip import HipRuntimeInfo, get_hip_info, HipRuntimeInfoMock


def _restore_default_hints() -> None:
    sites = site.getsitepackages().copy()
    if site.ENABLE_USER_SITE:
        sites.append(site.getusersitepackages())

    loc_hints = ["/opt/cuda/targets/x86_64-linux/lib/", "/opt/rocm/lib/"] + list(
        itertools.chain.from_iterable(
            [
                os.path.join(loc, "nvidia/cuda_runtime/lib/"),
                os.path.join(loc, "torch/lib/"),
                os.path.join(loc, "triton/lib/"),
            ]
            for loc in sites
        )
    )

    loc_hints_ascii = [loc.encode("ascii") for loc in loc_hints]

    C._set_location_hints(loc_hints_ascii)


try:
    _restore_default_hints()
except ValueError as e:
    raise ValueError(
        f"Failed to configure loading hints for the library! Site locations: {site.getsitepackages()} and {site.getusersitepackages()}"
    ) from e


Visible = dict[Provider, list[int] | None]


def _is_int(value: Any, _prefix: str) -> int:
    try:
        value = int(value)
        return True
    except:
        raise ValueError(
            f"{_prefix}_VISIBLE_DEVICES environment variable contains values that are not integer - this is currently not supported: {value!r}"
        ) from None


class Implementation(ABC):
    def __init__(self) -> None:
        self._ctx: ContextManager["Implementation"] | None = None

    @abstractmethod
    def provider_check(self, provider: Provider) -> str: ...

    @abstractmethod
    def save_visible(self, clear: bool = True) -> ContextManager[Visible]: ...

    @abstractmethod
    def c_count(self) -> int: ...

    @abstractmethod
    def c_get(self, ord: int) -> Any: ...

    @abstractmethod
    def cuda_runtime_info(self, gpu_index: int) -> CudaRuntimeInfo | None: ...

    @abstractmethod
    def hip_runtime_info(self, gpu_index: int) -> HipRuntimeInfo | None: ...

    def set(self) -> "Implementation":
        from . import _set_impl

        return _set_impl(self)

    def __enter__(self) -> "Implementation":
        from . import _with_impl

        self._ctx = _with_impl(self)
        self._ctx.__enter__()
        return self

    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        if self._ctx is not None:
            return self._ctx.__exit__(type_, value, traceback)
        return None

    def query(
        self,
        provider: Provider = Provider.any(),
        required: Provider | None | Literal[True] = None,
        visible_only: bool = True,
    ) -> list[Properties]:
        from . import query

        return query(
            provider=provider, required=required, visible_only=visible_only, impl=self
        )

    def count(
        self, provider: Provider = Provider.all(), visible_only: bool = False
    ) -> int:
        from . import count

        return count(provider=provider, visible_only=visible_only, impl=self)

    def get(
        self, idx: int, provider: Provider = Provider.all(), visible_only: bool = False
    ) -> Properties:
        from . import get

        return get(idx=idx, provider=provider, visible_only=visible_only, impl=self)

    def checkprovider(self, p: Provider) -> str:
        from . import checkprovider

        return checkprovider(p=p, impl=self)

    def checkcuda(self) -> str:
        from . import checkcuda

        return checkcuda(impl=self)

    def checkamd(self) -> str:
        from . import checkamd

        return checkamd(impl=self)

    def hasprovider(self, p: Provider) -> bool:
        from . import hasprovider

        return hasprovider(p=p, impl=self)

    def hascuda(self) -> bool:
        from . import hascuda

        return hascuda(impl=self)

    def hasamd(self) -> bool:
        from . import hasamd

        return hasamd(impl=self)

    def __getstate__(self) -> dict[str, Any]:
        state = self.__dict__.copy()
        state["_ctx"] = None
        return state

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__dict__.update(state)


class GenuineImplementation(Implementation):
    def provider_check(self, provider: Provider) -> str:
        if provider == Provider.CUDA:
            return C.checkcuda()
        if provider == Provider.HIP:
            return C.checkamd()

        raise ValueError(f"Invalid provider: {provider}")

    @contextmanager
    def save_visible(self, clear: bool = True) -> Generator[Visible, None, None]:
        cuda = os.environ.get("CUDA_VISIBLE_DEVICES", None)
        hip = os.environ.get("HIP_VISIBLE_DEVICES", None)

        parsed_cuda: list[int] | None
        parsed_hip: list[int] | None
        if cuda is not None:
            parsed_cuda = {int(g) for g in cuda.split(",") if _is_int(g, "CUDA")}  # type: ignore[assignment]
            parsed_cuda = sorted(list(parsed_cuda))  # type: ignore[arg-type]
        else:
            parsed_cuda = None

        if hip is not None:
            parsed_hip = {int(g) for g in hip.split(",") if _is_int(g, "HIP")}  # type: ignore[assignment]
            parsed_hip = sorted(list(parsed_hip))  # type: ignore[arg-type]
        else:
            parsed_hip = parsed_cuda

        if clear:
            if cuda is not None:
                del os.environ["CUDA_VISIBLE_DEVICES"]
            if hip is not None:
                del os.environ["HIP_VISIBLE_DEVICES"]

        try:
            yield {Provider.CUDA: parsed_cuda, Provider.HIP: parsed_hip}
        finally:
            if clear:
                if cuda is not None:
                    os.environ["CUDA_VISIBLE_DEVICES"] = cuda
                if hip is not None:
                    os.environ["HIP_VISIBLE_DEVICES"] = hip

    def c_count(self) -> int:
        return int(C.count())

    def c_get(self, ord: int) -> Any:
        return C.get(ord)

    def cuda_runtime_info(self, gpu_index: int) -> CudaRuntimeInfo | None:
        return get_cuda_info(gpu_index)

    def hip_runtime_info(self, gpu_index: int) -> HipRuntimeInfo | None:
        return get_hip_info(gpu_index)


class MockImplementation(Implementation):
    def __init__(
        self,
        cuda_count: int | None = 1,
        hip_count: int | None = None,
        cuda_visible: list[str | int] | None = None,
        hip_visible: list[str | int] | None = None,
        name: str | list[str] = "{} Mock Device",
        major: int = 1,
        minor: int = 2,
        total_memory: int = 8 * 1024**3,
        sms_count: int = 12,
        sm_threads: int = 2048,
        sm_shared_memory: int = 16 * 1024,
        sm_registers: int = 512,
        sm_blocks: int = 4,
        block_threads: int = 1024,
        block_shared_memory: int = 8 * 1024,
        block_registers: int = 256,
        warp_size: int = 32,
        l2_cache_size: int = 8 * 1024**2,
        concurrent_kernels: bool = True,
        async_engines_count: int = 0,
        cooperative: bool = True,
        cuda_utilisation: int = 0,
        cuda_memory: int = 1,
        cuda_pids: list[int] = [],
        hip_gfx: str = "942",
        hip_drm: int = 128,
        hip_node_idx: int = 2,
        hip_pids: list[int] = [],
        _hip_drm_stride: int = 8,
    ) -> None:
        if (cuda_count is not None and cuda_count < 0) or (
            hip_count is not None and hip_count < 0
        ):
            raise ValueError("Negative number of mock devices!")

        self.cuda_count = cuda_count
        self.hip_count = hip_count
        self.overall_count = (cuda_count or 0) + (hip_count or 0)

        self.cuda_visible: list[int] | None
        self.hip_visible: list[int] | None

        if isinstance(name, str):
            self.names = [name] * self.overall_count
        else:
            if len(name) < self.overall_count:
                raise ValueError(
                    f"Insufficient names: {len(name)}, needs at least: {self.overall_count}"
                )
            self.names = name

        self.cobj_args = {
            "major": major,
            "minor": minor,
            "total_memory": total_memory,
            "sms_count": sms_count,
            "sm_threads": sm_threads,
            "sm_shared_memory": sm_shared_memory,
            "sm_registers": sm_registers,
            "sm_blocks": sm_blocks,
            "block_threads": block_threads,
            "block_shared_memory": block_shared_memory,
            "block_registers": block_registers,
            "warp_size": warp_size,
            "l2_cache_size": l2_cache_size,
            "concurrent_kernels": concurrent_kernels,
            "async_engines_count": async_engines_count,
            "cooperative": cooperative,
        }

        self.cuda_runtime_args = {
            "utilisation": cuda_utilisation,
            "used_memory": cuda_memory,
            "pids": cuda_pids,
        }

        self.hip_runtime_args = {
            "gfx": hip_gfx,
            "drm": hip_drm,
            "node_idx": hip_node_idx,
            "pids": hip_pids,
        }

        self._hip_drm_stride = _hip_drm_stride

        if cuda_visible is not None:
            self.cuda_visible = sorted(
                list({int(idx) for idx in cuda_visible if _is_int(idx, "CUDA")})
            )
        else:
            self.cuda_visible = None

        if hip_visible is not None:
            self.hip_visible = sorted(
                list({int(idx) for idx in hip_visible if _is_int(idx, "HIP")})
            )
        else:
            self.hip_visible = None

    def provider_check(self, provider: Provider) -> str:
        if provider == Provider.CUDA:
            return (
                ""
                if self.cuda_count is not None
                else "Mock implementation has not been configured to report CUDA runtime"
            )
        if provider == Provider.HIP:
            return (
                ""
                if self.hip_count is not None
                else "Mock implementation has not been configured to report HIP runtime"
            )

        raise ValueError(f"Invalid provider: {provider}")

    @contextmanager
    def save_visible(self, clear: bool = True) -> Generator[Visible, None, None]:
        cuda = self.cuda_visible.copy() if self.cuda_visible is not None else None
        hip = self.hip_visible.copy() if self.hip_visible is not None else None

        if clear:
            self.cuda_visible = None
            self.hip_visible = None

        try:
            yield {Provider.CUDA: cuda, Provider.HIP: hip if hip is not None else cuda}
        finally:
            if clear:
                self.cuda_visible = cuda
                self.hip_visible = hip

    def _count_hip(self) -> int:
        if not self.hip_count:
            return 0
        if self.hip_visible is not None:
            count = sum(
                1 for idx in self.hip_visible if idx >= 0 and idx < self.hip_count
            )
        elif self.cuda_visible is not None:
            count = sum(
                1 for idx in self.cuda_visible if idx >= 0 and idx < self.hip_count
            )
        else:
            count = self.hip_count

        return count

    def _count_cuda(self) -> int:
        if not self.cuda_count:
            return 0
        if self.cuda_visible is not None:
            count = sum(
                1 for idx in self.cuda_visible if idx >= 0 and idx < self.cuda_count
            )
        else:
            count = self.cuda_count
        return count

    def c_count(self) -> int:
        cuda_count = self._count_cuda()
        hip_count = self._count_hip()
        return cuda_count + hip_count

    def c_get(self, ord: int) -> Any:
        if ord < 0 or ord >= self.overall_count:
            raise IndexError("Invalid device index")

        index = ord
        provider = "CUDA"
        if ord >= (self.cuda_count or 0):
            index = ord - (self.cuda_count or 0)
            provider = "HIP"

        return MockCObj(ord=ord, name=self.names[ord], provider=provider, index=index, **self.cobj_args)  # type: ignore[arg-type]

    def cuda_runtime_info(self, gpu_index: int) -> CudaRuntimeInfo | None:
        if self.cuda_count is None or gpu_index < 0 or gpu_index >= self.cuda_count:
            return None

        return CudaRuntimeInfoMock(gpu_index, **self.cuda_runtime_args)  # type: ignore[arg-type]

    def hip_runtime_info(self, gpu_index: int) -> HipRuntimeInfo | None:
        if self.hip_count is None or gpu_index < 0 or gpu_index >= self.hip_count:
            return None

        ret = HipRuntimeInfoMock(gpu_index, **self.hip_runtime_args)  # type: ignore[arg-type]
        ret.drm += gpu_index * self._hip_drm_stride
        ret.node_idx += gpu_index
        return ret
