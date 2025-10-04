from __future__ import annotations
import numpy as np
from typing import (
    List,
    Tuple,
    Union,
    Iterator,
    Iterable,
    TypeVar,
    Generic,
    Any,
    TYPE_CHECKING,
    Type,
    Sequence
)
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from .matrix import Matrix  # only for type checking, no runtime import

T = TypeVar("T", bound="VectorBase")

Number = Union[int, float]


class VectorBase(Generic[T], Sequence[float], ABC):
    """Base class for all vector implementations"""

    @classmethod
    @abstractmethod
    def _dimension(cls) -> int:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(str(x) for x in self)})"

    def __repr__(self) -> str:
        return str(self)

    def __iter__(self) -> Iterator[float]:
        raise NotImplementedError("Subclasses must implement __iter__")

    def __len__(self) -> int:
        raise NotImplementedError("Subclasses must implement __len__")

    def __getitem__(self, index: int) -> float:
        raise NotImplementedError("Subclasses must implement __getitem__")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("Subclasses must implement __getitem__")

    def to_list(self) -> List[float]:
        return list(self)

    def to_tuple(self) -> Tuple[float, ...]:
        return tuple(self)

    def to_numpy(self) -> np.ndarray:
        return np.array(list(self))
    
    def _get_component(self, char : str) -> float:
        components = vars(self)
        for key in components.keys():
            if key[1] == char:
                return components[key]
        raise ValueError(f"Invalid swizzle character: {char}")
    
    def _set_component(self, char : str, value : float):
        components = vars(self)
        for key in list(components.keys()):
            if key[1] == char:
                return setattr(self, key, float(value))
        raise ValueError(f"Invalid swizzle character: {char}")

    @classmethod
    def from_numpy(cls: Type[T], array: np.ndarray) -> T:
        if len(array) < cls._dimension():
            raise ValueError(f"Array must have at least {cls._dimension()} elements")
        return cls(*array[:cls._dimension()])

    @property
    def magnitude(self) -> float:
        return np.sqrt(sum(x**2 for x in self))

    def normalize(self: T) -> T:
        mag = self.magnitude
        if mag == 0:
            return self
        cls: Type[T] = type(self)
        return cls(*(x / mag for x in self))

    @property
    def normalized(self: T) -> T:
        return self.normalize()

    def distance_to(self, other: T) -> float:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can only calculate distance to another {self.__class__.__name__}"
            )
        return np.sqrt(sum((a - b) ** 2 for a, b in zip(self, other)))

    def dot(self, other: T) -> float:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Can only calculate dot product with another {self.__class__.__name__}"
            )
        return sum(a * b for a, b in zip(self, other))

    def reverse(self : T) -> T:
        cls: Type[T] = type(self)
        return cls(*(-x for x in self))

    @property
    def reversed(self : T) -> T:
        return self.reverse()


