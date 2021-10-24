class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        in_edges = [0 for _ in range(n)]
        out_edges = [set() for _ in range(n)]
        for x, y in relations:
            in_edges[y-1] += 1
            out_edges[x-1].add(y-1)
        min_time_to_start = [0 for _ in range(n)]
        max_finish_time = 0
        startable_courses = []
        
        # start every no-prereq course at the same time
        for index, count in enumerate(in_edges):
            if count == 0:
                startable_courses.append(index)

        while startable_courses:
            # start any course with no prereqs left
            course = startable_courses.pop()
            time_finished = min_time_to_start[course] + time[course]
            for next_course in out_edges[course]:
                min_time_to_start[next_course] = max(min_time_to_start[next_course], time_finished)
                
                # indicate that a prereq of next_course is finished
                in_edges[next_course] -= 1
                
                # if no prereqs left, we can start next_course at its min time to start
                if not in_edges[next_course]:
                    startable_courses.append(next_course)
                    
            # update max finish time
            max_finish_time = max(max_finish_time, time_finished)
        return max_finish_time
                
        