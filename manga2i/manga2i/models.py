from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class TagAttributes:
    name: Dict[str, str]
    description: Dict[str, str]
    group: str
    version: int

@dataclass
class Tag:
    id: str
    type: str
    attributes: TagAttributes

@dataclass
class Attributes:
    title: str
    description: str
    originalLanguage: str
    lastVolume: Optional[str]
    lastChapter: Optional[str]
    publicationDemographic: str
    status: str
    year: int
    grade: float
    tags: List[Tag]
    availableTranslatedLanguages: List[str]
    url_cover: str

@dataclass
class Manga:
    id: str
    type: str
    attributes: Attributes