#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from court import Court


class Court_book(object):
    def get_input(self, book_info):
        """
        对用户输入字符串进行合法性检查

        @param book_info: 用户输入的信息
        @return:
        """
        book_info_list = book_info.split(' ')
        legal_bookinfo = {}.fromkeys("user_id", "court_id", "booking_date", "start_time", "end_time")
        # 输入长度不符合
        if len(book_info_list) < 4 or len(book_info_list) > 5:
            print(self.input_error_msg)

        # 输入用户信息不符合格式
        if re.match("U[0-9]*$", book_info_list[0]) == None:
            print(self.input_error_msg)
        else:
            legal_bookinfo["user_id"] = book_info_list[0]

        # 输入日期不符合格式
        if self.is_date_legal(book_info_list[1]) == False:
            print(self.input_error_msg)
        else:
            legal_bookinfo["booking_date"] = book_info_list[1]

        # 输入时间
        (start_time, end_time) = self.is_time_legal(book_info_list[2])
        if (start_time, end_time) == (False, False):
            print(self.input_error_msg)
        else:
            book_info_list["start_time"] = start_time
            book_info_list["end_time"] = end_time

        # 预定或取消
        #if (len(book_info_list) == 4):

    def is_date_legal(self, booking_date):
        """

        @param booking_date:
        @return:
        """
        try:
            date = datetime.strptime(booking_date, '%Y-%m-%d')
            seven_days = date.weekday()
        except:
            seven_days = 0
        if seven_days == 0:
            return False
        else:
            return True

    def is_time_legal(self, booking_time):
        """

        @param booking_time:
        @return:
        """
        match_time = re.match("(?P<start_time>\d{1,2}):00~(?P<end_time>\d{1,2}):00", booking_time)
        if match_time != None:
            start_time = match_time.group(1)
            end_time = match_time.group(2)
            if start_time >= end_time or start_time < 9 or end_time > 22:
                return (False, False)
            else:
                return (start_time, end_time)
        else:
            return (False, False)

    if len(book_info_list) == 4:
        # user_id, order_date, order_time, court_id = book_info_list
        success_flag = self.parse_book(book_info_list)
        if success_flag == True:  # 预定成功
            print(self.book_suc_msg)
        elif success_flag == False:  # 与现有的冲突
            print(self.book_conflict_msg)

    elif len(book_info_list) == 5:
        cancel_info_list = book_info_list[0:5]
        self.parse_cancel(cancel_info_list)