class Vector2(VectorBase["Vector2"]):
    @classmethod
    def _dimension(cls) -> int:
        return 2

    def __init__(self, *args):
        self._x : float
        self._y : float
        if len(args) == 2:
            self._x, self._y = map(float, args)
        elif len(args) == 1 and isinstance(args[0], Union[Iterable, "Vector2"]):
            self._x, self._y = map(float, args[0])
        elif len(args) == 1 and isinstance(args[0], Number):
            self._x = self._y = float(args[0])
        elif len(args) == 0:
            self._x = self._y = self._z = 0.0
        else:
            raise TypeError("Invalid arguments for Vector2")
    
    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y
    
    @property
    def xy(self) -> "Vector2":
        return Vector2(self._x, self._y)

    @x.setter
    def x(self, value : float):
        self._x = value
    
    @y.setter
    def y(self, value : float):
        self._y = value
    
    @xy.setter
    def xy(self, values : Iterable):
        values = list(values)
        if len(values) != 2:
            raise ValueError(f"Vector2 requires exactly 2 values, got {len(values)}")
        self._x, self._y = values

    def __getattr__(self, name: str) -> Union[float, Vector2, Vector3, Vector4, Tuple[float, ...]]:
        try:
            attributes = tuple(self._get_component(char) for char in name)
            length = len(attributes)
            if length == 1:
                return attributes[0]
            types = {2 : Vector2, 3 : Vector3, 4 : Vector4}
            return types.get(length, tuple)(attributes)
        except:
            pass
        if len(attributes) == 0:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        else:
            return attributes
    
    def __setattr__(self, name: str, value: float) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
            return
        for char in name:
            try:
                self._set_component(char, value)
            except:
                object.__setattr__(self, char, value)


    def __iter__(self) -> Iterator[float]:
        yield self._x
        yield self._y

    def __len__(self) -> int:
        return 2

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        else:
            raise IndexError("Vector2 index out of range")

    def __setitem__(self, index: int, value: float):
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value
        else:
            raise IndexError("Vector2 index out of range")

    def __add__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, Vector2):
            return Vector2(self._x + other.x, self._y + other.y)
        elif isinstance(other, (float, int)):
            return Vector2(self._x + other, self._y + other)
        return NotImplemented

    def __radd__(self, other: Union[float, int]) -> "Vector2":
        if isinstance(other, (float, int)):
            return Vector2(self._x + other, self._y + other)
        return NotImplemented

    def __sub__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, Vector2):
            return Vector2(self._x - other.x, self._y - other.y)
        elif isinstance(other, (float, int)):
            return Vector2(self._x - other, self._y - other)
        return NotImplemented

    def __rsub__(self, other: Union[float, int]) -> "Vector2":
        if isinstance(other, (float, int)):
            return Vector2(other - self._x, other - self._y)
        return NotImplemented

    def __mul__(
        self, other: Union["Vector2", float, int, "Matrix"]
    ) -> Union["Vector2", Any]:
        from .matrix import (
            Matrix,
        )  # runtime import inside method to avoid circular import

        if isinstance(other, (int, float)):
            return Vector2(self._x * other, self._y * other)
        elif isinstance(other, Vector2):
            return Vector2(self._x * other.x, self._y * other.y)
        elif isinstance(other, Matrix):
            if other.cols != 2:
                raise ValueError(
                    f"Cannot multiply Vector2 with Matrix({other.rows}×{other.cols})"
                )
            result = [0.0] * other.rows
            for i in range(other.rows):
                for j in range(other.cols):
                    if j == 0:
                        result[i] += self._x * other.data[i][j]
                    else:
                        result[i] += self._y * other.data[i][j]
            if len(result) == 2:
                return Vector2(result[0], result[1])
            return result
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            return Vector2(self._x * other, self._y * other)
        return NotImplemented

    def __truediv__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            return Vector2(self._x / other, self._y / other)
        elif isinstance(other, Vector2):
            return Vector2(self._x / other.x, self._y / other.y)
        return NotImplemented

    def __rtruediv__(self, other: Union[float, int]) -> "Vector2":
        if isinstance(other, (float, int)):
            return Vector2(other / self._x, other / self._y)
        return NotImplemented

    def __floordiv__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            return Vector2(self._x // other, self._y // other)
        elif isinstance(other, Vector2):
            return Vector2(self._x // other.x, self._y // other.y)
        return NotImplemented

    def __rfloordiv__(self, other: Union[float, int]) -> "Vector2":
        if isinstance(other, (float, int)):
            return Vector2(other // self._x, other // self._y)
        return NotImplemented

    def __mod__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            return Vector2(self._x % other, self._y % other)
        elif isinstance(other, Vector2):
            return Vector2(self._x % other.x, self._y % other.y)
        return NotImplemented

    def __rmod__(self, other: Union[float, int]) -> "Vector2":
        if isinstance(other, (float, int)):
            return Vector2(other % self._x, other % self._y)
        return NotImplemented

    def __pow__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            return Vector2(self._x**other, self._y**other)
        elif isinstance(other, Vector2):
            return Vector2(self._x**other.x, self._y**other.y)
        return NotImplemented

    def __rpow__(self, other: Union[float, int]) -> "Vector2":
        if isinstance(other, (float, int)):
            return Vector2(other**self._x, other**self._y)
        return NotImplemented

    # In-place operations
    def __iadd__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, Vector2):
            self._x += other.x
            self._y += other.y
        elif isinstance(other, (int, float)):
            self._x += other
            self._y += other
        else:
            return NotImplemented
        return self

    def __isub__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, Vector2):
            self._x -= other.x
            self._y -= other.y
        elif isinstance(other, (int, float)):
            self._x -= other
            self._y -= other
        else:
            return NotImplemented
        return self

    def __imul__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            self._x *= other
            self._y *= other
        elif isinstance(other, Vector2):
            self._x *= other.x
            self._y *= other.y
        else:
            return NotImplemented
        return self

    def __itruediv__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            self._x /= other
            self._y /= other
        elif isinstance(other, Vector2):
            self._x /= other.x
            self._y /= other.y
        else:
            return NotImplemented
        return self

    def __ifloordiv__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            self._x //= other
            self._y //= other
        elif isinstance(other, Vector2):
            self._x //= other.x
            self._y //= other.y
        else:
            return NotImplemented
        return self

    def __imod__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            self._x %= other
            self._y %= other
        elif isinstance(other, Vector2):
            self._x %= other.x
            self._y %= other.y
        else:
            return NotImplemented
        return self

    def __ipow__(self, other: Union["Vector2", float, int]) -> "Vector2":
        if isinstance(other, (int, float)):
            self._x **= other
            self._y **= other
        elif isinstance(other, Vector2):
            self._x **= other.x
            self._y **= other.y
        else:
            return NotImplemented
        return self

    # Comparison
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Vector2):
            return self._x == other.x and self._y == other.y
        return NotImplemented

    def __lt__(self, other: Union["Vector2", float, int]) -> bool:
        if isinstance(other, Vector2):
            return self._x < other.x and self._y < other.y
        elif isinstance(other, (int, float)):
            return self._x < other and self._y < other
        return NotImplemented

    def __gt__(self, other: Union["Vector2", float, int]) -> bool:
        if isinstance(other, Vector2):
            return self._x > other.x and self._y > other.y
        elif isinstance(other, (int, float)):
            return self._x > other and self._y > other
        return NotImplemented

    def __le__(self, other: Union["Vector2", float, int]) -> bool:
        if isinstance(other, Vector2):
            return self._x <= other.x and self._y <= other.y
        elif isinstance(other, (int, float)):
            return self._x <= other and self._y <= other
        return NotImplemented

    def __ge__(self, other: Union["Vector2", float, int]) -> bool:
        if isinstance(other, Vector2):
            return self._x >= other.x and self._y >= other.y
        elif isinstance(other, (int, float)):
            return self._x >= other and self._y >= other
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self._x, self._y))


