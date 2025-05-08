from enum import Enum

class CaseOption(Enum):
    ORIGINAL = 'original'
    UPPER = 'upper'
    LOWER = 'lower'


def format_sequence(sequence_obj, case=CaseOption.ORIGINAL, max_length=0) -> str:
    seq = sequence_obj.get_secuencia()

    # Aplicar o formato de letras
    if case == CaseOption.UPPER:
        seq = seq.upper()
    elif case == CaseOption.LOWER:
        seq = seq.lower()
    # Se é ORIGINAL, non se fai nada

    # Dividir en liñas segundo o max_length
    if max_length > 0:
        seq_lines = [seq[i:i+max_length] for i in range(0, len(seq), max_length)]
        formatted_seq = '\n'.join(seq_lines)
    else:
        formatted_seq = seq

    return f">{sequence_obj.get_id()}\n{formatted_seq}"

# Exemplo de uso
if __name__ == '__main__':
    from sequences import Sequence  # Asegúrate de que a clase está dispoñible

    s = Sequence("S1", "ACTGATCGTTGCA")
    print(format_sequence(s, case=CaseOption.LOWER, max_length=4))
    print()
    print(format_sequence(s, case=CaseOption.ORIGINAL, max_length=0))
