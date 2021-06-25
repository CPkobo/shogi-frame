class Game():
    initial_state = [
        "+",
        "o", "q", "s", "u", "z", "u", "s", "q", "o", 
        "_", "v", "_", "_", "_", "_", "_", "x", "_",
        "m", "m", "m", "m", "m", "m", "m", "m", "m", 
        "_", "_", "_", "_", "_", "_", "_", "_", "_", 
        "_", "_", "_", "_", "_", "_", "_", "_", "_", 
        "_", "_", "_", "_", "_", "_", "_", "_", "_", 
        "M", "M", "M", "M", "M", "M", "M", "M", "M", 
        "_", "X", "_", "_", "_", "_", "_", "V", "_", 
        "O", "Q", "S", "U", "Z", "U", "S", "Q", "O",
        "|"
    ]
    pos2len = {
        "91":1, "81":2, "71":3, "61":4, "51":5, "41":6, "31":7, "21":8, "11":9,
        "92":10, "82":11, "72":12, "62":13, "52":14, "42":15, "32":16, "22":17, "12":18,
        "93":19, "83":20, "73":21, "63":22, "53":23, "43":24, "33":25, "23":26, "13":27, 
        "94":28, "84":29, "74":30, "64":31, "54":32, "44":33, "34":34, "24":35, "14":36,
        "95":37, "85":38, "75":39, "65":40, "55":41, "45":42, "35":43, "25":44, "15":45,
        "96":46, "86":47, "76":48, "66":49, "56":50, "46":51, "36":52, "26":53, "16":54,
        "97":55, "87":56, "77":57, "67":58, "57":59, "47":60, "37":61, "27":62, "17":63,
        "98":64, "88":65, "78":66, "68":67, "58":68, "48":69, "38":70, "28":71, "18":72,
        "99":73, "89":74, "79":75, "69":76, "59":77, "49":78, "39":79, "29":80, "19":81,
        "00": 0,
    }

    piece2mark = {
        "FU": "M",
        "TO": "N",
        "KY": "O",
        "NY": "P",
        "KE": "Q",
        "NK": "R",
        "GI": "S",
        "NG": "T",
        "KI": "U",
        "HI": "V",
        "RY": "W",
        "KA": "X",
        "UM": "Y",
        "OU": "Z",
    }

    piece2got = {
        "m": "M", "n": "M",
        "o": "O", "p": "O",
        "q": "Q", "r": "Q",
        "s": "S", "t": "S",
        "u": "U",
        "v": "V", "w": "V",
        "x": "X", "y": "X",

        "M": "m", "N": "m",
        "O": "o", "P": "o",
        "Q": "q", "R": "q",
        "S": "s", "T": "s",
        "U": "u",
        "V": "v", "W": "v",
        "X": "x", "Y": "x"
    }

    O18 = {
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
        "10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F", "16": "G", "17": "H", "18": "I"
    }

    def __init__(self):
        self.figs = []
        self.steps = []
        self.having = {
            "M": 0,
            "O": 0,
            "Q": 0,
            "S": 0,
            "U": 0,
            "V": 0,
            "X": 0,
            "m": 0,
            "o": 0,
            "q": 0,
            "s": 0,
            "u": 0,
            "v": 0,
            "x": 0,
        }
        self.is_black_win = True
    
    def read_csa(self, csa, encode="UTF-8"):
        state = self.initial_state
        f = open(csa, "r", encoding=encode)
        started = False
        lines = f.readlines()
        f.close()

        i = 0
        for line in lines:
            if line.strip() == "+":
                break
            else:
                i += 1

        turn = "+"
        for line in lines[i+1:]:
            if line.startswith("$"):
                continue
            turn = line[0]
            state[0] = turn
            old_pos = self.pos2len[line[1:3]]
            new_pos = self.pos2len[line[3:5]]
            mark = self.piece2mark[line[5:7]] if turn == "+" else self.piece2mark[line[5:7]].lower()
            is_black = turn == "+"
            if old_pos != 0:
                state[old_pos] = "_"
            else:
                self.having[mark] -= 1
            if state[new_pos] != "_":
                got = self.piece2got[state[new_pos]]
                self.having[got] += 1
            state[new_pos] = mark

            self.steps.append(line.strip())
            self.figs.append(self._create_fig(state))

        self.is_black_win = turn == "+"

    def _create_fig(self, state):
        banmen = "".join(state)
        mochigoma = self._create_having_str()
        return f"{banmen}{mochigoma}"
        
    def _create_having_str(self):
        M = self.O18[str(self.having["M"])]
        O = self.having["O"]
        Q = self.having["Q"]
        S = self.having["S"]
        U = self.having["U"]
        V = self.having["V"]
        X = self.having["X"]

        m = self.O18[str(self.having["m"])]
        o = self.having["o"]
        q = self.having["q"]
        s = self.having["s"]
        u = self.having["u"]
        v = self.having["v"]
        x = self.having["x"]
        return f"{M}{O}{Q}{S}{U}{V}{X}|{m}{o}{q}{s}{u}{v}{x}"

    def get_steps(self):
        return self.steps

    def get_figs(self):
        return self.figs

    def get_pretty_figs(self):
        pfig = []
        for fig in self.figs:
            pfig.append(
                fig[1:10] + "\n"
                + fig[10:19] + "\n"
                + fig[19:28] + "\n"
                + fig[28:37] + "\n"
                + fig[37:46] + "\n"
                + fig[46:55] + "\n"
                + fig[55:64] + "\n"
                + fig[64:73] + "\n"
                + fig[73:82] + "\n"
                + fig[83:]
            )
        return pfig

    def get_winner(self):
        if self.is_black_win:
            return "SENTE win"
        else:
            return "GOTE win"