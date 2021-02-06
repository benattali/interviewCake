import unittest


def merge_ranges(meetings: list[tuple]) -> list[tuple]:
    meetings.sort()
    merged_meetings = []

    start_meeting = meetings[0][0]
    end_meeting = meetings[0][1]

    for meeting in meetings[1:]:
        if meeting[0] > end_meeting:
            meeting_to_add = (start_meeting, end_meeting)
            merged_meetings.append(meeting_to_add)
            start_meeting = meeting[0]
            end_meeting = meeting[1]
        else:
            if meeting[1] > end_meeting:
                end_meeting = meeting[1]

    meeting_to_add = (start_meeting, end_meeting)
    merged_meetings.append(meeting_to_add)

    return merged_meetings


print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
# Tests


# class Test(unittest.TestCase):
#     def test_meetings_overlap(self):
#         actual = merge_ranges([(1, 3), (2, 4)])
#         expected = [(1, 4)]
#         self.assertEqual(actual, expected)

#     def test_meetings_touch(self):
#         actual = merge_ranges([(5, 6), (6, 8)])
#         expected = [(5, 8)]
#         self.assertEqual(actual, expected)

#     def test_meeting_contains_other_meeting(self):
#         actual = merge_ranges([(1, 8), (2, 5)])
#         expected = [(1, 8)]
#         self.assertEqual(actual, expected)

#     def test_meetings_stay_separate(self):
#         actual = merge_ranges([(1, 3), (4, 8)])
#         expected = [(1, 3), (4, 8)]
#         self.assertEqual(actual, expected)

#     def test_multiple_merged_meetings(self):
#         actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
#         expected = [(1, 8)]
#         self.assertEqual(actual, expected)

#     def test_meetings_not_sorted(self):
#         actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
#         expected = [(1, 4), (5, 8)]
#         self.assertEqual(actual, expected)

#     def test_one_long_meeting_contains_smaller_meetings(self):
#         actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
#         expected = [(1, 12)]
#         self.assertEqual(actual, expected)

#     def test_sample_input(self):
#         actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
#         expected = [(0, 1), (3, 8), (9, 12)]
#         self.assertEqual(actual, expected)


# unittest.main(verbosity=2)
