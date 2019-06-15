import re
from collections import defaultdict
from copy import deepcopy

_VALID_SHORT_NAME = re.compile("-[a-zA-Z]")
_VALID_LONG_NAME = re.compile("--(?!-)[-a-zA-Z]+")


def _norm_option_name(opt_name: str) -> str:
    assert opt_name is not None
    return opt_name.strip()


def _default_option_long_name(opt_name: str) -> str:
    opt_name = _norm_option_name(opt_name)
    return "--" + opt_name.lower().replace(" ", "-")


def _default_option_short_name(opt_name: str) -> str:
    opt_name = _norm_option_name(opt_name)
    first_char = opt_name[0]
    assert first_char.isalpha(), "first character not a letter"
    return "-" + opt_name[0]


class Option:
    def __init__(
        self,
        value_type: type = str,
        default_value=None,
        short_name: str = None,
        long_name: str = None,
        optional: bool = True,
    ):
        self.value_type = value_type
        self.default_value = default_value
        self.short_name = short_name and _default_option_long_name(short_name)
        self.long_name = long_name and _default_option_short_name(long_name)

        assert self.long_name is not None or self.short_name is not None
        self.optional = optional
        self.name = None
        self.arguments = []

    def matches(self, word):
        return word in (self.long_name, self.short_name)


class Parser:
    def __init__(self, cls):
        public_members = {
            m: getattr(cls, m) for m in vars(cls) if not m.startswith("_")
        }
        options = {
            m: v for m, v in public_members.items() if isinstance(v, Option)
        }
        self.options = deepcopy(options)
        self.expecting_arguments_for = None

    def __call__(self, argv):
        arguments = defaultdict(list)
        for word in argv:
            if self.expecting_arguments_for is not None:
                pass
            option_name = self._find_option(word)
            if option_name is None:
                ...
            else:
                ...

    def _find_option(self, word):
        for option_name, option in self.options.items():
            if word in [option.long_name, option.short_name]:
                return option_name
        return None


def cli(cls):
    return Parser(cls)
