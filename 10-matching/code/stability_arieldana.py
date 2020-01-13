# Programmers: Ariel Bar and Dana Morhaim
# Since:       2020-01


prefer = {}
prefer["galia"] = ["shlomo", "tomer", "raphi"]
prefer["batya"] = ["shlomo", "raphi", "tomer"]
prefer["aviva"] = ["raphi", "shlomo", "tomer"]
prefer["raphi"] = ["aviva", "galia", "batya"]
prefer["shlomo"] = ["aviva", "batya", "galia"]
prefer["tomer"] = ["batya", "galia", "aviva"]

match = {"aviva": "shlomo",
         "batya": "tomer",
         "galia": "raphi"

         }
match2 = {"aviva": "raphi",
          "batya": "shlomo",
          "galia": "tomer"

          }
match3 = {"aviva": "tomer",
          "batya": "raphi",
          "galia": "shlomo"

          }


def preferM(prefer, w, m, m1):
    for y in prefer[w]:
        if y == m1:
            return False
        if y == m:
            return True


def isStable(prefer, match):
    """Return true if the match is stable.
       >>> isStable(prefer,match)
       raphi and aviva prefer each other over the current engagement
       False
       >>> isStable(prefer,match2)
       True
       >>> isStable(prefer,match3)
       raphi and aviva prefer each other over the current engagement
       shlomo and aviva prefer each other over the current engagement
       shlomo and batya prefer each other over the current engagement
       False

       """
    key_list = list(match.keys())
    val_list = list(match.values())
    flag = True

    for a, b in match.items():
        for x in prefer[a]:
            if preferM(prefer, a, x, b) and preferM(prefer, x, a, key_list[val_list.index(x)]) and x != b:
                print(x, "and", a, "prefer each other over the current engagement")
                flag = False
    return flag


if __name__ == "__main__":
    import doctest

    doctest.testmod()


