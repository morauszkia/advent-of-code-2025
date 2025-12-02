def get_ranges(filepath):
    with open(filepath) as file:
        content = file.read()
    return [get_endpoints(pair) for pair in content.split(",")]


def get_endpoints(pair):
    hyphen_index = pair.index("-")
    start = int(pair[:hyphen_index])
    end = int(pair[hyphen_index + 1:])
    return start, end
