import re


def matches(match_pattern, value):
    """Determine if a given string matches a given pattern.
      pattern: list, str
      value: str
    """
    if not match_pattern:
        return False
    if not isinstance(match_pattern, list):
        patterns = [match_pattern]
    else:
        patterns = match_pattern

    for pattern in patterns:
        if pattern == value:
            return True
        if "*" not in pattern:
            continue
        # replace users/* or users\* with users.*
        # pattern.replace("\\", ".*")
        # pattern.replace("/*", ".*")
        # convert * matching into regex
        regex_pattern = r"^{0}".format(pattern.replace(".", r"\.").replace("*", ".*"))
        # import pdb
        # pdb.set_trace()
        if re.match(regex_pattern, value):
            return True

    return False