class Vector3(VectorBase["Vector3"]):
    _dimension : int = 3

    def __init__(self, *args):
        self._x : float
        self._y : float
        self._z : float
        if len(args) == 3:
            self._x, self._y, self._z = map(float, args)
        elif len(args) == 1 and isinstance(args[0], Union[Iterable, "Vector3"]):
            self._x, self._y, self._z = map(float, args[0])
        elif len(args) == 1 and isinstance(args[0], Number):
            self._x = self._y = self._z = float(args[0])
        elif len(args) == 0:
            self._x = self._y = self._z = 0.0
        else:
            raise TypeError("Invalid arguments for Vector3")

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z
    
    @property
    def xyz(self) -> "Vector3":
        return Vector3(self._x, self._y, self._z)
    
    @x.setter
    def x(self, value : float):
        self._x = value
    
    @y.setter
    def y(self, value : float):
        self._y = value
        
    @z.setter
    def z(self, value : float):
        self._z = value
    
    @xyz.setter
    def xyz(self, values : Iterable):
        values = list(values)
        if len(values) != 3:
            raise ValueError(f"Vector3 requires exactly 3 values, got {len(values)}")
        self._x, self._y, self._z = values

    def __getattr__(self, name: str) -> Union[float, Vector2, Vector3, Vector4, Tuple[float, ...]]:
        try:
            attributes = tuple(self._get_component(char) for char in name)
            length = len(attributes)
            if length == 1:
                return attributes[0]
            types = {2 : Vector2, 3 : Vector3, 4 : Vector4}
            return types.get(length, tuple)(attributes)
        except:
            pass
        if len(attributes) == 0:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        else:
            return attributes
    
    def __setattr__(self, name: str, value: float) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
            return
        for char in name:
            try:
                self._set_component(char, value)
            except:
                object.__setattr__(self, char, value)
    
    def __iter__(self) -> Iterator[float]:
        yield self._x
        yield self._y
        yield self._z

    def __len__(self) -> int:
        return 3

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        elif index == 2:
            return self._z
        else:
            raise IndexError("Vector3 index out of range")

    def __setitem__(self, index: int, value: float):
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value
        elif index == 2:
            self._z = value
        else:
            raise IndexError("Vector3 index out of range")

    def __add__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, Vector3):
            return Vector3(self._x + other.x, self._y + other.y, self._z + other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self._x + other, self._y + other, self._z + other)
        return NotImplemented

    def __radd__(self, other: Union[float, int]) -> "Vector3":
        if isinstance(other, (float, int)):
            return Vector3(self._x + other, self._y + other, self._z + other)
        return NotImplemented

    def __sub__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, Vector3):
            return Vector3(self._x - other.x, self._y - other.y, self._z - other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self._x - other, self._y - other, self._z - other)
        return NotImplemented

    def __rsub__(self, other: Union[float, int]) -> "Vector3":
        if isinstance(other, (float, int)):
            return Vector3(other - self._x, other - self._y, other - self._z)
        return NotImplemented

    def __mul__(
        self, other: Union["Vector3", float, int, "Matrix"]
    ) -> Union["Vector3", Any]:
        from .matrix import (
            Matrix,
        )  # runtime import inside method to avoid circular import

        if isinstance(other, (int, float)):
            return Vector3(self._x * other, self._y * other, self._z * other)
        elif isinstance(other, Vector3):
            return Vector3(self._x * other.x, self._y * other.y, self._z * other.z)
        elif isinstance(other, Matrix):
            if other.cols != 3:
                raise ValueError(
                    f"Cannot multiply Vector3 with Matrix({other.rows}×{other.cols})"
                )
            result = [0.0] * other.rows
            for i in range(other.rows):
                for j in range(other.cols):
                    if j == 0:
                        result[i] += self._x * other.data[i][j]
                    elif j == 1:
                        result[i] += self._y * other.data[i][j]
                    else:
                        result[i] += self._z * other.data[i][j]
            if len(result) == 3:
                return Vector3(result[0], result[1], result[2])
            return result
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            return Vector3(self._x * other, self._y * other, self._z * other)
        return NotImplemented

    def __truediv__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            return Vector3(self._x / other, self._y / other, self._z / other)
        elif isinstance(other, Vector3):
            return Vector3(self._x / other.x, self._y / other.y, self._z / other.z)
        return NotImplemented

    def __rtruediv__(self, other: Union[float, int]) -> "Vector3":
        if isinstance(other, (float, int)):
            return Vector3(other / self._x, other / self._y, other / self._z)
        return NotImplemented

    def __floordiv__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            return Vector3(self._x // other, self._y // other, self._z // other)
        elif isinstance(other, Vector3):
            return Vector3(self._x // other.x, self._y // other.y, self._z // other.z)
        return NotImplemented

    def __rfloordiv__(self, other: Union[float, int]) -> "Vector3":
        if isinstance(other, (float, int)):
            return Vector3(other // self._x, other // self._y, other // self._z)
        return NotImplemented

    def __mod__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            return Vector3(self._x % other, self._y % other, self._z % other)
        elif isinstance(other, Vector3):
            return Vector3(self._x % other.x, self._y % other.y, self._z % other.z)
        return NotImplemented

    def __rmod__(self, other: Union[float, int]) -> "Vector3":
        if isinstance(other, (float, int)):
            return Vector3(other % self._x, other % self._y, other % self._z)
        return NotImplemented

    def __pow__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            return Vector3(self._x**other, self._y**other, self._z**other)
        elif isinstance(other, Vector3):
            return Vector3(self._x**other.x, self._y**other.y, self._z**other.z)
        return NotImplemented

    def __rpow__(self, other: Union[float, int]) -> "Vector3":
        if isinstance(other, (float, int)):
            return Vector3(other**self._x, other**self._y, other**self._z)
        return NotImplemented

    # In-place operations
    def __iadd__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, Vector3):
            self._x += other.x
            self._y += other.y
            self._z += other.z
        elif isinstance(other, (int, float)):
            self._x += other
            self._y += other
            self._z += other
        else:
            return NotImplemented
        return self

    def __isub__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, Vector3):
            self._x -= other.x
            self._y -= other.y
            self._z -= other.z
        elif isinstance(other, (int, float)):
            self._x -= other
            self._y -= other
            self._z -= other
        else:
            return NotImplemented
        return self

    def __imul__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            factor = float(other)
            self._x *= factor
            self._y *= factor
            self._z *= factor
        elif isinstance(other, Vector3):
            self._x *= other.x
            self._y *= other.y
            self._z *= other.z
        else:
            return NotImplemented
        return self

    def __itruediv__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            self._x /= other
            self._y /= other
            self._z /= other
        elif isinstance(other, Vector3):
            self._x /= other.x
            self._y /= other.y
            self._z /= other.z
        else:
            return NotImplemented
        return self

    def __ifloordiv__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            self._x //= other
            self._y //= other
            self._z //= other
        elif isinstance(other, Vector3):
            self._x //= other.x
            self._y //= other.y
            self._z //= other.z
        else:
            return NotImplemented
        return self

    def __imod__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            self._x %= other
            self._y %= other
            self._z %= other
        elif isinstance(other, Vector3):
            self._x %= other.x
            self._y %= other.y
            self._z %= other.z
        else:
            return NotImplemented
        return self

    def __ipow__(self, other: Union["Vector3", float, int]) -> "Vector3":
        if isinstance(other, (int, float)):
            self._x **= other
            self._y **= other
            self._z **= other
        elif isinstance(other, Vector3):
            self._x **= other.x
            self._y **= other.y
            self._z **= other.z
        else:
            return NotImplemented
        return self

    # Comparison
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Vector3):
            return self._x == other.x and self._y == other.y and self._z == other.z
        return NotImplemented

    def __lt__(self, other: Union["Vector3", float, int]) -> bool:
        if isinstance(other, Vector3):
            return self._x < other.x and self._y < other.y and self._z < other.z
        elif isinstance(other, (int, float)):
            return self._x < other and self._y < other and self._z < other
        return NotImplemented

    def __gt__(self, other: Union["Vector3", float, int]) -> bool:
        if isinstance(other, Vector3):
            return self._x > other.x and self._y > other.y and self._z > other.z
        elif isinstance(other, (int, float)):
            return self._x > other and self._y > other and self._z > other
        return NotImplemented

    def __le__(self, other: Union["Vector3", float, int]) -> bool:
        if isinstance(other, Vector3):
            return self._x <= other.x and self._y <= other.y and self._z <= other.z
        elif isinstance(other, (int, float)):
            return self._x <= other and self._y <= other and self._z <= other
        return NotImplemented

    def __ge__(self, other: Union["Vector3", float, int]) -> bool:
        if isinstance(other, Vector3):
            return self._x >= other.x and self._y >= other.y and self._z >= other.z
        elif isinstance(other, (int, float)):
            return self._x >= other and self._y >= other and self._z >= other
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self._x, self._y, self._z))

    def cross(self, other: "Vector3") -> "Vector3":
        """Calculate the cross product with another Vector3"""
        if not isinstance(other, Vector3):
            raise TypeError("Can only calculate cross product with another Vector3")
        return Vector3(
            self._y * other.z - self._z * other.y,
            self._z * other.x - self._x * other.z,
            self._x * other.y - self._y * other.x,
        )


