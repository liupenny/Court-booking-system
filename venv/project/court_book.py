#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from court import Court


class Court_book(object):
    def __init__(self):
        """
        初始化
        """
        self.court_id = ('A', 'B', 'C', 'D')
        self.court = {}.fromkeys(self.court_id)

        self.input_error_msg = "Error: the booking is invalid!"
        self.book_suc_msg = "Success: the booking is accepted!"
        self.book_conflict_msg = "Error: the booking conflicts with existing booking!"

    def parse_book(self, legal_bookinfo):
        """

        @param legal_bookinfo:
        user_id: 用户编号
        court_id: 场地编号
        booking_date: 预定的日期
        start_time: 开始时间
        end_time: 结束时间
        @return:
        """
        court_id = legal_bookinfo["court_id"]
        booking_date = legal_bookinfo["booking_date"]
        start_time = legal_bookinfo["start_time"]
        end_time = legal_bookinfo["end_time"]
        self.court[court_id].

            conflict_flag = self.court_a.find_conflict(booking_date, start_time, end_time)
            if (conflict_flag == False):
                return False
            else:
                self.court_a.book(legal_bookinfo)
            return True

    def parse_cancel(self, book_info_list):
        """
        处理取消预定的信息

        @param book_info_list:
        @return:
        """
        return "Success"

    def get_input(self, book_info):
        """
        对用户输入字符串进行合法性检查

        @param book_info: 用户输入的信息
        @return:
        """
        book_info_list = book_info.split(' ')
        legal_bookinfo = {}.fromkeys("user_id","court_id", "booking_date", "seven_days","start_time", "end_time","booking_time")
        # 输入长度不符合
        if len(book_info_list) < 4 or len(book_info_list) > 5:
            print(self.input_error_msg)

        # 输入用户信息不符合格式
        if re.match("U[0-9]*$", book_info_list[0]) == None:
            print(self.input_error_msg)
        else:
            legal_bookinfo["user_id"] = book_info_list[0]

        # 输入日期不符合格式
        seven_days = self.is_date_legal(book_info_list[1])
        if seven_days == 0:
            print(self.input_error_msg)
        else:
            legal_bookinfo["booking_date"] = book_info_list[1]
            legal_bookinfo["seven_days"] = seven_days

        # 输入时间
        (start_time, end_time) = self.is_time_legal(book_info_list[2])
        if (start_time, end_time) == (False, False):
            print(self.input_error_msg)
        else:
            legal_bookinfo["start_time"] = start_time
            legal_bookinfo["end_time"] = end_time

        # 预定或取消
        if len(book_info_list) == 4:
            # user_id, order_date, order_time, court_id = book_info_list
            success_flag = self.parse_book(legal_bookinfo)
            if success_flag == True:  # 预定成功
                print(self.book_suc_msg)
            elif success_flag == False:  # 与现有的冲突
                print(self.book_conflict_msg)
        elif len(book_info_list) == 5 and book_info_list[4] == "C":
        # 进行取消试验
            self.parse_cancel(legal_bookinfo)


    def is_date_legal(self, booking_date):
        """
        通过日期判断是周几

        @param booking_date:
        @return:错误时间是周0
        """
        try:
            date = datetime.strptime(booking_date, '%Y-%m-%d')
            seven_days = date.weekday()
        except:
            seven_days = 0
        return seven_days

    def is_time_legal(self, booking_time):
        """
        判断时间格式是否正确

        @param booking_time:
        @return:错误时间返回（False，False）
        """
        match_time = re.match("(?P<start_time>\d{1,2}):00~(?P<end_time>\d{1,2}):00", booking_time)
        if match_time != None:
            start_time = match_time.group(1)
            end_time = match_time.group(2)
            if start_time >= end_time or start_time < 9 or end_time > 22:
                return (False,False)
            else:
                return (start_time, end_time)
        else:
            return (False,False)




    #def book(self):

if __name__ == '__main__':
    court = Court_book()
    court.book()