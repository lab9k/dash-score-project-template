from dataclasses import dataclass
from typing import List
import pkgutil


@dataclass
class PathUtil:
    pieces: List[str]
    children: List['PathUtil']

    def fs_path(self) -> str:
        return join_path(*self.pieces)

    def mod_path(self) -> str:
        return join_mod(*self.pieces)

    def is_page(self) -> bool:
        return 'layout' in self.pieces

    def url(self) -> str:
        pieces = self.pieces.copy()
        if 'pages' in pieces:
            pieces.remove('pages')
        if 'layout' in pieces:
            pieces.remove('layout')
        return join_path('', *pieces)

    def append_piece(self, piece: str):
        self.pieces.append(piece)

    def prepend_piece(self, piece: str):
        self.pieces.insert(0, piece)


def find_module_names_in_path(path: PathUtil) -> List[str]:
    return [name for _, name, _ in pkgutil.iter_modules([path.fs_path()])]


def join_path(*parts: str) -> str:
    return '/'.join(parts)


def join_mod(*parts: str) -> str:
    return '.'.join(parts)


def walk_package(name: str) -> List[PathUtil]:
    packages = pkgutil.walk_packages([name])
    return [PathUtil([loader.path.split('/')[-1], name], []) for loader, name, _ in packages]
