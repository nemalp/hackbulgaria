def reduce_file_path(path):
    reduced_path = []
    parts = [part for part in path.split('/') if part not in ['.', '']]

    while len(parts) != 0:
        part = parts.pop()

        if part == "..":
            if len(parts) != 0:
                parts.pop()
        else:
            reduced_path.insert(0, part)

    return "/" + "/".join(reduced_path)

print(reduce_file_path("/srv/www/htdocs/wtf/"))
