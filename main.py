def duplicados(self):
    sets = set(self)
    if len(self) == len(sets):
        return False
    else:
        return True
