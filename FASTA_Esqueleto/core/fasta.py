# Carga y lee un archivo y lo escribe en un nuevo archivo

from sequences import Sequence
from formatter import CaseOption

def load_fasta(filepath: str) -> list:
    sequences = []
    with open(filepath, 'r') as file:
        identifier = None
        seq_lines = []

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if identifier is not None:
                    sequences.append(Sequence(identifier, ''.join(seq_lines)))
                identifier = line[1:]
                seq_lines = []
            else:
                seq_lines.append(line)

        if identifier is not None:
            sequences.append(Sequence(identifier, ''.join(seq_lines)))

    return sequences


def write_fasta(sequences, filepath, case, max_length):
    from formatter import format_sequence  # evitar import circular

    with open(filepath, 'w') as f:
        for seq in sequences:
            formatted = format_sequence(seq, case=case, max_length=max_length)
            f.write(formatted + '\n')


if __name__ == '__main__':
    from sequences import Sequence

    seqs = [
        Sequence("S1", "ACGTACGTACGT"),
        Sequence("S2", "TTGGAACC")
    ]
    write_fasta(seqs, 'salida.fasta', case=CaseOption.UPPER, max_length=4)
   
    fasta_file = 'Fasta_Esqueleto/core/test_data/test_1.fasta'
    seqs = load_fasta(fasta_file)
    for seq in seqs:
        print(seq)
