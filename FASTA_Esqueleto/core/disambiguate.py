# Junta todo el resto de clases

import sys
from fasta import load_fasta, write_fasta
from transformations import RenameDuplicatedSequencesTransformation
from formatter import CaseOption
from argsparser import parse_args, validate_args_count_and_names

def main():
    args = parse_args(sys.argv[1:])
    validate_args_count_and_names(args, ['input', 'output'])

    input_path = args['input']
    output_path = args['output']

    # Leer secuencias desde el archivo FASTA
    sequences = load_fasta(input_path)

    # Renombrar identificadores duplicados
    transformer = RenameDuplicatedSequencesTransformation()
    sequences = transformer.transform(sequences)

    # Escribir las secuencias transformadas al archivo de salida
    write_fasta(sequences, output_path, case=CaseOption.ORIGINAL, max_length=0)

if __name__ == '__main__':
    main()