class Vector4(VectorBase["Vector4"]):
    _dimension : int = 4

    def __init__(self, *args):
        self._x : float
        self._y : float
        self._z : float
        self._w : float
        if len(args) == 4:
            self._x, self._y, self._z, self._w = map(float, args)
        elif len(args) == 1 and isinstance(args[0], Union[Iterable, "Vector4"]):
            self._x, self._y, self._z, self._w = map(float, args[0])
        elif len(args) == 1 and isinstance(args[0], Number):
            self._x = self._y = self._z = self._w = float(args[0])
        elif len(args) == 0:
            self._x = self._y = self._z = self._w = 0.0
        else:
            raise TypeError("Invalid arguments for Vector4")

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z
    
    @property
    def w(self) -> float:
        return self._w
    
    @property
    def xyzw(self) -> "Vector4":
        return Vector4(self._x, self._y, self._z, self._w)
    
    @x.setter
    def x(self, value : float):
        self._x = value
    
    @y.setter
    def y(self, value : float):
        self._y = value
        
    @z.setter
    def z(self, value : float):
        self._z = value
        
    @w.setter
    def w(self, value : float):
        self._w = value
    
    @xyzw.setter
    def xyzw(self, values : Iterable):
        values = list(values)
        if len(values) != 4:
            raise ValueError(f"Vector4 requires exactly 4 values, got {len(values)}")
        self._x, self._y, self._z, self._w = values
    
    def __getattr__(self, name: str) -> Union[float, Vector2, Vector3, Vector4, Tuple[float, ...]]:
        try:
            attributes = tuple(self._get_component(char) for char in name)
            length = len(attributes)
            if length == 1:
                return attributes[0]
            types = {2 : Vector2, 3 : Vector3, 4 : Vector4}
            return types.get(length, tuple)(attributes)
        except:
            pass
        if len(attributes) == 0:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        else:
            return attributes
    
    def __setattr__(self, name: str, value: float) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
            return
        for char in name:
            try:
                self._set_component(char, value)
            except:
                object.__setattr__(self, char, value)

    def __iter__(self) -> Iterator[float]:
        yield self._x
        yield self._y
        yield self._z
        yield self._w

    def __len__(self) -> int:
        return 4

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        elif index == 2:
            return self._z
        elif index == 3:
            return self._w
        else:
            raise IndexError("Vector4 index out of range")

    def __setitem__(self, index: int, value: float):
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value
        elif index == 2:
            self._z = value
        elif index == 3:
            self._w = value
        else:
            raise IndexError("Vector4 index out of range")

    def __add__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, Vector4):
            return Vector4(
                self._x + other.x, self._y + other.y, self._z + other.z, self._w + other.w
            )
        elif isinstance(other, (float, int)):
            return Vector4(
                self._x + other, self._y + other, self._z + other, self._w + other
            )
        return NotImplemented

    def __radd__(self, other: Union[float, int]) -> "Vector4":
        if isinstance(other, (float, int)):
            return Vector4(
                self._x + other, self._y + other, self._z + other, self._w + other
            )
        return NotImplemented

    def __sub__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, Vector4):
            return Vector4(
                self._x - other.x, self._y - other.y, self._z - other.z, self._w - other.w
            )
        elif isinstance(other, (float, int)):
            return Vector4(
                self._x - other, self._y - other, self._z - other, self._w - other
            )
        return NotImplemented

    def __rsub__(self, other: Union[float, int]) -> "Vector4":
        if isinstance(other, (float, int)):
            return Vector4(
                other - self._x, other - self._y, other - self._z, other - self._w
            )
        return NotImplemented

    def __mul__(
        self, other: Union["Vector4", float, int, "Matrix"]
    ) -> Union["Vector4", Any]:
        from .matrix import (
            Matrix,
        )  # runtime import inside method to avoid circular import

        if isinstance(other, (int, float)):
            return Vector4(
                self._x * other, self._y * other, self._z * other, self._w * other
            )
        elif isinstance(other, Vector4):
            return Vector4(
                self._x * other.x, self._y * other.y, self._z * other.z, self._w * other.w
            )
        elif isinstance(other, Matrix):
            if other.cols != 4:
                raise ValueError(
                    f"Cannot multiply Vector4 with Matrix({other.rows}×{other.cols})"
                )
            result = [0.0] * other.rows
            for i in range(other.rows):
                for j in range(other.cols):
                    if j == 0:
                        result[i] += self._x * other.data[i][j]
                    elif j == 1:
                        result[i] += self._y * other.data[i][j]
                    elif j == 2:
                        result[i] += self._z * other.data[i][j]
                    else:
                        result[i] += self._w * other.data[i][j]
            if len(result) == 4:
                return Vector4(result[0], result[1], result[2], result[3])
            return result
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            return Vector4(
                self._x * other, self._y * other, self._z * other, self._w * other
            )
        return NotImplemented

    def __truediv__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            return Vector4(
                self._x / other, self._y / other, self._z / other, self._w / other
            )
        elif isinstance(other, Vector4):
            return Vector4(
                self._x / other.x, self._y / other.y, self._z / other.z, self._w / other.w
            )
        return NotImplemented

    def __rtruediv__(self, other: Union[float, int]) -> "Vector4":
        if isinstance(other, (float, int)):
            return Vector4(
                other / self._x, other / self._y, other / self._z, other / self._w
            )
        return NotImplemented

    def __floordiv__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            return Vector4(
                self._x // other, self._y // other, self._z // other, self._w // other
            )
        elif isinstance(other, Vector4):
            return Vector4(
                self._x // other.x,
                self._y // other.y,
                self._z // other.z,
                self._w // other.w,
            )
        return NotImplemented

    def __rfloordiv__(self, other: Union[float, int]) -> "Vector4":
        if isinstance(other, (float, int)):
            return Vector4(
                other // self._x, other // self._y, other // self._z, other // self._w
            )
        return NotImplemented

    def __mod__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            return Vector4(
                self._x % other, self._y % other, self._z % other, self._w % other
            )
        elif isinstance(other, Vector4):
            return Vector4(
                self._x % other.x, self._y % other.y, self._z % other.z, self._w % other.w
            )
        return NotImplemented

    def __rmod__(self, other: Union[float, int]) -> "Vector4":
        if isinstance(other, (float, int)):
            return Vector4(
                other % self._x, other % self._y, other % self._z, other % self._w
            )
        return NotImplemented

    def __pow__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            return Vector4(self._x**other, self._y**other, self._z**other, self._w**other)
        elif isinstance(other, Vector4):
            return Vector4(
                self._x**other.x, self._y**other.y, self._z**other.z, self._w**other.w
            )
        return NotImplemented

    def __rpow__(self, other: Union[float, int]) -> "Vector4":
        if isinstance(other, (float, int)):
            return Vector4(other**self._x, other**self._y, other**self._z, other**self._w)
        return NotImplemented

    # In-place operations
    def __iadd__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, Vector4):
            self._x += other.x
            self._y += other.y
            self._z += other.z
            self._w += other.w
        elif isinstance(other, (int, float)):
            self._x += other
            self._y += other
            self._z += other
            self._w += other
        else:
            return NotImplemented
        return self

    def __isub__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, Vector4):
            self._x -= other.x
            self._y -= other.y
            self._z -= other.z
            self._w -= other.w
        elif isinstance(other, (int, float)):
            self._x -= other
            self._y -= other
            self._z -= other
            self._w -= other
        else:
            return NotImplemented
        return self

    def __imul__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            self._x *= other
            self._y *= other
            self._z *= other
            self._w *= other
        elif isinstance(other, Vector4):
            self._x *= other.x
            self._y *= other.y
            self._z *= other.z
            self._w *= other.w
        else:
            return NotImplemented
        return self

    def __itruediv__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            self._x /= other
            self._y /= other
            self._z /= other
            self._w /= other
        elif isinstance(other, Vector4):
            self._x /= other.x
            self._y /= other.y
            self._z /= other.z
            self._w /= other.w
        else:
            return NotImplemented
        return self

    def __ifloordiv__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            self._x //= other
            self._y //= other
            self._z //= other
            self._w //= other
        elif isinstance(other, Vector4):
            self._x //= other.x
            self._y //= other.y
            self._z //= other.z
            self._w //= other.w
        else:
            return NotImplemented
        return self

    def __imod__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            self._x %= other
            self._y %= other
            self._z %= other
            self._w %= other
        elif isinstance(other, Vector4):
            self._x %= other.x
            self._y %= other.y
            self._z %= other.z
            self._w %= other.w
        else:
            return NotImplemented
        return self

    def __ipow__(self, other: Union["Vector4", float, int]) -> "Vector4":
        if isinstance(other, (int, float)):
            self._x **= other
            self._y **= other
            self._z **= other
            self._w **= other
        elif isinstance(other, Vector4):
            self._x **= other.x
            self._y **= other.y
            self._z **= other.z
            self._w **= other.w
        else:
            return NotImplemented
        return self

    # Comparison
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Vector4):
            return (
                self._x == other.x
                and self._y == other.y
                and self._z == other.z
                and self._w == other.w
            )
        return NotImplemented

    def __lt__(self, other: Union["Vector4", float, int]) -> bool:
        if isinstance(other, Vector4):
            return (
                self._x < other.x
                and self._y < other.y
                and self._z < other.z
                and self._w < other.w
            )
        elif isinstance(other, (int, float)):
            return (
                self._x < other and self._y < other and self._z < other and self._w < other
            )
        return NotImplemented

    def __gt__(self, other: Union["Vector4", float, int]) -> bool:
        if isinstance(other, Vector4):
            return (
                self._x > other.x
                and self._y > other.y
                and self._z > other.z
                and self._w > other.w
            )
        elif isinstance(other, (int, float)):
            return (
                self._x > other and self._y > other and self._z > other and self._w > other
            )
        return NotImplemented

    def __le__(self, other: Union["Vector4", float, int]) -> bool:
        if isinstance(other, Vector4):
            return (
                self._x <= other.x
                and self._y <= other.y
                and self._z <= other.z
                and self._w <= other.w
            )
        elif isinstance(other, (int, float)):
            return (
                self._x <= other
                and self._y <= other
                and self._z <= other
                and self._w <= other
            )
        return NotImplemented

    def __ge__(self, other: Union["Vector4", float, int]) -> bool:
        if isinstance(other, Vector4):
            return (
                self._x >= other.x
                and self._y >= other.y
                and self._z >= other.z
                and self._w >= other.w
            )
        elif isinstance(other, (int, float)):
            return (
                self._x >= other
                and self._y >= other
                and self._z >= other
                and self._w >= other
            )
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self._x, self._y, self._z, self._w))


