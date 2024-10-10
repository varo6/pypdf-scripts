
def pages_args(npages:str) -> list[int]: 

    if "," in npages:
        return[int(i) for i in npages.split(",")]
    elif "-" in npages:
        start, end = npages.split("-")
        return list(range(int(start), int(end)))
    else:
        return [int(npages)]
