
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    singleton = Singleton()
    another_singleton = Singleton()
    print(f"singleton is another_singleton: {singleton is another_singleton}")
    singleton.only_one_var = "I'm only one var"
    print(f"another_singleton.only_one_var: {another_singleton.only_one_var}")