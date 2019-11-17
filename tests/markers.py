import pytest
from _pytest.mark import MarkDecorator

smoke: MarkDecorator = pytest.mark.smoke
unittest: MarkDecorator = pytest.mark.unittest
