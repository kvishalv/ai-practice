from problems.lru_cache.src.cache import LRUCache


def test_get_missing_key_returns_minus_one() -> None:
    cache = LRUCache(2)
    assert cache.get(99) == -1


def test_put_and_get() -> None:
    cache = LRUCache(2)
    cache.put(1, 10)
    assert cache.get(1) == 10


def test_eviction_of_least_recently_used_item() -> None:
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.get(1)
    cache.put(3, 30)

    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 30


def test_updating_existing_key_moves_it_to_front() -> None:
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(1, 15)
    cache.put(3, 30)

    assert cache.get(1) == 15
    assert cache.get(2) == -1
