class IOstring:
    def IO(self):
        self.str1=""

    def some(self):
        self.str1=input("give input: ")

    def print_IO(self):
        print("the result is: ",self.str1.upper())

str1=IOstring()
str1.some()
str1.print_IO()
        