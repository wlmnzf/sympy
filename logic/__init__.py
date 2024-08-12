from .boolalg import (to_cnf, to_dnf, to_nnf, And, Or, Not, Xor, Nand, Nor, Implies,
    Equivalent, ITE, POSform, SOPform, simplify_logic, bool_map, true, false,
    gateinputcount,BelongsRel,ContainsRel)
from .inference import satisfiable

__all__ = [
    'to_cnf', 'to_dnf', 'to_nnf', 'And', 'Or', 'Not', 'Xor', 'Nand', 'Nor',
    'Implies', 'Equivalent', 'ITE', 'POSform', 'SOPform', 'simplify_logic',
    'bool_map', 'true', 'false', 'gateinputcount','BelongsRel','ContainsRel',

    'satisfiable',
]
