class CuttingString:
    def __init__(self, string: str, cut_string: str) -> None:
        self.string, self.__cut_string = string, cut_string
    @property
    def cut_string(self) -> str:
        return self.__cut_string
    @cut_string.setter
    def cut_string(self, cut_string: str) -> None:
        self.__cut_string = cut_string
    def correct_cut_string(self) -> bool:
        if len(self.__cut_string) > len(self.string):
            return False
        else:
            return True
    def FunctionCuttingString1(self):
        counter = 0
        for index, value in enumerate(self.string):
            if counter == len(self.__cut_string):
                print(f"\nподстрока -> '{self.__cut_string}' была удалена из строки -> '{self.string}'")
                return self.string[:index-len(self.__cut_string)] + self.string[index::]
            elif value == self.__cut_string[counter]:
                counter += 1
            else:
                counter = 0
        else:
            if counter == len(self.__cut_string):
                print(f"\nподстрока -> '{self.__cut_string}' была удалена из строки -> '{self.string}'")
                return self.string[:index - len(self.__cut_string) + 1] + self.string[index + 1::]
            else:
                return f"подстрока -> '{self.__cut_string}' не была найдена в строке -> '{self.string}'"
    def FunctionCuttingString2(self):
        if self.__cut_string in self.string:
            print(f"подстрока -> '{self.__cut_string}' была удалена из строки -> '{self.string}'")
            return self.string.replace(self.__cut_string, "")
        else:
            return f"подстрока -> '{self.__cut_string}' не была найдена в строке -> '{self.string}'"

cutting_string = CuttingString(input("Введите исходную строку:\n"), input("Ввидете подстроку, которую хотите вырезать:\n"))
if not(cutting_string.correct_cut_string()):
    print("длина вырезаемой строки превышает исходную.\nПовторите ввод:\n")
    cutting_string.cut_string(input("Ввидете подстроку, которую хотите вырезать:\n"))

print(f"Результат работы 1-ой программы:\n{cutting_string.FunctionCuttingString1()}\n")
print(f"Результат работы 2-ой программы:\n{cutting_string.FunctionCuttingString2()}\n")

