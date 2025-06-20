def count_words(file_content):
    l = file_content.split()
    return len(l)

def count_chars(file_content):
    counts = {}

    for s in file_content:
        if s.lower() not in counts:
            counts[s.lower()] = 1
        else:
            counts[s.lower()] += 1
    
    return counts

def sort_dict(dict):
    l = []

    for k,v in dict.items():
        l.append({ "char": k, "num": v})

    return sorted(l, key=lambda x: x["char"])    
