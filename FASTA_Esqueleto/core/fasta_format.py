import sys
from fasta import load_fasta, write_fasta # función que hicimos para leer
from formatter import CaseOption, format_sequence
from argsparser import parse_args, validate_args_count_and_names
from transformations import RenameDuplicatedSequencesTransformation


def main():
    args = parse_args(sys.argv[1:])
    validate_args_count_and_names(args, ['input', 'output'])

    input_path = args['input']
    output_path = args['output']
    case_str = args.get('case', 'original')
    
    try:
        max_length = int(args.get('max_length', '0'))
        if max_length < 0:
            raise ValueError("El valor de --max-length debe ser mayor o igual a 0.")
    except ValueError as e:
        print(f"Error: {e}")
    exit(1)

    # Convertir el string del argumento a CaseOption
    case_map = {
        'original': CaseOption.ORIGINAL,
        'upper': CaseOption.UPPER,
        'lower': CaseOption.LOWER
    }

    case = case_map.get(case_str.lower(), CaseOption.ORIGINAL)

    # Leer el fichero de entrada
    sequences = load_fasta(input_path)

    # Renombrar las secuencias con identificadores duplicados
    transformer = RenameDuplicatedSequencesTransformation()
    sequences = transformer.transform(sequences)
    
    # Escribir el fichero de salida
    write_fasta(sequences, output_path, case=case, max_length=max_length)


if __name__ == '__main__':
    main()
