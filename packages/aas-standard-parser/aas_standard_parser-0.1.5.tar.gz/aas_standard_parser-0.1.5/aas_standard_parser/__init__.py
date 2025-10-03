from datetime import datetime
import importlib.metadata

# TODO: introduce MIT license
__copyright__ = f"Copyright (C) {datetime.now().year} :em engineering methods AG. All rights reserved."
__author__ = "Daniel Klein, Celina Adelhardt, Tom Gneuß"

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev"
    
__project__ = "aas-standard-parser"
__package__ = "aas-standard-parser"

from aas_standard_parser.aimc_parser import AIMCParser
from aas_standard_parser.aid_parser import AIDParser


__all__ = ["AIMCParser", "AIDParser"]
