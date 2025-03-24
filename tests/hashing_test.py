def test_clock_id_hash_basics(
    clock_id_test1, clock_id_test2, clock_id_other, clock_id_empty
):
    assert clock_id_test1 == clock_id_test2
    assert clock_id_test1 != clock_id_other
    assert clock_id_test1 != clock_id_empty
    assert hash(clock_id_test1) == hash(clock_id_test2)

    # Not true for all possible clock IDs (hashes can clash), but likely (and deterministic).
    assert hash(clock_id_test1) != hash(clock_id_other)


def test_port_id_hash_basics(port_id_domain0, port_id_domain1):
    assert port_id_domain0 != port_id_domain1
    assert hash(port_id_domain0) != hash(port_id_domain1)


def test_clock_id_collections(
    clock_id_test1, clock_id_test2, clock_id_other, clock_id_empty
):
    mapping = {clock_id_test1: "a", clock_id_other: "b", clock_id_empty: "c"}

    assert len(mapping) == 3
    assert mapping[clock_id_test1] == "a"
    assert mapping[clock_id_test2] == "a"


def test_port_id_collection(port_id_domain0, port_id_domain1):
    mapping = {port_id_domain0: "a", port_id_domain1: "b"}

    assert len(mapping) == 2
    assert mapping[port_id_domain0] == "a"
