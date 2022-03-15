def santa(age:int=31, gender:str=None):
    return_str = ""
    for _ in range(age):
        if gender=="male": return_str += "HOHOHO, PIMP!\n"
        else: return_str += "HOEHOEHOE!\n"
    return return_str
