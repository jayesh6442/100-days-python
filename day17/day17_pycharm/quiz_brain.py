class QuiaBrain:
    def __int__(self,q_list):
        self.question_number = 0
        self.qustion_list = q_list
    def next_question(self):
        current_questoin = self.qustion_list[self.question_number]
        input(f"Q.{self.question_number} : {current_questoin}(True/false): ")