# Provide convenient aliases
Vec2 = Vector2
vec2 = Vector2
Vec3 = Vector3
vec3 = Vector3
Vec4 = Vector4
vec4 = Vector4


# Add utility functions for conversion between different vector dimensions
def vec2_to_vec3(v: Vector2, z: float = 0.0) -> Vector3:
    """Convert a Vector2 to a Vector3 by adding the z component"""
    return Vector3(v.x, v.y, z)


def vec2_to_vec4(v: Vector2, z: float = 0.0, w: float = 1.0) -> Vector4:
    """Convert a Vector2 to a Vector4 by adding the z and w components"""
    return Vector4(v.x, v.y, z, w)


def vec3_to_vec2(v: Vector3) -> Vector2:
    """Convert a Vector3 to a Vector2 by dropping the z component"""
    return Vector2(v.x, v.y)


def vec3_to_vec4(v: Vector3, w: float = 1.0) -> Vector4:
    """Convert a Vector3 to a Vector4 by adding the w component"""
    return Vector4(v.x, v.y, v.z, w)


def vec4_to_vec2(v: Vector4) -> Vector2:
    """Convert a Vector4 to a Vector2 by dropping the z and w components"""
    return Vector2(v.x, v.y)


def vec4_to_vec3(v: Vector4) -> Vector3:
    """Convert a Vector4 to a Vector3 by dropping the w component"""
    return Vector3(v.x, v.y, v.z)