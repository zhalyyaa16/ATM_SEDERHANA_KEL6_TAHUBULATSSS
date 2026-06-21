from data import akun

def render(no_rekening, pin):

    if no_rekening in akun and akun[no_rekening]["pin"] == pin:
        return no_rekening
    return None