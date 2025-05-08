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

if __name__ == '__main__':
    print(parse_args(['--test=a']))
    print(parse_args(['--test=a', '--test_2=b']))
    print(parse_args(['--test=a', '--test_2=b', ' --test_lag']))