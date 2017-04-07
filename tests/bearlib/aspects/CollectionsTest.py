import pytest

from coalib.bearlib.aspects.collections import aspectlist
from coalib.bearlib.aspects.Metadata import Metadata


class aspectlistTest:

    def test__init__(self):
        with pytest.raises(TypeError) as exc:
            aspectlist(['String'])
        exc.match("'String' is not an aspectclass or "
                  'an instance of an aspectclass')

    def test__contains__(self):
        list_of_aspect = aspectlist(
            [Metadata.CommitMessage.Shortlog, Metadata.CommitMessage.Body])
        assert Metadata.CommitMessage.Shortlog in list_of_aspect
        assert Metadata.CommitMessage.Shortlog.ColonExistence in list_of_aspect
        assert Metadata.CommitMessage.Body in list_of_aspect
        assert Metadata not in list_of_aspect
        assert Metadata.CommitMessage.Emptiness not in list_of_aspect

        with pytest.raises(TypeError) as exc:
            'Metadata.CommitMessage.Shortlog' in list_of_aspect
        exc.match("'Metadata.CommitMessage.Shortlog' is not an "
                  'aspectclass or an instance of an aspectclass')
        with pytest.raises(TypeError) as exc:
            str in list_of_aspect
        exc.match("<class 'str'> is not an "
                  'aspectclass or an instance of an aspectclass')
