import re
import classes.globals as g


class ProductRooRule(object):
    def __init__(self, heading, id_rule, description, subheading):
        self.heading = heading
        self.id_rule = id_rule
        self.description = description
        self.subheading = subheading
        self.rule = None
        self.alternate_rule = None

        self.components = []
        self.description = g.process_description(self.description)
        self.get_chapter()
        self.get_min_max()

    def get_chapter(self):
        tmp = self.subheading[0:2]
        self.chapter = int(tmp)

    def get_min_max(self):
        if "ex" in self.heading:
            self.is_ex_code = True
        else:
            self.is_ex_code = False

        self.heading = self.heading.replace("to", " - ")
        self.heading = self.heading.replace("ex", "")
        self.heading = self.heading.strip()

        if "chapter" in self.heading.lower():
            tmp = self.subheading[0:2]
            self.min = tmp + "0" * 8
            self.max = tmp + "9" * 8
        else:
            if "190120" in self.heading:
                a = 1
            tmp = self.heading.strip() + ""
            tmp = tmp.replace(" ", "")
            tmp = tmp.replace(".", "")
            if "-" in self.heading:
                parts = tmp.split("-")

                if len(parts[1]) == 6:
                    if parts[1][-2:] == "00":
                        parts[1] = parts[1][0:4]

                self.min = parts[0] + "0" * (10 - len(parts[0]))
                self.max = parts[1] + "9" * (10 - len(parts[1]))
            else:
                self.min = tmp + "0" * (10 - len(tmp))
                tmp2 = tmp.rstrip("0")
                self.max = tmp2 + "9" * (10 - len(tmp2))

        if self.is_ex_code:
            self.heading = "ex " + self.heading
