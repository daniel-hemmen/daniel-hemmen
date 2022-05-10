def get_int(i=''):
    # prompt until input is positive int
    while True:
        try:
            n = int(input(i))
        except ValueError:
            continue
        else:
            if n <= 0:
                continue
            else:
                return n
