import pytest

from sca_unit import StructuralState, assess_structures


def test_identical_structures() -> None:
    first = StructuralState.create(
        identity="state-a",
        nodes=["A", "B", "C"],
        edges=[("A", "B"), ("B", "C")],
    )

    second = StructuralState.create(
        identity="state-b",
        nodes=["A", "B", "C"],
        edges=[("A", "B"), ("B", "C")],
    )

    result = assess_structures(first, second)

    assert result.compatibility == pytest.approx(1.0)
    assert result.conflict == pytest.approx(0.0)
    assert result.verdict == "identical"


def test_partially_compatible_structures() -> None:
    first = StructuralState.create(
        identity="state-a",
        nodes=["A", "B", "C"],
        edges=[("A", "B"), ("B", "C")],
    )

    second = StructuralState.create(
        identity="state-b",
        nodes=["B", "C", "D"],
        edges=[("B", "C"), ("C", "D")],
    )

    result = assess_structures(first, second)

    assert 0.0 < result.compatibility < 1.0
    assert result.conflict == pytest.approx(0.0)
    assert result.verdict == "partial"


def test_conflicting_shared_structure() -> None:
    first = StructuralState.create(
        identity="state-a",
        nodes=["A", "B", "C"],
        edges=[("A", "B"), ("B", "C")],
    )

    second = StructuralState.create(
        identity="state-b",
        nodes=["A", "B", "C"],
        edges=[("A", "C")],
    )

    result = assess_structures(first, second)

    assert result.conflict == pytest.approx(1.0)
    assert result.verdict == "conflicting"


def test_unrelated_structures() -> None:
    first = StructuralState.create(
        identity="state-a",
        nodes=["A", "B"],
        edges=[("A", "B")],
    )

    second = StructuralState.create(
        identity="state-b",
        nodes=["X", "Y"],
        edges=[("X", "Y")],
    )

    result = assess_structures(first, second)

    assert result.compatibility == pytest.approx(0.0)
    assert result.verdict == "unrelated"


def test_rejects_unknown_edge_nodes() -> None:
    with pytest.raises(ValueError):
        StructuralState.create(
            identity="invalid",
            nodes=["A"],
            edges=[("A", "B")],
        )