from typing import Protocol, TypeVar, Iterator, Union, runtime_checkable, Any



# T_co is a common naming convention for covariant type vars
T_num = TypeVar("T_num", covariant=True)

class SequenceLike(Protocol):
    def __getitem__(self, index: int | slice) -> Union[Any, "SequenceLike"]: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...