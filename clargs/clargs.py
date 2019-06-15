import inspect


def cli(cls):
    public_members = {
        m: getattr(cls, m) for m in vars(cls) if not m.startswith("_")
    }
    options = {m: v for m, v in public_members.items() if not callable(v)}
    print(options)

    return cls
