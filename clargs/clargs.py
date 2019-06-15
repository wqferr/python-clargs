def _norm_option_name(opt_name: str) -> str:
    return opt_name.strip().lower()


def _default_option_long_name(opt_name: str) -> str:
    opt_name = _norm_option_name(opt_name)
    return "--" + opt_name.replace(" ", "-")


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
        self.short_name = _default_option_long_name(short_name)
        self.long_name = _default_option_short_name(long_name)
        self.optional = optional


def cli(cls):
    public_members = {
        m: getattr(cls, m) for m in vars(cls) if not m.startswith("_")
    }
    options = {m: v for m, v in public_members.items() if not callable(v)}
    print(options)

    return cls
