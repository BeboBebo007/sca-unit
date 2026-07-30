from sca_unit import StructuralState, assess_structures

first = StructuralState(
    identity="baseline",
    nodes={"api", "database"},
    edges={("api", "database")},
)

second = StructuralState(
    identity="changed",
    nodes={"api", "cache"},
    edges={("api", "cache")},
)

result = assess_structures(first, second)

print("SCA-Unit structural assessment example")
print("first_identity:", result.first_identity)
print("second_identity:", result.second_identity)
print("node_similarity:", result.node_similarity)
print("edge_similarity:", result.edge_similarity)
print("compatibility:", result.compatibility)
print("conflict:", result.conflict)
print("verdict:", result.verdict)