from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import configparser

SECTIONS = {'legacy', 'not-web-essential', 'equivalent-api'}
BUG_URIS = {'rdar://', 'https://bugs.webkit.org'}

@dataclass
class AllowList:
    allowed: list[str]

    @classmethod
    def from_configparser(cls, parser: configparser.ConfigParser) -> AllowList:
        allowed = []
        for section in parser:
            assert section in SECTIONS or \
                any(section.startswith(uri) for uri in BUG_URIS), \
                f'Unrecognized allowlist section name "{section}"'
            for name, _ in parser.items(section, raw=True):
                allowed.append(name)
        return cls(allowed)

    @classmethod
    def from_files(cls, *files: list[Path]) -> AllowList:
        parser = configparser.ConfigParser(allow_no_value=True,
                                           delimiters=('=',))
        parser.read(*map(str, files))
        return  cls.from_configparser(parser)
