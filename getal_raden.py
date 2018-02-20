from random import randint
import sys
from pyemojify import emojify

BOLD = '\033[1m'
END = '\033[0m'

def is_gok_juist(gok, getal):
    if gok == getal:
        return True
    if gok < getal:
        groter_dik = BOLD + 'groter' + END
        print "de computer heeft een {} getal bedacht".format(groter_dik)
        return False
    if gok > getal:
        kleiner_dik = BOLD + 'kleiner' + END
        print "de computer heeft een {} getal bedacht".format(kleiner_dik)
        return False


def feleciteer_speler(vraag_counter):
    dikke_duim = emojify(" :thumbsup:  joepie!! het klopt je hebt gewonnen!!")
    print dikke_duim
    print "je hebt het binnen {} keer geraden!".format(vraag_counter)
    gefeliciteerd = emojify(":sparkles: gefeliciteerd :sparkles:")
    print gefeliciteerd
    sys.exit(1)


if __name__ == '__main__':
    kleinste_getal = 1
    grotste_getal = 100
    getal = randint(kleinste_getal, grotste_getal)

    print "Hallo! Ben je er klaar voor? " \
          "Het getal is tussen {} en {}".format(
        kleinste_getal, grotste_getal)

    gok = 0
    vraag_counter = 0
    aantal_dat_je_mag_vragen = 7

    while gok != getal and vraag_counter < aantal_dat_je_mag_vragen:
        _gok = raw_input("Wat denk je is het getal?   ")
        if not _gok.isdigit():
            print "je moet een getal invoeren, probeer opnieuw..."
            continue
        gok = int(_gok)
        if _gok > grotste_getal or _gok < kleinste_getal:
            print "je moet een getal tussen {} and {} invoeren, " \
                  "probeer opnieuw...".format(
                kleinste_getal, grotste_getal)
            continue
        juist = is_gok_juist(gok, getal)
        if juist:
            feleciteer_speler(vraag_counter+1)
        vraag_counter += 1
        print "je mag nog {} keer raden\n".format(aantal_dat_je_mag_vragen - vraag_counter)

    print "ah stom zeg dat het niet is gelukt echt jammer."
    print "de computer heeft dit getal bedacht: {}".format(getal)
