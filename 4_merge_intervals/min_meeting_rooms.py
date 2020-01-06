from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    min_count = 0
    rooms = []

    # 遍历meetings,只要是重复的，就加到堆中，不是重复的，就把原来堆里面的全部pop出来，最后统计下最大的堆的数据量
    for meeting in meetings:

        while len(rooms) > 0 and meeting.start >= rooms[0].end:
            heappop(rooms)

        heappush(rooms, meeting)
        # 只需要找到最大的重叠部分，该部分实际上就是最少的房间数
        min_count = max(len(rooms), min_count)

    return min_count


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
