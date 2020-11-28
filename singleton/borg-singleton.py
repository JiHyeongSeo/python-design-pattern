class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class Child(Borg):
    pass

class AnotherChild(Borg):
    _shared_state = {}

if __name__ == "__main__":
    borg = Borg()
    another_borg = Borg()
    print(f"borg is another_borg : {borg is another_borg}")

    child = Child()
    borg.only_one_var = "I'm ther only one var"
    print(f"child.only_one_var: {child.only_one_var}")

    another_child = AnotherChild()
    print(f"another_child.only_one_var: {another_child.only_one_var}")