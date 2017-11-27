"""

Write helper function if the code gets visual noise so the reader will easily understand what's going on even if
the implementation itself gets complicated.


"""


from urllib.parse import parse_qs



def get_parsed_qs(qs):
    values = parse_qs(qs, keep_blank_values=True)
    return values


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found




if __name__ == '__main__':
    qs = 'red=5&blue=0&green='
    p_qs = get_parsed_qs(qs)
    print(get_first_int(p_qs, 'red'))
    print(get_first_int(p_qs, 'green'))
    print(get_first_int(p_qs, 'black'))
