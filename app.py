IONS_CODE_POS_BASED = ['I1', 'I2', 'I3', 'IIA1', 'IIA2', 'IIA3', 'IIA4', 'IIA5', 'IIB1', 'IIB2', 'IIB3', 'IIB4', 'III1', 'III2', 'III3', 'IV1', 'IV2', 'IV3', 'IV4', 'V1', 'V2', 'V3', 'VI1', '01', '02', '03']

#Grp I
class Pb_2p:
    position = "I1, IIA2"
    name = "Pb_2p"
    reactions={

    }
class Ag_1p:
    position = "I2"
    name = "Ag_1p"
    reactions = {
    }
class Hg_1p:
    position = "I3"
    name = "Hg_1p"
    reactions={

    }

#Grp IIA
class Hg_2p:
    position = "IIA1"
    name = "Hg_2p"
    reactions={

    }
class Bi_3p:
    position = "IIA3"
    name = "Bi_3p"
    reactions={

    }
class Cu_2p:
    position = "IIA4"
    name = "Cu_2p"
    reactions={

    }
class Cd_2p:
    position = "II2A5"
    name = "Cd_2p"
    reactions={

    }

#Grp IIB
class As_3p:
    position = "I2, II2"
    name = "As_3p"
    reactions={

    }
class Sb_3p:
    position = "I2, II2"
    name = "Sb_3p"
    reactions={

    }
class Sn_2p:
    position = "I2, II2"
    name = "Sn_2p"
    reactions={

    }
class Sn_4p:
    position = "I2, II2"
    name = "Sn_4p"
    reactions={

    }

#Grp III
class Fe_3p:
    position = "III1"
    name = "Fe_3p"
    reactions={
    }
class Al_3p:
    position = "III2"
    name = "Al_3p"
    reactions={

    }
class Cr_3p:
    position = "III3"
    name = "Cr_3p"
    reactions={

    }

#Grp IV
class Zn_2p:
    position = "IV1"
    name = "Zn_2p"
    reactions={

    }
class Mn_2p:
    position = "IV2"
    name = "Mn_2p"
    reactions={

    }
class Ni_2p:
    position = "IV3"
    name = "Ni_2p"
    reactions={

    }
class Co_2p:
    position = "IV4"
    name = "Co_2p"
    reactions={

    }

#Grp V
class Ca_2p:
    position = "V1"
    name = "Ca_2p"
    reactions={

    }
class Sr_2p:
    position = "V2"
    name = "Sr_2p"
    reactions={

    }
class Ba_2p:
    position = "V3"
    name = "Ba_2p"
    reactions={

    }

#Grp VI
class Mg_2p:
    position = "VI1"
    name = "Mg_2p"
    reactions={

    }

#Grp 0
class Na_1p:
    position = "01"
    name = "Na_1p"
    reactions={

    }
class K_1p:
    position = "02"
    name = "K_1p"
    reactions={

    }
class NH4_1p:
    position = "03"
    name = "NH4_1p"
    reactions={

    }


class Solution:
    _IONS_CODE_NAME_BASED = {
        'I1' : Pb_2p, 'I2' : Ag_1p, 'I3' : Hg_1p,
        'IIA1' : Hg_2p, 'IIA2' : Pb_2p, 'IIA3': Bi_3p, 'IIA4': Cu_2p, 'IIA5': Cd_2p,
        'IIB1' : As_3p, 'IIB2' : Sb_3p, 'IIB3' : Sn_2p, 'IIB4' : Sn_4p,
        'III1' : Fe_3p, 'III2' : Al_3p, 'III3' : Cr_3p,
        'IV1' : Zn_2p, 'IV2' : Mn_2p, 'IV3' : Co_2p, 'IV4' : Ni_2p,
        'V1' : Ca_2p, 'V2' : Sr_2p, 'V3' : Ba_2p,
        'VI1' : Mg_2p,
        '01' : Na_1p, '02' : K_1p, '03' : NH4_1p  
    } 

    def __init__(self, ions:list):
        self.ions = [self._IONS_CODE_NAME_BASED[i]() for i in ions]

def name_memorisation(n):
    from random import randint
    for i in range(n):
        j = randint(0, len(IONS_CODE_POS_BASED) - 1)
        print("Enter the name of the ion with code", IONS_CODE_POS_BASED[j], " : ")
        if input() == Solution._IONS_CODE_NAME_BASED[IONS_CODE_POS_BASED[j]].name:
            print("Correct. Congratulations!")
        else: 
            print("Incorrect. Better Luck Next Time. The correct answer was {0}".format(Solution._IONS_CODE_NAME_BASED[IONS_CODE_POS_BASED[j]].name))
        

if __name__ == "__main__":
    name_memorisation(int(input("Enter the number of questions you want to answer: ")))

    # basic_radicals = []
    # x = True
    # while x != '':
    #     x = input("Enter Radical")
    #     if x != '':
    #         basic_radicals.append(x)
    # s = Solution(basic_radicals)
    # print([i.position for i in s.ions])