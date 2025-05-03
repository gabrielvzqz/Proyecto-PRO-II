import sys
from core.fasta import load_fasta, write_fasta # función que hicimos para leer
from core.formatter import CaseOption, format_sequence
from argsparser import parse_args


def main():
    args = parse_args(sys.argv[1:])

    input_path = args['input']
    output_path = args['output']
    case_str = args.get('case', 'original')
    max_length = int(args.get('max_length', '0'))

    # Convertir el string del argumento a CaseOption
    case_map = {
        'original': CaseOption.ORIGINAL,
        'upper': CaseOption.UPPER,
        'lower': CaseOption.LOWER
    }

    case = case_map.get(case_str.lower(), CaseOption.ORIGINAL)

    # Leer el fichero de entrada
    sequences = load_fasta(input_path)

    # Escribir el fichero de salida
    write_fasta(sequences, output_path, case=case, max_length=max_length)


if __name__ == '__main__':
    main()
