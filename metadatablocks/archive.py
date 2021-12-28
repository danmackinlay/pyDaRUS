# generated by datamodel-codegen:
#   filename:  archive.json
#   timestamp: 2021-12-28T01:04:36+00:00

from __future__ import annotations

from typing import Optional

from easyDataverse.core import DataverseBase
from pydantic import Field


class Archive(DataverseBase):
    active_until: Optional[str] = Field(
        None,
        description='A date (YYYY-MM-DD) up to which the data set is in the active state',
        multiple=False,
        typeClass='primitive',
        typeName='archiveActiveUntil',
    )
    archived_from: Optional[str] = Field(
        None,
        description='A date (YYYY-MM-DD) from whith the data set is archived',
        multiple=False,
        typeClass='primitive',
        typeName='archiveArchivedFrom',
    )
    archived_for: Optional[str] = Field(
        None,
        description='The period for which the record is to be archived. ',
        multiple=False,
        typeClass='controlledVocabulary',
        typeName='archiveArchivedFor',
    )
    archived_at: Optional[str] = Field(
        None,
        description='The location where the files are archived',
        multiple=True,
        typeClass='primitive',
        typeName='archiveArchivedAt',
    )
    _metadatablock_name: Optional[str] = 'archive'
