# Renombra los identificadores (S1, S2...) que estén duplicados

import sys
from fasta import load_fasta, write_fasta
from formatter import CaseOption, format_sequence
from argsparser import parse_args
from sequences import Sequence


# Clase para renombrar identificadores duplicados
class RenameDuplicatedSequencesTransformation:
    def __init__(self):
        pass

    def transform(self, sequences):
        from collections import defaultdict
        # Primera pasada: contar ocurrencias
        count_map = defaultdict(int)
        for seq in sequences:
            count_map[seq.get_id()] += 1

        # Segunda pasada: renombrar si hay duplicados
        current_count = defaultdict(int)
        transformed = []

        for seq in sequences:
            identifier = seq.get_id()
            seq_data = seq.get_secuencia()

            if count_map[identifier] == 1:
                # Solo aparece una vez, lo dejamos como está
                new_identifier = identifier
            else:
                # Aparece varias veces, añadimos sufijo
                current_count[identifier] += 1
                new_identifier = f"{identifier}.{current_count[identifier]}"

            transformed.append(Sequence(new_identifier, seq_data))

        return transformed
    