from contextlib import contextmanager


class FediRequestCache:
    def __init__(self):
        self.url = None
        self.id = None

    def get(self, key: str, fallback: callable):
        return self.find_cached_result(key, fallback)

    def find_cached_result(self, key, fallback):
        msg = "this should be overwritten by a child class"
        raise NotImplementedError(msg)


# this is used in spov
@contextmanager
def temp_setting(obj, attr, value):
    """
    # Usage:
    with temp_setting(fedivis.settings, 'AUX_NODE_MIN_NUM_LEVEL_N_LEAVES', 2):
        self.assertEqual(b1.evaluate_script("currentActiveNode.id"), "node1")
    """
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, original)
