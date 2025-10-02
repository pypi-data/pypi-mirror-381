# file sage/core/sage.middleware.services.neuromem./search_engine/kv_index/base_kv_index.py

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseKVIndex(ABC):
    def __init__(
        self,
        config: Optional[dict] = None,
        texts: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
    ):
        """
        初始化索引基类。
        Initialize the base class for KV Index.
        """
        self.config = config or {}
        self.name = self.config.get("name", None)

    @abstractmethod
    def insert(self, text: str, id: str) -> None:
        """
        插入一条新数据。
        Insert a new entry.
        """
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """
        删除指定id的数据。
        Delete an entry by id.
        """
        pass

    @abstractmethod
    def search(self, query: str, topk: int = 10) -> List[str]:
        """
        检索相关数据，返回最相关的id列表。
        Search for relevant entries and return the most relevant ids.
        """
        pass

    @abstractmethod
    def update(self, id: str, new_text: str) -> None:
        """
        更新指定id的数据内容。
        Update the entry corresponding to the given id.
        """
        pass

    @classmethod
    @abstractmethod
    def load(cls, name: str, root_path: str) -> "BaseKVIndex":
        """
        加载索引实例。
        Load the index instance.
        """
        pass

    @abstractmethod
    def store(self, root_path: str) -> Dict[str, Any]:
        """
        存储索引数据到指定目录。
        Store the index data to the specified directory.
        """
        pass

    @staticmethod
    @abstractmethod
    def clear(dir_path: str) -> None:
        """
        删除指定目录下的所有索引数据。
        Remove all index data under the specified directory.
        """
        pass
