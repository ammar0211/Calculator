class Calc():
    def __init__(self):
        self.total = 0
        self.current = ' 5'
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

        

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

