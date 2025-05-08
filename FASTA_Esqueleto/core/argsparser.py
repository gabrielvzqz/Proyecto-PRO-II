def parse_args(args):
    toret = {}
    for arg in args:
        args_split = arg.split('=')
        name = args_split[0].replace('--', '')

        if len(args_split) == 2:
            toret[name] = args_split[1]
        else:
            toret[name] = True
    
    return toret
def validate_args_count_and_names(args_dict, expected_keys):
    if len(args_dict) < len(expected_keys):
        print(f"Error: Faltan argumentos. Se esperaban: {', '.join(expected_keys)}.")
        exit(1)

    for key in expected_keys:
        if key not in args_dict:
            print(f"Error: El argumento '--{key}' es obligatorio.")
            exit(1)

if __name__ == '__main__':
    print(parse_args(['--test=a']))
    print(parse_args(['--test=a', '--test_2=b']))
    print(parse_args(['--test=a', '--test_2=b', ' --test_lag']))