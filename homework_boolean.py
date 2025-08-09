def votes(age, nationality, criminal):
    if age < 18: return "Вы ещё несовершеннолетний"
    if nationality != "Русский": return "Вы должны быть русским"
    if criminal != "": return "У вас не должно быть судимостей"
    return "Вы можете голосовать"


def tests():
    assert votes(16, "Француз", "Воровство") == "Вы ещё несовершеннолетний"
    assert votes(18, "Француз", "Воровство") == "Вы должны быть русским"
    assert votes(18, "Русский", "Воровство") == "У вас не должно быть судимостей"
    assert votes(18, "Русский", "") == "Вы можете голосовать"


tests()
