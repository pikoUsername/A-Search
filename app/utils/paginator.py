from dataclasses import dataclass
from typing import List


@dataclass
class Paginator:
    __slots__ = (
        "xs_to_parts",
        "data", "get_page_by_id",
        "get_all_page_id", "page_to_devide",
        "group_by_count",
    )

    data: str
    pages_to_devide: int = 5
    __sorted_data: List[str] = None

    @classmethod
    def xs_to_parts(cls):
        devide = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]

        cls.__sorted_data = devide(cls.data, cls.pages_to_devide)

    @classmethod
    def group_by_count(cls, dic: dict, size: int):
        output, temp, count = [], {}, 0
        for k, v in dic.items():
            for x in v:
                if count == size:
                    output.append(temp)
                    temp, count = {}, 0
                temp[k] = temp.get(k, []) + [x]
                count += 1
        if temp:
            output.append(temp)
        cls.__sorted_data = output

    def get_page_by_id(self, _id: int):
        if _id < 0:
            raise TypeError("ID More Than 0")

        try:
            return self.__sorted_data[_id]
        except IndexError:
            return self.get_page_by_id(_id - 1)

    @property
    def get_all_page_id(self) -> List[int]:
        return list(range(len(self.__sorted_data)))
